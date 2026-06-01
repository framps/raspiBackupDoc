# Create a clone at the end of a backup

> [!NOTE]
> This feature is available starting with *raspiBackup* version 0.7.3 and as of now in Beta

*raspiBackup* can restore a backup to a locally connected device immediately after creating it.
This provides a backup that can be used right away to immediately restart a failed device or an OS that no longer boots
by switching the boot medium. Without this feature, an existing backup must first be restored
and requires more time. If the rsync backup type is used, the restore is simply a synchronization with the backup and
completes very quickly. A tar backup type always is a full restore of the backup and therefore takes much longer.

Only the rsync and tar backup types, as well as both backup modes, are supported.

> [!NOTE]
> In the following, the clone device is assumed to be `/dev/sda`. Other examples would be `/dev/mmcblk1` or `/dev/nvme1n1`.
> Additionally, a PARTUUID of `2a6bd249-01` is assumed.

Steps to enable cloning:

1) Create a backup

2) Restore the backup to the clone device `/dev/sda`

3) List the PARTUUIDs of the clone device using `blkid | grep "/dev/sda"` and select a PARTUUID. For example, `2a6bd249-01`.

4) Enable cloning

   1) Manually edit the configuration file /usr/local/etc/raspiBackup.conf

      In the `DEFAULT_CLONE_DEVICE` option, the clone device `/dev/sda` must be specified, and a PARTUUID must be configured in the `DEFAULT_CLONE_PARTUUID` option.

   2) Installer

      In the installer, the `<clone device>` and the PARTUUID must be configured as `M3->C10`. The PARTUUID
 must be separated from the clone device by spaces.

      **Note**: The cloning device must be connected.

5) Creating a backup and a clone

   1) Command line

      At the command line, specify the option `--clone <clone device>` when starting the backup. `<clone device>`
refers to the locally connected device to which the current backup is to be synchronized or restored. In the example, it would be `--clone /dev/sda`

      **Note**: A PARTUUID must have been configured beforehand.

   2) Regular automatic invocation

      If the installer is configured to run on a regular basis, a backup and a clone are automatically created at regular intervals.

> [!IMPORTANT]
> The following checks are performed to prevent accidental overwriting of other connected devices:
> 1) The configuration variable `DEFAULT_CLONE_PARTUUID` must match the PARTUUID of a partition on the cloned device.
> 2) The partitioning of the clone device must match the partitioning of the running system. The size of the last partition may differ.

> [!CAUTION]
> In certain configurations, the Raspberry Pi may boot from the cloning device after a reboot.
> This can occur particularly when booting via USB from a USB hard drive or USB SSD and the cloning device is also connected via USB. Thorough testing is essential in such cases.

If you want to disable the creation of a clone, you must use the installer to delete the clone device and the PARTUUID at `M3->C10`, or do so manually in the configuration file.

[.status]: translated
