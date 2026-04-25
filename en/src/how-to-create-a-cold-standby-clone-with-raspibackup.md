# How can I create a clone with *raspiBackup*?

*raspiBackup* regularly creates any backup versions that can be restored if necessary.
can be restored if necessary. Often, however, you simply want to have the last backup
backup on a medium so that you can use it immediately in the event of an error, i.e. a clone.
in the event of an error, i.e. a clone.

**raspiBackup** does not offer a direct option to create a clone.

However, this is possible with the help of a small auxiliary tool: With this
a backup is created and this backup is then restored to a medium.
to a medium. If the backup type `rsync` is used, the restore is only a
synchronization of the changes from the last backup to the current backup and
finishes much earlier.
For all other backup types and backup modes, the restore is always a standard restore and not a synchronization.

The help tool is called [raspiBackupAndClone.sh](https://github.com/framps/raspiBackup/blob/master/helper/raspiBackupAndClone.sh) and is available on *GitHub*.

The following steps are necessary to use it:

> [!NOTE]
> \<clonedevice\> is the device that is to receive the clone, e.g. `/dev/mmcblk0` or `/dev/sda`.

 1. Install and configure **raspiBackup**
 1. Install `raspiBackupAndClone.sh`

     1. download `raspiBackupAndClone.sh`
        ```
        curl -s -O https://raw.githubusercontent.com/framps/raspiBackup/refs/heads/master/helper/raspiBackupAndClone.sh
        ```
     2. Move the script to `/usr/local/bin`
        ```
        sudo mv raspiBackupAndClone.sh /usr/local/bin
        ```
     3. Make `raspiBackupAndClone.sh` executable
        ```
        sudo chmod x /usr/local/bin/raspiBackupAndClone.sh
        ```
> [!IMPORTANT]
> Don't forget to execute the following steps to initialize the \<clonedevice\>
> [!WARNING]
> Make sure that the specified \<clonedevice\> is the correct device. Otherwise,
> you risk losing data.

 3. One-time initialization of the cloned device

     1. Create a rsync backup with
        ```
        sudo raspiBackup
        ```
     2. Restore the backup just created to the cloned device with
        ```
        sudo raspiBackup -d <clonedevice> <backup directory>
        ```

 1. Run **raspiBackupAndClone** once manually
    ```
    sudo raspiBackupAndClone.sh <clonedevice>
    ```
    and carefully test the clone
 
 3. Use `raspiBackupAndClone.sh` instead of `raspiBackup.sh`

     1. In the file `/etc/systemd/system/raspiBackup.service`
        ```
        ExecStart=/usr/local/bin/raspiBackup.sh
        ```
        change to
        ```
        ExecStart=/usr/local/bin/raspiBackupAndClone.sh <clonedevice>
        ```
        ```
        sudo nano /etc/systemd/system/raspiBackup.service
        ```

[.status]: translated
[.source]: https://www.linux-tips-and-tricks.de/de/raspibackupcategoried/684-wie-kann-man-mit-raspibackup-einen-clone-erstellen
[.source]: https://www.linux-tips-and-tricks.de/en/raspibackupcategorye/685-how-to-create-a-cold-standby-clone-with-raspibackup


