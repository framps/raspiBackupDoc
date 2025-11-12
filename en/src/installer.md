# Installer - Invocation and options

The download and installation of the *raspiBackup* installer is described [here](installation-in-5-minutes.md).

## Invocation

```
sudo raspiBackupInstallUI {Options}
```

There are two different ways to invoke the *raspiBackup* installer `raspiBackupInstallUI`:

1. Invoke without options or with option `-t`
    The installer starts with a menu via which *raspiBackup* can be configured.
    Option `-t` controls whether crond or systemd is used.
1. Invoke with options
    If an option other than `-t` is used, the installer executes the selected function
    immediately without a menu.

## Options

The following options allow the installer to perform certain functions directly without a menu:

* -i: Re/Installation of *raspiBackup*
* -e: Re/Installation of the *raspiBackup* sample extensions
* -h: Display a help text
* -U: Update from the installer `raspiBackupInstallUI
* -u: Uninstall *raspiBackup* including installer
* -t: Use either crond or systemd as backup timer with option -i, default is systemd

<a name="uninstallation"></a>
## Uninstallation

*raspiBackup* and the installer can also be uninstalled:

```
sudo raspiBackupInstallUI -u
```

**Note:**
This will delete the installer as well as *raspiBackup* with all its files!



## Details on some menu items

<a name="backup versions"></a>
### Backup versions - Menu C3

*raspiBackup* offers two different ways to store backup versions
to keep backup versions:

1. A *maximum number of backups* that is kept for each backup type (option -k).
   In the configuration file, the number of backups can be defined for each backup type (option --keep\<type\>).
   If the number is exceeded, the oldest backup is deleted.

1. Use of the *intelligent backup strategy*. Backups are created according to a specific rule
   which defines the number of days, weeks, months and years a backup should be kept. Older backups
   are deleted in each case. In the installer, the number of
   backups to be kept is defined with 4 numbers. The default is
   `7 4 12 3`.
 
   1. Daily backups (7)
   1. Weekly backups (4)
   1. Monthly backups (12)
   1. Annual backups (3)

   The intelligent backup strategy is described in detail [here](smart-recycle.md).


<a name="services"></a>
### Services to stop and start - Menu C6

Since *raspiBackup* does not back up any memory contents, all services that hold important information
in memory should be stopped before the backup.

*raspiBackup* offers the option of automatically stop services before the backup and then 
restart them afterwards. All services preselected in the installer should always be stopped.
As it cannot be ruled out that other services on the system may also hold important data
in the memory and should be stopped before the backup, the list of services that are not
active services must be carefully checked and, if necessary, these services must also be
selected so that they are stopped before the backup.

After selecting the services that are to be stopped, the order in which they are to be stopped must be defined.
In general, the sequence does not matter, but if a service has dependencies on another service, the service should
only be stopped after the dependent service. For example
all services that work with a database should be stopped before stopping the database
so that they can complete any open transactions.

<a name="regularbackup"></a>
### Regular backup - Menu C9

*raspiBackup* offers the possibility to create regular backups automatically.
This is done by default via *Systemd*, but can also be started with **Cron* 
if the option `-t` is used when the installer is started.

The day of the week on which a backup is to be created can be defined in the installer.
It's also possible to have a daily backup.
The time of the backup is also defined in hours and minutes. The default is Sunday at 05:00.


## Default configuration and location of the configuration file

The installer creates the following files:

  - Configuration file `/usr/local/etc/raspiBackup.conf`

    The following default values are set in this file and can be changed with the
    can be changed with the installer. All other options must be changed with an editor
    or overwritten with a invocation option.

    | Option | Setting |
    |----------------------|----------------------|
    | backup path | /backup |
    | backup mode | normal |
    | backup type | rsync |
    | language | language of the system |
    | zip | no |
    | message detail | normal |
    | backup count | 3 |
    | Services start | none |
    | Services stop | none |
    | Weekly backup | no |
    | backup day | Sunday |
    | backup time | 05:00 a.m. |

    [Invocation and options](backup-options.md) are described in detail.

  - *Systemd timer* Configuration `/etc/systemd/system/raspiBackup.timer`.

    This file controls the invocation of *raspiBackup* and in the standard case the
    weekly backup is switched off. However, it can be switched on with the installer.

  - *raspiBackup*.sh `/usr/local/bin`

  - *raspiBackupInstallUI.sh* `/usr/local/bin`



## Call the installation without installer directly from the command line - online

If you do not want to use a menu-driven installation, you can run the installation of *raspiBackup*
and the sample extensions or uninstall directly from the command line.

(This installation installs the standard configuration).

```
curl https://raspibackup.linux-tips-and-tricks.de/install | sudo bash -s -- -i
```

Any other installer option can be specified instead of `-i`.

Changes to the configuration can now be made manually using an editor.
See [Invocation and options](invocation-options.md).

You can also use the installer with its menus to adjust the configuration of the primary
options and to switch the regular backup on or off.

[.status]: translated


