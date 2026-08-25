---
title: Configuring Password Storage Strategy
description: "JasperReports Server provides robust password security management by combining strict reuse restrictions with industry-standard cryptographic storage. Together, these features ensure compliance with..."
---

# Configuring Password Storage Strategy

JasperReports Server provides robust password security management by combining strict reuse restrictions with industry-standard cryptographic storage. Together, these features ensure compliance with global security frameworks (including OWASP, NIST, PCI DSS, and ISO/IEC 27001) while maintaining a seamless user experience.

Modern password storage and migration eliminates the risks associated with reversible encryption. The system uses advanced, one-way hashing algorithms (Password-Based Key Derivation Function 2 (PBKDF2), SCrypt, and Argon2). This database-agnostic upgrade provides significantly stronger credential protection and removes the need for keystore synchronization for user login credentials, which no longer require reversible encryption.

Transitioning to modern storage requires zero downtime. Legacy password migration is performed manually using the batch processing migration utility. High-efficiency hashing ensures a negligible impact on system performance, maintaining authentication times.

## Password Storage Strategies

JasperReports Server supports two distinct password security strategies, namely legacy and modern, to manage how user credentials are encrypted and validated in the database. The strategy must be specified in the `password.strategy` property.

- The legacy strategy (`password.strategy=legacy`) uses older encryption methods and is only there for backward compatibility during system upgrades. It relies on a hardcoded, unchangeable AES encryption mechanism. Because this encryption is reversible, it creates a major security risk if your database or keys are ever compromised. This strategy completely ignores any modern configuration variables you set under the `password.modern.*` properties.

- The modern strategy (`password.strategy=modern`) is the platform standard, built to meet current security frameworks and protect user data against modern attacks. It is the default, recommended setup for all new installations and upgraded environments. Instead of risky, reversible encryption, it uses secure, configurable one-way hashing algorithms so stored credentials can never be decrypted back into plain text. This strategy is also highly customizable, automatically reading and applying any fine-tuning variables you define under the `password.modern.*` application properties.

## Password Storage Strategy Comparison

Configuring your password hashing parameters correctly is essential for balancing strong security with good system performance. This section covers how to set up these algorithms for production environments.

## Algorithms Supported

The following table lists the algorithms supported for modern password strategy:

| Algorithm | Best For                                  | Security Strength |
|-----------|-------------------------------------------|-------------------|
| PBKDF2    | General, standard use (Default)           | High              |
| SCrypt    | Extra protection against hardware attacks | Very High         |
| Argon2    | Maximum security against modern threats   | Highest           |

!!! info "Important"

    - PBKDF2: The default choice for general use, providing NIST-approved compliance for regulatory needs.

    - Argon2: While this offers the highest level of security against modern threats, specific recommendations may vary depending on your target environment's security requirements and available resources.

    - Every algorithm uses unique salts and configurable complexity settings to maximize protection.

## Algorithm Selection

The following table provides the necessary information required to select the most appropriate password hashing algorithm based on your organization's specific security and performance priorities.

| Your Priority | Recommended Algorithm | Security Strength |
|----|----|----|
| Maximum security | Argon2 | The best choice for maximum security. It is highly resistant to advanced hacking methods, including attacks using specialized hardware like GPUs. |
| Balanced security and performance | SCrypt | Offers a strong balance between security and speed. It effectively resists hardware-based attacks while remaining fast and efficient on system resources. |
| Maximum compatibility | PBKDF2 | The default, highly compatible choice. It works in almost any environment and provides fast performance while meeting standard industry guidelines. |
| Regulatory compliance | PBKDF2 | Specifically recommended for meeting strict government or healthcare regulations (like FIPS 140-2) that require standard, audited security methods. |

## Parameters Used

The following table outlines the settings available for tuning strong hashing algorithms like PBKDF2, Argon2 or Scrypt, detailing how each parameter balances security and system performance.

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th>Hashing Parameter</th>
<th>Purpose</th>
<th>Security/Performance Impact</th>
<th>Typical Range</th>
<th>How it Works</th>
</tr>
</thead>
<tbody>
<tr>
<td>Iterations</td>
<td>Sets how many times the hash function repeats.</td>
<td>Higher values significantly slow down attackers but also increase the time it takes for a real user to log in.</td>
<td><p>10,000 - 500,000</p>
<p>**Note** For Argon2, the value is 3.</p></td>
<td>This makes the process harder for computers to handle quickly, forcing a slight delay (50-500ms) that blocks rapid-fire guessing.</td>
</tr>
<tr>
<td>Memory Cost</td>
<td>Specifies how much RAM is needed to calculate a hash.</td>
<td>Prevents attackers from using specialized hardware (like GPUs) that have limited memory to crack passwords quickly.</td>
<td>16 KiB - 256 MiB</td>
<td>By requiring more memory, it makes an attack much more expensive and difficult for an intruder to execute.</td>
</tr>
<tr>
<td>CPU Cost</td>
<td>Controls the amount of processing power used for each step.</td>
<td>Ensures the hashing process is demanding enough to prevent easy calculation by common processors.</td>
<td>1 - 8</td>
<td>Acts as a difficulty multiplier to protect credentials without ruining the user experience.</td>
</tr>
<tr>
<td>Parallelism</td>
<td>Specifies how many processing threads are used at once.</td>
<td>Allows modern multi-core servers to verify passwords faster for legitimate users.</td>
<td>1 - 4</td>
<td>Helps the server work more efficiently, providing a faster response time while still maintaining a high security barrier.</td>
</tr>
<tr>
<td>Salt Length</td>
<td>Defines the length of a unique random string added to each password.</td>
<td>Ensures that even if two users have the same password, their stored hashes will be completely different.</td>
<td>16 - 64 (Bytes)</td>
<td>Using at least 16 bytes makes it impossible for attackers to use pre-calculated tables to "look up" passwords.</td>
</tr>
</tbody>
</table>

### Algorithm-specific Parameters

#### PBKDF2

PBKDF2 is a standard, CPU-bound algorithm. Its security is controlled by a single primary setting, making it straightforward to configure.

Parameters

The parameters include:

- Iterations: This is the only parameter that affects the security of PBKDF2. Increasing this number makes the hash stronger.

- Salt Length: A standard 32-byte unique string is used for every password.

- The Memory Cost, CPU Cost, and Parallelism parameters have no effect when using PBKDF2, even though the same set of parameters are shared across all three algorithms.

**Configuration example:**

``` properties
password.modern.algorithm=pbkdf2
password.modern.salt.length=32
password.modern.iterations=100000
password.modern.memory.cost=131072
password.modern.cpu.cost=4
password.modern.parallelism=4
```

Performance Impact

A higher number increases security at the cost of performance, while a lower number maximizes performance at the cost of security.

| Security Difficulty (Iterations) | Verification Speed | Security Strength |
|----------------------------------|--------------------|-------------------|
| 10,000                           | Very Fast          | Minimum           |
| 50,000                           | Fast               | Acceptable        |
| 100,000 (Default)                | Balanced           | Recommended       |
| 200,000                          | Slower             | High              |
| 500,000                          | Slow               | Very High         |

Performance Expectations

- Standard Speed (100,000 iterations): Typically takes very less time to verify a password on modern hardware.

- Direct Scaling: If you increase the iteration count, the verification time increases proportionally (for example, doubling iterations doubles the wait time).

- Memory usage: Very efficient, consuming only about 1–2MB per hash.

- CPU impact: It utilizes one full CPU core while hashing, which is standard for this process.

#### SCrypt

Scrypt is a memory-hard cryptographic function that enhances password security by requiring both high computational power and memory.

Parameters

The parameters include:

- Iterations: Determines how many times the hashing process repeats, making it harder for attackers to guess passwords.

- Memory Cost: Sets the amount of memory (RAM) required, which forces attackers to use more expensive, memory-intensive hardware.

- CPU Cost: Controls the block size of the hashing process to increase processing complexity.

- Parallelism: Defines how many simultaneous threads can be used, helping balance strong security with faster verification for users.

- Salt Length: The recommended size for the unique random data added to each password to prevent pre-calculated attack tables (32 bytes).

**Configuration example:**

``` bash
#password.modern.algorithm=scrypt
#password.modern.salt.length=32
#password.modern.iterations=100000
#password.modern.memory.cost=131072
#password.modern.cpu.cost=4
#password.modern.parallelism=4
```

Performance Impact

| Memory Cost | Memory Usage | Security Level        |
|-------------|--------------|-----------------------|
| 16,384      | 16 MB        | Minimum               |
| 65,536      | 64 MB        | Recommended (default) |
| 131,072     | 128 MB       | High security         |
| 262,144     | 256 MB       | Very high security    |

Performance and Expectations

- Standard Speed (65,536 memory cost): Verifying a password usually takes 40–80ms and uses 64 MB of memory.

- Hardware Protection: Because this is a "memory-hard" algorithm, it requires significant RAM to run. This makes it much harder for attackers to use specialized, high-speed hardware (like GPUs) to guess passwords.

- Performance Warning: Because memory cost significantly impacts speed, you should test carefully before increasing it, as even small adjustments can lead to noticeably longer wait times for users.

- Efficiency: The system can utilize multiple CPU cores to perform these tasks, helping it run smoothly on modern servers.

#### Argon2

Argon2 is a highly secure password-hashing algorithm featuring a memory-hard, GPU-resistant design to neutralize custom hardware attacks.

Parameters

The parameters include:

- Time Cost: Sets how many passes the algorithm takes. Higher values significantly increase the time required for an attacker to try and crack a password.

- Memory Cost: Determines how much computer memory is required to calculate the hash. By requiring significant RAM, it prevents attackers from using specialized, high-speed hardware like GPUs to guess passwords.

- Parallelism: Defines the number of simultaneous processing threads. This allows the system to handle complex security checks efficiently on modern multi-core servers.

- Salt Length: Defines the length of the unique, random string added to each password (16 bytes recommended). This ensures that even identical passwords result in completely different stored hashes, blocking attackers from using pre-calculated look-up tables.

**Configuration example:**

``` bash
#password.modern.algorithm=argon2
#password.modern.salt.length=16
#password.modern.iterations=3
#password.modern.memory.cost=65536
#password.modern.cpu.cost=4
#password.modern.parallelism=4
```

Performance Impact

| Memory Cost    | Security Level          |
|----------------|-------------------------|
| 32,768 (32 MB) | High                    |
| 65,536 (64 MB) | Very high (recommended) |

Performance and Expectations

- High Memory usage: This algorithm uses a significant amount of RAM, which makes it much harder for attackers to use specialized hardware to guess passwords.

- Multi-threading support: It is optimized for modern multi-core processors, ensuring security checks remain fast even under high load.

Security Advantages

- Proven Industry Standard: Winner of the Password Hashing Competition (PHC), making it one of the most trusted algorithms available.

- Hardware Attack Defense: Provides superior protection against high-speed cracking attacks using GPUs, ASICs, and FPGAs.

- Advanced Leak Resistance: The Argon2id variant is specifically designed to protect against side-channel attacks, offering an extra layer of defense for your credentials.

## Configuration

### Build Configuration

The `jasperserver/buildomatic/default_master.properties` file is used to customize your default security settings before you perform a fresh installation or an upgrade.

``` bash
# Modern Password Algorithm Configuration
password.strategy=modern
password.modern.algorithm=pbkdf2
password.modern.salt.length=32
password.modern.iterations=100000
password.modern.memory.cost=131072
password.modern.cpu.cost=4
password.modern.parallelism=4
password.migration.batch.size=1000
```

### Deployment Configuration

While these settings are automatically generated from your build configuration during the installation or upgrade process, you can manually adjust the configured strategy or its parameters by editing the `webapps/jasperserver-pro/WEB-INF/js.password-storage-config.properties` file and restarting the application server.

``` bash
# =============================================================================
# PASSWORD STORAGE CONFIGURATION
# =============================================================================

# Password strategy: modern | legacy
# - modern: Use modern password hashing (PBKDF2/SCrypt/Argon2) - RECOMMENDED
# - legacy: Keep current reversible encryption - for backward compatibility only
# This value comes from default_master.properties or defaults to 'modern' from default.properties
password.strategy=modern

# =============================================================================
# MODERN PASSWORD ALGORITHM CONFIGURATION
# (Only used when password.strategy=modern)
# (IGNORED when password.strategy=legacy - legacy uses hardcoded AES)
# =============================================================================

# Algorithm selection: pbkdf2 | scrypt | argon2
# pbkdf2 - Default, CPU-bound, FIPS-compliant, low memory
# scrypt - Memory-hard, resistant to hardware attacks
# argon2 - Best security (PHC winner), memory-hard and GPU-resistant
password.modern.algorithm=pbkdf2

# Salt length in bytes (recommended: 32)
password.modern.salt.length=32

# PBKDF2 iterations (recommended: 100000)
# Higher values = more secure but slower
password.modern.iterations=100000

# Memory cost (recommended: 131072)
# Only used when algorithm=SCrypt
password.modern.memory.cost=131072

# SCrypt CPU cost (recommended: 4)
# Only used when algorithm=SCrypt
password.modern.cpu.cost=4

# Parallelism factor (recommended: 4)
# Used by SCrypt and Argon2
password.modern.parallelism=4

# =============================================================================
# PASSWORD MIGRATION CONFIGURATION
# =============================================================================

# Batch size for password migration (default: 1000)
# Larger values = faster migration but more memory usage
# Note: Migration is run manually via PasswordMigrationUtility command-line tool
password.migration.batch.size=1000
```

## Scenarios: Post Deployment Impact of Parameter Changes

### Scenario 1: Increasing Security Parameters

#### What Happens?

- New passwords: Any password created or changed from this point on will use the new, stricter settings.

- Existing passwords: Current passwords stay as they are, using the original settings.

- Mixed environment: Both old and new password formats will safely coexist in your database.

- Authentication: The system automatically recognizes which format a user has and authenticates them without issues.

Example:

``` text
Old password: modern:pbkdf2:50000:... (weaker)
New password: modern:pbkdf2:100000:... (stronger)
```

#### Performance Impact

- Higher iterations: Logging in will take slightly longer for users with the new passwords because the system has to work harder to verify them.

- Higher memory cost: If you are using SCrypt, the server will use more memory during authentication.

- Mixed load: You will see variable authentication times across your system depending on whether a user is on the old or new settings.

### Scenario 2: Decreasing Security Parameters

#### What Happens?

- New passwords: Any new or updated passwords will use the lower, faster settings.

- Existing passwords: Current passwords remain unchanged and continue to use the older, stronger settings.

- Security risk: New passwords will be less secure and easier to crack. We do not recommend this unless it is absolutely necessary.

#### When This Might Be Needed?

- Performance bottlenecks: If high-traffic spikes are causing login delays.

- Resource constraints: If your servers or embedded systems are running out of memory/CPU capacity.

- Emergency measures: As a temporary fix while troubleshooting system performance issues.

### Scenario 3: Changing Algorithm

#### What Happens?

- New passwords: Any password created or changed from this point on will use the newly selected algorithm.

- Existing passwords: Current passwords stay exactly as they are and continue to work perfectly.

- Mixed environment: The system automatically handles multiple algorithms coexisting in the database at the same time.

#### How It Works?

The system supports seamless transitions between different algorithms because:

- Self-describing formats: The algorithm type is embedded directly into the stored password string.

- Smart verification: When a user logs in, the system reads which algorithm was used to create that specific password, rather than blindly using your current configuration.

- Zero user disruption: Users can log in without issues, even right after you change the algorithm settings.

**Example:**

``` yaml
Before: modern:pbkdf2:100000:65536:4:salt:hash
After:  modern:scrypt:100000:131072:8:salt:hash
```

**Real-world scenario:**

``` bash
# Step 1: Change configuration from PBKDF2 to SCrypt
password.modern.algorithm=scrypt

# Step 2: Restart application
# - New users get SCrypt passwords
# - Existing PBKDF2 users can still login (automatic transition)
```

### Recommendations

- OWASP recommendations:

  - PBKDF2: Minimum of 10,000 iterations

  - SCrypt: Minimum memory cost of 16,384

  - Salt size: Minimum of 16 bytes (128 bits)

- NIST guidelines:

  - Iterations: At least 10,000 iterations

  - Salt size: At least 16 bytes

  - Hash output: At least 256 bits

## JIUser and JIPasswordMigration Tables

Two new columns, namely `password_strategy` and `password_algorithm` are added to the `JIUser` table.

A new table, `JIPasswordMigration`, is added. This table is used to monitor your password migration process. It helps you track when migrations occurred, the encryption methods used, and the overall outcome of the process.

The `JIPasswordMigration` table records the date of the migration, the total number of users processed, and a count of both successful updates and failed attempts. It also tracks the migration status:

- `in_progress`: The migration is currently running.

- `completed`: All users were updated successfully.

- `failed`: The migration did not succeed due to errors.

- `partial`: The migration was only partially successful. Some users were updated, while others encountered errors.
