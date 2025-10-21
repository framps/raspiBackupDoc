# Backup configuration options

Most of the invocation options can also be defined in the configuration file
`/usr/local/etc/raspiBackup.conf`.
See [Backup options](backup-options.md).

<div class="table-wrapper-for-options">

------------------

<!-- toc -->

------------------

### DEFAULT_BEFORE_STOPSERVICES / DEFAULT_AFTER_STARTSERVICES

The commands defined here are executed before or after the backup
stopping and starting system services (option -a and -o).

| Config option | Default |
|-----------------------------|----------|
| DEFAULT_BEFORE_STOPSERVICES | none |
| DEFAULT_AFTER_STARTSERVICES | none |


### DEFAULT_DD_BACKUP_SAVE_USED_PARTITIONS_ONLY

With this option, dd backups only save the space occupied by defined partitions.
This means that a 32GB SD card, for example, which only has an 8GB partition defined, only requires 8GB for the
and not 32GB. To do this, however, you must use gparted or resize2fs
ito reduce the root partition size accordingly, because the root partition usually fills
the entire rest of the SD card.

See also [FAQ16](faq.md#faq16).

| Config option | Default |
|----------------------------|----------|
| DEFAULT_DD_BACKUP_SAVE_USED_PARTITIONS_ONLY | none |

### DEFAULT_LINK_BOOTPARTITIONFILES

Rarely changing boot partition backups are linked with hardlinks to save backup space.
Prerequisite: The backup space supports hard links
(ext3/ext4 file system).

| Config option | Standard |
|----------------------------|----------|
| DEFAULT_LINK_BOOTPARTITIONFILES | none |

### DEFAULT_MAIL_ON_ERROR_ONLY

An email notification is only sent in the event of an error.
**Note:**
If *raspiBackup* crashes due to exceptional circumstances, it may happen that no e-mail is sent,

| Config option | Default |
|----------------------------|----------|
| DEFAULT_MAIL_ON_ERROR_ONLY | none |

### DEFAULT_REBOOT_SYSTEM

This option can be used to configure a reboot of the backed up system at the end of the backup.

**Note**: The services that were stopped before the backup are not restarted.
restarted. This is unnecessary as they are started anyway when the system is restarted.

| Config option | Default |
|----------------------------|----------|
| DEFAULT_REBOOT_SYSTEM | 0 |

### DEFAULT_RSYNC_BACKUP_ADDITIONAL_OPTIONS

Backup options that can be used for rsync backup in addition
to the standard options of *raspiBackup*.

**Use at your own risk!

| Config-Option | Standard |
|----------------------------|----------|
| DEFAULT_RSYNC_BACKUP_ADDITIONAL_OPTIONS | none |

### DEFAULT_RSYNC_BACKUP_OPTIONS

This can be used to overwrite the rsync default backup options.

**Use at your own risk!

| Config option | Standard |
|----------------------------|----------|
| DEFAULT_RSYNC_BACKUP_OPTIONS | --delete -aHAx |

### DEFAULT_TAR_BACKUP_OPTIONS

This can be used to overwrite the tar default backup options.

**Use at your own risk!

| Config-Option | Standard |
|----------------------------|----------|
| DEFAULT_TAR_BACKUP_OPTIONS | -cpi |


### DEFAULT_TAR_BACKUP_ADDITIONAL_OPTIONS

Backup options that are used for tar backup in addition
to the standard options.

**Use at your own risk!

| Config option | Standard |
|----------------------------|----------|
| DEFAULT_TAR_BACKUP_ADDITIONAL_OPTIONS | none |

</div>

[.status]: translated


