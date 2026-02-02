# Restore Introduction

*raspiBackup* provides **complete** restores, i.e. all partitions are usually restored.

In contrast, in partition-oriented mode, the partitions to be restored can be selected
and thus only parts can be restored.

During a restore, new partitions are created on the target data device (SD card, USB disk, ...)
and then with the appropriate tool (`dd`, `tar` or `rsync`)
the data is restored there.

The target data device must therefore not the currently used operating system.
It must be another card, USB disk, SSD or NVMe device connected with a card reader.

A restore requires a **Linux system**for a tar or rsync backup. You should usually use a Raspberry for this. Other Linux systems
also work, but it is not 100% guaranteed that they will always work.

If an external root file system has been backed up (hybrid boot mode), it will also be restored to an external device.
(Only in normal backup mode with `tar` or `rsync` backup).

A [manual restore](manual-restore.md) of the data with the previously used backup tools `dd`, `tar` or `rsync` is of course also possible.
It is also possible to restore individual files (manually),
especially with the `rsync` backup.

The backup script can also be used to clone systems:
A backup is created and then restored to another device.
A typical application is to copy an SD card to an SSD or NVMe
and then operate the system with the SSD/NVMe and no longer with an SD card.

For a complete list of all restore options see [here](restore-options.md).

------------------

Further topics on this page:

<!-- toc -->

------------------


## Recovery scenario with a Raspberry with Raspberry Pi OS

Any backup can be restored using the Raspberry Pi.

1. Start a *Raspberry Pi OS* on the Raspberry

1. Install *raspiBackup

1. Connect the system device to which the backup is to be restored (e.g. an SD card with an SD card reader or SSD).

1. Connect the medium that contains the backup (e.g. a hard disk)
   and mount it or mount a network drive with the backup data.

1. If the root partition is located on an external partition (hybrid boot mode), connect another device with a pre formatted partition
   which will get the external partition been restored

1. Start *raspiBackup* for restore to the [device](#devicenames).

This is usually used:

  - The system device `/dev/sda`
  - The backup partition `/dev/sdbx`
  - And a possible root partition `/dev/sdcx`.


If a network drive is used, the root partition is usually `/dev/sdbx`.

The actual device assignment may differ and should **always** be checked,
to avoid other partitions being overwritten by mistake.

E.g. with

```
sudo parted -l
```


## Restore scenario for Windows users on a Windows system

Only a `dd` backup can (also) be restored directly under Windows,
with the [Win32DiskImager](http://sourceforge.net/projects/win32diskimager/).

## Restore scenario for Linux users

``` admonish note title="Note"
In principle, any Linux OS can be used to restore a backup.
But with possible incompatibilities of its tools, compared to the Linux tools used for the backup
Linux tools used for the backup, there may be problems.
An occasional candidate for this is `sfdisk`,
which has changed to be incompatible with both *Jessie* and *Bullseye*.

Therefore:

**A restore should always be performed with the same OS that was used to create the backup.
the backup was created**.
```

The device to which the backup is to be restored is connected to the Linux system,
the backup partition is mounted
and a partition is provided for any external root file system in hybrid boot mode.

Then start *raspiBackup* to restore to a [device](#devicenames).

If no Raspberry Pi OS and/or no Raspberry Pi is used,
the option [--unsupportedEnvironment](general-options.md#parm_unsupportedEnvironment) must be specified.

See also [Supported hardware and software](supported-hardware-and-software.md).


## Example calls

Hardware required for the restore:

1. A running Raspberry Pi with a running *Raspberry Pi OS* or another
   Linux operating system or another Linux computer with *raspiBackup* installed.

1. A connected target device of the backup

1. A connected backup device (via USB or network)

1. If an external root partition is to be restored or the USB boot mode is used where no
   mode is used where an SD card is no longer used, another disk must be connected via USB.
   another disk must be connected

Similarities of the example calls:

1. The backed up system is called "raspberrypi" in the example call.
1. The **target** disk that is to receive the restore of the boot/boot and root partition
   boot and root partition is available in the example as `/dev/sdf`.
   [Further below](#devicenames) is described how to find out the current value for `-d`
1. **Attention**: All existing data on the **target** data carriers will be deleted after a confirmation prompt
   from *raspiBackup* before the restore.
1. The backup to be restored is available under
   `/remote/raspifix/disks/backup/rsync/raspberrypi/raspberrypi-rsync-backup-20141230-213032/`


### Restore to an SD card

```
sudo raspiBackup.sh -d /dev/sdf /remote/raspifix/disks/backup/rsync/raspberrypi/raspberrypi-rsync-backup-20141230-213032/
```

### Restore to a USB device without SD card (USB boot mode)

```
sudo raspiBackup.sh -d /dev/sdf /remote/raspifix/disks/backup/rsync/raspberrypi/raspberrypi-rsync-backup-20141230-213032/
```

### Restore to an SD card and an external partition (hybrid boot mode)

1. To receive the restore of the external root partition, a correspondingly large partition `/dev/sda` was created on `/dev/sda`.
   Formatting is not necessary.

```
sudo raspiBackup.sh -d /dev/sdf -R /dev/sda1 /remote/raspifix/disks/backup/rsync/raspberrypi/raspberrypi-rsync-backup-20141230-213032/
```

<a name="devicenames"></a>
## How to find out the device names of the external SD card and external disk?

Enter the following command on the Raspberry:

```
fdisk -l | egrep "^Disk /|^/dev"
```

The output then looks like this, for example:

```
pi@raspberrypi:~# sudo fdisk -l | egrep "^Disk /|^/dev"
Disk /dev/mmcblk0: 8011 MB, 8011120640 bytes
/dev/mmcblk0p1 8192 122879 57344 c W95 FAT32 (LBA)
/dev/mmcblk0p2 122880 15646719 7761920 83 Linux
Disk /dev/sda: 15.5 GB, 15548284928 bytes
Disk /dev/sdb: 300.1 GB, 300069052416 bytes
/dev/sdb1 1 586072367 293036183 ee GPT
```

Here you can see that

  - The internal SD card `/dev/mmcblk0` is 8GB in size
  - The new external SD card `/dev/sda` is 16GB in size
  - The external disk `/dev/sdb`, to which the root partition is to be moved,
    300GB in size and has a partition `/dev/sdb1`.

The parameter for `-d` is therefore `/dev/sda` (external SD card).

If an external root partition was also backed up, `-R /dev/sdb1` (external root partition) is also required
(hybrid boot mode).

The parameters must of course be adapted to the local conditions.


**Note**:

A backup should be tested regularly: Whether the restore still works
and still contains all data.

Nothing is more frustrating when, at the moment you need the backup,
the backup is corrupt or does not contain all the data...

A test is quite simple with the Raspberry:

Insert a new SD card, restore the backup and boot from the new SD card.
If no SD card is used, e.g. an SSD, the restore test can also be performed with a hard disk.
as long as it is large enough to hold all the data on the SSD.

If for any reason the restore with the script fails, you can of course
at any time use the standard
Linux tools that were used for the backup - `dd`, `tar` or `rsync` - to manually
restore. However, this is not quite as convenient as with the script
and appropriate Linux knowledge is required ;-)
See also [Manual restore of a backup](manual-restore.md).

[.status]: translated
[.source]: https://linux-tips-and-tricks.de/de/raspibackup#restore
[.source]: https://linux-tips-and-tricks.de/de/wiederherstellen


