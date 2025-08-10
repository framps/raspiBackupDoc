# Backup Konfigurationsoptionen

Die meisten Aufrufoptionen können auch in der Konfigurationsdatei
definiert werden. Siehe dazu [Backup-Optionen](backup-options.md).

<div class="table-wrapper-for-options">

------------------

<!-- toc -->

------------------

### DEFAULT_BEFORE_STOPSERVICES / DEFAULT_AFTER_STARTSERVICES

Die hier definierten Befehle werden vor bzw. nach dem Backup
vor bzw. nach dem Stoppen von Systemservices (Option -a und -o) ausgeführt.

| Config-Option               | Standard |
|-----------------------------|----------|
| DEFAULT_BEFORE_STOPSERVICES |          |
| DEFAULT_AFTER_STARTSERVICES |          |


### DEFAULT_DD_BACKUP_SAVE_USED_PARTITIONS_ONLY

dd Backups sichern durch diese Option nur den von definierten Partitionen belegten Platz.
Dadurch benötigt z.B. eine 32GB SD Karte, die nur eine 8GB Partition definiert hat, für den
Backup nur 8GB und nicht 32GB. Dazu muss aber mittels gparted oder resize2fs
die root Partition entsprechend verkleinert werden, denn üblicherweise füllt
die root Partition den gesamten Rest der SD Karte aus.

Siehe dazu auch [FAQ16](faq.md#faq16).

| Config-Option              | Standard |
|----------------------------|----------|
| DEFAULT_DD_BACKUP_SAVE_USED_PARTITIONS_ONLY |          |

### DEFAULT_LINK_BOOTPARTITIONFILES

Sich selten ändernde Bootparition Backups werden mit Hardlinks verknüpft, um
Backupspace zu sparen. Voraussetzung: Der Backupspace unterstützt Hardlinks
(ext3/ext4 Filesystem).

| Config-Option              | Standard |
|----------------------------|----------|
| DEFAULT_LINK_BOOTPARTITIONFILES |          |

### DEFAULT_MAIL_ON_ERROR_ONLY

Nur im Fehlerfalle wird eine eMailbenachrichtigung gesendet.
**Hinweis:**
Sollte *raspiBackup* wegen außergewöhnlicher Umstände abstürzen, kann es passieren,
dass keine eMail gesendet wird.

| Config-Option              | Standard |
|----------------------------|----------|
| DEFAULT_MAIL_ON_ERROR_ONLY |          |

### DEFAULT_REBOOT_SYSTEM

Mit dieser Option kann ein Reboot des gesicherten Systems am Ende des Backups
konfiguriert werden.

**Hinweis**: Die Services, die vor dem Backup gestoppt wurden, werden nicht wieder
gestartet. Das ist unnötig, da sie sowieso beim Neustart gestartet werden.

| Config-Option              | Standard |
|----------------------------|----------|
| DEFAULT_REBOOT_SYSTEM      |    0     |

### DEFAULT_RSYNC_BACKUP_ADDITIONAL_OPTIONS

Backupoptionen, die beim rsync Backup zusätzlich
zu den Standardoptionen von *raspiBackup* genutzt werden.

**Benutzung auf eigene Gefahr!**

| Config-Option              | Standard |
|----------------------------|----------|
| DEFAULT_RSYNC_BACKUP_ADDITIONAL_OPTIONS |          |

### DEFAULT_RSYNC_BACKUP_OPTIONS

Damit können die rsync Standard-Backupoptionen überschrieben werden.

**Benutzung auf eigene Gefahr!**

| Config-Option              | Standard |
|----------------------------|----------|
| DEFAULT_RSYNC_BACKUP_OPTIONS | --delete -aHAx |

### DEFAULT_TAR_BACKUP_OPTIONS

Damit können die tar Standard-Backupoptionen überschrieben werden.

**Benutzung auf eigene Gefahr!**

| Config-Option              | Standard |
|----------------------------|----------|
| DEFAULT_TAR_BACKUP_OPTIONS | -cpi     |


### DEFAULT_TAR_BACKUP_ADDITIONAL_OPTIONS

Backupoptionen, die beim tar Backup zusätzlich
zu den Standardoptionen genutzt werden.

**Benutzung auf eigene Gefahr!**

| Config-Option              | Standard |
|----------------------------|----------|
| DEFAULT_TAR_BACKUP_ADDITIONAL_OPTIONS |          |

</div>

[.status]: rst
