# Manual restore of an rsync backup

A backup created by *raspiBackup* contains all the information required for a restore
and can be restored manually.

For various reasons, a *raspiBackup* user wanted to restore a rsync backup
manually and has kindly described this in detail.

```
# Manually create the partitions:
sfdisk /dev/sdb < /backup/pi/pi-rsync-backup-20170812-134552/pi-backup.sfdisk

# Restore MBR:
dd of=/dev/sdb if=/backup/pi/pi-rsync-backup-20170812-134552/pi-backup.mbr count=1
sync

# Inform the operating system about partition table changes:
partprobe /dev/sdb

# Format and mount root partition
mkfs -t vfat /dev/sdb1
mkfs -t vfat /dev/sdb6
mkfs.ext4 /dev/sdb5
mkfs.ext4 /dev/sdb7

mkdir -p /mnt/sdb1
mkdir -p /mnt/sdb5
mkdir -p /mnt/sdb6
mkdir -p /mnt/sdb7

mount /dev/sdb1 /mnt/sdb1
mount /dev/sdb5 /mnt/sdb5
mount /dev/sdb6 /mnt/sdb6
mount /dev/sdb7 /mnt/sdb7

# udevadm settle waits for udevd to process the device creation events for all hardware devices, thus ensuring that any device nodes have been created successfully before proceeding:
udevadm settle

# rsync-Restore:
rsync --numeric-ids -aAHXv --exclude=/pi-backup.* /backup/pi/pi-rsync-backup-20170812-134552/mmcblk0p1/ /mnt/sdb1
rsync --numeric-ids -aAHXv --exclude=/pi-backup.* /backup/pi/pi-rsync-backup-20170812-134552/mmcblk0p5/ /mnt/sdb5
rsync --numeric-ids -aAHXv --exclude=/pi-backup.* /backup/pi/pi-rsync-backup-20170812-134552/mmcblk0p6/ /mnt/sdb6
rsync --numeric-ids -aAHXv --exclude=/pi-backup.* /backup/pi/pi-rsync-backup-20170812-134552/mmcblk0p7/ /mnt/sdb7

# Fake-HW-Clock patch:
# logItem "Updating hw clock"
echo $(date -u +"%Y-%m-%d %T") > /mnt/sdb7/etc/fake-hwclock.data

# logItem "Syncing filesystems"
sync

# umount all recovery-folders:
umount /mnt/sdb*

# Eject SD card:
eject /dev/sdb

# Clean up mount directories:
rmdir /mnt/sdb*

# Insert SD card into Pi and test!!!
# works :-)
```

[.status]: translated
[.source]: https://www.linux-tips-and-tricks.de/de/raspibackupcategoried/497-raspibackup-manueller-restore-eines-backups
[.source]: https://www.linux-tips-and-tricks.de/en/raspibackupcategorye/498-raspibackup-manual-restore


