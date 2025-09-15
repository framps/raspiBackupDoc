# SMB as backup destination

It is actually recommended to use NFS instead of SMB to store the backups
from *raspiBackup*.
Then you can use backup type rsync and only ever create a delta backup
instead of a full backup, which is necessary with SMB.
But there may still be reasons why you want to store a *raspiBackup* on an
SMB drive.

The following describes how to configure this on a Synology
is to be configured. AutoFS is also configured.
If autoFS is not already used, the same behavior can be achieved with *raspiBackup* using the
option `DynamicMount` to achieve the same behavior.

To automatically mount the SMB backup partition when *raspiBackup* uses it
uses it, a shared folder must be defined and configured on the NAS.

In the following instructions, the shared folder name "raspiBackup"
is assumed.

## Installation of autoFS

```
sudo apt install autofs
```

### AutoFS configuration

  - `/etc/auto.cifs`

    ```
    synoRaspiBackup -fstype=cifs,rw,credentials=/home/pi/scratch.conf,cache=none,iocharset=utf8,file_mode=0664,dir_mode=0775,vers=3.1.1,soft,iocharset=utf8 ://<synologyIP>/raspiBackup
    ```

This defines an SMB shared folder with the name `raspiBackup`
is defined on the NAS with the mountpoint `synoRaspiBackup`.

  - `/etc/auto.master`.

    ```
    /mnt /etc/auto.cifs --timeout=600 --ghost
    ```

ensures that the SMB partition of the NAS in `/mnt/synoRaspiBackup
is automatically mounted as soon as it is accessed.

## Definition of the SMB access data

  - `/home/pi/raspiBackup.conf`
    ```
    user=<AdministratorName>
    password=<AdministratorPassword>
    ```

### Make access data readable only for the user pi

```
chmod 600 /home/pi/raspiBackup.conf
```

## Definition of the SMB partition as backup partition in raspiBackup

Call the raspiBackupInstaller with `sudo raspiBackupInstallUI`
and definition of `/mnt/synoRaspiBackup` (`M3 -> C2`)

[.status]: translated
[.source]: https://www.linux-tips-and-tricks.de/de/raspibackupcategoried/687-raspibackup-nutzung-einer-synology-als-backupspace-mit-cifs-samba-und-autofs


