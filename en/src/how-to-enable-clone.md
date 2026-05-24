# How to create a clone at the end of a backup

> [!NOTE]
> This feature is available starting with *raspiBackup* version 0.7.3

*raspiBackup* can restore a backup to a locally connected device immediately after creating it.
This provides a backup that can be used right away to immediately restart a failed device or an OS that no longer boots
by switching the boot medium. Without this feature, an existing backup must first be restored.
This takes a little longer. If the rsync backup type is used, the restoration is simply a synchronization with the backup and
completes very quickly. The dd and tar backup types always involve a full restoration of the backup and therefore take longer.

Steps to enable cloning:

1) Create a backup with cloning disabled.

2) Restore the backup to the clone device

3) Enable cloning

   1) Command line

      When starting the backup from the command line, you must also specify the option `--clone <Clone Device>`. `<Clone Device>`
      refers to the locally connected device to which the current backup is to be synchronized or restored.

   2) Installer

      In the installer, configure `<Clonegerät>` at `M3->C10`. After that, you no longer need to specify the `--clone` option on the command line. The regular backup then will also create a clone all the time.

   3) Update the configuration file /usr/local/etc/raspiBackup.conf

      The cloned device has to be configured in the DEFAULT_CLONE_DEVICE option.

> [!CAUTION]
> The clone device will be overwritten with the backup.
> It is therefore essential to ensure that the clone device is the correct device.
> Otherwise, you risk losing data. That is why you must use `/dev/disk/by-partuuid/<PARTUUID>` and not simply `/dev/sda` or something similar. The PARTUUIDs of the available partitions can be displayed using the following command: `lsblk -o NAME,FSTYPE,LABEL,PARTUUID`


> [!WARNING]
> In certain configurations, the Raspberry Pi may boot from the clone device after a reboot.
> This can occur especially when booting via USB from a USB hard drive or USB SSD and the cloning device is also connected via USB.

> [!NOTE]
> If the rsync backup type is used, a backup must be restored to the clone device once to initialize the clone, so that subsequent backups can simply be synchronized. For details see [here](restore-intro.md)

If you want to disable cloning, you must use the installer to delete the cloned device at `M3->C10`. If you want to restore a backup manually, you must first disable cloning.

[.status]: translated
