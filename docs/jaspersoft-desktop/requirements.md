# Requirements

What a computer needs to run Jaspersoft Desktop.

## Operating system

| System | Versions | Processor |
| --- | --- | --- |
| **macOS** | macOS 13 Ventura or later | Apple silicon (M1 and later) or Intel: a package for each |
| **Windows** | Windows 10 or Windows 11, 64-bit | x64 or ARM64: a package for each |
| **Linux** | A 64-bit distribution with a desktop: Ubuntu 18.04, Debian 10, openSUSE 15.5, Fedora 39 or later | x64 or ARM64: a package for each |

These are the systems the application's frameworks support: its window is Chrome's engine, which
sets the same limits for Chrome itself.

## Memory, disk and screen

| | Minimum | Recommended |
| --- | --- | --- |
| **Memory** | 4 GB | 8 GB or more |
| **Disk** | 2 GB free | 4 GB free |
| **Screen** | 1366 × 768 | 1920 × 1080 or more |

The application takes about 1.6 GB once installed. Its updates and the local history of your
reports are kept in your user folder, and need some room besides.

A wide screen pays off: the designer shows the page with the explorer, the palette, the outline
and the properties around it, and the AI assistant's column beside them.

## Nothing else to install

Jaspersoft Desktop includes everything it needs:

- **Java**: its own Java runtime, used by nothing else. A Java already installed on the computer
  is neither needed nor used, nor changed.
- **JasperReports**: the engine the reports are designed for, in its latest version.
- **JDBC drivers** for PostgreSQL, MariaDB (and MySQL) and HSQLDB. Others are added to a
  workspace when it needs them (see [Workspace settings](workspace-settings.md)).
- **A sample database**, with the samples and the tutorials of this guide (see
  [The sample database](sample-database.md)).

## Network

Jaspersoft Desktop works without a network once it is activated. It connects to the internet:

- to **activate** it and to renew its license: once, and then from time to time. An activation
  without an internet connection is possible too (see
  [Activating Jaspersoft Desktop](activation-and-licensing.md));
- for its **updates**;
- to reach the **AI model service** you configure, if you use the AI assistant;
- to reach your **databases** and **JasperReports Server**, wherever they are.

It uses the proxy settings of the system.

The report engine of Jaspersoft Desktop runs on your computer and answers only on it
(`127.0.0.1`): nothing of it can be reached from the network, and no firewall rule is needed.

## Accounts

- A **Jaspersoft Community account**, to activate Jaspersoft Desktop (community.jaspersoft.com).
- For JasperReports Server: an account on the server.
- For the AI assistant: an account, and a key, with an AI model service; or Ollama, on your own
  computer (see [Designing reports with AI](ai-assistant.md)).
