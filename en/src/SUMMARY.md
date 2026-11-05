<!-- vim: set conceallevel=0: -->
# raspiBackup

```
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

Note: This file here (SUMMARY.md) is used by *mdbook* to determine the
contents and structure of the book to be generated.

The following data is evaluated for this:

  - the headings level 1 (#)
  - links for prefix- and suffix-chapters
  - all lists (even nested)
  - horizontal rules ---

Lists are only allowed to contain links.
Any link provides the title of a chapter and the name of the corresponding file.

That allows for some tricks:

1.) Comments are possible in this file. E.g.:
    a.) This leading note. Additionally the comment is marked up as code block.
        So the list above won't be parsed as such.
    b.) "TODO marker" or similar.

2.) Chapters can be "deactivated" by making the link invalid.

    For example:

    private](very-private.md)

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
```


[Introduction](introduction.md)

[Usage tips](help.md)

# User guide

- [Function overview](function-overview.md)

- [Supported hardware and software](supported-hardware-and-software.md)

- [Language support](language-support.md)

- [Quickstart - Installation in 5 minutes](installation-in-5-minutes.md)
    - [Use without installation](using-raspibackup-without-installation.md)

- [Installer - invocation and options](installer.md)
    - [Manual installation and configuration](manual-installation-and-configuration.md)
    - [Statistics](statistics.md)
    - [Updates](updates.md)

- [Typical use cases](usecases.md)
    - [Typical backup use cases](usecases-backup.md)
    - [Typical restore use cases](usecases-restore.md)

- [Function details](function-intro.md)
    - [Backup](backup-intro.md)
        - [Decision tree for backup types](backup-types.md)
        - [Comparison of partition-oriented and normal backup](normal-or-partition-backup.md)
        - [Backup directory structure](backup-directory-structure.md)
        - [Intelligent rotation strategy](smart-recycle.md)
        - [Snapshots](snapshots.md)
        - [Docker support](docker-support.md)
        - [Configuration update when upgrading to a new version](configuration-update-when-upgrading-to-a-new-version.md)
        - [Multiple backup tasks](multiple-backup-tasks.md)
        - [eMail configuration examples](configuration-examples.md)
            - [msmtp configuration for a web.de account](msmtp-configuration-for-web-de-account.md)
            - [Exim4 configuration](exim4-configuration.md)
            - [nullmailer configuration](nullmailer-configuration.md)
   - [Backup and clone](how-to-enable-clone.md)
   - [Restore](restore-intro.md)
        - [Restore single files/directories](how-to-retrieve-single-files-or-directories-from-the-backup.md)
        - [Manual rsync restore](manual-restore.md)
        - [Manual tgz restore](manual-restore-of-a-tgz-backup.md)
   - [General](more-questions-and-answers.md)
        - [Notifications](notifications.md)
        - [Which filesystem can be used on the backup partition?](which-filesystem-can-be-used-on-the-backup-partition.md)
        - [How do hardlinks work together with rsync?](how-do-hardlinks-work-with-rsync.md)
        - [Why is it better not to use dd as a backup type?](why-shouldn-t-you-use-dd-as-backup-type.md)
        - [Move the Raspberry OS from SD card to SSD, USB disk or USB stick](migrate-the-raspberry-os-from-sd-card-to-ssd-usb-disk-or-usb-pen-drive.md)
        - [How can I install and test the beta version?](how-can-i-install-and-test-the-beta-version.md)
        - [Is an external root partition supported (hybrid boot mode)?](external-root-partition.md)
        - [Tips for large SD cards, HDDs and SSDs](large_devices.md)

- [raspiBackup - Invocation and options](invocation-options.md)
    - [Backup](backup.md)
        - [Options](backup-options.md)
        - [Configuration](backup-config-options.md)
    - [Restore](restore.md)
        - [Options](restore-options.md)
        - [Configuration](restore-config-options.md)
    - [General](general.md)
        - [Options](general-options.md)
        - [Configuration](general-config-options.md)
    - [Options grouped by topic](options-by-topic.md)

- [Frequently asked questions / FAQ](faq.md)

- [Error messages and troubleshooting](error-messages.md)

- [raspiBackupDialog](raspibackupdialog-a-convenient-helper-script-for-raspibackup.md)

- [Backup targets](backup-targets.md)
    - [NFS as backup target](nfs-as-backuptarget.md)
    - [SMB as backup target](smb-as-backuptarget.md)
    - [AVM FRITZ!Box as backup target](avm-fritzbox-as-backuptarget.md)
    - [WebDAV as backup target](webdav-as-backuptarget.md)

- [Tips for home automation](tips-homeautomation.md)

- [Helpful links on the subject of backup](helpful-links.md)
- [Other backup tools](other-raspberry-backup-tools.md)

- [Miscellaneous](miscellaneous.md)
    - [Version history](version-history.md)
    - [*raspiBackup* logo](raspibackup-has-a-new-logo.md)
    - [10 years *raspiBackup*](10-years-raspibackup.md)
    - [Executed regression tests](regressiontests-executed.md)
    - [Development environment](development-environment.md)
    - [Users all over the world](list-of-countries-raspibackup-is-used-in-the-world.md)
    - [Version of this documentation](doc-version-info-automatically-generated.md)
    - [Markdown playground](markdown-playground.md)

# Developer guide

- [Extension points](hooks-for-own-scripts.md)
- [Extension scripts](extension-scripts.md)
- [Support new languages](local-language-support-for-languages-other-than-de-and-en-l10n.md)

[.status]: z_SUMMARY
[.status]: translated
