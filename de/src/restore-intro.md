# Restore Einführung

*raspiBackup* stellt **komplette** Wiederherstellungen zur Verfügung, d.h. alle Partitionen
werden i.d.R. wiederhergestellt.
Im Gegensatz dazu können beim partitionsorientierten Modus die zu restorenden Partitionen ausgewählt
und somit nur Teile restored werden.

Bei einem Restore werden auf dem Ziel-Datenträger (SD-Karte, USB-Platte, ...)
neue Partitionen angelegt und dann mit dem entsprechenden Tool (`dd`, `tar` oder `rsync`)
die Daten dorthin restored.

Der Ziel-Datenträger darf also aktuell nicht vom Betriebssystem selbst benutzt werden.
Es muss eine weitere, mit einem Kartenleser angeschlossene Karte, USB-Platte, SSD oder NVMe Gerät sein.

Ein Restore benötigt ein **Linuxsystem**. Dazu sollte man i.d.R. eine Raspberry nehmen. Andere Linuxsysteme
funktionieren auch, es ist aber nicht 100% garantiert, dass es damit immer funktioniert.

Sollte ein externes Rootfilesystem gesichert worden sein, wird es auch wieder
auf ein externes Gerät zurückgespielt
(Nur bei normalem Backupmodus mit `tar` oder `rsync` Backup).

Ein [manueller Restore](manual-restore.md)  der Daten mit den zuvor benutzten Backuptools `dd`, `tar` oder `rsync`
ist natürlich auch möglich. Ebenso ist (manuell) auch die Wiederherstellung einzelner Dateien
möglich, insbesondere beim `rsync` Backup sehr einfach.

Das Backupscript kann auch genutzt werden, um Systeme zu kopieren:
Es wird ein Backup erstellt und dann auf einem anderen Gerät restored.
Typische Anwendung ist, eine SD Karte auf eine SSD oder NVMe zu kopieren
und danach das System mit der SSD/NVMe und nicht mehr mit einer SD Karte zu betreiben.

------------------

Weitere Themen auf dieser Seite:

<!-- toc -->

------------------

[.status]: review-comment "Für Einsteiger teilweise noch unklar beschrieben."


## Wiederherstellungsszenario mit einer Raspberry mit RaspbianOS

Jedes Backup kann mit der/einer Raspberry Pi wiederhergestellt werden.

1. Ein *Raspberry Pi OS* auf der Raspberry starten

1. *raspiBackup* installieren

1. Das System, das wiederhergestellt werden soll, anschließen.

1. Das Medium, welches das Backup enthält (z.B. eine Platte), anschließen
   und mounten bzw. ein Netzwerklaufwerk mit den Backupdaten mounten.

1. Falls die Rootpartition ausgelagert wurde, ein weiteres Gerät mit
   einer vorformatierten Partition anschließen,
   die die ausgelagerte Rootpartition enthalten soll,
   welche wiederhergestellt werden wird

1. *raspiBackup* zum Restore starten, Aufruf siehe [unten](#devicenames).

Dabei wird üblicherweise genutzt:

  - das Systemgerät `/dev/sda`
  - die Backuppartition `/dev/sdbx`
  - und eine eventuelle Rootpartition `/dev/sdcx`


Wird ein Netzlaufwerk benutzt, ist die Rootpartition üblicherweise `/dev/sdbx`.

Die aktuelle Gerätebelegung kann abweichen und sollte **immer** überprüft werden,
um zu vermeiden, dass andere Partitionen irrtümlicherweise überschrieben werden.

Z.B. mit

```
sudo parted -l
```


## Wiederherstellungsszenario für Windowsbenutzer auf einem Windowssystem

Nur ein `dd` Backup lässt sich (auch) direkt unter Windows,
mit dem [Win32DiskImager](http://sourceforge.net/projects/win32diskimager/), restoren.

## Wiederherstellungsszenario für Linuxnutzer

``` admonish note title="Hinweis"
Im Prinzip kann zwar jedes Linux OS genutzt werden, um ein Backup zu restoren.
Aber bei möglichen Inkompatibiliäten dessen Tools, im Vergleich zu den beim Backup
verwendeten Linux-Tools, kann es Probleme geben.
Ein gelegentlich auftauchender Kandidat dafür ist `sfdisk`,
das sich sowohl zu *Jessie* als auch zu *Bullseye* inkompatibel geändert hatte.

Deshalb:

**Ein Restore sollte immer mit demselben OS vorgenommen werden, mit dem auch
das Backup erstellt wurde**.
```

Es wird das Gerät, auf welches das Backup restored werden soll,
an das Linuxsystem angeschlossen, die Backuppartition gemounted
und eine Partition für ein eventuelles externes Rootfilesystem bereitgestellt.

Dann *raspiBackup* zum Restore starten, Aufruf siehe [unten](#devicenames).

Wenn kein RaspbianOS und/oder keine Raspberry Pi genutzt werden,
muss noch die Option [--unsupportedEnvironment](general-options.md#--unsupportedenvironment) angegeben werden.

Siehe auch [Unterstützte Hard- und Software](supported-hardware-and-software.md).


## Beispielaufrufe

Notwendige Hardware für den Restore:

1. Eine laufende Raspberry Pi mit einem laufenden *Raspberry Pi OS* oder einem anderen
   Linux Betriebssystem oder ein anderer Linux Rechner mit installiertem *raspiBackup*.

1. Ein angeschlossenes Zielgerät des Backups

1. Ein angeschlossenes Backupdevice (per USB oder Netz)

1. Falls eine externe Rootpartition wiederherzustellen ist oder der USB Boot
   Mode benutzt wird, wo keine SD Karte mehr benutzt wird, muss noch per USB eine
   weitere Platte angeschlossen sein

Gemeinsamkeiten der Beispielaufrufe:

1. Das gesicherte System heißt im Beispielaufruf "raspberrypi".
1. Der **Ziel**-Datenträger, der den Restore der Boot-/bzw.
   Boot- und Root-Partition erhalten soll, ist im Beispiel als `/dev/sdf` verfügbar.  
   [Weiter unten](#devicenames) ist beschrieben, wie man den aktuellen Wert für `-d` herausfinden kann
1. **Achtung**: Alle bestehenden Daten der **Ziel**-Datenträger werden nach einer Sicherheitsabfrage
   von *raspiBackup* vor dem Restore gelöscht.
1. Das zu restorende Backup ist verfügbar unter
   `/remote/raspifix/disks/backup/rsync/raspberrypi/raspberrypi-rsync-backup-20141230-213032/`


### Restore auf eine SD Karte

```
sudo raspiBackup.sh -d /dev/sdf /remote/raspifix/disks/backup/rsync/raspberrypi/raspberrypi-rsync-backup-20141230-213032/
```

### Restore auf ein USB Gerät ohne SD Karte (USB boot mode)

```
sudo raspiBackup.sh -d /dev/sdf /remote/raspifix/disks/backup/rsync/raspberrypi/raspberrypi-rsync-backup-20141230-213032/
```

### Restore auf eine SD Karte und eine externe Partition

1. Um den Restore der externe Rootpartition aufzunehmen, wurde auf `/dev/sda`
   eine entsprechend große Partition `/dev/sda1` angelegt. Eine Formatierung ist nicht notwendig.

```
sudo raspiBackup.sh -d /dev/sdf -R /dev/sda1 /remote/raspifix/disks/backup/rsync/raspberrypi/raspberrypi-rsync-backup-20141230-213032/
```

<a name="devicenames"></a>
## Wie kann man die Gerätenamen der externen SD Karte und externen Platte herausfinden?

Auf der Raspberry ist folgender Befehl einzugeben:

```
fdisk -l | egrep "^Disk /|^/dev"
```

Die Ausgabe sieht dann z.B. wie folgt aus:

```
pi@raspberrypi:~# sudo fdisk -l | egrep "^Disk /|^/dev"
Disk /dev/mmcblk0: 8011 MB, 8011120640 bytes
/dev/mmcblk0p1            8192      122879       57344    c  W95 FAT32 (LBA)
/dev/mmcblk0p2          122880    15646719     7761920   83  Linux
Disk /dev/sda: 15.5 GB, 15548284928 bytes
Disk /dev/sdb: 300.1 GB, 300069052416 bytes
/dev/sdb1               1   586072367   293036183+  ee  GPT
```

Hier sieht man, dass

  - die interne SD Karte `/dev/mmcblk0` 8GB groß ist
  - die neue externe SD Karte `/dev/sda` 16GB groß ist
  - die externe Platte `/dev/sdb`, auf die die Rootpartition gebracht werden soll,
    300GB groß ist und eine Partition `/dev/sdb1` hat.

Somit ist der Parameter für  `-d` `/dev/sda` (Externe SD Karte).

Falls eine externe Rootpartition mitgesichert wurde, ist noch `-R /dev/sdb1` (Externe
Rootpartition) notwendig.

Die Parameter müssen natürlich den lokalen Gegebenheiten angepasst werden.


**Hinweis**:

Ein Backup sollte regelmäßig getestet werden: Ob der Restore immer noch
funktioniert und auch immer noch alle Daten beinhaltet.

Nichts ist so frustrierend, wenn man in dem Moment, wo man das Backup benötigt,
feststellt, dass das Backup korrupt ist oder nicht alle Daten enthält...

Ein Test ist bei der Raspberry recht einfach:

Eine neue SD-Karte einlegen, das Backup restoren und von der neuen SD-Karte booten.
Wird keine SD Karte genutzt, also z.B. eine SSD, kann der Restoretest
auch mit einer Platte vorgenommen werden,
sofern sie groß genug ist, alle Daten der SSD aufzunehmen.

Falls aus irgendwelchen Gründen der Restore mit dem Script fehlschlägt, kann man
natürlich jederzeit die vom Script gesicherten Daten mit den Standard
Linuxtools, die zum Backup genutzt wurden - `dd`, `tar` oder `rsync` - manuell
restoren. Allerdings geht das dann nicht ganz so bequem wie mit dem Script
und es sind entsprechende Linux Kenntnisse erforderlich ;-)
Siehe dazu auch [Manueller Restore eines Backups](manual-restore.md).

[.status]: rst
[.source]: https://linux-tips-and-tricks.de/de/raspibackup#restore
[.source]: https://linux-tips-and-tricks.de/de/wiederherstellen
