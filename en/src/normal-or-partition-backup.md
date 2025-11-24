# Comparison of partition-oriented backup and normal backup

There are two backup modes:

1. Normal backup

   In this mode, the first two partitions (the boot partition and the root partition)
   of the SD card are backed up. In addition, the `tar` and `rsync` backup
   also back up an external root partition, i.e. a root partition stored on a USB stick or USB disk.
   If the target device is larger than the source device during the restore,
   the second partition is automatically extended accordingly.

   The entire SD card can also be backed up with the `dd` backup.
   However, we strongly advise against using an `dd` backup.
   See: [Why is it better not to use dd as a backup type?](why-shouldn-t-you-use-dd-as-backup-type.md)

3. Partition-oriented backup

   In this mode, every partition on the system or a specific selected
   number of partitions are backed up with `tar` or `rsync`. The number of
   partitions is arbitrary. During restore, you can also select which partitions
   are to be restored.
   If you are restoring to the original system because changes
   to the system have prevented it from booting, with an rsync backup you can restore only the changes
   instead of the entire backup, and the restore will be much faster.
   If the target device is larger than the
   source device during the restore, the last partition is expanded to use the entire target device.

[.status]: translated
[.source]: https://www.linux-tips-and-tricks.de/de/raspibackup#Vergleich
[.source]: https://www.linux-tips-and-tricks.de/en/backup

