# Manual tgz restore

The backup directory created by *raspiBackup* contains all information required to restore
this backup also manually with standard Linux tools. The following page describes how to restore a normal tgz backup.

## Create the partitions on the SD card

First of all the SD card has to be plugged in in into a Raspberry which is used to restore the
backup. It usually is detected as /dev/sda or /dev/sdb. Use lsblk to check what's the device
used by the  SD card. In the following description I use /dev/sdb now.

Next mount the backuppartition on a mountpoint. /mnt iis used in the following description for the backup partition
and hostname raspberry and /media for the target SD card partitions.

Now create the partitions with
```
sudo sfdisk /dev/sdb < /mnt/raspberry/raspberry-tgz-backup-20170812-134552/raspberry-backup.sfdisk
```
This will create two partitions.

You can check whether everything is OK with
```
sudo fdisk -l /dev/sdb

Disk /dev/sdb: 7.43 GiB, 7969177600 bytes, 15564800 sectors
Disk model: MassStorageClass
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0xa02ea338Device Boot Start End Sectors Size Id Type
/dev/sdb1 8192 532479 524288 256M c W95 FAT32 (LBA)
/dev/sdb2 532480 15564799 15032320 7.2G 83 Linux
```

## Restore first partition (boot partition)

```
sudo dd of=/dev/sdb1 if=/mnt/raspberry/raspberry-tgz-backup-20170812-134552/raspberry-backup.img
sync
```

You can check whether everything is OK with following commands:i
```
sudo mount /dev/sdb1 /media; ls /media; sudo umount /media
```

You should get a list of all boot files.
```
bcm2708-rpi-b.dtb bcm2708-rpi-zero-w.dtb bcm2710-rpi-3-b-plus.dtb bcm2711-rpi-4-b.dtb config.txt fixup4x.dat issue.txt LICENCE.broadcom start4x.elf
bcm2708-rpi-b-plus.dtb bcm2709-rpi-2-b.dtb bcm2710-rpi-cm3.dtb bcm2711-rpi-cm4.dtb COPYING.linux fixup_cd.dat kernel7.img overlays start_cd.elf
bcm2708-rpi-b-rev1.dtb bcm2709-rpi-cm2.dtb bcm2710-rpi-zero-2.dtb bcm2711-rpi-cm4s.dtb fixup4cd.dat fixup.dat kernel7l.img start4cd.elf start_db.elf
bcm2708-rpi-cm.dtb bcm2710-rpi-2-b.dtb bcm2710-rpi-zero-2-w.dtb bootcode.bin fixup4.dat fixup_db.dat kernel8.img start4db.elf start.elf
bcm2708-rpi-zero.dtb bcm2710-rpi-3-b.dtb bcm2711-rpi-400.dtb cmdline.txt fixup4db.dat fixup_x.dat kernel.img start4.elf start_x.elf
```

## Restore second partition (root partition)

Now format the second partition with
```
sudo mkfs.ext4 /dev/sdb2
```

You can check whether everything is OK with following commands:
```
sudo mount /dev/sdb2 /media; df -h /media
```

You should get something like
```
Filesystem Size Used Avail Use% Mounted on
/dev/sdb2 7.0G 24K 6.6G 1% /media
```

Now restore the tgz Backup on the partition created just now:

```
sudo tar --exclude /boot --same-owner --same-permissions --numeric-owner -x -v -z -f /mnt/raspberry/raspberry-tgz-backup-20170812-13455/raspberry-tgz-backup-20170812-134552.tgz -C /media
sudo umount /media
sudo umount /mnt
```

During the restore you should see the list of all files restored.

## Boot the restored system

Now remove the target SD card, insert it in another Raspberry and boot the Raspberry with the restored backup.

[.status]: rst
[.source]: https://www.linux-tips-and-tricks.de/en/raspibackupcategorye/646-raspibackup-manual-restore-of-a-tgz-backup

