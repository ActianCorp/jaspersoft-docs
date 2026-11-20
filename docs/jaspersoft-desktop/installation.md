---
title: "Installation"
description: "Jaspersoft Desktop comes as one package per system. Check the requirements first, then follow the section of your system."
---

# Installation

Jaspersoft Desktop comes as one package per system. Check the [requirements](requirements.md)
first, then follow the section of your system.

| System | Package |
| --- | --- |
| macOS, Apple silicon | `jaspersoft-desktop-<version>-mac-arm64.dmg` |
| macOS, Intel | `jaspersoft-desktop-<version>-mac-x64.dmg` |
| Windows, 64-bit Intel or AMD | `jaspersoft-desktop-<version>-win-x64.exe` |
| Windows, 64-bit ARM | `jaspersoft-desktop-<version>-win-arm64.exe` |
| Linux, 64-bit Intel or AMD | `jaspersoft-desktop-<version>-linux-x64.tar.gz` |
| Linux, 64-bit ARM | `jaspersoft-desktop-<version>-linux-arm64.tar.gz` |

Not sure which Mac you have? Apple menu › **About This Mac**: **Chip** says Apple M1, M2… for
Apple silicon; **Processor** says Intel otherwise.

## macOS

1. Open the `.dmg`. A window shows Jaspersoft Desktop and the **Applications** folder.
2. Drag **Jaspersoft Desktop** onto **Applications**, and wait for the copy to finish.
3. Eject the disk image (the eject button next to it in the Finder's sidebar).
4. Start Jaspersoft Desktop from **Applications**, Launchpad or Spotlight.

If macOS says it cannot check the application, open **System Settings › Privacy & Security**,
and click **Open Anyway** next to the message about Jaspersoft Desktop; or right-click the
application in **Applications** and choose **Open**. macOS asks this once.

## Windows

1. Run `jaspersoft-desktop-<version>-win-x64.exe` (`win-arm64.exe` on an ARM computer).
2. Accept the license agreement.
3. Choose where to install: by default, in your user folder. No administrator rights are needed,
    and the installation is yours only: another user of the computer installs their own.
4. Click **Install**, then **Finish** to start Jaspersoft Desktop.

The installer adds Jaspersoft Desktop to the **Start** menu and to the desktop.

If Windows SmartScreen stops the installer, click **More info**, then **Run anyway**.

## Linux

1. Unpack `jaspersoft-desktop-<version>-linux-x64.tar.gz` (or `-linux-arm64.tar.gz`, for a
    computer with an ARM processor) where you keep applications: `tar xzf
    jaspersoft-desktop-<version>-linux-x64.tar.gz` in `~/Applications`, for example, or a double
    click in your file manager. What it unpacks is a folder named after the download.
2. Give the sandbox helper of that folder the permissions it needs, once, with your user's
    `sudo` rights. The window of Jaspersoft Desktop is Chrome's engine. Chrome starts each of its
    processes in a sandbox, and it uses a small program, `chrome-sandbox`, to set the sandbox up.
    That program must belong to the root account and carry the set-user-ID bit, so that it can
    protect your account from the processes it starts. Only an administrator can give these
    permissions, and an archive cannot carry them. Use the path of the folder you unpacked:

    ```bash
    sudo chown root:root ~/Applications/jaspersoft-desktop-<version>-linux-x64/chrome-sandbox
    sudo chmod 4755 ~/Applications/jaspersoft-desktop-<version>-linux-x64/chrome-sandbox
    ```

    Replace `<version>` and `x64` as in the name of the folder of step 1 (`arm64` for an ARM
    computer).

    Without them Jaspersoft Desktop does not start: the terminal says `The SUID sandbox helper
    binary was found, but is not configured correctly`, and no window opens. Do this again for
    each new version, in its new folder.

3. Start `jaspersoft-desktop` in that folder: from a terminal, or with a double click in your
    file manager. Rename the folder if you like — `~/Applications/Jaspersoft Desktop` reads
    better than the name of a download. A later version comes as a folder of its own, to unpack
    and put in its place.

To find it in your desktop's menu, add a launcher for it, as your desktop allows.

## The first start

The first start takes a little longer: Jaspersoft Desktop prepares its report engine. The home
screen says **Getting Jaspersoft Desktop ready…** meanwhile; what you open shows as soon as it is.

1. On macOS and Linux, Jaspersoft Desktop shows its **license agreement** (on Windows the installer
    did): read it and accept it.
2. **Activate** it with your Jaspersoft Community account: see
    [Activating Jaspersoft Desktop](activation-and-licensing.md).
3. The home screen opens. The **Samples** workspace is already among the recent folders, with the
    files of the tutorials of this guide.

Where to go from there: [Working with workspaces](workspaces.md), then
[Creating your first report](first-report.md).

## Updates

Jaspersoft Desktop looks for updates of its report engine, its designer and its home screen by
itself. An update downloads in the background; when it is ready, the bar at the bottom of the window
— on the home screen or in a workspace — says **Build … is ready**: click **Restart to update**.
Your workspace reopens as you left it.

Some updates need a new installation, of a new package: that bar then says **Build … needs
a new installation**. Install the new package over the old one, as the first time; your settings,
connections and licenses are kept.

## Where Jaspersoft Desktop keeps its data

Your reports are where you put them: in the folders you open, or on JasperReports Server.
Jaspersoft Desktop keeps the rest in a folder of your user account:

| System | Folder |
| --- | --- |
| macOS | `~/Library/Application Support/jaspersoft-desktop` |
| Windows | `%APPDATA%\jaspersoft-desktop`, and its updates in `%LOCALAPPDATA%\jaspersoft-desktop` |
| Linux | `~/.config/jaspersoft-desktop` |

It holds the recent workspaces and connections, the AI settings, the license file, the local
history of your reports and the log (**Help › Show Logs** opens it). The passwords of your
connections and the keys of the AI services are there too, encrypted with a key the system keeps
for your account (the Keychain on macOS, Windows' data protection, the keyring on Linux): they
cannot be read from a copy of the folder.

The **Samples** workspace is copied to `Documents/Jaspersoft Desktop/Samples`.

## Uninstalling

- **macOS**: drag Jaspersoft Desktop from **Applications** to the Trash.
- **Windows**: **Settings › Apps › Installed apps**, Jaspersoft Desktop, **Uninstall**.
- **Linux**: delete its folder.

Your reports, the Samples workspace and the data folder above stay. Delete the data folder too to
remove everything, the license file included. To use the license on another computer, deactivate
this one first (see [Activating Jaspersoft Desktop](activation-and-licensing.md)).
