---
title: Configuring Password Strategy
description: The defaultmaster.properties file handles the configuration for the password strategy.
---

# Configuring Password Strategy

The `default_master.properties` file handles the configuration for the password strategy.

To configure the `default_master.properties` file for password strategy,

- Edit the `default_master.properties` file to configure settings specific to your password strategy and algorithms.

- Uncomment any of the settings, along with the sample values for each supported algorithm, as per your requirement.

  For example: To uncomment `# password.modern.algorithm=scrypt`, change it to `password.modern.algorithm=scrypt`.

!!! note

    - By default, `password strategy=modern`.

      To enable the legacy strategy, set `password.strategy=legacy` and comment out all other strategy configurations.

    - By default, `password.modern.algorithm=pbkdf2`.

      To enable a specific algorithm, comment out the other two algorithms along with their respective properties present in the `default_master.properties` file.

      For example, to use Argon2, you must comment out both PBKDF2 and Scrypt and their configurations.

``` bash
# =============================================================================
# PASSWORD STORAGE CONFIGURATION
# =============================================================================

# Password strategy: modern | legacy
# - modern: Use modern password hashing (pbkdf2/scrypt/argon2) - RECOMMENDED
# - legacy: Keep current reversible encryption - for backward compatibility only
# Default: modern (secure by default for new installations)
password.strategy=modern

# Modern password algorithm configuration (PBKDF2 - recommended, default)
password.modern.algorithm=pbkdf2
password.modern.salt.length=32
password.modern.iterations=100000
password.modern.memory.cost=131072
password.modern.cpu.cost=4
password.modern.parallelism=4

# Alternative: SCrypt configuration (uncomment to use, comment out PBKDF2 above)
#password.modern.algorithm=scrypt
#password.modern.salt.length=32
#password.modern.iterations=100000
#password.modern.memory.cost=131072
#password.modern.cpu.cost=4
#password.modern.parallelism=4

# Alternative: Argon2 configuration (uncomment to use, comment out PBKDF2 above)
#password.modern.algorithm=argon2
#password.modern.salt.length=16
#password.modern.iterations=3
#password.modern.memory.cost=65536
#password.modern.cpu.cost=4
#password.modern.parallelism=4

# Password migration configuration
# Note: Migration is run manually via PasswordMigrationUtility command-line tool
password.migration.batch.size=1000
```

For information about the algorithms and configuration, see the JasperReports Server Security Guide.

!!! note

    After installing using the legacy strategy, if you decide to switch to the modern strategy later, you need to run a password migration for your existing users. For information on how to bulk migrate these passwords, see the [Running Password Migration](password-migration.md) section.
