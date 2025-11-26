# Frequently asked questions (FAQ)

<!-- toc -->

---

<a name="faq0"></a>
### 0) How was *raspiBackup* created?

*framp* had three Raspis running at home. Two of them run 7/24.
Every server should be backed up regularly because unforeseen
circumstances can always occur that require a restoration of a previous
status. Especially the SD card of the Raspberry tends to
fail from time to time. In order to be prepared for this, a
script was written, which initially created a dd backup, then later, as a dd backup always
backs up the entire SD card although only fractions of it are
of it are used, a tar backup was created automatically. Finally
a rsync backup was implemented to save backup time and space through the usage of hardlinks.
and backup space. After a restore was necessary again and again
and everything worked well, *framp* thought that the script
could also be helpful for other Raspberry friends and published
*raspiBackup*. See also [10 years *raspiBackup*](10-years-raspibackup.md)

<a name="faq1"></a>
### 1) Is a backup of a running system reliable? Shouldn't the entire system be stopped before the backup?

The safest method is of course to stop the system completely.
During a backup, only what is on the storage medium is backed up
and not what is still in the main memory.

Unfortunately, it is not possible to backup a Raspberry automatically without a lot of effort.
But if all active services such as mysql, samba, nfs,
owncloud, web server are always stopped before the backup
to avoid data inconsistencies, the backup can be used to restore the Raspberry.
If the services are not stopped,
there is a high probability that the backup will become inconsistent.
For this purpose, the parameters `-a` and `-o` are used to specify the corresponding stop and
start commands before and after the backup. See also [FAQ18](#faq18) on this.

The installer can be used to select systemd services that are to be stopped
and restarted after the backup and the parameters for
option `-a` and option `-o` are set accordingly.

<a name="faq2"></a>
### 2) How can I restore a backup?

Any backup can be restored using *raspiBackup*. (See
[here](restore.md) the details). As a Windows user you can
use the appropriate Windows tools to restore dd backups. For other
backup types such as tar or rsync a Linux is necessary.

However, you can use the Raspberry for this: You nstall on a new SD
card RaspbianOS and copy *raspiBackup* to it. Then you connect
the device to which the backup is to be restored
and the medium with the backup to the Raspberry.
Then invoke *raspiBackup* and have the desired backup written back to the
device. Then shut down the system,
insert the device with the restored backup and restart the
Raspberry again.


<a name="faq3"></a>
### 3) What can *raspiBackup* back up and restore?

In normal mode, *raspiBackup* backs up two partitions with tar or rsync:
The boot and the root partition that exist on the system. If
the root partition has been moved to an external medium, the external
root partition is also backed up. With dd backup, the entire SD card is
is backed up. In this case, however, no external root partition can be backed up (hybrid boot mode).

In partition-oriented mode, any number of partitions of the system are
system are backed up. However, no other external partitions are backed up.

<a name="faq4"></a>
### 4) Which Linux backup methods are available?

The dd backup as well as the tar and rsync backup are available. dd and
tar backups can still be compressed with zip. On
[this page](backup-types.md) you can find
the advantages and disadvantages of the respective backup methods.


<a name="faq5"></a>
### 5) Is it possible to restore the backup without *raspiBackup*?

This has been a basic requirement for *raspiBackup*: It must be possible
to restore the backup manually with appropriate Linux tools and knowledge.

The backup creates files that contain the readable output from the Linux
commands sfdisk, blkid and fdisk from the system. This allows to
first restore the partition structure of the backup with the corresponding Linux tools.
Then you can restore the partition backups with the
corresponding Linux tools.


<a name="faq6"></a>
### 6) Is it possible to restore the backups with *raspiBackup* to smaller and larger SD cards?

With the dd backup type you have to
repartitioning after the restore and to adjust the partition size
if you want to use all the space for the second partition. A
dd restore to a smaller device does not work.

It works without problems on a smaller or larger device
if tar or rsync backup is used. In normal backup mode
the size of the root partition is automatically adjusted, i.e.
reduced or enlarged accordingly. If the size is increased
the entire available space is used.
If more space is used by the backup of the system
than the restore device has, there will of course be errors during the restore.
In partition-oriented backup mode, the last partition is adjusted accordingly.

With the `-0` (zero) option, the new device is not partitioned but the existing partitioning of the
of the backed up system is used.
This gives you complete control over the size of the restored partitions.
This means that before the restore you can specify exactly how
large the partitions on the new SD card should be and thus also restore to
smaller SD cards. This also works for partition-oriented backups.

A dd backup cannot be restored to a smaller card. It must be
reduced in size. This can be done like this. Or you can use [pishrink](https://github.com/Drewsif/PiShrink).

A partition-oriented backup can be restored to smaller devices
by preformatting it with your desired partitions and then restoring the backup with the
option -0 to restore the backup.


<a name="faq7"></a>
### 7) How can I influence the partitioning of the target SD card?

There are two options that influence the partitioning behavior of *raspiBackup*
partitioning behavior: Option `-1` (one) forces *raspiBackup* to partition the
backup SD card to the destination SD card even if the partitions are smaller or
or larger than the target SD card. With the option `-0` (zero)
option, *raspiBackup* does not perform any partitioning and uses the existing
partition of the target SD card. This means that you can create and format the partitions
and format them the way you want them and they will then be used by
by *raspiBackup*.


<a name="faq8"></a>
### 8) On which media can I store the backups with *raspiBackup*?

Generally on any device that can be mounted under Linux

  - External USB stick
  - External USB disk
  - smb network drive
  - nfs network drive
  - sshfs network drive
  - webdav network drive
  - ftpfs network drive

<a name="faq9"></a>
### 9) How can I extend the function of *raspiBackup* and additionally execute something before or after the backup and/or restore?

There are various possibilities:

  - A [wrapperscript](https://raw.githubusercontent.com/framps/raspiBackup/refs/heads/master/helper/raspiBackupWrapper.sh)
    is used and performs additional actions before and after the
    backup run, e.g. to save other things.

  - Any extension points (extensions) can be called before and after the backup
    and/or restore from *raspiBackup*. Two
    example extensions (see [here](hooks-for-own-scripts.md)) additionally report the CPU temperature before
    and after the backup run as well as the occupied main memory. An
    eMailExtension allows you to control any other eMail client.

<a name="faq10"></a>
### 10) Which eMailClients are supported by *raspiBackup*?

*raspiBackup* supports exim4, postfix and nullmailer, ssmtp, msmtp and
sendEmail. Other email clients can be addressed via an email extension
(for details see [here](hooks-for-own-scripts.md)).

<a name="faq11"></a>
### 11) My eMailClient is unfortunately not supported by *raspiBackup*. How can I still receive emails?

*raspiBackup* can use an email extension (extension plugpoint) to send the email.
To do this, you have to write a small script, which sets the
eMailParameters corresponding to the eMailClient used and
calls the eMailClient with the correct syntax. An example extension
for mailx is included in the [extension examples](hooks-for-own-scripts.md).


<a name="faq12"></a>
### 12) I have a question about or a problem with *raspiBackup*. How can I get help?

First of all: The emphasis is on *raspiBackup* questions. For Linux questions
or problems see [FAQ38](#faq38) and [FAQ47](#faq47).

There are several options:

- In [*GitHub*](https://github.com/framps/raspiBackup), issues can be created for questions or problems.
This is the preferred option. This requires a one-time
  registration is necessary. This and the use of *GitHub* is free of charge.

- In the Raspberry forum there is a [subforum on backups](https://forum-raspberrypi.de/forum/board/153-backup/), where questions about
  *raspiBackup* can be asked and problems can be reported. *framp* will be informed about
  all new threads and can dedicate himself to the thread.

See also these [Notes](introduction.md#contact_options)

**Note:** Any other means of contact will be ignored.

<a name="faq13"></a>
### 13) I have found a bug in *raspiBackup*. Where can I report the bug and when will I get a fix for it?

As in any software, it can happen that *raspiBackup* has bugs.
The various channels through which problems can be reported are
described in [FAQ12](#faq12).

<a name="faq14"></a>
### 14) Do I somehow get automatically informed that there is a new version of *raspiBackup*?

*raspiBackup* checks whether there is a newer version each time it is called. If yes
a corresponding message is displayed and the notification email
indicates this in the title with a smiley ;-). Then you can go to [this
page](version-history.md) to see what the new version brings and then use the parameter -U
parameter to update the version.

<a name="faq15"></a>
### 15) How can I go back to a previous *raspiBackup* version if I notice after an upgrade that the new version does not work as I expect it to?

*raspiBackup* creates a backup every time a new version is activated with the -U option.
With the option -V you can always
go back to a previous version. A list of all
backed up *raspiBackup* versions is displayed and you can select the version to
restore.


<a name="faq16"></a>
### 16) I have a 32GB SD card of which I only need 8GB. However, a dd backup always backs up 32GB, i.e. 24GB too much.

The dd backup always backs up the whole SD card. There is the
configuration parameter DEFAULT_DD_BACKUP_SAVE_USED_PARTITIONS_ONLY, which
ensures that only the defined partitions are backed up. I.e.
you only have to use gparted or another partitioning tool to create a smaller
partition of 8GB. The current partition sizes can be checked 
with the lsblk command.

Alternatively, you can use [raspiBackupWrapper Script](https://github.com/framps/raspiBackup/blob/master/helper/raspiBackupWrapper.sh) after the backup with
*raspiBackup* [pishrink](https://github.com/Drewsif/PiShrink) and reduce the dd image to the possible minimum.

<a name="faq17"></a>
### 17) How can I tell that the rsync backup is actually using hardlinks to save disk space?

Hardlinks are successfully used by *raspiBackup* when a local USB stick
stick, a local USB disk or a partition mounted via NFS,
formatted with ext3/ext4 is used. SMB and sshfs
do not support hardlinks.

**Note:** Windows Explorer ignores hardlinks and therefore displays an incorrect
effective disk usage. A Linux system must therefore be used to
check the assignment. The Raspberry is ideal for this.

The command `sudo du -sh *` shows the memory space actually used
and `sudo du -shl *` shows the memory space that would be used,
if no hardlinks were used (the one that Windows
incorrectly displays) .

Example:

```
root@raspberrypi:/media/nas-backup/raspberrypi# du -sh *
4,5G raspberrypi-rsync-backup-20160822-184617
4,5M raspberrypi-rsync-backup-20160822-190436
5,2M raspberrypi-rsync-backup-20160822-195250
5,7M raspberrypi-rsync-backup-20160822-201610

root@raspberrypi:/media/nas-backup/raspberrypi# du -shl *
4,7G raspberrypi-rsync-backup-20160822-184617
4,7G raspberrypi-rsync-backup-20160822-190436
4,7G raspberrypi-rsync-backup-20160822-195250
4,7G raspberrypi-rsync-backup-20160822-2016
```

Note: [How do hardlinks work together with rsync?](how-do-hardlinks-work-with-rsync.md).
And also a [Youtube video](https://www.youtube.com/watch?v=pIhSca_q2lo&t=4s).

<a name="faq18"></a>
### 18) Which services must be stopped before the backup and then restarted?

All services that store any system states in databases or in the
memory or on the file system should be stopped so that inconsistent data
statuses are not created during the backup, which are then only
noticed when the system is restored and 
unusable.

Systemd services can be configured with the installer that is stored in the
configuration file DEFAULT_STARTSERVCIES and DEFAULT_STOPSERVCIES
accordingly. Applications that do not run as system services must be
be added manually with the two options in the config file.
After this, the installer can no longer be used to configure these two
options.

The following services should be stopped in any case:

| Service | Stop command |
|-----------|-------------|
| nfs | systemctl stop nfs-kernel-server |
| Samba | systemctl stop samba |
| Pilight | systemctl stop pilight |
| Cups | systemctl stop cups |
| Minidlna | systemctl stop minidlna |
| Apache | systemctl stop apache2 |
| Wordpress | systemctl stop wordpress |
| nginx | systemctl stop nginx |
| mysql | systemctl stop mysql |
| seafile | systemctl stop seafile |
| Owncloud | See Apache |
| FHEM | systemctl stop fhem |
| iobroker | systemctl stop iobroker |
| cron | systemctl stop cron |

The services should then be restarted using the DEFAULT_STARTSERVICES option.
The sequence should then be exactly the reverse of the
stop sequence.

The installer automatically ensures that the selected Systemd
controlled services are stopped and started in the corresponding order.
started in the appropriate order. Unfortunately, Systemd does not guarantee that the dependencies
of the services are taken into account. For a few applications there are also
further tips on this page that should be taken into account.

Example for -a

```
-a "systemctl startpilight && systemctlstartsamba && systemctl startnfs-kernel-server"
```

Example for -o

```
-o "systemctl stop nfs-kernel-server && systemctl stop pilight && systemctl stop samba"
```

In the configuration file it then looks like this, for example:

```
DEFAULT_STOPSERVICES="systemctl stop nfs-kernel-server && systemctl stop pilight && systemctl stop samba"
```

resp.

```
DEFAULT_STARTSERVICES="systemctl startsamba&& systemctl startpilight && systemctl  startnfs-kernel-server"
```

Attention: The commands are executed as root. No sudo is necessary.

With the --systemstatus option, the debug log contains the list of started
system services and the open files before the start of the backup
is output.

If you explicitly do not want to stop and start any services, a
colon must be specified as a service, i.e. -a : -o :


<a name="faq19"></a>
### 19) What formatting must a partition have on which a backup is stored?

In principle, any file system that can be mounted on Linux can be used.
However, there are a few things to consider:

- A rsync backup uses hardlinks which are supported by ext3/4.
  Then only changed files are backed up and identical files are linked via
  hardlinks. An ext4 file system which is shared via smb
  does not support hardlinks. An alternative is NFS. If no hardlinks are
  supported, rsync cannot be used.

- FAT32 can only store files up to 4GB. A dd backup will be as large
  as the SD card (unless the configuration option
  DEFAULT_DD_BACKUP_SAVE_USED_PARTITIONS_ONLY is used) and therefore usually
  larger than 4GB. The same applies to the tar backup which also very
  quickly becomes larger than 4GB. An alternative to this is NTFS.

General recommendation: Use ext3/4 if possible. On Linux use NFS
for network drives. On Windows use NTFS on exported smb
network drives. Only use FAT32 if you are sure that the backups will not
backups are not larger than 4GB.

<a name="faq20"></a>
### 20) I have problems backing up my backups to a Synology. How can I fix this?

There are several users of *raspiBackup* who successfully back up their backups via nfs3 on a
Synology successfully. There is a special page where
users of *raspiBackup* have described what they have configured on the Synology
so that everything works.


<a name="faq21"></a>
### 21) The contents of the boot partition do not change. Why is the boot partition always backed up again with every backup?

This is true in 98% of cases. However, a firmware update can update the
boot partition. With the configuration parameter
DEFAULT_LINK_BOOTPARTITIONFILES, the boot partitions in the backup are linked with
hardlinks - if these are supported. This allows you to save
60MB of backup space per backup. However, the boot partition is always
backed up first to test whether it has changed from the previous
backup and then replaced by a hard link. This means that this
option only makes sense if you have a very small backup space.

<a name="faq22"></a>
### 22) How can I use different backup configurations in different backup runs?

The configuration parameters of *raspiBackup* are read in the following order
read in and take effect. Later files or options can overwrite previous
overwrite previous options.

1. `/usr/local/etc/raspiBackup.conf`
1. `./.raspiBackup.conf` (current directory)
1. `~/.raspiBackup.conf` (home directory)
1. The optional configuration file specified with the `-f` option
1. Invocation parameter


<a name="faq23"></a>
### 23) I would like to track the backup progress. Is there an option to get a progress bar?

There is the option -g for dd, tar and rsync. The option should only be
be used when starting *raspiBackup* manually.


<a name="faq24"></a>
### 24) *raspiBackup* reports an error `ACL_TYPE_ACCESS, Operation not supported` when using the backup type rsync

The error message looks something like this:

```
??? RBK0024E: Backup program rsync has received an error.
rsync: set_acl: sys_acl_set_file(media/pi, ACL_TYPE_ACCESS): Operation not supported (95)
```

The reason is that nfs version 4 with rsync does not support Posix ACLs.
However, these are not necessary in 99% of cases.

Note: Synology does not support ACLs with NFS as of 13.5.2022.

Note: The following command will find all files with ACLs:
```
sudo getfacl -Rs /
```
The command takes time to complete.

Possible solutions:

1. use *tar* and not *rsync

2. As of *raspiBackup* release 0.7.2, the option `DEFAULT_RSYNC_BACKUP_OPTION_EXCLUDE_ACLS=1` forces rsync
to backup no ACLs

1. use a locally connected device which is formatted with *ext4

1. use *nfs* *nfs* version3. Read [this article](https://www.linux-tips-and-tricks.de/de/faq/2-uncategorised/605-wie-kann-man-acls-mit-rsync-auf-nfs-gemounteten-partitionen-sichern). This
   option does not work with a Synology.

1. use `raspiBackupWrapper.sh`, which contains code that creates a loopback
   device which uses an image formatted with *ext4* as backup partition
   and can therefore store ACLs.  (For experienced users only).

In Bullseye, Debian has introduced persistent journaling and thus
exists /var/log/journal with ACLs on the system. If you are using *raspiBackup* Release
0.6.6 or earlier must at least upgrade to release 0.6.6.1 or use the workaround
described on *GitHub* in [Issue 393](https://github.com/framps/raspiBackup/issues/393).


<a name="faq25"></a>
### 25) Error message `dev/... has unsupported feature(s): metadata_csum E2FSCK: Get a newer version of e2fsck`

Solution:
Before the restore, edit `/etc/mke2fs.conf` and remove the metadata_csum from both ext4 options
Then perform the restore with *raspiBackup*.

[.workaround]: _ "Problems with syntax highlighting in vim-markdown with non-balanced-underlines"

<a name="faq26"></a>
### 26) Why do I get the message `???? RBK0160E: Destination /dev/sda with xx GiB is smaller than the backup source with yy GiB` although both SD cards are the same size?

SD cards that are specified with a certain size (e.g. 16GB) are nevertheless
different in size. With the command `sudo fdisk -l /dev/mmcblk0`
you get the following output, for example, which tells you the exact size:

```
sudo fdisk -l /dev/mmcblk0

Disk /dev/mmcblk0: 15.5 GB, 15548284928 bytes
With another SD card, also 16GB in size, you get e.g.
Disk /dev/mmcblk0: 15.9 GB, 15931539456 bytes
```

You can therefore transfer the first image to the second SD card but not vice versa.

Solution:

- Use a larger SD card
- Reduce the size of the source image. The pishrink tool is suitable for this.
- Create the backup with the parameter
  DEFAULT_DD_BACKUP_SAVE_USED_PARTITIONS_ONLY parameter (see also
  FAQ16)
- Before creating the backup, use *gparted* to make the root partition slightly
  smaller (several hundred MB or equal to 1 GB). Then the
  backup also fits on SD cards that are somewhat smaller.


<a name="faq27"></a>
### 27) I have a tar or rsync backup and would like to convert it to a dd backup. Is that possible?

There is a script [raspiBackupRestore2Image.sh](https://raw.githubusercontent.com/framps/raspiBackup/refs/heads/master/helper/raspiBackupRestore2Image.sh).
This allows you to create a dd from a tar
or rsync backup in the backup directory.


<a name="faq28"></a>
### 28) Why do file changes disappear from a restored backup after a reboot?

Unfortunately, the SD card is defective at the location where the file system
stores changes (superblock). As this is held in the main memory,
you only notice the error after a reboot.

Solution:
The backup must be restored to a new error-free SD card.
card that is free of errors.


<a name="faq29"></a>
### 29) I get the message rsync: chown "(file-fad)" failed: Operation not permitted (1). How can I solve this?

Kurt got this problem, found the solution and kindly
shared. DougieLawson has described the [solution to the problem](https://www.raspberrypi.org/forums/viewtopic.php?t=122066#p831840) .

In the end, the following entry in /etc/fstab

```
192.168.2.203:/data/raspi /media/nas nfs nfsvers=3,defaults 0 0
```

should be changed as follows

```
192.168.2.203:/data/raspi /media/nas nfs defaults,nfsvers=4,noatime,noauto,x-systemd.automount 0 0
```

BastiFanta has found another reason for this:

> I had to create the NFS share with the no_root_squash option, see
> for more details: <https://www.selflinux.org/selflinux/html/nfs03.html>

<a name="faq30"></a>
### 30) I like *raspiBackup* and would like to honor the development and support. How can I do that?

For example, give a [tip](introduction.md#donation).


<a name="faq31"></a>
### 31) I get an error message from *raspiBackup*. What can I do to get rid of it?

There is a page where all the most common error messages from *raspiBackup*
are described in detail including actions to fix them.
Visit [this page](error-messages.md).


<a name="faq32"></a>
### 32) After upgrading to v0.6.3.2 I get error messages RBK0021E: Backup program of type tar terminated with RC 1 or RBK0021E: Backup program of type rsync terminated with RC 23.

These errors were ignored in previous versions. However, as this
inconsistent backups can be created, they are no longer ignored.
ignored.

The following options exist to eliminate the problem:

  - Stop the service that changes the file during the backup. This can be done
    either be done with the installer (M3->C6) if it is a system service or
    service or you have to manually change the two options
    options DEFAULT_STOPSERVICES and DEFAULT_STARTSERVICES in the configuration file with the commands
    commands to stop and start the service.
    Tip: The --systemstatus option provides a list of active services and their
    of the active services and their open files. This allows you to
    find out which service is modifying a file during the backup
    modified during the backup.

  - With the DEFAULT_EXCLUDE_LIST option you can exclude the files that change during the backup.
    files that change during the backup can be excluded from the backup.
    files are important files of an application then the restored
    application will no longer start. So check urgently beforehand whether
    important and test thoroughly whether the restored application starts again
    starts again if the files are missing.

  - inotifywait -m -e delete -e create -e move -e modify -e attrib <directory>

It may be necessary to add the -r option so that all subdirectories are also
subdirectories are also monitored.

  - Use the configuration options `RSYNC_IGNORE_ERRORS` or
    `TAR_IGNORE_ERRORS` to ignore the error. Details can be found
    [here](#faq59)

<a name="faq33"></a>
### 33) I have a Cubieboard, Banana Pi, Odroid, Hummingboard, or Beagle Board. Can *raspiBackup* also backup these?

In principle, this should be possible or is already possible for certain non
Raspberry hardware. Just try it out. But *raspiBackup* will [only for
RaspbianOS and Raspberry HW](supported-hardware-and-software.md). I.e. if it works, be
happy. But if it doesn't work, don't ask for support. :-)

The option `--unsupportedEnvironment` must then be specified as an invocation parameter.


<a name="faq34"></a>
### 34) I want to restore my 16GB dd backup and get the message that the target SD card is too small. Why is that?

SD cards have a certain size, e.g. 16GB, but they never have exactly this size
but there are small deviations downwards
and upwards. Since the dd backup is the same size as the SD card, the dd
backup cannot be written back if you get a slightly smaller SD card.
For this reason, the last partition of a DD backup should always be
partitioned a little smaller than the maximum possible. See also
also [FAQ16](#faq16). However, you can use [pishrink](https://github.com/Drewsif/PiShrink) to reduce the size of the dd image and then
and then restore it with *raspiBackup*.


<a name="faq35"></a>
### 35) I would like to move my root file system to a USB disk. Can I do this with *raspiBackup* during the restore?

If it is a tar or rsync backup, this is possible. Simply use the
-R option.


<a name="faq36"></a>
### 36) What do the return codes (RC) mean with which *raspiBackup* ends in the event of an error?

  - 101 - A program error has been detected
  - 102 - A Linux command returns an error
  - 103 - *raspiBackup* was terminated with CTRLC.
  - 105 - There were errors when stopping services
  - 106 - There were errors when starting services
  - 107 - A parameter in an option is incorrect
  - 108 - Files are not found
  - 109 - The Linux backup program dd, tar or rsync received an error during backup
  - 110 - A link to a file cannot be created
  - 111 - There are errors when collecting the partition information
  - 112 - There are errors when creating partitions during restore
  - 114 - A dd image cannot be created
  - 115 - Required partitions were not found
  - 116 - The restore was canceled by the user
  - 117 - The backup program dd, tar or rsync used has received an error when restoring

  - 118 - Specified devices were not found
  - 119 - A directory cannot be created
  - 120 - Linux tools required by *raspiBackup* are missing
  - 121 - No valid boot partition could be found
  - 122 - The extension BEFORE_START_SERVICES ended incorrectly
  - 123 - The extension BEFORE_STOP_SERVICES ended incorrectly
  - 124 - The e-mail extension ended with an error
  - 130 - A file operation failed (chmod, mv, ...)
  - 131 - A mount failed
  - 132 - The environment (HW/SW) is unsupported
  - 133 - The RESTORE_EXTENSION ends incorrectly
  - 134 - The BACKUP_EXTENSIONa ends incorrectly
  - 135 - A file download ends with an error
  - 136 - An invalid backup directory not created by *raspiBackup* was specified
  - 137 - An invalid restore device was specified
  - 138 - An invalid boot device was specified
  - 138 - USBMOUNT detected
  - 140 - An error occured during cleanup
  - 143 - Overlay file system detected
  - 144 - Creation of the backup folder on the backup partition at the end of the backup ends incorrectly
  - 145 - Resize of a partition ends incorrectly
  - 147 - UUID update ends with error

<a name="faq37"></a>
### 37) The email subject sometimes has a smiley at the beginning. What does it mean?

| smiley | meaning |
| ------ | --------- |
| ;-)    | There is a newer release of *raspiBackup*. An upgrade should be made with the -U option. You can go back with the -V option. |
| :-D | There is a beta version of the next *raspiBackup* release. Beta testers are welcome and can install the beta with the -U option. After testing, you can revert to the current version with the -V option. |
| O.o | A warning message has been written. |
| :-( |The *raspiBackup* release is outdated and contains a serious error. It should urgently be replaced by the current release with the -U option. |


<a name="faq38"></a>
### 38) Where can I ask questions and get help with Linux questions and problems that have nothing to do with *raspiBackup*?

*raspiBackup* was developed to make it as easy as possible for Linux beginners to back up their
Raspberry. However, a certain amount of
Linux knowledge is necessary. Common problems with *raspiBackup* are simple Linux problems. Such questions are not answered in the
contact channels. There are forums with
competent members who are happy to help. A recommended one is the
[German Raspberry Pi forum](https://forum-raspberrypi.de/forum/).
Another is the [English Raspberry forum](https://forums.raspberrypi.com/).

<a name="faq39"></a>
### 39) Where can I find the debug log of raspiBackup?

See [FAQ41](#faq41)

<a name="faq40"></a>
### 40) How can I update my configuration after a version update?

This is done automatically by *raspiBackup* during the upgrade. See also
[Configuration update when upgrading to a new version](configuration-update-when-upgrading-to-a-new-version.md).

<a name="faq41"></a>
### 41) Where can I find the debug log of raspiBackup?

The debug log is called `raspiBackup.log` for backup and `raspiBackup.logr` for restore.

- If *raspiBackup* ends successfully, the log file is located in the backup directory.
- If *raspiBackup* does not end successfully, the log file is located in the home directory of the caller.
    - If *raspiBackup* was started via the console, the log file usually is located in `/home/<user>` or `/root`.
    - If *raspiBackup* was started via cron or systemd in the background, the log file is located in `/root`.
- If *raspiBackup* ends unexpectedly or was stopped with kill, the log file is located in `/tmp`.
- The log file for the restore is located in current directory when`raspiBackup` was invoked. This usually is `/home/<user>` or `/root`.

<a name="faq42"></a>
### 42) Where can the /boot and /root partitions be located?

*raspiBackup* supports the following configurations in normal backup mode
backup mode, whereby only the `/boot`
and `/root` are always backed up. Other partitions are ignored.

- `/boot` and `/root` on SD card or another device (disk, SSD, ...)
- `/boot` on SD card and `/root` on another device (disk, SSD, ...)
  This is necessary if you have an older Raspberry that does not yet support
  does not yet support USB boot, but you no longer want to have the root partition
  on the SD card.

<a name="faq43"></a>
### 43) How can I find all the documentation pages for *raspiBackup* or pages on a specific topic?

Initially all documentation for *raspiBackup* was on
[this page](https://www.linux-tips-and-tricks.de).

Now everything is on this website.

<a name="faq44"></a>
### 44) Why does the image with the restore backup not start?

See [FAQ49](#faq49)

<a name="faq45"></a>
### 45) How can I temporarily switch options on and off in the call?

Many options are used to switch something on or off. Normally
the options are defined once in the configuration file and that's it.
However, if you want to temporarily overwrite options in the configuration file
you can use the option with a `+` for switch on and `-` for switch off.
Example: If you have switched on the zipping of dd backups by default
by default, you can temporarily switch it off with the `-z-` option.

<a name="faq46"></a>
### 46) Why is it not recommended to use the dd backup type?

See [this article](why-shouldn-t-you-use-dd-as-backup-type.md).


<a name="faq47"></a>
### 47) Where can I get help with pure Linux questions or problems that have nothing to do with *raspiBackup* as such?

See [FAQ38](#faq38)

<a name="faq48"></a>
### 48) Can I restore the backup to a running system?

Technically this is possible, but the result is anything but a running system.
system. That is why *raspiBackup* aborts immediately if you try to do this.
A restore must always be done to another SD card or another device,
which is connected to the Raspberry.

<a name="faq49"></a>
### 49) My backup which I have restored to an SD card does not start. Why not?

In 99.9% of cases, the SD card to which the restore is performed is defective. If you
restored to another SD card, preferably a new one, the problem usually
no longer occurs. There is also the option -C that you can use at
restore to check the SD card for bad blocks during formatting.
However, this makes the restore process take much longer. See
also [this page](why-shouldn-t-you-use-dd-as-backup-type.md) for problems with a dd backup.


<a name="faq50"></a>
### 50) My backup or restore takes forever. What could be the reason?

The backup and restore time depends on the size of the data to be
data to be backed up as well as the performance of the backup partition. If backups are made via
the network via SMB or NFS, it takes even longer. With
rsync the first backup takes longer as the first backup is a full backup.
Only the following backups are incremental backups and therefore
usually faster.

It can happen that the backup or restore run does not end or takes an extremely long time.
This is usually due to the fact that errors occur during the backup
- write or read errors that are caused by the Linux
backup tools `dd`, `tar` or `rsync`.

With `rsync` it may also be due to the fact that ACLs are to be backed up but
authorization does not exist or ACLs are not supported by the backup partition.
The latter applies to NFS and SMB
mounted backup partitions. See [FAQ24](#faq24).

If the mount option `sync` is used, it should be replaced by the option `async`.
option.

Option --timestamps helps to find the step where *raspiBackup* takes so long.
takes so long. After that, the debug log will help.


<a name="faq51"></a>
### 51) How are the progress bar statistics calculated?

*raspiBackup* does not calculate anything. Instead, the options of the
offered progress bar are used instead. For dd it is the option
status=progress and for rsync the option info=progress2. tar does not have its own
progress indicator and therefore the data stream is streamed through pv.
The details of the respective progress indicator can be found in the
documentation, the options in the respective tools and the Linux tool
pv tool.


<a name="faq52"></a>
### 52) How can I download and run a test version or a temporary fix from *GitHub*?

There is a [script at *GitHub*](https://github.com/framps/raspiBackup/blob/master/scripts/raspiBackupDownloadFromGit.sh). You have to invoke it as follows:

```
curl -s https://raw.githubusercontent.com/framps/raspiBackup/master/scripts/raspiBackupDownloadFromGit.sh | sudo bash -s -- <brand name>
```

Where <branchname> must be the *GitHub* branch from which you want to download
`raspiBackup.sh` you want to download. Then invoke this *raspiBackup* version
as follows (**Attention:** Pay attention to the leading dot !)

```
sudo ./raspiBackup.sh <options>
```


<a name="faq53"></a>
### 53) What are *raspiBackup* snapshots?

*raspiBackup* snapshots are special backups with two special
properties:

- They are not included in the backup recycle process and must therefore be
  be deleted manually in the backup directory
- They have a description in the backup directory name by which a
  *raspiBackup* snapshot can be easily recognized and with which you can give a
  description to the snapshot so that it is easy to recognize.

A snapshot is created with the -M option and can be used very well
to take a snapshot at certain times when setting up a new system
so that you can go back in the event of an error.
Based on the description, you can recognize which status you have saved with the
snapshot.


<a name="faq54"></a>
### 54) How can I access the boot partition files in the backup directory?

*raspiBackup* saves the boot partition data in an image file. With the
following commands you can access the files in this image:

```
sudo losetup -f <hostname>-backup.img
sudo mount /dev/loop0 /mnt
```


<a name="faq55"></a>
### 55) Why do I suddenly have duplicate PARTUUIDs on my system?

During the restore of a backup, the PARTUUID of the original system is reused for the partitions.
the partitions is used again. If this restored system is mounted on the
original system, the PARTUUIDs appear twice and there will usually be
problems when booting the original system. For these cases there is
the option `-updateUUIDs` when restoring, so that the same PARTUUID is not used on the restored system.
As of release 0.6.9, a new PARTUUID is always
generated. If you do not want this, you must use the option
`-updateUUIDs-` this must be switched off.

<a name="faq56"></a>
### 56) How can I start *raspiBackup* automatically on an unsupported system?

To do this, the file /etc/systemd/system/raspiBackup.service must be changed:

Change the line ExecStart=/usr/local/bin/raspiBackup.sh to

ExecStart=/usr/local/bin/raspiBackup.sh --unsupportedEnvironment.


<a name="faq57"></a>
### 57) How can I update *raspiBackup* to a new release?

*raspiBackup* reports when a new release or beta is available. An
update is started with the `-U` option. With the option `-V` you can go back
to a previous release. Betas are often updated several times.
To install the latest version, the options
`-U` and `-S` must be used.


<a name="faq58"></a>
### 58) What do I have to consider if I want to back up to an nfs mounted backup partition with rsync?

The partition must be exported from the NFS server with `no_root_squash` and nfs version 4 if no ACLs are used and nfs version 3 otherwise.

<a name="faq59"></a>
### 59) rsync reports that files have disappeared during the backup process on the system and aborts with return code 24. How can I prevent this?

There are the following possibilities:

- The service that deletes the file is stopped and restarted before the backup
- The file or the directory in which the file is located is excluded from the backup
- If none of this can be used, there is also the option
  DEFAULT_RSYNC_IGNORE_ERRORS="24" with which *raspiBackup* ignores the RC24.

Attention: There are rare circumstances in which a rsync RC 24 is an error that cannot be
ignored. See [here at bugzilla.samba.org](https://bugzilla.samba.org/show_bug.cgi?id=3653#c12).
This means that you should try to eliminate the error with option 1 or 2 if possible.

[.status]: translated
[.source]: https://linux-tips-and-tricks.de/de/faq

