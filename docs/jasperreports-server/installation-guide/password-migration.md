---
title: Running Password Migration
description: "You can upgrade old, legacy passwords to secure one-way hashing (Password-Based Key Derivation Function 2 (PBKDF2), SCrypt, or Argon2)."
---

# Running Password Migration

You can upgrade old, legacy passwords to secure one-way hashing (Password-Based Key Derivation Function 2 (PBKDF2), SCrypt, or Argon2).

System administrators may need to run a password migration in scenarios such as:

- If you upgrade to a newer version of JasperReports Server using samedb upgrade script and switch from the legacy to the modern password strategy at the same time, new users automatically use the modern strategy. However, you will need to run a migration to convert your existing users with legacy passwords.

- If you initially chose the legacy strategy during installation or upgrade but later decide to switch to the modern one, a password migration is required to convert all existing legacy user passwords over to the new strategy.

Before enabling modern password storage in your production environment, complete this pre-migration checklist to ensure a smooth transition and prevent data loss.

## Pre-Migration Checklist

Following is the checklist:

- Password migration is a permanent, one-way process, take a full database backup before proceeding. If you need to roll back, a database restore is the only option.

- Always run and verify the migration on a non-production system first to catch any performance bottlenecks or configuration issues.

- Ensure that all of your core database upgrade scripts have successfully finished running before starting the password utility.

- Manually check your database to verify that the `password_strategy` column exists in the `JIUser` table.

!!! note

    - Once passwords are upgraded to the modern format, you can not automatically flip a switch to change them back to the legacy format.

    - The only way to undo this migration and return to the old format is to restore your database from a backup.

    - Because this change is permanent, make sure to plan your migration carefully before running it in production.

## Migration Process Details

The password migration process includes:

- Detect (optional, `migrate-passwords-dry-run`): The script scans the database to see what it's working with. It automatically figures out the database type, counts the total number of users, and flags everyone who is still using an old, legacy password format. This creates a clean baseline before any data actually changes.

- Migrate (`migrate-passwords`): The system converts legacy passwords to the modern hashed format. To avoid overloading the database, users are processed in configurable batches (`password.migration.batch.size`). For every eligible internal user, the utility decrypts the existing legacy password, generates a new unique salt, re-hashes the password with the configured algorithm, and updates the `password`, `password_strategy`, and `password_algorithm` columns in the `JIUser` table. The progress is shown in the console logs. The `anonymousUser` account and externally authenticated users are skipped by design.

- Verify (optional, `detect-password-strategy`): The system performs a read-only check that reports the current distribution of modern versus legacy passwords across the database. When the legacy count is one (`anonymousUser`) and the modern count matches the total number of users, migration is complete. (The per-run counts of migrated, skipped, and failed accounts are reported in the `migrate-passwords` Migration Summary output.)

- Clean up migration tracking (optional, `cleanup-password-migration`): After a successful migration, you can remove completed records from the `JIPasswordMigration` tracking table to keep the database tidy. This affects only the tracking table, it does not change any passwords. Only records with a completed status are removed. In-progress, partial, and failed records are retained for troubleshooting.

With the bulk migration method, you can upgrade all passwords at once during a scheduled maintenance window. The migration utility `./js-ant migrate-passwords` reads its configuration from the `WEB-INF/js.password-storage-config.properties` file located in the deployed webapp.

``` bash
cd jasperserver/buildomatic

# Dry run first (recommended)
./js-ant migrate-passwords-dry-run

# Review output, then run actual migration
./js-ant migrate-passwords
```

Output example:

``` yaml
migrate-passwords:
     Password migration utility initialized:
      - Database: postgresql
      - Algorithm: pbkdf2
      - Batch size: 1000
      - Dry run: false

     Migration statistics:
      - Total users: 6
      - Users needing migration: 6
      - Users already modern: 0
      - Excluded users: 0

     Skipping anonymousUser with empty password (expected)

     Migration summary:
      - Successfully migrated: 5
      - Skipped: 1
      - Failed: 0

     Final migration statistics:
      - Total users: 6
      - Modern passwords: 5
      - Legacy passwords: 1
    Migration completed successfully!
```

## Post-Migration Verification

After running the migration script, you can verify that all user credentials were successfully upgraded by using the `./js-ant detect-password-strategy` command.

``` bash
# Check migration status
./js-ant detect-password-strategy

# Expected output:
# Total users: 6
# Modern passwords: 5
# Legacy passwords: 1
```

If the legacy passwords count is one and the modern password count matches the total number of users, the migration is complete and successful.

## Clean up Migration Tracking

After a successful migration, you can use the `./js-ant cleanup-password-migration` command to remove completed records from the `JIPasswordMigration` table to keep the database tidy. This is an optional step and affects only the tracking table. It does not change any user passwords.

``` bash
cd jasperserver/buildomatic
   # Remove completed migration tracking records
   ./js-ant cleanup-password-migration
```

Only records with a completed status are removed. In-progress, partial, and failed records are retained for troubleshooting.

## Migration Reporting Metrics

The final report groups accounts into three categories:

- `Successfully Migrated`: The number of accounts safely upgraded from legacy encryption to the new hashing format.

- `Skipped`: Accounts bypassed on purpose (like the `anonymousUser` with an empty password or external users). These are not errors.

- `Failed`: Unexpected errors during the migration that an admin needs to look into.

!!! note

    The `anonymousUser` account usually uses an empty password string and external users use their own passwords. The migration utility automatically detects and skips these accounts by design, logging it under the `Skipped` counter rather than marking it as a failure.

## Password Storage Strategy Scenarios

The following table details how the system handles user passwords during and after migration, depending on the chosen storage strategy and existing configuration.

<table>
<thead>
<tr>
<th>Existing Password</th>
<th>Migration Executed</th>
<th>Strategy Configured</th>
<th>Impact: Existing Users</th>
<th>Impact: New/Updated Users</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="4">Legacy</td>
<td rowspan="2">No</td>
<td>Legacy</td>
<td>Nothing changes. Credentials stay in the old format.</td>
<td>New passwords use the old, less secure format.</td>
</tr>
<tr>
<td>Modern</td>
<td>Users stay on the old format until they change their password.</td>
<td>New passwords use the new, secure format.</td>
</tr>
<tr>
<td rowspan="2">Yes</td>
<td>Legacy</td>
<td>No changes occur because the tool skips legacy setups.</td>
<td>New passwords use the old, less secure format.</td>
</tr>
<tr>
<td>Modern</td>
<td>All passwords are automatically upgraded to the secure format.</td>
<td>No changes occur because the tool skips legacy setups. New passwords use the new, secure format.</td>
</tr>
</tbody>
</table>

If you are doing a fresh install or an upgrade, you need to set your password strategy and algorithm in the `default_master.properties` file so it applies during setup. For a server that is already up and running, administrators can just update these settings in the `js.password-storage-config.properties` file and restart the app server to apply the changes.

!!! note

    The password migration process only runs when `password.strategy=modern`. The current deployed strategy is set to `legacy`, meaning all current and new passwords will remain in the `legacy` format.

    To enable password migration, update the setting to `password.strategy=modern` in the following configuration file:

    `.../webapps/jasperserver-pro/WEB-INF/js.password-storage-config.properties`.
