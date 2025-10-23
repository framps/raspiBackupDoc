# Tips for large SD cards, HDDs and SSDs

When *raspiBackup* was created, there were only small SD cards and disks.
SSDs were still a luxury and also small. Nowadays, the SD cards are tens of GB in size and the disks and SSDs have tens of TB.

In *raspiBackup* Release 0.7, new features were therefore introduced to help minimize backup
and restore times for large devices. For this purpose, the partition-oriented mode is to be used
and not the normal mode, as this only supports 2 partitions. The assumption is that the
first two partitions house the OS and other large partitions are used for data.

In partition-oriented mode, you can select which partitions are to be backed up
and which partitions are to be restored (`option -T`). This allows you to regularly
back up only the first two partitions on which the OS is located in a very short time.
The other large partitions, which are used for data, can be backed up separately
at other times when fast backups are not required. If the system does not boot,
only the first two system partitions have to be restored.

It is even faster if the `option -00` is used when restoring an rsync backup. Then the partitions
are not reformatted and the complete partitions are not restored,
but only the changes that have occurred in the meantime are restored via rsync.
In this way, you can quickly restore individual partitions to the state they had at
the time of the backup. Of course, this only works if the device of the original system
and the file system are not defective. Otherwise, a complete long restore must be carried out.

If you want to make full use of devices > 2TB,
[mbr2gpt from RonR](https://forums.raspberrypi.com/viewtopic.php?t=196778) can be used toi
convert the system from mbr to gpt.

[.status]: translated
