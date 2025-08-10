# Manueller Restore eines rsync Backups

Ein von *raspiBackup* erstelltes Backup enthält alle für einen Restore
notwendigen Informationen und kann manuell restored werden.

Ein *raspiBackup* Nutzer wollte aus verschiedenen Gründen einen rsync Backup
manuell restoren und hat das freundlicherweise detailliert beschrieben.

```
# Manuelles Anlegen der Partitionen:
sfdisk /dev/sdb < /backup/pi/pi-rsync-backup-20170812-134552/pi-backup.sfdisk

# MBR restoren:
dd of=/dev/sdb if=/backup/pi/pi-rsync-backup-20170812-134552/pi-backup.mbr count=1
sync

# Inform the operating system about partition table changes:
partprobe /dev/sdb

# Root-Partition formatieren & mounten:
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

# rsync-Restoren:
rsync --numeric-ids -aAHXv --exclude=/pi-backup.* /backup/pi/pi-rsync-backup-20170812-134552/mmcblk0p1/ /mnt/sdb1
rsync --numeric-ids -aAHXv --exclude=/pi-backup.* /backup/pi/pi-rsync-backup-20170812-134552/mmcblk0p5/ /mnt/sdb5
rsync --numeric-ids -aAHXv --exclude=/pi-backup.* /backup/pi/pi-rsync-backup-20170812-134552/mmcblk0p6/ /mnt/sdb6
rsync --numeric-ids -aAHXv --exclude=/pi-backup.* /backup/pi/pi-rsync-backup-20170812-134552/mmcblk0p7/ /mnt/sdb7

# Fake-HW-Clock patchen:
# logItem "Updating hw clock"
echo $(date -u +"%Y-%m-%d %T") > /mnt/sdb7/etc/fake-hwclock.data

# logItem "Syncing filesystems"
sync

# umount all recovery-folders:
umount /mnt/sdb*

# SD-Karte auswerfen:
eject /dev/sdb

# Mount-Verzeichnisse aufräumen:
rmdir /mnt/sdb*

# SD-Karte in Pi stecken und testen!!!
# Boing! geht :-)
```

[.status]: rst
[.source]: https://www.linux-tips-and-tricks.de/de/raspibackupcategoried/497-raspibackup-manueller-restore-eines-backups
[.source]: https://www.linux-tips-and-tricks.de/en/raspibackupcategorye/498-raspibackup-manual-restore

