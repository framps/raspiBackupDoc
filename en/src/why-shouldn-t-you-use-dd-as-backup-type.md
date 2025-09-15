# Why is it better not to use dd as a backup type?

Many users of *raspiBackup* use `dd` as backup type.
Especially users who work more with *Windows* than with *Linux*, because they can restore a
dd backup under Windows with *win32imager* or similar tools.

dd can of course be used as a backup tool, but there is a certain
risk that does not exist with the tar and rsync backup methods.
It is therefore recommended that every user of *raspiBackup* should use tar or rsync
instead.

## Why?

1. dd backs up an entire partition 1 to 1 at bit level. Errors are reported
   are reported if the bits cannot be read. However, there are also
   file system errors occur from time to time. These are usually caused by
   sudden power failure. These errors are not noticed by dd. This means that dd backs up
   a partition including the file system errors, which are then also restored during the restore.
   restored. Thus you have an exact copy of the system with
   file system errors. You keep creating backups in the belief that everything is OK
   and then delete old backups at some point. Thus, little by little
   unnoticed, backups without file system errors are replaced by backups with file system errors.
   replaced. If a restore is then required, you no longer have a backup without
   file system errors and can only hope that the file system errors have not
   have damaged any important system data. Otherwise the backup is
   useless.

2. When restoring a dd backup, the backup is restored 1 to 1 at bit level.
   is restored. If the SD card is not OK, often no error is reported by
   dd is reported. If you then boot the system, it does not start or there are
   error messages from system services. Then the users get in touch and
   create a problem report because *raspiBackup* is not working correctly.
   After they are then asked to perform a restore to a new SD card
   the problem disappears. These problem reports are
   unnecessary effort that should be avoided.

## What now?

Switching to tar is quick and easy. The same file system can be used on the
on the backup partition can be used as for dd.

However, the restore can no longer be carried out with Windows programs such as *Win32DiskImager*
or *Etcher*.

Instead, you can start *raspiBackup* on a Raspberry.
If you only have **one** Raspberry available, you should get a one-time
"emergency SD card" with Raspbian and *raspiBackup* and put it aside,
until you need it...

For rsync you need an ext2/3/4 file system on the backup partition. This
can be created under Linux. The restore is also done with
*raspiBackup* on a Raspberry.

## Further disadvantages of dd backups

With a dd backup, the entire partition is always backed up - even if
only a fraction of the partition (e.g. 33%) is used. This means that with a
64GB partition, 42GB are always backed up for nothing, the backup process takes
unnecessarily takes 66% longer and the backup occupies 66% more disk space.
more disk space. There is the option **DD_BACKUP_SAVE_USED_PARTITIONS_ONLY** with which
only the existing root partition is backed up and not the entire device.

## Which backup type is the best?

The most efficient backup type is *rsync*. By using hardlinks
only files that have changed are copied and therefore all but the first
the first backup process is completed relatively quickly. In addition, the
files are unpacked and can be accessed directly if only a few files from the backup are needed.
a few files from the backup are required. With *tar* and *dd* you have to
the backups have to be unpacked first.

## Further information

  - [How do hardlinks work](how-do-hardlinks-work-with-rsync.md)
  - [Which file system can be used on the backup device?](which-filesystem-can-be-used-on-the-backup-partition.md)

[.status]: translated
[.source]: https://www.linux-tips-and-tricks.de/de/raspibackupcategoried/579-warum-sollte-man-dd-als-backupmethode-besser-nicht-benutzen
[.source]: https://www.linux-tips-and-tricks.de/en/raspibackupcategorye/581-why-shouldn-t-you-use-dd-as-backup-method


