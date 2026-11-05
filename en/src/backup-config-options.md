# Backup configuration options

The following options can only be defined in a [configuration file](invocation-options.md#configFiles).
Most invocation options can also be configured there. See [Backup options](backup-options.md).

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
This means that a 32GB SD card, for example, which only has an 8GB partition defined, only needs 8GB
and not 32GB for the backup. To do this, however, gparted or resize2fs have to be used
beforehand to reduce the root partition size, because the root partition usually fills
the entire rest of the SD card and therefore unused space is also backed up.

See also [FAQ16](faq.md#faq16).

| Config option | Default |
|----------------------------|----------|
| DEFAULT_DD_BACKUP_SAVE_USED_PARTITIONS_ONLY | none |

### DEFAULT_LINK_BOOTPARTITIONFILES

Rarely changing boot partition backups are linked with hardlinks to save backup space.
Prerequisite: The backup space supports hardlinks
(ext3/ext4 file system).

| Config option | Default |
|----------------------------|----------|
| DEFAULT_LINK_BOOTPARTITIONFILES | none |

### DEFAULT_MAIL_ON_ERROR_ONLY

An eMail notification is only sent in the event of an error.

**Exceptions:**

In the following cases an eMail will be sent despite this option:
1. For every warning message
1. Notification of the availability of a new release (RBK0080I)
1. Notification of the availability of a beta (RBK0168I)
1. Notification to perform a restore test again (RBK0202I)

**Note:**

If *raspiBackup* crashes due to exceptional circumstances, it may happen that no eMail is sent.

| Config option | Default |
|----------------------------|----------|
| DEFAULT_MAIL_ON_ERROR_ONLY | none |

### DEFAULT_REBOOT_SYSTEM

This option can be used to configure a reboot of the backed up system at the end of the backup.

**Note**: The services that were stopped before the backup are not restarted. This is unnecessary as they are started anyway when the system is restarted.

| Config option | Default |
|----------------------------|----------|
| DEFAULT_REBOOT_SYSTEM | 0 |

### DEFAULT_RSYNC_BACKUP_ADDITIONAL_OPTIONS

Backup options that are used for rsync backup in addition
to the standard options of *raspiBackup*.

**Use at your own risk!**

| Config option | Default |
|----------------------------|----------|
| DEFAULT_RSYNC_BACKUP_ADDITIONAL_OPTIONS | none |

### DEFAULT_RSYNC_BACKUP_OPTIONS

This can be used to overwrite the rsync default backup options.

**Use at your own risk!**

| Config option | Default |
|----------------------------|----------|
| DEFAULT_RSYNC_BACKUP_OPTIONS | --delete -aHAx |

### DEFAULT_TAR_BACKUP_OPTIONS

This can be used to overwrite the tar default backup options.

**Use at your own risk!**

| Config option | Default |
|----------------------------|----------|
| DEFAULT_TAR_BACKUP_OPTIONS | -cpi |

### DEFAULT_RSYNC_BACKUP_OPTION_EXCLUDE_ACLS

**Available starting with release 0.7.2**

This option can be used to disable the backup of ACLs with rsync.
Useful when the backup partition is connected via nfs and ACLs are not supported.

| Config option | Default |
|----------------------------|----------|
| DEFAULT_RSYNC_BACKUP_OPTION_EXCLUDE_ACLS | 0 |

### DEFAULT_TAR_BACKUP_ADDITIONAL_OPTIONS

Backup options that are used for tar backup in addition
to the standard options.

**Use at your own risk!**

| Config option | Default |
|----------------------------|----------|
| DEFAULT_TAR_BACKUP_ADDITIONAL_OPTIONS | none |

</div>

[.status]: translated


