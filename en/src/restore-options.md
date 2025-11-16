# Restore options

By default, *raspiBackup* restores the [**entire system**](restore-intro.md) in normal backup mode.
In partition-oriented mode, however, you can select which partitions are to be restored,
If the partition-oriented mode
the `rsync` backup type is used, a delta restore can also be selected for a restore (option -00).
This means that only the changed files and deleted files from the backup are copied with `rsync
and files not present in the backup - i.e. newly created files - are deleted.
This allows a very fast restore.

Independent of *raspiBackup*, a [manual restore](manual-restore.md)
of the data with the previously used backup tools `dd`, `tar` or `rsync` is also possible.
This requires appropriate knowledge of the Linux backup tools.

It is also possible to manually [restore individual files/directories](how-to-retrieve-single-files-or-directories-from-the-backup.md).

------------------

<!-- toc -->

------------------

<div class="table-wrapper-for-options">

<a name="parm_C"></a>
### -C: Check for badblocks

When formatting, `mkfs.ext4 -c` is used to check for bad blocks.
Note: This increases the restore time.

| Option | Default | In Installer | Configuration name |
|--------|----------|--------------|--------------------|
| -c | off | no | DEFAULT_CHECK_FOR_BAD_BLOCKS |

<a name="parm_d"></a>
### -d: Restoredevice

Device on which the backup is restored.

| Option | Default | In Installer | Configuration name |
|--------|----------|--------------|--------------------|
| -d | none | no | DEFAULT_RESTORE_DEVICE |

Example: `-/dev/sda`

**Note:** The parameter must be a device and not a partition. It must not be a
partition number such as `/dev/sda1` must not be present.

**Attention:** This device is usually completely deleted and recreated! With `tar` and
and `rsync` backup, the size of the *root* partition is automatically
reduced or enlarged if the target device has a different size
than the backed up system. Of course, there must still be enough space on the target device for the
data of the source system on the target device. If there is not enough space, the restore will fail.

<a name="parm_N"></a>
### -N: Extensions to be called before and after the restore

Activation of own script extensions (plugins). See [this page](hooks-for-own-scripts.md),
which also offers two sample extensions that control the CPU temperature and the
memory usage before and after the backup run.

| option name | default | in installer | configuration name |
|-------------|----------|--------------|--------------------|
| -N | none | no | DEFAULT_EXTENSIONS |


<a name="parm_R"></a>
### -R: External root partition

This option can be used to restore backups of systems that use an external
partition as root partition, such as USB sticks or hard disks.
This is only possible if a `tar` or `rsync` backup is available.
The parameter defines the partition on which the root directory is to be restored.
is to be restored.  Example: `/dev/sdb1`.

| Option | Default | In Installer | Configuration name |
|--------|----------|--------------|--------------------|
| -R | no | no | |

**Note:** Only use this option if both an SD card and an external
external root file system is used on one device. Otherwise the `-d` option is sufficient.
This option is only useful for older Raspberries that do not support USB boot.

**Attention:** The partition will be **reformatted**. Therefore, make sure that it is the
correct partition and that the partition is large enough to accommodate the partition
of the backup!

**Note:** This option is only available if the normal backup mode has been used.
In partition-oriented mode (option `-P`) no external root partition can be
backed up.

<a name="parm_resizeLastPartitionFS"></a>
### --resizeLastPartitionFS: Letzte Partition anpassen

**Available starting with release 7.2**

During the restoration of a partition-oriented backup
the last partition can be extended to the maximum available
size of the target device. If the
option is switched off with `--resizeLastParitionFS-`, the last partition is created as large
as it was on the original system.

| Option | Default | In Installer | Configuration name |
|--------|----------|--------------|--------------------|
| --resizeLastPartitionFS | yes | no | |


<a name="parm_resizeRootFS"></a>
### --resizeRootFS: Expand root parition 

During the restore, the root partition can be expanded to the maximum available
size of the target device. If the
option is switched off with `--resizeRootFS-`, the root partition is created as large
as it was on the original system. If the -P option is used, the last partition on the
partition on the device is extended. If there are more than 2 partitions, it is not the root partition.

| Option | Default | In the installer | Configuration name |
|--------|----------|--------------|--------------------|
| --resizeRootFS | yes | no |

<a name="parm_T"></a>
### -T: Partitions to restore

With the partition-oriented `rsync` backup, partitions can be
selected that are to be restored. With `"*"` all partitions are
restored.

| Option | Default | In Installer | Configuration name |
|--------|----------|--------------|--------------------|
| -T | "1,2" | no | DEFAULT_PARTITIONS_TO_RESTORE | |

<a name="parm_updateUUIDs"></a>
### --updateUUIDs: Customize the UUIDs

When restoring, the PARTUUIDs, UUIDs and LABELs are always
restored. This usually causes problems if you mount the restored
system on the original system. With this option, new PARTUUIDs, UUIDs and LABELs are generated during the
generated during the restore.

| Option | Default | In Installer | Configuration name |
|--------|----------|--------------|--------------------|
| --updateUUIDs | yes | no |

<a name="parm_Y"></a>
### -Y: Automated restore

By default, before the restore, the system displays what the restored device currently
looks like 
and asks whether you really want to overwrite the device. If the
restore is to be automated, this option suppresses the query.

**Caution:** This may result in the wrong device being overwritten unintentionally
and delete important data.

| Option | Default | In Installer | Configuration name |
|--------|----------|--------------|--------------------|
| -Y | off | no |

In addition, the option `DEFAULT_YES_NO_RESTORE` must be set accordingly in the configuration file
for thei restoredevices.

<a name="parm_0"></a>
### -0: No partitioning

No new partition layout is created on the target device, but the existing one is used.
This allows you to perform the desired partitioning before the restore.
For details see [FAQ #6](faq.md#faq6)

| Option | Default | In Installer | Configuration name |
|--------|----------|--------------|--------------------|
| -0 | off | no |

<a name="parm_00"></a>
### -00: No partitioning and formatting

This will not format the partitions selected with the `-T`
option during an `rsync` partition-oriented backup.
This speeds up the restore process considerably, as only new, changed or deleted files are synced,

| Option | Default | In Installer | Configuration name |
|--------|----------|--------------|--------------------|
| -00 | off | no |

<a name="parm_1"></a>
### -1: Ignore partitioning errors

The partition layout will be created on the SD card as it exists on the source device
and any errors that are detected - including the error that the target
error that the target device is too small - are ignored.  See [FAQ #6](faq.md#faq6) for more details.
more details.

| Option | Default | In Installer | Configuration Name |
|--------|----------|--------------|--------------------|
| -1 | off | no |

Note: This option can have unexpected results.
Only use this option if you know what you are doing.

</div>

[.status]: translated


