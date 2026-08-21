---
title: "Bash Shell for Solaris, IBM AIX, HP UX, and FreeBSD"
description: "The bash shell is required to run the js-install shell scripts described in Installing the WAR File for Production. The following js-install and js-upgrade scripts are in the buildomatic folder:"
---

# Bash Shell for Solaris, IBM AIX, HP UX, and FreeBSD

The bash shell is required to run the `js-install` shell scripts described in [Installing the WAR File for Production](../warfileinstall/war_intro.md). The following `js-install` and `js-upgrade` scripts are in the buildomatic folder:

`js-install`` .sh`

`js-upgrade-newdb .sh`

`js-upgrade-samedb .sh`

The bash shell is not included by default in all Unix platforms. When the bash shell is not available, you will need to download and install the bash shell specific to your platform.

Alternatively, you can manually run the same "buildomatic" Ant targets that are run by the `js-install` script. These Ant targets are listed in [Troubleshooting Your Server Configuration](../warfileinstall/war_troubleshooting_jrs.md).

Also, make sure you have updated your local Ant to include `ant-contrib.jar`, which supports conditional logic in Ant. Copy the `ant-contrib.jar` to your `<ant_home>/lib` folder from:

`buildomatic/extra-jars/ant-contrib.jar`.

For more information, see [Forgot to Copy the File ant-contrib.jar](error_running_buildomatic_scripts.md).

If you try using the Ant that is included with the JasperReports Server WAR file Distribution ZIP package, you may get the same non-bash syntax error. You may get the error below, for example:

`js-ant help-install`

`ANT_HOME=../apache-ant: is not an identifier`

If you have the bash shell installed, you can try running the js-ant command by calling bash explicitly, for example:

`bash js-ant help-install`
