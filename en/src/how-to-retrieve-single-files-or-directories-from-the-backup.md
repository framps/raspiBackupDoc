# Restore individual files/directories from a backup

Sometimes a complete restore of the entire system is not required, but only
individual file(s) or directories.
This is not directly supported by *raspiBackup*.
Since *raspiBackup* only uses standard Linux tools to restore the entire system,
this can be done manually for all backup types.

However, these activities must be carried out on a Linux system.

The easiest way to do this is with rsync backups. dd and tar backups require a few
additional steps on the command line.


## dd backup

First, the dd image file must be made available.

In the following example, the USB disk partition is `/dev/sda1` and is mounted to
`/mnt` mounted with:

```
sudo mount -o ro /dev/sda1 /mnt
```

Search there for the desired backup generation and the image file.

Next, determine the sector offset in the image file with fdisk.

```
sudo fdisk -l raspberrypi-dd-backup-20160415-222900.img

Disk raspberrypi-dd-backup-20160415-222900.img: 7.5 GiB, 8011120640 bytes, 15646720 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk label type: dos
Disk identifier: 0x000798a3

Device Boot Start End Sectors Size Id Type
raspberrypi-dd-backup-20160415-222900.img1 8192 122879 114688 56M c W95 FAT32 (LBA)
raspberrypi-dd-backup-20160415-222900.img2 122880 15646719 15523840 7.4G 83 Linux
```

So there are 8192 for the first partition and 122880 for the second partition.

Now the partition is mounted after `/media`, in the example the second, the root partition.
Note: The offset must be multiplied by the sector size, in this case 512.

```
sudo mount -o ro,norecovery,loop,offset=$((122880*512)) raspberrypi-dd-backup-20160415-222900.img /media
```

You can now access all the backup data in the `/media` directory.

```
ls /media/

backup boot dev home lost found mnt proc root sbin srv tmp var
bin boot.bak etc lib media opt remote run selinux sys usr
```

Unmount the partition to exit:

```
sudo umount /media
sudo umount /mnt
```


## tar backup

First the tar file must be made available.

In the following example, the USB disk partition is `/dev/sda1` and is mounted to `/mnt` with :

```
sudo mount -o ro /dev/sda1 /mnt
```

Assume that the entire directory `/etc` in the tar file is to be accessed.
This can be done with the following command.

```
tar -xf raspberrypi-tar-backup-20171028-205746.tar -C /tmp etc
```
But you have to be patient, because depending on the size of the tar file, this can take some time.

Finally, the `/etc` directory has been extracted from the tar file to `/tmp`. Access is now possible there.


## rsync backup

Access to the rsync backup directory must be available at the beginning.

In the following example, the USB disk partition is `/dev/sda1` and is mounted to `/mnt` with :

```
sudo mount -o ro /dev/sda1 /mnt
```

The contents can now be accessed directly:

```
cd /mnt/backups/raspberrypi/raspberrypi-rsync-backup-20160705-212724-8G

ls -la

total 57592
drwxr-xr-x 26 pi pi 4096 Jul 5 2016 .
drwxr-xr-x 14 root root 4096 Apr 18 2018 ...
drwxr-xr-x 2 root root 4096 Nov 15 2015 backup
drwxr-xr-x 2 root root 4096 May 29 2016 bin
drwxr-xr-x 2 root root 4096 Jan 1 1970 boot
drwxr-xr-x 3 root root 4096 Apr 20 2014 boot.bak
drwxr-xr-x 2 root root 4096 Jul 4 2016 dev
drwxr-xr-x 125 root root 12288 Jul 5 2016 etc
drwxr-xr-x 3 root root 4096 Feb 1 2015 home
drwxr-xr-x 16 root root 4096 May 29 2016 lib
drwx------ 2 root root 4096 Dec 15 2012 lost found
drwxr-xr-x 2 root root 4096 Jul 3 2016 media
drwxr-xr-x 2 root root 4096 Jan 8 2014 mnt
drwxr-xr-x 3 root root 4096 Mar 1 2015 opt
-rwxr-xr-x 1 pi pi 126799 Jul 5 2016 pi
dr-xr-xr-x 2 root root 4096 Jan 1 1970 proc
drwx------ 2 root root 4096 Jul 10 2013 .pulse
-rw------- 2 root root 256 Dec 16 2012 .pulse-cookie
-rw-r--r-- 1 root root 58720256 Jul 5 2016 raspberrypi-backup.img
-rw-r--r-- 1 root root 512 Jul 5 2016 raspberrypi-backup.mbr
-rw-r--r-- 1 root root 273 Jul 5 2016 raspberrypi-backup.sfdisk
drwxr-xr-x 4 root root 4096 Aug 15 2013 remote
drwx------ 13 root root 4096 Jul 3 2016 root
drwxr-xr-x 2 root root 4096 Jul 5 2016 run
drwxr-xr-x 2 root root 4096 May 29 2016 sbin
drwxr-xr-x 2 root root 4096 Jun 20 2012 selinux
drwxr-xr-x 3 root root 4096 Mar 7 2014 srv
dr-xr-xr-x 2 root root 4096 Jul 4 2016 sys
drwxxrwxrwx 2 root root 4096 Jul 5 2016 tmp
drwxr-xr-x 10 root root 4096 Dec 15 2012 usr
drwxr-xr-x 12 root root 4096 Jul 8 2014 var
```

[.status]: translated
[.source]: https://www.linux-tips-and-tricks.de/en/raspibackupcategorye/596-how-to-retrieve-single-files-or-directories-from-the-backup



