<!-- vim: set conceallevel=0: -->
# raspiBackup

```
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

Note: This file here (SUMMARY.md) is used by *mdbook* to determine the
contents and structure of the book to be generated.

Following data is read for this:

  - the headings level 1 (#)
  - links for prefix- and suffix-chapters
  - all lists (even nested)
  - horizontal rules ---

Lists are only allowed to have links in it.
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

# User guide

- [Function overview](function-overview.md)

- [Supported hardware and software](supported-hardware-and-software.md)

- [Language support](language-support.md)

- [Function detail](function-intro.md)
    - [Backup](backup-intro.md)
        - [Decision tree for backup types](backup-types.md)
        - [Comparison of partition orientated and normal backup](normal-or-partition-backup.md)
        - [Backup directory structure](backup-directory-structure.md)
        - [Rotation strategy](smart-recycle.md)
        - [Snapshots](snapshots.md)
        - [Configuration update when upgrading to a new version](configuration-update-when-upgrading-to-a-new-version.md)
        - [Configuration examples](configuration-examples.md)
            - [msmtp configuration for a web.de account](msmtp-configuration-for-web-de-account.md)
            - [Exim4 configuration](exim4-configuration.md)
            - [nullmailer configuration](nullmailer-configuration.md)

    - [Restore](restore-intro.md)
        - [Restore single files/directories](how-to-retrieve-single-files-or-directories-from-the-backup.md)
        - [Manual rsync restore](manual-restore.md)
        - [Manual tgz restore](manual-restore-of-a-tgz-backup.md)

    - [General](more-questions-and-answers.md)
        - [Which filesystem can be used on the backup partition?](which-filesystem-can-be-used-on-the-backup-partition.md)
        - [How do hardlinks work with rsync?](how-do-hardlinks-work-with-rsync.md)
        - [Why shouldn't you use dd as backup type?](why-shouldn-t-you-use-dd-as-backup-type.md)
        - [How to create a cold standby clone with raspiBackup?](how-to-create-a-cold-standby-clone-with-raspibackup.md)
        - [Migrate the Raspberry OS from SD-card to SSD, USB-disk or USB-pen-drive](migrate-the-raspberry-os-from-sd-card-to-ssd-usb-disk-or-usb-pen-drive.md)
        - [How can I install and test the beta version?](how-can-i-install-and-test-the-beta-version.md)
        - [Is an external root partition supported?](external-root-partition.md)

- [Installation and first backup](installation.md)
    - [Quickstart-Installation in 5 minutes](installation-in-5-minutes.md)
    - [Manual installation and configuration](manual-installation-and-configuration.md)
    - [Statistics](statistics.md)
    - [Updates](updates.md)

- [Usage and options](details.md)
    - [Backup](backup.md)
        - [Options](backup-options.md)
        - [Configuration](backup-config-options.md)
    - [Restore](restore.md)
        - [Options](restore-options.md)
        - [Configuration](restore-config-options.md)
    - [general](general.md)
        - [Options](general-options.md)
        - [Configuration](general-config-options.md)
    - [Options grouped by topic](options-by-topic.md)

- [Frequently asked questions / FAQ](faq.md)

- [Error messages](error-messages.md)

- [Helper scripts](helper-scripts.md)
    - [raspiBackupDialog - a convenient helper script](raspibackupdialog-a-convenient-helper-script-for-raspibackup.md)
    - [More helpful scripts](useful-helper-scripts.md)

- [Backup targets](backup-targets.md)
    - [NFS as backupspace](nfs-as-backupspace.md)
    - [SMB as backupspace](smb-as-backupspace.md)
    - [AVM FRITZ!Box as backupspace](avm-fritzbox-as-backupspace.md)
    - [WebDAV as backupspace](webdav-as-backupspace.md)

- [Tips for home automation](tips-homeautomation.md)

- [Helpful links regarding backup](helpful-links.md)
- [Other backup tools](other-raspberry-backup-tools.md)

- [Miscellaneous](miscellaneous.md)
    - [Version history](version-history.md)
    - [*raspiBackup* logo](raspibackup-has-a-new-logo.md)
    - [10 years *raspiBackup*](10-years-raspibackup.md)
    - [Executed regression tests](regressiontests-executed.md)
    - [Development environment](development-environment.md)
    - [Users all over the world](list-of-countries-raspibackup-is-used-in-the-world.md)
    - [Version of this documentation](doc-version-info-automatically-generated.md)
    - [Markdown Playground](markdown-playground.md)

# Developer guide

- [Hooks for own scripts](hooks-for-own-scripts.md)
- [Plugpoints](extension-scripts.md)
- [Support new languages](local-language-support-for-languages-other-than-de-and-en-l10n.md)


[.status]: z_SUMMARY
