# Error messages and -search

It can happen that *raspiBackup* does not run successfully and writes error messages.
writes error messages. This is 90% of the time due to incorrect
configurations or parameterization.

There are three types of *raspiBackup* messages:

1. Information. The message number ends with the letter "I"
1. Warnings. The message number ends with the letter "W"
1. Error. The message number ends with the letter "E"

The error messages are self-explanatory and should indicate the specific cause.
If not, the following measures will help to localize the error more precisely:

1. Start *raspiBackup* in the command line and not automatically via systemd in order to
   exclude systemd misconfigurations

1. A log file `raspiBackup.log` is created in the backup directory with every successful run
   which contains a lot of detailed information and helps to find the causes of errors.
   Searching for error messages and causes in this log file can help to localize the error,
   localize the error.

   If the backup aborts with errors, the log file is saved to the home directory of the caller before it is cleaned up.
   to the home directory of the caller.

   Furthermore, the parameter `-v` can also help if errors occur in the
   Linux backup tools occur.

1. If the information in the log file does not help you to find the cause of the error yourself
   itself, it is possible to report the error.
   See the notes in [FAQ12](faq.md#faq12) on how to report problems.

---

In some cases, further explanations are required for the error messages.
These can be found below.

*raspiBackup* has about 200 error messages and to list them here completely
and explain them in detail is a lot of work.

So if you are looking for an explanation for an error message and cannot find it here,
should first use a search engine and look for the error message number.
error message number. If this does not lead to success, an issue should be created in [*GitHub*](https://github.com/framps/raspiBackup/issues)
and then it will be added here. In this way, all frequent and important
error messages of *raspiBackup* will be collected and explained here.

Messages in the number range 0-999 are written by *raspiBackup*.
Messages from 1000-1999 are written by the example extensions. All
other number ranges can be used by your own extension messages.

In addition, *raspiBackup* exits with an error code that indicates the cause of the error.
indicates the cause. A list of error codes can be found at the [end of this page](#exitcodes).

## *raspiBackup* - Error messages, causes and actions

<!-- toc -->

### RBK0005E: Backup terminated with errors. See previous error messages.

Cause:

*raspiBackup* ended with an error and did not create a backup. A debug log was created in the home directory of the caller.

Further actions:

A preceding error message describes the exact cause of the termination. Search for this and rectify the cause.


### RBK0013E: There are more than two partitions that can only be backed up with backup type DD or DDZ or the -P option

Cause:

*raspiBackup* only backs up the first two partitions in normal backup mode. If more partitions exist, this message is displayed.

Further actions:

Either delete the other partitions or use the option
`--ignoreAdditionalPartitions`. This explicitly states that further partitions
partitions exist but may NOT be backed up. Alternatively you can
back up everything with the backup type `dd` or use the partition-oriented mode.

### RBK0015E: An instance of *raspiBackup* is already active.

Cause:

*raspiBackup* prevents it from being started several times in parallel. Either
*raspiBackup* is still running or the previous *raspiBackup* run terminated with an error and the lock
an error and the lock was not removed.

Further actions:

With `ps -ef | grep raspiBackup` you can check whether *raspiBackup* is currently running.
If yes, you have to wait until *raspiBackup* has finished.
If not, the lock file must be deleted with `sudo rm /var/lock/raspiBackup`.

### RBK0019E: Option -a and -o not specified.

Cause:

*raspiBackup* allows a running system to be backed up. Before the backup
all important running services should be stopped and restarted at the end,
to avoid creating an inconsistent backup. If you have not defined any services to be stopped and
services to be stopped and started via the installer, the services must be specified with the
both options in the call.

These options can be configured with the *raspiBackup* installer for Systemd services.

Further actions:

The two options with corresponding parameters must be specified when calling
or the services must be defined with the installer in the configuration file.
must be defined with the installer. Details can be found in [FAQ18](faq.md#faq18).


### RBK0020E: File system of the rsync backup directory %s does not support softlinks.

Cause:

A backup file system that is to record an `rsync` backup must support softlinks
must support soft links. This is only supported by *EXT2*, *EXT3* and *EXT4*. *FAT32* or *NTFS*
do not support them. Details can be found in [FAQ19](faq.md#faq19)

Further actions:

Either the backup partition must be formatted with EXT2, 3 or 4 or another backup type such as
another backup type such as `dd` or `tar` must be used.


### RBK0021E: Backup program of type %1 terminated with RC %2.

Cause:

A backup program (`dd`, `tar` or `rsync`) used by *raspiBackup*,
has received an error. The RC indicates the error code. Usually
the backup program writes a more detailed message that helps to find the cause.
find the cause.

Further actions:

RC 1 at dd Backup reports a read or write error of a file. An RC 1
for tar and RC 23 or RC 24 for rsync means that a file has changed during the backup.
changed during the backup.

RC 2 for tar means that some serious error has occurred. It is also possible
permissions are missing on the backup device or there is no free space on the backup partition.
is available on the backup partition.

RC23 on rsync can also be an access problem or an ACL problem with NFS.
See [FAQ24](faq.md#faq24) for the ACL problem and NFS.

The corresponding error messages from the backup tool can be found if the lines following the
executeCmd command in the debug log and they are also displayed
displayed on the console or in the e-mail.

Previous messages show the exact error message of the backup program.
If these do not help to find the cause, the `-v` option can be used with tar and
rsync can be used to get detailed messages from the backup programs in the
debug log, which will hopefully help.

Or you can add

```
DEFAULT_RSYNC_BACKUP_ADDITIONAL_OPTIONS="--info=NAME0"
```

in the *raspiBackup* config file for rsync to log only error messages and
and avoid a detailed log, which you get with option -v.

After that, it often helps to enter the error message in a search engine,
to find the cause. On the [FAQ page](faq.md) there are many error messages and their
their causes and troubleshooting measures. With rsync you will find in the
debug log after calling rsync all error messages from rsync and can use them to
the cause of the termination.

Alternatively, you can have tar and rsync ignore errors. See [FAQ32](faq.md#faq32).

However, the backup partition is also often the cause - especially if it is a partition connected via the network
connected partition (NFS, SMB) - is the problem. Mostly it is
network problems or misconfigurations. It has also happened that the
partition was on a device that had write errors.

If there is a read error, this is an indication that the system device or SD card
should be replaced. To do this, restore the last backup to a new system device.

If the backup partition is mounted via NFS, read [this article](https://www.linux-tips-and-tricks.de/de/raspibackupmeldungen/2-uncategorised/605-wie-kann-man-acls-mit-rsync-auf-nfs-gemounteten-partitionen-sichern).

If authorization problems exist, it must be ensured that the
user root has all rights on the backup device.

### RBK0027E: No external device connected to %1. The SD card would be used for the backup.

Cause:

*raspiBackup* checks whether an external partition is mounted on the backup path, because
if not, the backup would be stored on the SD card, which makes no sense
and if the SD card is small, it will overflow.

Further actions:

Now be %1 `/backup` which is the default path. In this directory
an external backup device must be mounted.
A corresponding entry in `/etc/fstab` can be used to connect the mount point `/backup` to an external partition.
to an external partition. You can check this with

```
findmnt /backup
```

If you know what you are doing, you can switch off the error message with the option -c
option.


### RBK0028E: %s is not a recovery directory of $MYNAME."

Cause:

*raspiBackup* creates a directory on the backup partition with the host name of the
the host name of the backed up system and the respective backups are stored in subdirectories under it.
Such a backup subdirectory must be specified.

The format of the backup directory has the following appearance:

  - `troubadix@raspbian12-rsync-backup-20250615-050123`

Further actions:

Specify a correct backup directory.


### RBK0030E: %s file creation with dd ends incorrectly with RC %s.

Cause:

An error occurred when creating a file with dd. RC 1 means a read or write error.
or write error.

Further actions:

When restoring, the SD card is almost certainly corrupt and another SD card should be used.
should be used. There are write problems on the backup medium during the backup,
which must be solved. Previous messages from the backup tool provide
further indication of the cause of the error.


### RBK0039E: Mail Program %s is not installed to send email.

Cause:

The configured mail program for sending e-mails was not found.
found. The error usually occurs if *Postfix* or
*nullmailer* has been set up as MTA.

Further actions:

Install the configured e-mail program or install bsd-mailx or mailutils
install.


### RBK0047E: An error occurred when starting services. RC %s.
### RBK0048E: An error occurred while stopping services. RC %s.

Cause:

The commands of the -a/-o option or the configuration parameter
DEFAULT_STARTSERVICES/DEFAULT_STOPSERVICES, which are to start/stop services,
generate an error.

Further actions:

You have to find out which of the start commands/stop commands has an error.
Therefore, enter each start command/stop command once using `sudo` and watch for error messages.
for error messages. The cause of the error message must then be eliminated.

### RBK0051W: Target %s with %s is larger than 2TB and requires gpt instead of mbr. Otherwise only 2TB are used.

Cause:

The destination partition is larger than 2TB and therefore *GPT* partitioning is required on it.
If the backup only has one MBR, the target partition can only be extended up to 2TB.

Further actions:

The system to be restored still uses *MBR* and must be converted to *GPT*.
Then another backup must be created - this time with *GPT*. This can then be
be restored to disks larger than 2TB.

### RBK0061E: No boot partition files found in %s that start with %s.

Cause:

*raspiBackup* searches for the boot partition backup in the backup directory and
does not find it.

Further actions:

A directory was specified as the backup directory which contains no or incomplete backup data.
incomplete backup data. It is documented in the [Backup directory structure](backup-directory-structure.md) chapter,
which files must be in the backup directory.
A backup directory always begins with the host name of the Raspberry followed
followed by the backup type and the creation date of the backup.
Examples: `raspberrypi-dd-backup-20160415-222900` oder
`raspberrypi-rsync-backup-20160416-094106`


### RBK0077E: Restore was terminated with errors. See previous error messages.

Cause:

There were errors during the restore. This can either be when creating the partitions
or during the actual restore of the backup data.

Further actions:

First check any previous error messages. Then check the debug log
to check whether there were any problems when creating the partitions.  To do this, search for `Checking
that no-one is using this disk right now` and error messages. There
there is a known problem with a new sfdisk version in Bullseye when
a backup of such a system is restored on a Linux with an older sfdisk
version is restored. The error message is

```
>>> line 5: unsupported command
```
The solution to this is to either use a Linux with the sfdisk version of Bullseye

```
sfdisk --version
sfdisk from util-linux 2.36.1
```

or manually delete the 5th line in the file with the extension .sfdisk in the backup directory.


### RBK0086E: Restore device must not be a partition.

Cause:

*raspiBackup* wants to create partitions when restoring the backup
create partitions. To do this, the entire device must be specified as the
as the target device. A single partition is not allowed.

Further actions:

Instead of e.g. `/dev/sdb1`, which is a single partition, e.g.
`/dev/sdb` must be specified. But ATTENTION: All data on the SD card
will then be overwritten. So make sure beforehand that no other data
on other partitions are still required. See also [this page](restore.md) for
recovery.

### RBK0087E: Restore directory %s was not created by *raspiBackup*.

Cause:

*raspiBackup* generates a backup directory which follows a specific format.
format. Its format must be as follows:
`<hostname>-<backuptype>-backup-<date>-<time>`.
For more information, see chapter [Backup directory structure](backup-directory-structure.md).

Further actions:

The backup directory must be renamed according to the above form.


### RBK0105I: New backup directory %1 is deleted.

Cause:

An error occurred and *raspiBackup* deletes the empty or inconsistent new backup directory.
new backup directory.

Further actions:

A previous message indicates an error that must be rectified.


### RBK0109E: Unsupported file system %s on partition %s.

Cause:

*raspiBackup* does not support this file system format

Further actions:

Create an issue in *GitHub* and it may be,
that the filesystem support is then built into *raspiBackup*.


### RBK0142E: Boot device cannot be recognized.

Cause:

*raspiBackup* cannot recognize the boot device. This usually happens when a hardware
hardware other than a Raspberry is used or an operating system other than
operating system other than *Raspberry Pi OS* or *Ubuntu* is used.

Further actions:

Report the problem on *GitHub*.


### RBK0147E: Backup of partition %1 failed with RC %2.

Cause:

*raspiBackup* has received an error from the backup program used when
backing up a partition in partition-oriented mode.

Further actions:

See RBK0021E


### RBK0150W: Maximum file size in backup directory %s is limited to 4GB.

Cause:

The file system of the backup partition only allows file sizes up to 4GB and is virtually unusable for backups.
almost unusable for backups.

Further actions:

Another file system must be created on the backup space. Which one this
must be depends on the backup method. On [this page](which-filesystem-can-be-used-on-the-backup-partition.md) you will find a table from which the correct
table from which the correct file system can be taken.


### RBK0154E: A restore is not possible if a partition of %1 is mounted.

Cause:

When a partition is rewritten, it must not be mounted.

Further actions:

With the command `sudo mount | grep <device>` (<device> is mentioned in the message)
to find out which partition is mounted and with `sudo umount <partition>`, where
<partition> must be the mounted partition, the partition (e.g. /dev/sda1)
release it.


### RBK0160E: Target %1 with %2 is smaller than the backup source with %3.

Cause:

The backup is larger than the device to which it is to be restored
and therefore cannot be restored. The message only appears for dd
backup. With tar or rsync backup, the full size of the device is not necessary, depending on the assignment.
device is necessary.

Further actions:

A larger SD card must be used. Alternatively, you can use the tool
pishrink to reduce the size of the dd image and then restore it with *raspiBackup*.
See also [FAQ26](faq.md#faq26).


### RBK0164E: No hardlinks can be created. RC %s.

Cause:

Hardlinks required by rsync are only supported by an ext3 or ext4
file system. See also [this page](which-filesystem-can-be-used-on-the-backup-partition.md).

Further actions:

Either select a different backup type such as tar or dd or use a backup partition
backup partition that is formatted ext3 or ext4.


### RBK0172E: Directory %s cannot be created.

Cause:

The root user is not authorized to create the new backup directory.

Further actions:

If the backup directory is mounted via NFS, the option
NO_ROOT_SQUASH in the `/etc/exports` file of the NFS server. Otherwise the
backup directory is mounted with insufficient rights.


### RBK0178E: Creation of %s file ends incorrectly with RC %s."

Cause:

dd backup of the boot partition fails with an error code.
Error code RC1 is an input/output error.

Further actions:

See what the error code from dd means.
If it is RC1, check the boot partition and/or the backup partition.


### RBK0196W: %1 does not support hard links.

Cause:

*rsync* uses hardlinks to reduce backup time and space. Hardlinks
are supported by ext3/ext4 filesystems, which are mounted locally or via NFS,
are supported. SMB and SSHFS do not support hardlinks.

Further actions:

Either use a backup partition that supports hard links or use the tar or dd backup.
the tar or dd backup. Please note, however, that each backup is then a full backup
and therefore requires more time and space.


### RBK0197W: Sending email with %s ends incorrectly with RC %s.

Cause:

An e-mail cannot be sent.

Further actions:

In most cases, the cause when setting up the notification lies in a
misconfiguration of the MTA used. Often *raspiBackup* does not receive an error when
error when sending the e-mail, but it still does not arrive.

The configuration of an MTA is often complicated and is not a problem for
*raspiBackup*. In the log of the MTA used you will find error messages that
help to find the cause. In this context, reference is made to [FAQ47](faq.md#faq47).
In any case, you should check what the RC of the mail client means and
can find clues as to where the cause lies. For example, it may also be that
the mail recipient has problems receiving the e-mail.


### RBK0203E: Boot device cannot be recognized. Please report the problem with a debug log created with option '-l debug'."

Cause:

*raspiBackup* tries to recognize the boot device and cannot do so for some reason.
for some reason.

Further actions:

A *GitHub* issue should be created with the debug log attached,
to find the cause.


### RBK0211E: External partition %s mounted to %s is not backed up with option -P.

Cause:

With the -P option, only the partitions of the system device can be backed up with *raspiBackup*.

Further actions:

By using the normal backup mode, a backup can also be made during a USB
boot can also be performed. If there are more than 2 partitions, you can use the
the --ignoreAdditionalPartitions option can be used to exclude the backup of further partitions.
can be excluded.


### RBK0263E: File system on %s does not support Linux file attributes.

Cause:

The rsync backup method requires that the backup partition is able to store Linux
file attributes. The current file system does not support this.
It is usually an NTFS file system. If the backup partition is mounted via NFS
this error message is a sign that the NFS
partition is not exported with no_root_squash.

Further actions:

Either the backup method dd or tar must be selected or a backup partition
backup partition that supports Linux file attributes must be used.
Details can be found on [this page](which-filesystem-can-be-used-on-the-backup-partition.md).

### RBK0266E: The authorization to create Linux file attributes on %s is missing (file system: %s)

Cause:

A backup partition mounted via NFS lacks the necessary authorization
for root to set all file attributes. As a rule, the NFS server does not export the
backup partition with no_root_squash. This option must be set in the file
/etc/exports on the NFS server for the exported partition.
A file system must also be exported that supports Linux file attributes
file attributes - i.e. ext3 or ext4. ntfs or fat32 cannot be used.

Further actions:

Export the backup partition on the NFS server with no_root_squash.

### RBK0268E: Only Raspberries with Raspberry PI OS are supported.

Cause:

*raspiBackup* is only supported for Raspberry Pis and RaspbianOS. You can use
option --unsupportedEnvironment you can still try to use *raspiBackup*,
because it also runs under many other Linux distributions and
raspberry-compatible hardware. In case of errors, however, no support is provided due to a lack of test hardware
and software and time, no support is provided. [Supported hardware and software](supported-hardware-and-software.md)

Further actions:

Use the --unsupportedEnvironment option and hope that *raspiBackup* can handle
can handle the existing software and hardware.

### RBK0273E: %s invalid backup directory(s) or files found in %s."

Cause:

Only backup directories created by *raspiBackup* may exist in the backup directory of a system.
backup directories may exist in the backup directory of a system. Any other directories or files
will generate this error message. This usually happens when you manually
renaming backup directories.

Further actions:

Delete or move directories or files not created by *raspiBackup* to other locations.
or files to other locations.


### RBK0274E: The restore device %s has mounted partitions. Note: A restore to the active system is not possible.

Cause:

A restore may not be performed on a running system. Also
the restore device must not be mounted. This check prevents the accidental overwriting
an active and otherwise used device from being overwritten. If usbmount
is active, it must first be deactivated.

Further actions:

The restore device must be released with umount or usbmount must be deactivated.


### RBK0277E: Restore is not possible if 'usbmount' is installed.

Cause:

usbmount interferes with the restore of a backup and must not be installed.

Further actions:

Uninstall usbmount with the command `sudo apt-get remove usbmount`.
It is even better to prepare a dedicated SD card with a small *Raspberry Pi OS* (*Raspberry Pi OS
lite*) and use this SD card for the restore. There is no
usbmount is installed.


### RBK1005E: bc not found. bc must be installed with 'sudo apt-get install bc'.

Cause:

The disk example extension requires `bc` for computing.

Further actions:

Install bc with `sudo apt-get install bc` so that the disk example extension outputs valid values.

<a name=exitcodes></a>
## Exit codes

Normally *raspiBackup* terminates with an error code 0.
In case of error, *raspiBackup* terminates with one of the following error codes. An
error message provides more detailed information on the cause of the error.

  - RC_ASSERTION=101
  - RC_MISC_ERROR=102
  - RC_CTRLC=103
  - RC_STOP_SERVICES_ERROR=105
  - RC_START_SERVICES_ERROR=106
  - RC_PARAMETER_ERROR=107
  - RC_MISSING_FILES=108
  - RC_NATIVE_BACKUP_FAILED=109
  - RC_LINK_FILE_FAILED=110
  - RC_COLLECT_PARTITIONS_FAILED=111
  - RC_CREATE_PARTITIONS_FAILED=112
  - RC_DD_IMG_FAILED=114
  - RC_SDCARD_ERROR=115
  - RC_RESTORE_FAILED=116
  - RC_NATIVE_RESTORE_FAILED=117
  - RC_DEVICES_NOTFOUND=118
  - RC_CREATE_ERROR=119
  - RC_MISSING_COMMANDS=120
  - RC_NO_BOOT_FOUND=121
  - RC_BEFORE_START_SERVICES_ERROR=122
  - RC_BEFORE_STOP_SERVICES_ERROR=123
  - RC_EMAILPROG_ERROR=124
  - RC_MISSING_PARTITION=125
  - RC_FILE_OPERATION_ERROR=130
  - RC_MOUNT_FAILED=131
  - RC_UNSUPPORTED_ENVIRONMENT=132
  - RC_RESTORE_EXTENSION_FAILS=133
  - RC_BACKUP_EXTENSION_FAILS=134
  - RC_DOWNLOAD_FAILED=135
  - RC_BACKUP_DIRNAME_ERROR=136
  - RC_RESTORE_IMPOSSIBLE=137
  - RC_INVALID_BOOTDEVICE=138
  - RC_ENVIRONMENT_ERROR=139
  - RC_CLEANUP_ERROR=140
  - RC_NOT_SUPPORTED=143
  - RC_TEMPMOVE_FAILED=144
  - RC_RESIZE_ERROR=145
  - RC_UUID_UPDATE_IMPOSSIBLE=147

[.status]: translated
[.source]: https://www.linux-tips-and-tricks.de/de/raspibackup#fehler
[.source]: https://www.linux-tips-and-tricks.de/de/raspibackupmeldungen
[.source]: https://www.linux-tips-and-tricks.de/en/raspibackupmessagese



