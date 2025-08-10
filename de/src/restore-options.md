# Restore Optionen

*raspiBackup* restored standardmäßig beim normalen Backupmodus das [**gesamte System**](restore-intro.md).
Beim partitionsorientierten Modus kann dagegen beim Restore ausgewählt werden,
welche Partitionen restored werden sollen. Wird beim partitionsorientierten Modus
der `rsync` Backuptyp genutzt, kann bei einem Restore auch ein Deltarestore gewählt werden (Option -00).
Das heißt, es werden mit `rsync` nur die geänderten Dateien und gelöschte Dateien aus dem Backup
kopiert sowie nicht im Backup vorhandene Dateien - also neu erstellte Dateien - gelöscht.
Damit ist ein sehr schneller Restore möglich.

Unabhängig von *raspiBackup* ist auch ein [manueller Restore](manual-restore.md)
der Daten mit den zuvor benutzten Backuptools `dd`, `tar` oder `rsync` möglich.
Dazu sind dann entsprechende Kenntnisse der Linux Backuptools notwendig.

Ebenso ist manuell auch die [Wiederherstellung einzelner Dateien/Verzeichnisse](how-to-retrieve-single-files-or-directories-from-the-backup.md) möglich.

------------------

<!-- toc -->

------------------

<div class="table-wrapper-for-options">

<a name="parm_C"></a>
### -C: Auf Badblocks prüfen

Beim Formatieren wird mittels `mkfs.ext4 -c` auf Bad Blocks geprüft.
Hinweis: Die Restorezeit wird dadurch erhöht.

| Option | Standard | Im Installer | Konfigurationsname |
|--------|----------|--------------|--------------------|
| -c     |   aus    |              | DEFAULT_CHECK_FOR_BAD_BLOCKS |

<a name="parm_d"></a>
### -d: Restoredevice

Device, auf dem der Backup restored wird.

| Option | Standard | Im Installer | Konfigurationsname |
|--------|----------|--------------|--------------------|
| -d     |          |              | DEFAULT_RESTORE_DEVICE |

Beispiel: `-/dev/sda`

**Hinweis:** Der Parameter muss ein Device sein und keine Partition. Es darf keine
Partitionsnummer wie z.B. bei `/dev/sda1` vorhanden sein.

**Achtung:** Dieses Device wird i.d.R. vollständig gelöscht und neu angelegt! Beim `tar` und
`rsync` Backup wird automatisch die Größe der *root* Partition entsprechend
verkleinert oder vergrößert, wenn das Zielgerät eine andere Größe
hat als das gesicherte System. Dabei muss natürlich auf dem Zielgerät noch genügend Platz für die
Daten des Quellsystems vorhanden sein. Ist nicht genügend Platz, wird der Restore abbrechen.

<a name="parm_N"></a>
### -N: Erweiterungen, die vor und nach dem Restore aufgerufen werden sollen

Aktivierung von eigenen Scripterweiterungen (Plugins). Siehe dazu [diese Seite](hooks-for-own-scripts.md),
die auch zwei Beispielerweiterungen anbietet, die die CPU Temperatur und die
Speicherbelegung vor und nach dem Backuplauf ausgeben.

| Optionsname | Standard | Im Installer | Konfigurationsname |
|-------------|----------|--------------|--------------------|
| -N | keine |  | DEFAULT_EXTENSIONS |


<a name="parm_R"></a>
### -R: Externe Rootpartition

Durch diese Option kann man Backups von Systemen restoren, die eine externe
Partition als Rootpartition benutzen, wie USB Sticks oder Festplatten.
Dieses ist nur möglich, wenn ein `tar` oder `rsync` Backup vorliegt.
Der Parameter definiert die Partition, auf welchem das root Verzeichnis restored
werden soll.  Beispiel: `/dev/sdb1`.

| Option | Standard | Im Installer | Konfigurationsname |
|--------|----------|--------------|--------------------|
| -R     |          |              |                    |

**Hinweis:** Diese Option nur benutzen, wenn sowohl eine SD Karte als auch ein
externes Rootfilesystem auf einem Gerät benutzt wird. Sonst reicht die Option `-d`.
Die Option ist nur sinnvoll bei älteren Raspberries, die noch keinen USB Boot unterstützen.

**Achtung:** Die Partition wird **neu formatiert**. Deshalb aufpassen, dass es die
richtige Partition ist und dass die Partition groß genug ist, um die Partition
des Backups aufzunehmen!

**Hinweis:** Diese Option steht nur zur Verfügung, wenn der normale Backupmodus
benutzt wurde. Im partitionsorientierten Modus (Option `-P`) kann keine externe
Rootpartition mitgesichert werden.

<a name="parm_resizeRootFS"></a>
### --resizeRootFS: Rootfilesystem anpassen

Während der Wiederherstellung kann die Rootpartition auf die maximal verfügbare
Größe des Zielgerätes der externen Partition ausgedehnt werden. Wird die
Option ausgeschaltet mit `--resizeRootFS-`, wird die Rootpartition so groß
angelegt, wie sie auf dem Originalsystem war. Nutzt man die Option -P, so wird die letzte
Partition auf dem Gerät erweitert. Liegen mehr als 2 Partitionen vor, ist es dann nicht die Rootpartition.

| Option | Standard | Im Installer | Konfigurationsname |
|--------|----------|--------------|--------------------|
| --resizeRootFS     |  ja    |              |                    |

<a name="parm_T"></a>
### -T: Zu restorende Partitionen

Beim partitionsorientierten `rsync` Backup können damit
gezielt Partitionen ausgewählt werden, die zu restoren sind. Mit `"*"` werden
alle Partitionen restored.

| Option | Standard | Im Installer | Konfigurationsname |
|--------|----------|--------------|--------------------|
| -T     |   "1,2"  |              | DEFAULT_PARTITIONS_TO_RESTORE |                   |

<a name="parm_updateUUIDs"></a>
### --updateUUIDs: Anpassen der UUIDs

Beim Restore werden immer die PARTUUIDs, UUIDs und LABELs
des Originals restored. Dieses erzeugt i.d.R. Probleme, wenn man das restorte
System am Originalsystem mounted. Mit dieser Option werden neue PARTUUIDs, UUIDs und LABEL beim
Restore generiert.

| Option | Standard | Im Installer | Konfigurationsname |
|--------|----------|--------------|--------------------|
| --updateUUIDs     |  ja    |              |                    |

<a name="parm_Y"></a>
### -Y: Automatisierter Restore

Standardmäßig wird vor dem Restore angezeigt, wie das Restoredevice gerade
aussieht und abgefragt, ob man das Device wirklich überschreiben will. Soll der
Restore automatisiert erfolgen, wird mit dieser Option die Abfrage unterdrückt.

**Achtung:** Dadurch kann man u.U. unbeabsichtigt das falsche Device überschreiben
und wichtige Daten löschen.

| Option | Standard | Im Installer | Konfigurationsname |
|--------|----------|--------------|--------------------|
| -Y     |  loop    |              |                    |

Zusätzlich muss noch die folgende Option in die Konfigurationsdatei aufgenommen
werden und die Devices, auf welches restored werden darf, eingetragen werden.
Der Eintrag kann ein regulärer Ausdruck sein.

**Use with care!**

DEFAULT_YES_NO_RESTORE_DEVICE="loop"

<a name="parm_0"></a>
### -0: Keine Partitionierung

Es wird kein neues Partitionslayout auf dem Zielgerät erstellt, sondern das
existierende benutzt. Somit kann man eine gewünschte Partitionierung vor dem Restore vornehmen
und dann ein Backup restoren. Details dazu siehe [FAQ #6](faq.md#faq6)

| Option | Standard | Im Installer | Konfigurationsname |
|--------|----------|--------------|--------------------|
| -0     |  aus    |              |                    |

<a name="parm_00"></a>
### -00: Keine Partitionierung und Formatierung

Hiermit wird keine Formatierung der mit der Option `-T`
ausgewählten Partitionen bei einem `rsync` partitionsorientierten Backup
vorgenommen. Dadurch wird der Restoreprozess extrem beschleunigt, da nur neue,
geänderte oder gelöschte Dateien gesynced werden.

| Option | Standard | Im Installer | Konfigurationsname |
|--------|----------|--------------|--------------------|
| -00     |  aus    |              |                    |

<a name="parm_1"></a>
### -1: Partitionierungsfehler ignorieren

Das Partitionslayout wird auf der SD Karte erstellt, so wie es auf dem Quellgerät
existiert und dabei werden sämtliche Fehler, die entdeckt werden - inklusive des
Fehlers, dass das Zielgerät zu klein ist - ignoriert.  Siehe [FAQ #6](faq.md#faq6) für
weitere Details.

| Option | Standard | Im Installer | Konfigurationsname |
|--------|----------|--------------|--------------------|
| -1     |  aus    |              |                    |

Hinweis: Diese Option kann unerwartete Ergebnisse haben.
Benutze die Option nur, wenn Du weißt, was Du tust.

</div>

[.status]: rst
