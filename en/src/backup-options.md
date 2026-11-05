# Backup options

This list contains all invocation options of *raspiBackup* as well as
the corresponding configuration options.

<div class="table-wrapper-for-options">

------------------

<!-- toc -->

------------------

<a name="parm_a"></a>
### -a: Commands that start services after the backup

Commands to restart services after the backup. E.g. for SMB "service
smbd start" (**Attention:** quotation marks at the beginning and end). This option is
mandatory together with the `-o` option.

Several commands have to be separated by `&&`. These commands should have the
exact reverse order of the commands in the `-o` parameter.

**Example**:

```
-a "service nfs-kernel-server start && service smbd start"
```

If **no** service is really to be started, a colon ":" has to be given as an argument.

See also [FAQ1](faq.md#faq1) and [FAQ18](faq.md#faq18).

**Note**:
The parameters can be set with the installer. If they are changed manually, the installer
can no longer be used to change them.

**Attention**:
The commands are executed as root. No sudo is necessary.

| Option name | Default | In Installer | Configuration name |
|-------------|----------|--------------|--------------------|
| -a | none | configurable | DEFAULT_STARTSERVICES |

<a name="parm_b"></a>
### -b: Definition of the block size used for dd backup

Block size used for the dd backup.

| Option name | Default | In Installer | Configuration name |
|-------------|----------|--------------|--------------------|
| -b | 1 MB | no | DEFAULT_DD_BLOCKSIZE |

<a name="parm_B"></a>
### -B: Boot partition is backed up as tar instead of dd

The boot partition is not backed up with dd but with tar.

**Note:**
This option has no function if the partition-oriented mode
is used.

| Option name | Default | In Installer | Configuration name |
|-------------|----------|--------------|--------------------|
| -B | off | no | DEFAULT_TAR_BOOT_PARTITION_ENABLED |

<a name="parm_c"></a>
### -c: Allow local backup storage

No backup can be created on the root partition to protect against
unintentional full writing of the root partition by the backup.
It usually doesn't make sense to store a backup on the system partition.

This option disables the test, and a backup can be created on the root partition.

**ATTENTION**:
It is not checked whether the backup still fits on the root partition.

| Option name | Default | In Installer | Configuration name |
|-------------|----------|--------------|--------------------|
| -c | off | no | DEFAULT_SKIPLOCALCHECK |

<a name="parm_D"></a>
### -D: Further options for the dd backup

Further invocation options for the dd backup (e.g. "conv=notrunc,noerror,sync").

| Option name | Default | In Installer | Configuration name |
|-------------|----------|--------------|--------------------|
| -D | automatic | no | DEFAULT_DD_PARMS |

<a name="parm_dynamicMount"></a>
### --dynamicMount: Dynamically mount the backup partition

This mounts the specified partition or mountpoint before the backup
and unmounts it at the end. If it was already mounted,
the partition will not be unmounted at the end. The mountpoint has to be defined in /etc/fstab
and can then either be the mountpoint itself (e.g. /backup)
or the backup partition (e.g. /dev/sdb1).

| Option name | Default | In Installer | Configuration name |
|-------------|----------|--------------|--------------------|
| --dynamicMount | off | no | DEFAULT_DYNAMIC_MOUNT |

<a name="parm_F"></a>
### -F: Simulates the backup run and helps to quickly test the eMail notification

"Fake backup". This option is helpful for initial testing of *raspiBackup*.
The actual long-running backup is not triggered by this - but all option
checks as well as the sending of notification eMails and push messages are.

| Option name | Default | In Installer | Configuration name |
|-------------|----------|--------------|--------------------|
| -F | none | no | |

<a name="parm_ignoreAdditionalPartitions"></a>
### --ignoreAdditionalPartitions: More than two partitions are tolerated, but only the first two partitions are backed up

With this option, systems with more than two partitions are supported
in normal backup mode if tar or rsync backup is used. However,
only the first two partitions, /boot and /, are backed up and restored.

| Option name | Default | In Installer | Configuration name |
|-------------|----------|--------------|--------------------|
| --ignoreAdditionalPartitions | no | no | DEFAULT_IGNORE_ADDITIONAL_PARTITIONS |

<a name="parm_ignoreMissingPartitions"></a>
### --ignoreMissingPartitions: Test whether all partitions are backed up

In partition-oriented backup mode, it is checked whether all partitions
that were backed up in the last backup are also backed up again.
This option switches the test off.

| Option name | Default | In Installer | Configuration name |
|-------------|----------|--------------|--------------------|
| --ignoreMissingPartitions | no | no | DEFAULT_IGNORE_MISSING_PARTITIONS |

<a name="parm_k"></a>
### -k: Number of backups to be kept 

Number of backups to be kept per backup type, provided it is not 
overwritten by the keep option of the respective backup types.
This means that 3 dd, 3 tar and 3 rsync backups are kept by default.

**Note:**
 This option has no effect if the intelligent rotation strategy is used.

| Option name | Default | In Installer | Configuration name |
|-------------|----------|--------------|--------------------|
| -k | 3 | configurable | DEFAULT_KEEPBACKUPS |

<a name="parm_keepType"></a>
### --keep_{type}: Number of backups per type to be kept

Number of backups to be kept for each backup type.

{type} can be any backup type, i.e. dd, ddz, tar, tgz or rsync.

**Note:**
These options have no effect if the intelligent rotation strategy is used.

| Option name | Default | In Installer | Configuration name |
|-------------|----------|--------------|--------------------|
| --keep_dd | Parameter for option -k | no | DEFAULT_KEEPBACKUPS_DD |
| --keep_ddz | Parameter for option -k | no | DEFAULT_KEEPBACKUPS_DDZ |
| --keep_rsync | Parameter for option -k | no | DEFAULT_KEEPBACKUPS_RSYNC |
| --keep_tar | Parameter for option -k | no | DEFAULT_KEEPBACKUPS_TAR |
| --keep_tgz | Parameter for option -k | no | DEFAULT_KEEPBACKUPS_TGZ |

<a name="parm_M"></a>
### -M: Create a *raspiBackup* snapshot

This option creates a *raspiBackup* snapshot, which is not included in the
backup recycle process and is therefore not automatically deleted.
The specified text is appended to the end of the snapshot directory name. See also
[this page on snapshots](snapshots.md).

Example: The host name is "idefix" and the parameter for -M is "Initial boot
from SD". The following directory is then created:

```
idefix/idefix-rsync-backup-20170103-170717_idefix-Initial_boot_from_SD
```

**Note**:
*raspiBackup* snapshots are normal backups and not "real"
snapshots like those with LVM or btrfs. However, with rsync backups hardlinks
are used to reduce the snapshot time.

**Note**:
As the snapshot directories are not included in the backup recycle process,
they have to be deleted manually.

| Option name | Default | In Installer | Configuration name |
|-------------|----------|--------------|--------------------|
| -M | none | no | |

<a name="parm_N"></a>
### -N: Extensions to be called before and after the backup

Activation of own script extensions. See [this page](hooks-for-own-scripts.md),
which also offers two sample extensions that report the CPU temperature and the
memory usage before and after the backup run.

| Option name | Default | In Installer | Configuration name |
|-------------|----------|--------------|--------------------|
| -N | none | no | DEFAULT_EXTENSIONS |

<a name="parm_notifyStart"></a>
### --notifyStart: Notification at backup start

This option is used to enable that an
eMail or a push notification is sent when the backup starts.
Normally, a notification is only sent at the end of the backup.

| Option name | Default | In Installer | Configuration name |
|-------------|----------|--------------|--------------------|
| --notifyStart | no | no | DEFAULT_NOTIFY_START |

<a name="parm_o"></a>
### -o: Commands that stop services before the backup

Commands to stop services before the backup so that no inconsistent backup
is created. E.g. for SMB "service smbd stop" (**Attention:** quotation marks at the
beginning and end). This option is mandatory together with the `-a` option.

Several commands have to be separated by `&&`. These commands should have the
exact reverse order of the commands in the `-a` parameter.

**Example**:

```
-o "service smbd stop && service nfs-kernel-server stop"
```

If **no** service is really to be stopped, the colon ":" has to be given as an argument.

See also [FAQ1](faq.md#faq1) and [FAQ18](faq.md#faq18).

**Note**:
The parameters can be set with the installer. If they are changed manually, the installer
can no longer be used to change them.  

**Attention**:
The commands are executed as root. No sudo is necessary.

| Option name | Default | In Installer | Configuration name |
|-------------|----------|--------------|--------------------|
| -o | none | configurable | DEFAULT_STOPSERVICES |

<a name="parm_p"></a>
### -p: Backup directory

Specification of the backup directory in which the created
backup is to be saved.

| Option name | Default | In Installer | Configuration name |
|-------------|----------|--------------|--------------------|
| --p | off | configurable | DEFAULT_BACKUPPATH |

<a name="parm_rebootSystem"></a>
### --rebootSystem: Reboot the system after the backup

This option causes the system to be rebooted at the end of the
backup run and thus all services are restarted.
Therefore, arguments of the `-a` option are also ignored.

**Note**: If the `-F` option is used, no reboot is performed.

| Option name | Default | In Installer | Configuration name |
|-------------|----------|--------------|--------------------|
| --rebootSystem | off | no | DEFAULT_REBOOT_SYSTEM |

<a name="parm_smartRecycle"></a>
### --smartRecycle: Use of SmartRecycle

This option switches on the [intelligent rotation strategy - Smart Recycle](smart-recycle.md).
The `--keep` options are then ignored and do not need to be set to 0.

| Option name | Default | In Installer | Configuration name |
|-------------|----------|--------------|--------------------|
| --smartRecycle | off | configurable | DEFAULT_SMART_RECYCLE |

<a name="parm_smartRecycleDryrun"></a>
### --smartRecycleDryrun: Test mode of SmartRecycle

This option switches on the test mode of the [intelligent
rotation strategy - Smart Recycle](smart-recycle.md).


| Option name | Default | In Installer | Configuration name |
|-------------|----------|--------------|--------------------|
| --smartRecycleDryrun | yes | no | DEFAULT_SMART_RECYCLE_DRYRUN |


<a name="parm_smartRecycleOptions"></a>
### --smartRecycleOptions: Smartrecycle options

This option defines parameters for the [intelligent rotation strategy - Smart Recycle](smart-recycle.md).

| Option name | Default | In Installer | Configuration name |
|-------------|----------|--------------|--------------------|
| --smartRecycleOptions | "7 4 12 1" | configurable | DEFAULT_SMART_RECYCLE_OPTIONS |

<a name="parm_systemstatus"></a>
### --systemstatus: Show active services at backup startup

A list of active services and open files is created
in the debug file.

| Option name | Default | In Installer | Configuration name |
|-------------|----------|--------------|--------------------|
| --system status | off | no | |

<a name="parm_tarcompressiontool"></a>
### --tarCompressionTool: Definition of the tar compression tool to be used

**Available as of release 0.7.2**

The standard for compressing tar backups is gzip. With this option you can choose
another compression method, e.g. zstd.

| Option name | Default | In Installer | Configuration name |
|-------------|----------|--------------|--------------------|
| --tarCompressionTool | no | no | DEFAULT_TAR_COMPRESSION_TOOL |

Possible compression methods are: `bzip2`, `gzip`, `lzip`, `lzma`, `lzop`, `xz` and `zstd`.

Starting with release 0.7.3, `lz4` is also available.

The `--tarCompressionToolOptions` option can be used to specify options for the compression tool.

**Note:**

Don't use option `-z` in parallel, because this will deactivate this option and a gzipped tar file will be created.

<a name="parm_tarcompressiontooloptions"></a>
### --tarCompressionToolOptions: Additional options for the tar compression tool

**Available as of release 0.7.2**

| Option name | Default | In Installer | Configuration name |
|-------------|----------|--------------|--------------------|
| --tarCompressionToolOptions | no | no | DEFAULT_TAR_COMPRESSION_TOOL_OPTIONS |

<a name="parm_unsupportedEnvironment"></a>
### --unsupportedEnvironment: Use on unsupported HW and OS

If *raspiBackup* is started in [unsupported environments](supported-hardware-and-software.md),
this option is required. 

| Option name | Default | In Installer | Configuration name |
|-------------|----------|--------------|--------------------|
| --unsupportedEnvironment | off | no | |

**Note**:

If you want to back up an unsupported system on a regular basis, you must modify the following line `ExecStart=/usr/local/bin/raspiBackup.sh` in the file `/etc/systemd/system/raspiBackup.service` to `ExecStart=/usr/local/bin/raspiBackup.sh --unsupportedEnvironment`.

<a name="parm_P"></a>
### -P: Partition-oriented backup mode

Partition-oriented mode. In contrast to normal mode, where only the
first two partitions are backed up, any number of
partitions is backed up. The `-T` option is used to define which partitions are to be
backed up.

| Option name | Default | In Installer | Configuration name |
|-------------|----------|--------------|--------------------|
| -P | off | configurable | DEFAULT_PARTITIONBASED_BACKUP |


<a name="parm_T"></a>
### -T: Specify the partitions to be backed up during partition-oriented backup

If the partition-oriented backup mode was selected with the option `-P`,
this option can be used to define which partitions
should be backed up. Example: `-T "1 2 5"` backs up the first two and the fifth
partition. With `"*"` all partitions are backed up.

| Option name | Default | In Installer | Configuration name |
|-------------|----------|--------------|--------------------|
| -T | "1 2" | no | DEFAULT_PARTITIONS_TO_BACKUP |

<a name="parm_t"></a>
### -t: Type of backup (dd, tar, rsync)

Type of backup, which can be either dd, tar or rsync. On an
ext3/ext4 partition, rsync uses hardlinks to minimize the required storage space.

[Detailed information on the backup types](backup-types.md) An external root file system
used in hybrid boot mode is
automatically with a `tar` or `rsync` backup saved, unless the `-P` option is used.
With the `-z` option, the `dd` and `tar` backups are also zipped or reduced in size.
reduced in size.
The default compresion tool used is gzip for dd and tar. For tar the option [--tarcompressionTool](
https://framps.github.io/raspiBackupDoc/backup-options.html#--tarcompressiontool-definition-of-the-tar-compression-tool-to-be-used) can also be used instead of option `-z` to use another compression tool.

**Note**:
With the dd backup, the configuration parameter
DEFAULT_DD_BACKUP_SAVE_USED_PARTITIONS_ONLY can save backup time and space.

See also [FAQ16](faq.md#faq16).

| Option name | Default | In Installer | Configuration name |
|-------------|----------|--------------|--------------------|
| -t | rsync | configurable | DEFAULT_BACKUPTYPE |


<a name="parm_u"></a>
### -u: Exclude additional directories from the backup process

Extension of the exclude list during backup to ignore certain directories during backup.

**Attention**:
The parameters have to obey the respective syntax of the backup tool
otherwise the backup will be aborted or the desired files and directories are not excluded.

Example for rsync:
```
"--exclude=/backup/* --exclude=/rsnapshot/* --exclude=/www-data*/* --exclude=/home/pi/.local/share/Trash"
```

Example for tar:
```
"--exclude=/backup --exclude=/rsnapshot --exclude=/home/pi/.local/share/Trash"
```

The quotation marks are important! Further information on the syntax can be found
on the man page of the respective backup tools.

The following directories are never backed up:

- The backup path that was specified in the call
- All mounted partitions other than the root partition
- /proc
- /lost+found
- /sys
- /dev
- /tmp
- /run
- /var/swap
- /swapfile
- /media

In addition, all mounted directories from external devices that are not
mounted on / are not backed up. Only the boot partition
/dev/mmcblk0p1 and the root partition /dev/mmcblk0p2 or the external
root directory (hybrid boot mode) on e.g. /dev/sda1 are backed up.

**Note for the partition-oriented mode**:
If the -P option is used, the above-mentioned directories are excluded from all partition backups.

**rsync**:

- */directory/* - Excluded directory on all partitions
- mmcblk0p2/directory/* - Excluded directory on partition mmcblk0p2

**tar**:

- directory - Excluded directory on all partitions

| Option name | Default | In Installer | Configuration name |
|-------------|----------|--------------|--------------------|
| -u | none | no | DEFAULT_EXCLUDE_LIST |

<a name="parm_v"></a>
### -v: All messages from the backup tool used are logged

The tar and rsync backup tools used display detailed information
(verbose mode). This option is particularly useful for initial manual backup tests
in order to be able to track the backup progress.

| Option name | Default | In Installer | Configuration name |
|-------------|----------|--------------|--------------------|
| -v | off | no | DEFAULT_VERBOSE |

<a name="parm_z"></a>
### -z: Compression of the backup with dd or tar

Reduce backup size with gzip for dd or tar backup.

| Option name | Default | In Installer | Configuration name |
|-------------|----------|--------------|--------------------|
| -z | off | configurable | DEFAULT_ZIP_BACKUP |

**Note:** This option deactivates the tar compression tool options.


</div>

[.status]: translated
