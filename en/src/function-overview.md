# Function overview

This page contains a high-level overview of *raspiBackup*.

More detailed information can be found here in the further documentation
and on the [*GitHub* page](https://github.com/framps/raspiBackup).

**With *raspiBackup* you can quickly and securely obtain a complete system backup of your Raspberries and a configurable backup history on a regular basis.
and can thus completely restore your Raspberry so that it boots again with an old backup status**.
 
  - Open source

    *raspiBackup* is available under the GNU license as open source and free of charge.
    However, a [donation](introduction.md#donation) is still welcome 😉

  - Simple [installation](installation-in-5-minutes.md) with menu-driven installer (comparable to `raspi-config`)

    The most important options of *raspiBackup* can be configured in German, English, Finnish,
    Chinese and French, so that the first [backup in 5 minutes](installation-in-5-minutes.md) can be created.

  - All other options, some of which are very powerful, are [documented in detail](invocation-options.md)
    and can be defined in a configuration file.

  - Complete and incremental backups

      - The backup type `rsync` creates complete and then incremental backups
      - The backup types `dd` and `tar` always create complete backups
        Note: With the `dd` backup there is an option to switch on that only the space occupied by the partitions
        and not the entire SD card is backed up.

  - Two backup strategies

      - A defined number of backups are stored
      - Backups are kept according to the grandfather-father-son backup strategy (GVS).

  - Any directories and files can be excluded from the backup (`-u` option)

  - Automatic regular backup of a running Raspberry Pi (it backs itself up)

  - Different backup types can be mixed per system (e.g. one `rsync` backup per day, one `dd` backup per week)

  - Automatic stopping and starting of active services before and after the backup (`-a` and `-o` option)

  - Backup of any number of Raspberries in a backup directory

  - Messages in German and English

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

      1. boot from the SD card: Both partitions are on the SD card
         (every model)
      2. mixed mode: Boot from the SD card and use of the root partition
         from a USB device. This is necessary for older Raspberries that
         do not yet support USB boot.
      3. boot from a USB device or SSD (USB boot mode): Both partitions
         are located on a USB device. Supported by the newer Raspberries
         supported.

  - Any backup destinations are possible, e.g.

      - External USB stick
      - External USB disk
      - Synology NAS
      - *SMB* network drive
      - *NFS* network drive
      - *SSHFS* network drive
      - *WebDAV* network drive
      - *FtpFS* network drive
      - Generally any device that can be mounted under Linux

  - An external root file system on a hard disk or USB stick is automatically
    automatically during normal backup mode and restored during `tar` or `rsync` backup.
    or `rsync` backup.

  - Snapshots

    For example, at important update or installation times, snapshots can be
    snapshots can be created with a description. In the event of a major
    error or a system that no longer boots, they allow you to restart the system
    without having to start the update or reinstallation from scratch.
    having to start all over again.

  - Any number of backups from the past can be stored

    Not only a single backup is created, but also a backup history.
    You can either define a number of backups to be kept,
    or you can use the *GVS* principle (called "intelligent rotation strategy" in *raspiBackup*)
    called)

  - An intelligent backup strategy is available
    (backups of the last 7 days, the last 4 weeks, the last 12 months and the last n years are kept)

  - Simple restoration of a backup

    A backup of the backup type 'dd' can also be restored to a Windows system.
    *Win32Diskimager* or similar tools can be used.
    `tar` and `rsync` require a Linux system for restoration.
    It is recommended to use a preconfigured SD card with *Raspberry Pi OS*
    and start it on a Raspberry.

  - Adaptation of `/etc/fstab` and `/boot/cmdline.txt` to new UUIDs, PARTUUIDs
    or LABELs so that the system starts again immediately.

  - [Active social media channels](introduction.md#contact)

  - Notifications for new releases

    As soon as a beta or a new release is available, *raspiBackup* writes a
    message indicating this. An upgrade is easy to perform. Likewise a
    downgrade back to a previous release.

  - Regression test suite

    The basic functionality of *raspiBackup* (backup and restore) is automatically tested
    automatically tested for all backup types and modes to ensure that the new *raspiBackup
    new *raspiBackup* release works as reliably as before.

  - Documentation

    User manual, FAQs, configuration examples, NFS configuration on a Synology
    Synology, list of error messages and how to fix them and much more.
    and much more.

  - Help and sample scripts

    Various help and example scripts are available.

    For example, how *pishrink* can be used to make an `dd` backup even smaller
    or how a clone can be created in parallel in order to have an up-to-date boot medium
    boot medium that can be used at any time. And much, much more.

    A sample script helps to carry out further actions before and after the backup,
    such as mounting and unmounting the backup space.

  - Extension points

    Custom code can be executed before and after the backup in order to prepare and
    and post-processing during the backup and restore.

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
