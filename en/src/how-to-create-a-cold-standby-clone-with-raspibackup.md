# How can I create a clone with *raspiBackup*?

*raspiBackup* regularly creates any backup versions that can be restored if necessary.
can be restored if necessary. Often, however, you simply want to have the last backup
backup on a medium so that you can use it immediately in the event of an error, i.e. a clone.
in the event of an error, i.e. a clone.

*RaspiBackup does not offer a direct option to create a clone.

However, this is possible with the help of a small auxiliary tool: With this
a backup is created and this backup is then restored to a medium.
to a medium. If the backup type `rsync` is used, the restore is only a
synchronization of the changes from the last backup to the current backup and
is usually done quickly.

The help tool is called [raspiBackupAndClone.sh](https://github.com/framps/raspiBackup/blob/master/helper/raspiBackupAndClone.sh) and is available on *GitHub*.

The following steps are necessary to use it:

Note: <clonedevice> is the device that is to receive the clone, e.g. `/dev/mmcblk0` or `/dev/sda`.

 1. install `raspiBackupAndClone.sh

     1. download `raspiBackupAndClone.sh`
        ```
        curl -s -O https://raw.githubusercontent.com/framps/raspiBackup/refs/heads/master/helper/raspiBackupAndClone.sh
        ```
     2. move the script to `/usr/local/bin`
        ```
        sudo mv raspiBackupAndClone.sh /usr/local/bin
        ```
     3. make `raspiBackupAndClone.sh` executable
        ```
        sudo chmod x /usr/local/bin/raspiBackupAndClone.sh
        ```

 2. one-time initialization of the cloned device

     1. create a partition-oriented backup by calling
        ```
        sudo raspiBackup -P -t rsync <backup directory>
        ```
     2. restore the backup just created to the cloned device with
        ```
        sudo raspiBackup -d <clonedevice> <backup directory>
        ```

 3. set regular call of `raspiBackupAndClone.sh` instead of `raspiBackup.sh

     1. in the file `/etc/systemd/system/raspiBackup.service`
        ```
        ExecStart=/usr/local/bin/raspiBackup.sh
        ```
        change to
        ```
        ExecStart=/usr/local/bin/raspiBackupAndClone.sh <clonedevice>
        ````

If a backup is to be created manually,
must be called `raspiBackupAndClone.sh` instead of `raspiBackup.sh`.

Note: If no `rsync` backup is possible, the line `USE_RSYNC=1` must be deleted in `raspiBackupAndClone.sh`.
line `USE_RSYNC=1` must be changed to `USE_RSYNC=0`. Then the restore
takes considerably longer, however, as no synchronization but a full restore
is performed.

[.status]: translated
[.source]: https://www.linux-tips-and-tricks.de/de/raspibackupcategoried/684-wie-kann-man-mit-raspibackup-einen-clone-erstellen
[.source]: https://www.linux-tips-and-tricks.de/en/raspibackupcategorye/685-how-to-create-a-cold-standby-clone-with-raspibackup


