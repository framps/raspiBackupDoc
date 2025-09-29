# Snapshots

With the option `-M`, *raspiBackup* offers the possibility to create a kind of *snapshot*.
These are normal backups, but they have two special features:

  - Snapshots are **not automatically deleted** by the selected backup strategy
  - Snapshots must be given a description as a parameter to the `-M` option.
    This is appended to the end of the directory name and allows to give the snapshot
    directories meaningful names to remember their purpose.

This makes it very easy to create a snapshot out of sequence
and the reason for the snapshot can be recognized by the description.
This is very helpful, for example, before carrying out a
software update or planning another major change. If the
update goes wrong, you can quickly restore the previous status.
If it was successful, the snapshot must be deleted manually from the backup directory.

**Note:**
*raspiBackup* snapshots are not snapshots in the true sense of the word as they can be created with *btrfs*, for example.
They are normal `dd`, `tar` or `rsync` backups.
`rsync` backups are delta backups and are therefore complete more quickly than `dd` or `tar` backups.

There is a [Youtube video](https://www.youtube.com/watch?v=8BlF9B8EX6k),
in which the *raspiBackup* snapshots are explained and a demo is given.

[.status]: translated
[.source]: https://linux-tips-and-tricks.de/de/snapshots



