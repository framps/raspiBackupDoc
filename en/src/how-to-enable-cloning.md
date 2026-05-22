# How to create a clone at the end of a backup

> [!NOTE]
> This feature is available starting with *raspiBackup* version 0.7.3

*raspiBackup* can restore a backup to a locally connected device immediately after creating it.
This provides a backup that can be used right away to immediately restart a failed device or an OS that no longer boots
by switching the boot medium. Without this feature, an existing backup must first be restored.
This takes a little longer. If the rsync backup type is used, the restoration is simply a synchronization with the backup and
completes very quickly. The dd and tar backup types always involve a full restoration of the backup and therefore take longer.

To enable the creation of a clone, follow these steps:

1) Command line

   When starting the backup from the command line, you must also specify the option `--clone <Clone Device>`. `<Clone Device>`
   refers to the locally connected device to which the current backup is to be synchronized or restored.

2) Installer

   In the installer, configure `<Clonegerät>` at `M3->C10`. After that, you no longer need to specify the `--clone` option on the command line. The regular backup then will also create a clone all the time.

> [!CAUTION]
> The clone device will be overwritten with the backup. Only with the rsync backup type
> a check is performed to ensure that the partitioning matches. It is therefore essential to make sure that the clone device is the correct
> device. Otherwise, there is a risk of data loss.


> [!NOTE]
> If the rsync backup type is used, a backup must be restored to the clone device once to initialize the clone, so that subsequent backups can simply be synchronized. For details see [here](restore-intro.md)

If you want to disable the creation of a clone, you have to use the installer to delete the clone device at `M3->C10`

[.status]: translated
