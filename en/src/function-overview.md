# Function overview

This page contains a high-level overview of *raspiBackup*.

More detailed information can be found here in the further documentation
and on the [*GitHub* page](https://github.com/framps/raspiBackup).

**With *raspiBackup* you can quickly and securely obtain a complete system backup of your Raspberries and a configurable backup history on a regular basis
and can thus completely restore your Raspberry so that it boots again with an old backup status**.

  - Open source

    *raspiBackup* is available under the GNU license as open source and free of charge.
    However, a [donation](introduction.md#donation) is still welcome 😉

  - Simple [installation](installation-in-5-minutes.md) with menu-driven installer (comparable to `raspi-config`)

    The most important options of *raspiBackup* can be configured in German, English, Finnish,
    Chinese and French,
    so that the first [backup in 5 minutes](installation-in-5-minutes.md) can be created.

  - All other options, some of which are very powerful, are [documented in detail](invocation-options.md)
    and can be defined in a configuration file.

  - Complete and incremental backups

      - The backup type `rsync` creates complete and then incremental backups
        using [Hardlinks](how-do-hardlinks-work-with-rsync.md).
      - The backup types `dd` and `tar` always create complete backups (also zipped).
        **Note**: With the `dd` backup, you can activate the option that only the space occupied by the partitions
        and not the entire SD card is backed up.

    The individual backup types are described in detail [here](backup-types.md).
    There is also a [decision tree](backup-types.md#decisiontree),
    to quickly find the right backup type.

  - Two backup strategies

      - A defined number of backups are kept
      - Backups are kept according to the grandfather-father-son backup strategy (GVS).

  - Two [backup modes](normal-or-partition-backup.md):

      - the **normal backup mode** only backs up the boot and root partition
      - the **partition-oriented mode** backs up any number of partitions

  - Any directories and files can be excluded from the backup

  - Automatic regular backup of a running Raspberry Pi (it backs itself up)
    See also [FAQ1](faq.md#1-is-a-backup-of-a-running-system-reliable-should-not-stop-the-whole-system-before-the-backup)

  - Different backup types can be mixed per system (e.g. one `rsync` backup per day, one `dd` backup per week)

  - Automatic stopping and starting of active services before and after the backup

  - Backup of any number of Raspberries in a backup directory

  - Messages are supported in German and English, French or Finnish.  

  - Notifications

    The backup run messages can be sent from *raspiBackup* by e-mail or *Telegram*,
    *Slack* or *PushOver*. Smilies indicate the success or
    failure of the backup run. Other smilies inform about other important
    important events such as the availability of a beta or a new release
    or a reminder to perform a restoretest to test the backup integrity.
    test the backup integrity.

  - Supported email clients: *mailx*/*mail*, *sendEmail*, *ssmtp* and *msmtp*.
    Unsupported e-mail clients can be integrated using an e-mail plug-in.

  - Simple update of *raspiBackup* to the current version
  
  - Simple distribution of new script versions to a larger number of hosts

  - All boot modes are supported

      1. boot from a USB device or SSD (USB boot mode): Both partitions
         are located on a USB device. Supported by the newer Raspberries from model 3B
         supported
      2. boot from the SD card: Both partitions are on the SD card
         (every model)
      3. mixed mode: Boot from the SD card and use of the root partition
         from a USB device. This is necessary for older Raspberries that
         do not yet support USB boot

  - Any backup destinations are possible, e.g.

      - External USB stick
      - External USB disk or SSD
      - *SMB* network drive
      - *NFS* network drive
      - *SSHFS* network drive
      - WebDAV* network drive
      - *FtpFS* network drive
      - Generally any device that can be mounted under Linux

  - An external root file system on a hard disk or USB stick is automatically
    automatically backed up in mixed mode during normal backup mode
    and restored with `tar` or `rsync`.

  - Snapshots

    So-called *raspiBackup* [snapshots](snapshots.md) can be created manually.

    These are named backups that are not deleted automatically.
    They are used, for example, to back up important intermediate steps during system upgrades
    to be able to revert to previous versions at any time in the event of problems.
    be able to go back to previous versions at any time.

  - Any number of backups from the past can be stored

    Not only a single backup is created, but also a backup history.
    You can either define a number of backups to be kept,
    or you use the *GVS* principle (in *raspiBackup* called "Intelligent Rotation Strategy"
    see [Grandfather-father-son generation principle](https://www.framp.de/raspiBackupDoc/de/smart-recycle.md)).

  - An intelligent backup strategy is available
    For example, backups of the last 7 days, the last 4 weeks, the last 12 months and
    the last n years can be saved.

  - Simple restoration of a backup

    A backup of the `dd` backup type can also be restored to a Windows system.
    *Win32Diskimager* or similar tools can be used.
    `tar` and `rsync` require a Linux system for restoration.
    It is recommended to use a preconfigured SD card with *Raspberry Pi OS*
    and start it on a Raspberry.

  - Adaptation of `/etc/fstab` and `/boot/cmdline.txt` to new UUIDs, PARTUUIDs
    or LABELs so that the system starts again immediately.

  - Active social media channels](introduction.md#contact)

  - Notifications for new releases

    As soon as a beta or a new release is available, *raspiBackup* writes a
    message indicating this. An upgrade is easy to perform. Likewise a
    downgrade back to a previous release.

  - Regression test suite

    The basic functionality of *raspiBackup* (backup and restore) is automatically tested
    automatically tested for all backup types and modes to ensure that the new *raspiBackup
    new *raspiBackup* release works as reliably as before.

  - Documentation

    User manual with e.g. FAQs, configuration examples, NFS configuration,
    list of error messages and how to eliminate the error messages
    and much more is documented

  - Help and sample scripts

    Various [help and example scripts](useful-helper-scripts.md) are available.

    They can extend the functionality of *raspiBackup* and can either be used unchanged
    or adapted to your own requirements.

    For example, how *pishrink* can be used to make a `dd` backup even smaller
    or how a clone can be created in parallel in order to have an up-to-date boot medium
    boot medium that can be used at any time.

    An example script helps to perform further actions before and after the backup,
    such as mounting and unmounting the backup space.

    And much, much more.

  - Extension points

    For developers, *raspiBackup* offers various [extension points](hooks-for-own-scripts.md),
    to perform pre- and post-processing during backup as well as backing up
    by your own code.

  - Backup of *NVMe* storage

    Supported for Raspberry 5 and Compute Model 4 (CM4)

  - Supported operating systems

      - RaspbianOS / Raspberry Pi OS
      - Ubuntu

  - Simple system migration to other storage media

    Each backup can be restored to an SD card, USB disk or SSD as well as NVMe SSD
    can be restored. The system has already been moved to another device.

  - Support for *Volumio*

  - Support for *gpt* partitions


![Overview image](images/raspiBackupOverview.jpg)


[.status]: translated
[.source]: https://www.linux-tips-and-tricks.de/de/funktionsuebersicht
[.source]: https://www.linux-tips-and-tricks.de/de/raspibackup
[.source]: https://www.linux-tips-and-tricks.de/en/features
[.source]: https://www.linux-tips-and-tricks.de/en/backup


