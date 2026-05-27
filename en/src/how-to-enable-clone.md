# How to create a clone at the end of a backup

> [!NOTE]
> This feature is available starting with *raspiBackup* version 0.7.3 and as of now in Beta

*raspiBackup* can restore a backup to a locally connected device immediately after creating it.
This provides a backup that can be used right away to immediately restart a failed device or an OS that no longer boots
by switching the boot medium. Without this feature, an existing backup must first be restored
and requires more time. If the rsync backup type is used, the restore is simply a synchronization with the backup and
completes very quickly. A tar backup type always is a full restore of the backup and therefore takes much longer.
A dd backup type is not supported.

Steps to enable cloning:

1) Create a backup

2) Restore the backup to the clone device

3) Enable cloning

   1) Command line

      When starting the backup from the command line, you must also specify the option `--clone <Clone Device>`. `<Clone Device>`
      refers to the locally connected device to which the current backup is to be synchronized or restored.

   2) Installer

      In the installer, configure `<Clonegerät>` at `M3->C10`. After that, you no longer need to specify the `--clone` option on the command line. The regular backup then will also create a clone all the time.

   3) Update the configuration file /usr/local/etc/raspiBackup.conf

      The cloned device has to be configured in the DEFAULT_CLONE_DEVICE option.

> [!Note]
> The clone device will be overwritten by the backup. For this reason, *raspiBackup* performs various checks
> to prevent accidental overwriting of other connected devices,
> and then the cloning process is immediately aborted.
> 1) Only one instance of each cloned device type is allowed. This means, for example, that two /dev/sd or /dev/mmcblk devices are not allowed.
> 2) If multiple cloned device types are to be allowed anyway, the configuration variable `DEFAULT_CLONE_ROOT_PARTUUID` must contain the PARTUUID of the root partition of the cloned device, and it must match.

> [!WARNING]
> In certain configurations, the Raspberry Pi may boot from the clone device after a reboot.
> This can occur especially when booting via USB from a USB hard drive or USB SSD and the cloning device is also connected via USB.

If you want to disable cloning, use the installer to delete the cloned device at `M3->C10` or manualls delete the clone device in the config file.

[.status]: translated
