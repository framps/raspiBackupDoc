# Backup Optionen

Diese Liste enthält alle Aufrufoptionen von *raspiBackup* sowie
die entsprechenden Konfigurationsoptionen.

<div class="table-wrapper-for-options">

------------------

<!-- toc -->

------------------

<a name="parm_a"></a>
### -a: Befehle, die Services nach dem Backup starten

Befehle, um Services nach dem Backup wieder zu starten. Z.B. bei SMB "service
smbd start" (**Achtung:** Anführungszeichen an Anfang und Ende). Diese Option ist
zusammen mit der Option -o obligatorisch.

Mehrere Befehle müssen durch && getrennt werden. Diese Befehle sollten die
exakte umgekehrte Reihenfolge haben wie die Befehle beim Parameter -o.

**Beispiel**:

```
-a "service nfs-kernel-server start && service smbd start"
```

Soll wirklich **kein** Service gestartet werden, muss ein Doppelpunkt ":" als Argument mitgegeben werden.

Siehe dazu auch [FAQ1](faq.md#faq1) und [FAQ18](faq.md#faq18)

**Achtung**:
Die Befehle werden als root ausgeführt. Es ist kein sudo notwendig.

| Optionsname | Standard | Im Installer | Konfigurationsname |
|-------------|----------|--------------|--------------------|
| -a | keine | konfigurierbar | DEFAULT_STARTSERVICES |

<a name="parm_b"></a>
### -b: Definition der Blocksize, die beim dd Backup genutzt wird

Blocksize, die beim dd Backup benutzt wird

| Optionsname | Standard | Im Installer | Konfigurationsname |
|-------------|----------|--------------|--------------------|
| -b | 1 MB |  | DEFAULT_DD_BLOCKSIZE |

<a name="parm_B"></a>
### -B: Bootpartition wird als tar gesichert statt per dd

Die Bootpartition wird nicht per dd sondern per tar gesichert.

**Hinweis:**
Diese Option hat keine Funktion, wenn der partitionsorientierte Modus
benutzt wird.

| Optionsname | Standard | Im Installer | Konfigurationsname |
|-------------|----------|--------------|--------------------|
| -B | aus |  | DEFAULT_TAR_BOOT_PARTITION_ENABLED |

<a name="parm_c"></a>
### -c: Erlaube lokale Backupspeicherung

Es kann kein Backup auf der Rootpartition erstellt werden, um vor
unbeabsichtigtem Vollschreiben der Rootpartition durch das Backup zu schützen.
Auch macht es keinen Sinn, ein Backup auf der Systempartition abzulegen.

Mit dieser Option wird der Test ausgeschaltet und es kann ein Backup auf der
Rootpartition erstellt werden.

**ACHTUNG**:
Es wird nicht geprüft, ob das Backup noch auf die Rootpartition passt.

| Optionsname | Standard | Im Installer | Konfigurationsname |
|-------------|----------|--------------|--------------------|
| -c | aus |  | DEFAULT_SKIPLOCALCHECK |

<a name="parm_D"></a>
### -D: Weitere Optionen für den dd Backup

Weitere Aufrufoptionen für das dd Backup (z.B. "conv=notrunc,noerror,sync")

| Optionsname | Standard | Im Installer | Konfigurationsname |
|-------------|----------|--------------|--------------------|
| -D | automatisch |  | DEFAULT_DD_PARMS |

<a name="parm_dynamicMount"></a>
### --dynamicMount: Dynamisches Mounten der Backuppartition

Damit wird vor dem Backup die angegebene Partition bzw. der
Mointpoint gemounted und am Ende wieder umounted. Falls sie schon gemounted war,
wird sie am Ende die Partition nicht umounted. Der Mountpoint muss in /etc/fstab
definiert sein und kann dann entweder der Mountpoint selbst sein (z.B. /backup)
oder die Backuppartition (z.B. /dev/sdb1).

| Optionsname | Standard | Im Installer | Konfigurationsname |
|-------------|----------|--------------|--------------------|
| --dynamicMount | aus |  | DEFAULT_DYNAMIC_MOUNT |

<a name="parm_F"></a>
### -F: Simuliert den Backuplauf und hilft, die eMail Benachrichtgung schnell zu testen

"Fake backup". Diese Option ist hilfreich beim initialen Testen von *raspiBackup*.
Der eigentliche lange Backup wird dadurch nicht angestoßen - aber sämtliche
Optionsprüfungen wie auch das Senden der Benachrichtigungs-eMail und Pushnachrichten.

| Optionsname | Standard | Im Installer | Konfigurationsname |
|-------------|----------|--------------|--------------------|
| -F | None |  | None |

<a name="parm_ignoreAdditionalPartitions"></a>
### --ignoreAdditionalPartitions: Es werden mehr als zwei Partitionen toleriert, wobei aber nur die ersten beiden Partitionen gesichert werden.

Mit dieser Option sind Systeme mit mehr als zwei Partitionen unterstützt;
im normalen Backupmodus, wenn tar oder rsync Backup genutzt wird. Allerdings
werden nur die ersten beiden Partitionen, /boot und / gesichert und wiederhergestellt.

| Optionsname | Standard | Im Installer | Konfigurationsname |
|-------------|----------|--------------|--------------------|
| --ignoreAdditionalPartitions | nein |  | DEFAULT_IGNORE_ADDITIONAL_PARTITIONS |

<a name="parm_ignoreMissingPartitions"></a>
### --ignoreMissingPartitions: Test, ob alle Partitionen gesichert werden

Es wird im partitionsorientierten Backupmodus geprüft, ob alle Partitionen,
die im letzten Backup gesichert wurden, auch wieder gesichert werden.
Mit dieser Option wird der Test ausgeschaltet.

| Optionsname | Standard | Im Installer | Konfigurationsname |
|-------------|----------|--------------|--------------------|
| --ignoreMissingPartitions | nein |  | DEFAULT_IGNORE_MISSING_PARTITIONS |

<a name="parm_k"></a>
### -k: Anzahl der Backups die vorgehalten werden sollen

Anzahl der Backups, die pro Backuptyp vorzuhalten sind, sofern es nicht durch
die keep Option der jeweiligen Backuptypen überschrieben wird.
D.h., es werden standardmäßig 3 dd, 3 tar und 3 rsync Backups vorgehalten.

**Hinweis:**
 Diese Option ist wirkungslos, wenn die intelligente Rotationsstrategie benutzt wird.

| Optionsname | Standard | Im Installer | Konfigurationsname |
|-------------|----------|--------------|--------------------|
| -k | 3 | konfigurierbar | DEFAULT_KEEPBACKUPS |

<a name="parm_keepType"></a>
### --keep_{type}: Anzahl der Backups pro Typ, die vorgehalten werden sollen

Anzahl der Backups, die für den jeweiligen Backuptypen vorgehalten werden.

{type} kann jeder Backuptyp sein, also dd, ddz, tar, tgz oder rsync.

**Hinweis:**
Diese Optionen sind wirkungslos, wenn die intelligente Rotationsstrategie benutzt wird.

| Optionsname | Standard | Im Installer | Konfigurationsname |
|-------------|----------|--------------|--------------------|
| --keep_dd    | Parameter für Option -k | konfigurierbar | DEFAULT_KEEPBACKUPS_DD |
| --keep_ddz   | Parameter für Option -k | konfigurierbar | DEFAULT_KEEPBACKUPS_DDZ |
| --keep_rsync | Parameter für Option -k | konfigurierbar | DEFAULT_KEEPBACKUPS_RSYNC |
| --keep_tar   | Parameter für Option -k | konfigurierbar | DEFAULT_KEEPBACKUPS_TAR |
| --keep_tgz   | Parameter für Option -k | konfigurierbar | DEFAULT_KEEPBACKUPS_TGZ |

<a name="parm_M"></a>
### -M: Erstellen eines *raspiBackup* Snapshots

Mit der Option wird ein *raspiBackup* Snapshot erstellt, welcher nicht im
Backup-Recycleprozess berücksichtigt und somit nicht automatisch gelöscht wird.
Der Snapshot erhält am Ende des Verzeichnisnamens den angegebenen Text. Siehe auch
[diese Seite zu Snapshots](snapshots.md).

Beispiel: Der Hostname ist "idefix" und der Parameter für -M ist "Initial boot
from SD". Dann wird folgendes Verzeichnis angelegt:

```
idefix/idefix-rsync-backup-20170103-170717_idefix-Initial_boot_from_SD
```

**Hinweis**:
*raspiBackup* Snapshots sind normale Backups und keine "richtigen"
Snapshots wie die bei LVM oder BTRFS. Es werden aber beim rsync Backup Hardlinks
genutzt, um die Snapshotzeit zu reduzieren.

**Hinweis**:
Da die Snapshotverzeichnisse nicht im Backup-Recycleprozess berücksichtigt werden,
müssen sie manuell gelöscht werden.

| Optionsname | Standard | Im Installer | Konfigurationsname |
|-------------|----------|--------------|--------------------|
| -M | keiner |  |  |

<a name="parm_N"></a>
### -N: Erweiterungen, die vor und nach dem Backup aufgerufen werden sollen

Aktivierung von eigenen Scripterweiterungen (Plugins). Siehe dazu [diese Seite](hooks-for-own-scripts.md),
die auch zwei Beispielerweiterungen anbietet, die die CPU Temperatur und die
Speicherbelegung vor und nach dem Backuplauf ausgeben.

| Optionsname | Standard | Im Installer | Konfigurationsname |
|-------------|----------|--------------|--------------------|
| -N | keine |  | DEFAULT_EXTENSIONS |

<a name="parm_notifyStart"></a>
### --notifyStart: Benachrichtigung beim Backupstart

Mit dieser Option wird eingeschalten, dass eine
eMail oder eine Push-Benachrichtigung gesendet wird, wenn der Backup startet.
Normalerweise wird nur am Ende des Backups eine Benachrichtigung geschickt.

| Optionsname | Standard | Im Installer | Konfigurationsname |
|-------------|----------|--------------|--------------------|
| --notifyStart | nein |  | DEFAULT_NOTIFY_START |

<a name="parm_o"></a>
### -o: Befehle, die Services vor dem Backup stoppen

Befehle, um Services vor dem Backup zu stoppen, damit kein inkonsistentes Backup
erzeugt wird. Z.B. bei SMB "service smbd stop" (Achtung: Anführungszeichen an
Anfang und Ende). Diese Option ist zusammen mit der Option -a obligatorisch.

Mehrere Befehle müssen durch `&&` getrennt werden. Diese Befehle sollten die
exakte umgekehrte Reihenfolge haben wie die Befehle beim Parameter -a.

Beispiel:

```
-o "service smbd stop && service nfs-kernel-server stop"
```

Soll wirklich **kein** Service gestoppt werden, muss der Doppelpunkt ":" als Argument mitgegeben werden.

Siehe dazu auch [FAQ1](faq.md#faq1) und [FAQ18](faq.md#faq18)

**Achtung**:
Die Befehle werden als root ausgeführt. Es ist kein sudo notwendig.

| Optionsname | Standard | Im Installer | Konfigurationsname |
|-------------|----------|--------------|--------------------|
| -o | keine | konfigurierbar | DEFAULT_STOPSERVICES |

<a name="parm_p"></a>
### -p: Backupverzeichnis

Angabe des Backupverzeichnisses, in welchem das erstellte
Backup gespeichert werden soll.

| Optionsname | Standard | Im Installer | Konfigurationsname |
|-------------|----------|--------------|--------------------|
| --p | aus | konfigurierbar | DEFAULT_BACKUPPATH |

<a name="parm_rebootSystem"></a>
### --rebootSystem: Reboot des Systems nach dem Backup

Durch diese Option wird ein Reboot des Systems am Ende des
Backuplaufes vorgenommen und somit werden alle Services wieder gestartet.
Deshalb werden Argumente der Option -a auch ignoriert.

**Hinweis**: Wird die Option -F benutzt, wird kein reboot durchgeführt.

| Optionsname | Standard | Im Installer | Konfigurationsname |
|-------------|----------|--------------|--------------------|
| --rebootSystem | aus |  | DEFAULT_REBOOT_SYSTEM |

<a name="parm_smartRecycle"></a>
### --smartRecycle: Nutzung von SmartRecycle

Diese Option schaltet die [intelligente Rotationsstrategie - Smart Recycle](smart-recycle.md) ein.
Damit werden die --keep Optionen ignoriert und müssen nicht auf 0 gesetzt werden.

| Optionsname | Standard | Im Installer | Konfigurationsname |
|-------------|----------|--------------|--------------------|
| --smartRecycle | aus | konfigurierbar | DEFAULT_SMART_RECYCLE |

<a name="parm_smartRecycleDryrun"></a>
### --smartRecycleDryrun: Testmodus von SmartRecycle

Diese Option schaltet den Testmodus der [intelligenten
Rotationsstrategie - Smart Recycle](smart-recycle.md) ein.


| Optionsname | Standard | Im Installer | Konfigurationsname |
|-------------|----------|--------------|--------------------|
| --smartRecycleDryrun | ja |  | DEFAULT_SMART_RECYCLE_DRYRUN |


<a name="parm_smartRecycleOptions"></a>
### --smartRecycleOptions: Smartrecycle-Optionen

Diese Option definiert Parameter der [intelligenten Rotationsstrategie - Smart Recycle](smart-recycle.md).

| Optionsname | Standard | Im Installer | Konfigurationsname |
|-------------|----------|--------------|--------------------|
| --smartRecycleOptions | "7 4 12 1" | konfigurierbar | DEFAULT_SMART_RECYCLE_OPTIONS |

<a name="parm_systemstatus"></a>
### --systemstatus: Aktive Services beim Backupstart anzeigen

Es wird eine Liste der aktiven Services und offenen Dateien
in der Debugdatei erstellt.

| Optionsname | Standard | Im Installer | Konfigurationsname |
|-------------|----------|--------------|--------------------|
| --systemstatus | aus |  |  |

<a name="parm_unsupportedEnvironment"></a>
### --unsupportedEnvironment: Nutzung auf nicht unterstützter HW und OS

Wird *raspiBackup* auf nicht [unterstützten Umgebungen](supported-hardware-and-software.md)
gestartet, muss diese Option angegeben werden.

| Optionsname | Standard | Im Installer | Konfigurationsname |
|-------------|----------|--------------|--------------------|
| --unsupportedEnvironment | aus |  |  |

<a name="parm_P"></a>
### -P: Partitionsorientierter Backupmodus

Partitionsorientierter Modus. Damit wird im Gegensatz zum normalen Modus, wo nur
die ersten beiden Partitionen gesichert werden, eine beliebige Anzahl von
Partitionen gesichert. Mit der Option -T wird definiert, welche Partitionen zu
sichern sind.

| Optionsname | Standard | Im Installer | Konfigurationsname |
|-------------|----------|--------------|--------------------|
| -P | aus | konfigurierbar | DEFAULT_PARTITIONBASED_BACKUP |


<a name="parm_T"></a>
### -T: Angabe der Partitionen, die beim partitionsorientierten Backup gesichert werden sollen

Falls der partitionsorientierte Backupmodus mit der Option -P gewählt wurde,
kann mit dieser Option definiert werden, welche Partitionen gesichert werden
sollen. Beispiel: -T "1 2 5" sichert die ersten beiden und die fünfte
Partition. Mit * werden alle Partitionen gesichert.

| Optionsname | Standard | Im Installer | Konfigurationsname |
|-------------|----------|--------------|--------------------|
| -T | "1 2" |          | DEFAULT_PARTITIONS_TO_BACKUP |

<a name="parm_t"></a>
### -t: Typ des Backups (dd, tar, rsync)

Typ des Backups, der entweder dd, tar oder rsync sein kann. rsync benutzt bei
einer ext3/ext4 Partition Hardlinks, um den benötigten Speicherplatz zu
minimieren.

[Detailinformationen zu den Backuptypen](backup-types.md) Ein externes Rootfilesystem wird
automatisch bei `tar` oder `rsync` Backup mitgesichert, sofern nicht die Option `-P`
benutzt wird. Mit der Option `-z` werden die `dd` und `tar` Backups zusätzlich noch gezippt bzw.
verkleinert.

**Hinweis**:
Beim dd Backup kann durch den Konfigurationsparameter
DEFAULT_DD_BACKUP_SAVE_USED_PARTITIONS_ONLY Backupzeit und -platz gespart werden.

Siehe dazu auch [FAQ16](faq.md#faq16).

| Optionsname | Standard | Im Installer | Konfigurationsname |
|-------------|----------|--------------|--------------------|
| -t | rsync | konfigurierbar | DEFAULT_BACKUPTYPE |


<a name="parm_u"></a>
### -u: Weitere Verzeichnisse aus dem Backuprozess auszuschließen

Erweiterung der Excludeliste beim Backup, um bestimmte Verzeichnisse beim Backup
zu ignorieren.

**Achtung**:
Die Parameter müssen der jeweiligen Syntax des Backuptools
gehorchen und führen sonst zum Abbruch des Backups. Für rsync oder tar könnte
die Liste wie folgt aussehen:

```
"--exclude=/backup/* --exclude=/rsnapshot/* --exclude=/www-data*/* --exclude=/home/pi/.local/share/Trash"
```

Die Anführungszeichen sind wichtig! Weitere Informationen zu der Syntax finden
sich auf der man Page der jeweiligen Backuptools.

Folgende Verzeichnisse werden niemals gesichert:

- Der Backupfad, der im Aufruf angegeben wurde
- /proc/*
- /lost+found/*
- /sys/*
- /dev/*
- /tmp/*
- /boot/*
- /run/*
- /proc/*
- /lost+found/*
- /sys/*
- /dev/*
- /tmp/*
- /boot/*
- /run/*

Außerdem werden alle gemounteten Verzeichnisse von externen Geräten, die nicht
auf / gemounted sind, nicht gesichert. Es wird nur die Boot Partition
/dev/mmcblk0p1 und die Root Partition /dev/mmcblk0p2 bzw. das ausgelagerte
Rootverzeichnis auf z.B. /dev/sda1 gesichert.

**Hinweis für den partitionsorientierten Modus**:
Wenn die Option -P benutzt wird, werden in allen Partitionsbackups die o.g. Verzeichnisse ausgenommen.

**rsync**:

- */verzeichnis/* - Excluded Verzeichnis auf allen Partitionen
- mmcblk0p2/verzeichnis/* - Excluded Verzeichnis auf Partition mmcblk0p2

**tar**:

- verzeichnis/* - Excluded Verzeichnis auf allen Partitionen

| Optionsname | Standard | Im Installer | Konfigurationsname |
|-------------|----------|--------------|--------------------|
| -u | keine |  | DEFAULT_EXCLUDE_LIST |

<a name="parm_v"></a>
### -v: Alle Meldungen des verwendeten Backuptools werden protokolliert

Die verwendeten Backuptools tar und rsync zeigen detaillierte Informationen an
(Verbose mode). Die Option ist besonders nützliche bei initialen manuellen
Backuptests, um den Backupfortschritt verfolgen zu können.

| Optionsname | Standard | Im Installer | Konfigurationsname |
|-------------|----------|--------------|--------------------|
| -v | aus |  | DEFAULT_VERBOSE |

<a name="parm_z"></a>
### -z: Kompression des Backups bei dd oder tar

Backup verkleinern mit gzip bei dd oder tar Backup

| Optionsname | Standard | Im Installer | Konfigurationsname |
|-------------|----------|--------------|--------------------|
| -z | aus | konfigurierbar | DEFAULT_ZIP_BACKUP |


</div>

[.status]: rst
