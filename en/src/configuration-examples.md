# Application and configuration examples

Various application examples of
*raspiBackup* and their configuration are presented and explained. They are intended to
help you to find the right one from the multitude of possible applications or
customize the example according to your own requirements. An
overview of all options can be found in [Call and options](backup-options.md).
Various methods for restoring a backup are described in the [Restore](restore.md) chapter.

There are also configuration examples for various e-mail clients on the following pages:
   - msmtp
   - exim4
   - nullmailer

## Application examples

<!-- toc -->

### A Windows user wants to be able to back up his Raspberry and restore it to Windows.

To be able to restore an image under Windows, a dd
image of *raspiBackup* must be created. The following configuration options are
at least necessary:

```
DEFAULT_BACKUPTYPE=dd
DEFAULT_KEEPBACKUPS=n
```

## A Windows user has a 32GB SD card and only uses 12GB of it, which he only wants to back up

In addition to the options mentioned, the following option is required:

```
DEFAULT_DD_BACKUP_SAVE_USED_PARTITIONS_ONLY=1
```

However, it is also necessary to shrink the root partition of the Raspberry
Raspberry, as the entire free space on the SD card is backed up by default.
However, this is not possible under Windows, but a Linux system must be used
and use the tools `gparted` or `resize2fs` to shrink the root partition.

## A Windows user wants to create an absolutely minimal image with pishrink

To create a minimal backup, you can use the *pishrink* tool. For this purpose
there is the script `raspiBackupWrapper.sh`, with which at the end of the backup
the dd image via *pishrink* at the end of the backup. The option

```
DEFAULT_ZIP_BACKUP=1
```

also reduces the size of the image, but this cannot be restored directly
under Windows. It must first be unzipped.

## A Raspberry should be backed up as quickly as possible. The backup partition is an EXT4 file system mounted via NFS, which is provided by a NAS

First, the backup partition of the NAS must be mounted. This should be done in
`/etc/fstab` the NFS partition should be defined and automatically mounted under `/backup`.

```
DEFAULT_BACKUPTYPE=rsync
DEFAULT_KEEPBACKUPS=n
```

Since the backup file system is formatted with EXT4, *raspiBackup* can use hardlinks
and this speeds up the backup process a lot, as only the changed files are backed up.
files are backed up.

An example entry in `/etc/fstab` could look like this:

```
asterix:/backup /backup nfs users,rw,sync,hard,intr,noauto,user 0 0
```

where "asterix" is the hostname of the NAS and "/backup" is the exported NFS
mount. Further information on Synology-specific settings and
solutions can be found [here](nfs-as-backuptarget.md)


## A Raspberry is to be backed up to a file system mounted via SMB, which is provided by a Windows system

```
DEFAULT_BACKUPTYPE=tar
DEFAULT_KEEPBACKUPS=n
```

The remote Windows backup file system should be defined in `/etc/fstab` and
be mounted automatically. The entire system is backed up each time.
Please note that the file system on the SMB drive must support files larger
than 4GB, because the tar files are usually over 4GB in size. FAT32 is not
is not sufficient. See also [Which filesystem can be used on the backup partition](which-filesystem-can-be-used-on-the-backup-partition.md)

An example entry in `/etc/fstab` could look like this:

```
//asterix/backup/ /backup cifs noauto,noatime,user,utf8,umask=000,uid=1000,gid=1000,credentials=/etc/samba/auth.asterix.cifsuser 0 0
```

## A major change to the Raspberry is intended and various intermediate states should be backed up for security reasons

This requires a finished configuration of *raspiBackup* (see
previous examples). Then *raspiBackup* only needs to be configured with the option

```
-M "This is a descriptive name of the backup"
```

and a backup with exactly this descriptive name will be created in the backup directory `/backup`.

**Note**: This backup is a so-called [snapshot](snapshots.md) and is ignored during the backup recycle.
The backup can be deleted manually if required.

## A USB boot system is to be backed up with additional partitions

In this case, the partition-oriented backup is selected and the partitions to be
partitions to be backed up are configured. In the example, partition 5
should also be backed up.

```
DEFAULT_PARTITIONBASED_BACKUP=1
DEFAULT_BACKUPTYPE=rsync
DEFAULT_KEEPBACKUPS=n
DEFAULT_PARTITIONS_TO_BACKUP="1 2 5"
```


## A Raspberry is to be backed up to a locally connected USB stick or a locally connected USB disk

```
DEFAULT_BACKUPTYPE=rsync
DEFAULT_KEEPBACKUPS=n
DEFAULT_BACKUPPATH="/USBStick"
```

In order for `rsync` to use hardlinks and for the backup to be fast, the
backup partition must be formatted with ext3/4. If you want to exchange data with Windows
and the partition was formatted with Windows, use `tar` as the backup type.
backup type. However, the backup will then take longer and
and requires considerably more space.

**Note**: If the USB partition is to be accessible from Windows, it must be formatted with NTFS.
In this case, however, no backup type `rsync` is possible. NTFS can only be used with the backup types `dd` and `tar` and
the DEFAULT_BACKUPTYPE must then be set accordingly.

An example entry in `/etc/fstab` could look like this:

```
LABEL=usb /USBStick ext4 defaults,noatime,nofail 0 2
```
[.status]: translated
[.source]: https://linux-tips-and-tricks.de/de/konfigurationsbeispiele
[.source]: https://www.linux-tips-and-tricks.de/en/configuration-samples


