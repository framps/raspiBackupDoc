<center>     <!-- The blank line before the image definition is required! -->

![Icon](images/icons/Icon_rot_blau_final_64.png)
</center>


# Häufige Fragen (FAQ)

<!-- toc -->

---

<a name="faq0"></a>
### 0) Wie entstand *raspiBackup*?

Bei *framp* liefen zu Hause drei Raspis. Zwei davon 7/24 - also rund um die Uhr.
Ein jeder Server sollte regelmäßig gesichert werden denn es können immer mal
unvorhergesehene Umstände eintreten, die eine Wiederherstellung eines
vorherigen Standes erfordern. Speziell die SD-Karte der Raspberry neigt dazu,
immer mal wieder auszufallen. Um dafür gewappnet zu sein, wurde ein
kleines Script geschrieben, welches zuerst ein dd Backup, dann später, da
ein dd Backup ja immer die gesamte SD-Karte sichert obwohl nur Bruchteile
davon benutzt werden, ein tar Backup automatisch erstellte. Zum Schluss
wurde dann ein rsync Backup implementiert um durch die Hardlinks Backupzeit
und -space zu sparen. Nachdem imer mal wieder eine Wiederherstellung
notwendig war und alles gut klappte dachte *framp* dass das Script
auch anderen Raspberryfreunden hilfreich sein könnte und publizierte
*raspiBackup*. Siehe auch [10 Jahre *raspiBackup*](10-years-raspibackup.md)

<a name="faq1"></a>
### 1) Ist ein Backup eines laufenden Systems zuverlässig? Sollte nicht das gesamte System vor dem Backup gestoppt werden?

Die sicherste Methode ist natürlich das System vollständig zu stoppen.
Bei einem Backup wird nur gesichert was sich auf dem Speichermedium
und nicht was sich noch im Hauptspeicher befindet.

Ein Systemstopp ist leider nicht regelmäßig und automatisch
vornehmbar. Wenn man alle aktiven Services wie MySQL, SMB, NFS,
ownCloud, Webserver und alle anderen aktiven Services immer vor dem Backup
stoppt, um keine Dateninkonsistenzen zu erzeugen, kann das Backup zum
Wiederherstellen der Raspi genutzt werden. Stoppt man die Services nicht,
besteht eine hohe Wahrscheinlichkeit, dass das Backup inkonsistent wird.
Dazu gibt es die Parameter `-a` und `-o`, um die entsprechenden Stopp- und
Startbefehle vor bzw. nach dem Backup auszuführen. Siehe auch [FAQ18](#faq18) dazu.

Mit dem Installer können Systemd Services ausgewählt werden, die gestoppt
und nach dem Backup wieder gestartet werden sollen und die Parameter für
Option `-a` und Option `-o` werden entsprechend gesetzt.

<a name="faq2"></a>
### 2) Wie kann ich ein Backup wiederherstellen?

*raspiBackup* kann jedes Backup wieder zurück gespielt werden. (Siehe dazu
[hier](restore.md) die Details). Als Windowsbenutzer kann man
entsprechende Windowstools nutzen, um dd Backups wiederherzustellen. Für andere
Backuptypen wie tar oder rsync ist ein Linux notwendig.

Allerdings kann man dazu die Raspberry benutzen: Man bespielt eine neue SD
Karte mit RaspbianOS und kopiert darauf *raspiBackup*. Dann schließt man
das Gerät, auf welches das Backup zurückgespielt werden soll,
sowie das Medium mit dem Backup an die Raspberry an.
Danach ruft man *raspiBackup* auf und lässt ein gewünschtes Backup auf das
Gerät zurückschreiben. Anschließend fährt man das System runter,
legt das Gerät mit dem zurückgespielten Backup ein und startet die
Raspberry wieder.


<a name="faq3"></a>
### 3)   Was kann *raspiBackup* alles sichern und wiederherstellen?

Im normalen Modus sichert *raspiBackup* mit tar oder rsync zwei Partitionen:
Die Boot und die Rootpartition die auf dem System. Wenn
die Rootpartition auf ein externes Medium verlagert wurde wird auch die
externe Rootpartition gesichert. Mit dem dd Backup wird die gesamte SD-Karte
gesichert. Dann kann aber keine externe root Partition mitgesichert werden.

Im partitionsorientierten Modus werden beliebig viele Partitionen des
Systems gesichert. Weitere externe Partitionen werden aber nicht gesichert.

<a name="faq4"></a>
### 4)   Welche Linux Sicherungsmethoden stehen zur Verfügung?

Es steht der dd Backup sowie der tar und rsync Backup zur Verfügung. dd und
tar Backups können noch mit zip komprimiert werden. Auf
[dieser Seite](backup-types.md) können
die Vor- und Nachteile der jeweiligen Backupmethoden nachgelesen werden.


<a name="faq5"></a>
### 5)  Kann man die Sicherung auch ohne *raspiBackup* wiederherstellen?

Das ist eine Grundvoraussetzung für *raspiBackup* gewesen: Es muss möglich
sein, das Backup mit entsprechenden Linux-Kenntnissen zu Fuß restoren zu
können.

Die Sicherung legt Dateien an, die die lesbaren Ausgaben von den Linux
Befehlen sfdisk, blkid und fdisk von dem System enthält. Damit lässt sich
zuerst die Partitionsstruktur des Backups mit den entsprechenden Linuxtools
wiederherstellen. Danach kann man die Partitionsbackups mit den
entsprechenden Linuxtools wieder auf die Partitionen zurückspielen.


<a name="faq6"></a>
### 6)   Kann man die Sicherungen mit *raspiBackup* auch auf kleiner und größere SD-Karten wiederherstellen?

Beim dd Backuptyp muss man nach den Restore auf ein größeres Gerät mit
Linux Repartitionierungstools nach der Wiederherstellung die Partitionsgröße
anpassen, wenn man für die zweite Parition sämtlichen Platz nutzen will. Ein
dd Restore auf ein kleineres Gerät geht nicht.

Ohne Probleme funktioniert es bei einem kleineren oder größeren Gerät,
sofern tar oder rsync Backup. Beim normalen Backupmodus wird
automatisch die Größe der root Partition entsprechend angepasst, d.h.
entsprechend verkleinert oder vergrößert. Bei einer Vergrößerung wird
der gesamte zur Verfügung stehende Platz benutzt.
Wird von dem Backup des Systems mehr Platz benutzt
als das Restore Gerät hat gibt es natürlich Fehler beim Restore.
Beim partitionsorientierten Backupmodus wird die letzte Partition
entsprechend angepasst.

Mit der Option `-0` (Null) wird keine Partitionierung des neuen Gerätes
vorgenommen sondern die existierende Partitionierung des gesicherten
Systems genutzt.
Man hat damit vollständige Kontrolle über die Größe der Wiederhergestellten
Partitionen. D.h. man kann dadurch vor dem Restore genau festlegen, wie
groß die Partitionen auf der neuen SD-Karte sein sollen und somit auch auf
kleiner SD-Karten restoren. Das geht auch für partitionsorientierte Backups.

Ein dd Backup kann nicht auf eine kleiner Karte restored werden. Vorher muss
es verkleinert werden. Das geht z.B. so. Oder man benutzt [pishrink](https://github.com/Drewsif/PiShrink).

Einen partitionsorientierten Backup kann man auf kleinere Geräte restoren
indem man es mit ihren gewünschten Partitionen vorformatiert und dann mit der
Option -0 das Backup wiederherstellt.


<a name="faq7"></a>
### 7)   Wie kann ich die Partitionierung der Ziel SD-Karte beeinflussen?

Es gibt zwei Optionen die das Partitionierungsverhalten von *raspiBackup*
beeinflussen: Option `-1` (eins) zwingt *raspiBackup* die Partitionierung der
Backup SD-Karte auf die Ziel SD-Karte zu erstellen auch wenn die Partitionen
kleiner oder größer als die Ziel SD-Karte sind. Mit der Option `-0` (Null)
nimmt *raspiBackup* keine Partitionierung vor und verwendet die existierende
Partition der Ziel SD-Karte. Somit kann man vor dem Restore die Partitionen
anlegen und formatieren wie man sie haben möchte und diese wird dann von
*raspiBackup* benutzt.


<a name="faq8"></a>
### 8) Auf welchen Medien kann man mit *raspiBackup* die Backups ablegen?

Generell auf jedem Device, welches unter Linux gemounted werden kann

  - Externer USB Stick
  - Externe USB Platte
  - SMB Netzwerklaufwerk
  - NFS Netzwerklaufwerk
  - SSHFS Netzwerklaufwerk
  - WebDAV Netzwerklaufwerk
  - FtpFS Netzwerklaufwerk

<a name="faq9"></a>
### 9) Wie kann ich die Funktion von *raspiBackup* noch erweitern und zusätzlich etwas vor oder nach dem Backup und/oder Restore ausführen lassen?

Da gibt es verschiedene Möglichkeiten:

  - Ein [Wrapperscript](https://raw.githubusercontent.com/framps/raspiBackup/refs/heads/master/helper/raspiBackupWrapper.sh)
    wird benutzt und nimmt vor und nach dem
    Backuplauf weitere Aktionen vor wie z.B. weitere Dinge zu sichern.

  - Beliebige Erweiterungspunkte (Extensions) können vor und nach dem Backup
    und/oder restore von *raspiBackup* aufgerufen werden. Zwei
    Beispielerweiterungen (Siehe [hier](hooks-for-own-scripts.md)) melden zusätzlich die CPU Temperatur vor
    und nach dem Backuplauf sowie den belegten Hauptspeicher. Eine
    eMailExtension erlaubt es beliebige andere eMailClients anzusteuern.


<a name="faq10"></a>
### 10) Welche eMailClients werden von *raspiBackup* unterstützt?

*raspiBackup* unterstützt Exim4, Postfix und nullmailer, ssmtp, msmtp und
sendEmail. Andere eMailClients können über ein eMail Erweiterung (Extension)
angesprochen werden (Details siehe [hier](hooks-for-own-scripts.md)).


<a name="faq11"></a>
### 11) Mein eMailClient wird leider nicht von *raspiBackup* unterstützt. Wie kann ich trotzdem eMails erhalten?

*raspiBackup* kann eine eMailErweiterung (extension plugpoint) zum Senden der
eMail benutzen. Dazu muss ein kleines Script geschrieben werden, welches die
eMailParameter entsprechende dem verwendeten eMailClient aufbereitet und
den eMailClient mit der korrekten Syntax aufruft. Eine Beispielerweiterung
für mailx ist bei den [Erweiterungsbeispielen](hooks-for-own-scripts.md) enthalten.


<a name="faq12"></a>
### 12) Ich habe eine Frage zu oder ein Problem mit *raspiBackup*. Wie bekomme ich Hilfe?

Eines vorweg: Die Betonung liegt auf *raspiBackup* Fragen. Für Linuxfragen
oder -probleme siehe [FAQ38](#faq38) und [FAQ47](#faq47).

Es gibt verschiedene Optionen:

- In [*GitHub*](https://github.com/framps/raspiBackup) können Problemberichte (Issues) erstellt werden bei Fragen oder
  Problemen. Das ist meine präferierte Option. Dazu ist eine einmalige
  Registrierung notwendig. Diese sowie die Benutzung von *GitHub* ist kostenlos.

- Im Raspberry Forum gibt es ein [Unterforum zu Backups](https://forum-raspberrypi.de/forum/board/153-backup/), wo Fragen zu
  *raspiBackup* gestellt und Probleme berichtet werden können. *framp* wird über
  alle neuen Threads informiert und kann sich dem Thread widmen.

Siehe auch diese [Hinweise](introduction.md#kontakt)

**Hinweis:** Jegliche andere Kontaktwege werden ignoriert.


<a name="faq13"></a>
### 13) Ich habe einen Fehler in *raspiBackup* gefunden. Wo kann ich den Fehler melden und wann bekomme ich einen Fix dafür?

Wie in jeder Software kann es vorkommen, dass auch *raspiBackup* Fehler hat.
Die verschiedenen Kanäle über die Probleme berichtet werden können sind
in [FAQ12](#faq12) beschrieben.


<a name="faq14"></a>
### 14) Bekomme ich irgendwie automatisch mit dass es eine neue Version von *raspiBackup* gibt?

*raspiBackup* prüft bei jedem Aufruf ob es eine neuere Version gibt. Wenn ja
wird eine entsprechende Meldung ausgegeben und die Benachrichtigungsemail
weist im Titel mit einem Smiley ;-) darauf hin. Dann kann man auf [dieser
Seite](version-history.md) nachlesen, was die neue Version bringt und dann mit dem Parameter -U
einen Versionsupdate vornehmen lassen.


<a name="faq15"></a>
### 15) Wie kann ich auf eine vorhergehende *raspiBackup* Version zurückgehen, wenn ich nach einem Upgrade bemerke, dass die neue Version nicht so funktioniert wie ich es erwarte?

*raspiBackup* erstellt jedes mal wenn mit der Option -U eine neue Version
aktiviert wird eine Sicherungskopie. Mit der Option -V kann man jederzeit
auf eine vorhergehende Version zurückgehen. Es wird eine Liste von alle
gesicherten *raspiBackup* Versionen angezeigt und man kann die Version, die
zurückgespielt werden soll daraus auswählen.


<a name="faq16"></a>
### 16) Ich habe eine 32GB SD-Karte wovon ich nur 8GB benötige. Ein dd Backup sichert aber immer 32GB, d.h 24GB zu viel.

Der dd Backup sichert immer die ganze SD-Karte. Es gibt den
Konfigurationsparameter DEFAULT_DD_BACKUP_SAVE_USED_PARTITIONS_ONLY, der
dafür sorgt, dass nur die definierten Partitionen gesichert werden. D.h.
man muss mit gparted oder einem anderen Partitionierungstool nur eine
kleinere Partition von 8GB erstellen. Die aktuellen Partitionsgrößen kann
man mit dem Befehl lsblk kontrollieren.

Alternativ kann man per [raspiBackupWrapper Script](https://github.com/framps/raspiBackup/blob/master/helper/raspiBackupWrapper.sh) nach dem Backup mit
*raspiBackup* [pishrink](https://github.com/Drewsif/PiShrink) aufrufen lassen und das dd Image auf das mögliche
Minimum verkleinern.


<a name="faq17"></a>
### 17) Wie kann ich feststellen, dass der rsync Backup tatsächlich Hardlinks benutzt, um Speicherplatz zu sparen?

Hardlinks werden erfolgreich von *raspiBackup* benutzt wenn ein lokaler USB
Stick, eine lokale USB Platte oder auch eine per NFS gemountete Partition,
die mit ext3/ext4 formatiert ist, benutzt wird. SMB und SSHFS
unterstützen keine Hardlinks.

**Hinweis:** Der Windows Explorer ignoriert Hardlinks und zeigt deshalb eine
falsche effektive Belegung an. Es muss deshalb ein Linuxsystem genutzt
werden um die Belegung zu prüfen. Die Raspberry bietet sich dafür an.

Der Befehl `sudo du -sh *` zeigt den tatsächlich benutzen Speicherplatz an
und `sudo du -shl *` zeigt den Speicherplatz an, der belegt werden würde,
wenn keine Hardlinks benutzt werden würden (Das, was Windows
fälschlicherweise anzeigt) .

Beispiel:

```
root@raspberrypi:/media/nas-backup/raspberrypi# du -sh *
4,5G raspberrypi-rsync-backup-20160822-184617
4,5M raspberrypi-rsync-backup-20160822-190436
5,2M raspberrypi-rsync-backup-20160822-195250
5,7M raspberrypi-rsync-backup-20160822-201610

root@raspberrypi:/media/nas-backup/raspberrypi# du -shl *
4,7G raspberrypi-rsync-backup-20160822-184617
4,7G raspberrypi-rsync-backup-20160822-190436
4,7G raspberrypi-rsync-backup-20160822-195250
4,7G raspberrypi-rsync-backup-20160822-2016
```

Hinweis: [Wie funktionieren Hardlinks zusammen mit rsync?](how-do-hardlinks-work-with-rsync.md).
Und dazu noch ein [Youtube Video](https://www.youtube.com/watch?v=pIhSca_q2lo&t=4s).


<a name="faq18"></a>
### 18) Welche Services muss man vor dem Backup stoppen und anschliessend wieder starten?

Alle Services, die irgendwelche Systemzustände in Datenbanken oder im
Speicher oder auf dem Dateisystem speichern, sollten gestoppt werden, damit
nicht während des Backups inkonsistente Datenstände entstehen, die dann erst
beim wiederhergestellten System bemerkt werden und das Backup unbrauchbar
machen.

Systemd Services können mit dem Installer konfiguriert werden der in der
Konfigurationsdatei DEFAULT_STARTSERVCIES und DEFAULT_STOPSERVCIES
entsprechend setzt. Anwendungen die nicht als Systemservices laufen müssen
manuell mit den beiden Optionen in der Konfigdatei hinzugefügt werden.
Danach kann der Installer nicht mehr zur Konfiguration dieser beiden
Optionen genutzt werden.

Folgende Services sollten auf alle Fälle gestoppt werden:

| Service   | Stopp Befehl |
|-----------|-------------|
| NFS       | systemctl stop nfs-kernel-server |
| SMB/samba | systemctl stop samba |
| Pilight   | systemctl stop pilight |
| Cups      | systemctl stop cups |
| Minidlna  | systemctl stop minidlna |
| Apache    | systemctl stop apache2 |
| Wordpress | systemctl stop wordpress |
| nginx     | systemctl stop nginx |
| mysql     | systemctl stop mysql |
| seafile   | systemctl stop seafile |
| ownCloud  | Siehe Apache |
| FHEM      | systemctl stop fhem |
| iobroker  | systemctl stop iobroker |
| cron      | systemctl stop cron |

Die Services sollten dann per Option DEFAULT_STARTSERVICES wieder gestartet
werden. Die Reihenfolge sollte dann genau umgekehrt sein zu der
Stoppreihenfolge.

Der Installer sorgt automatisch dafür dass die ausgewählten Systemd
kontrollierten Services in der entsprechenden Reihenfolge gestoppt bzw.
gestartet werden. Leider garantiert Systemd nicht dass die Abhängigkeiten
der Services berücksichtigt werden. Zu ein paar Anwendungen gibt es auch
weitere Tipps auf dieser Seite die man berücksichtigen sollte.

Beispiel für -a

```
-a "systemctl start pilight && systemctl start samba && systemctl start nfs-kernel-server"
```

Beispiel für -o

```
-o "systemctl stop nfs-kernel-server && systemctl stop pilight && systemctl stop samba"
```

In der Konfigurationsdatei sieht es dann z.B. wie folgt aus:

```
DEFAULT_STOPSERVICES="systemctl stop nfs-kernel-server && systemctl stop pilight && systemctl stop samba"
```

bzw.

```
DEFAULT_STARTSERVICES="systemctl start samba&& systemctl start pilight && systemctl  start nfs-kernel-server"
```

Achtung: Die Befehle werden als root ausgeführt. Es ist kein sudo notwendig.

Mit der Option --systemstatus wird in das Debuglog die Liste der gestarteten
System Services sowie der offenen Dateien vor den Start des Backups
ausgegeben.

Möchte man ausdrücklich keine Services stoppen und starten muss ein
Doppelpunkt als Service angegeben werden, also -a : -o :


<a name="faq19"></a>
### 19) Welche Formatierung muss eine Partition haben auf der ein Backup abgelegt wird?

Prinzipiell kann jedes Filesystem benutzt werden was an Linux gemounted
werden kann. Allerdings gibt es ein paar Dinge zu beachten:

- Ein rsync Backup benutzt Hardlinks welche von ext3/4 unterstützt werden.
  Dann werden nur geänderte Dateien gesichert und gleiche Dateien per
  Hardlinks verknüpft. Ein ext4 Filesystem was über SMB freigegeben wird
  unterstützt keine Hardlinks. Eine Alternative ist NFS. Werden keine
  Hardlinks unterstützt kann rsync nicht genutzt werden.

- FAT32 kann nur Dateien bis zu 4GB speichern. Ein dd Backup wird so groß
  wie die SD-Karte (Außer es wird die Konfigurationsoption
  DEFAULT_DD_BACKUP_SAVE_USED_PARTITIONS_ONLY benutzt) und somit i.d.R.
  größer als 4GB. Selbiges trifft auf das tar Backup zu was auch sehr
  schnell größer als 4GB wird. Eine Alternative dazu ist NTFS.

Allgemeine Empfehlung: Benutze wenn möglich ext3/4. Auf Linux benutze NFS
für Netzwerklaufwerke. Auf Windows benutze NTFS auf exportierten SMB
Netzwerklaufwerken. Benutze FAT32 nur, wenn sichergestellt ist, dass die
Backups nicht größer werden als 4GB.


<a name="faq20"></a>
### 20) Ich habe Probleme beim Sichern meiner Backups auf einer Synology. Wie kann ich die beseitigen?

Es gibt diverse Benutzer von *raspiBackup* die ihre Backups per NFS auf einer
Synology erfolgreich sichern. Es gibt eine spezielle Seite wo ich und
Benutzer von *raspiBackup* beschrieben haben, was sie an der Synology
konfiguriert haben, damit alles funktioniert.


<a name="faq21"></a>
### 21) Der Inhalt der Bootpartition ändert sich doch nicht. Warum wir trotzdem immer die Bootpartition bei jedem Backup neu gesichert?

Das stimmt in 98% der Fälle. Allerdings kann ein Firmwareupdate die
Bootpartition ändern. Mit dem Konfigurationsparameter
DEFAULT_LINK_BOOTPARTITIONFILES werden die Bootpartitionen im Backup mit
Hardlinks verknüpft - sofern diese unterstützt werden. Damit kann man also
pro Backup 60MB Backupspace sparen. Allerdings wird immer die Bootpartition
erst einmal gesichert um dann zu testen ob sie sich zum vorhergehenden
Backup geändert hat und dann durch einen Hardlink ersetzt. D.h. diese
Option ist nur sinnvoll, wenn man einen sehr kleinen Backupspace hat.


<a name="faq22"></a>
### 22) Wie kann man verschiedene Backupkonfigurationen in verschiedenen Backupläufen benutzen?

Die Konfigurationsparameter von *raspiBackup* werden in folgender Reihenfolge
eingelesen und wirksam. Dabei können spätere Dateien bzw. Optionen vorherige
Optionen überschreiben.

1. `/usr/local/etc/raspiBackup.conf`
1. `./.raspiBackup.conf` (aktuelles Verzeichnis)
1. `~/.raspiBackup.conf` (Home Verzeichnis)
1. Die optionale Konfigurationsdatei, die mit der Option `-f` angegeben wurde
1. Aufrufparameter


<a name="faq23"></a>
### 23) Ich möchte den Backupfortschritt verfolgen. Gibt es eine Option um einen Fortschrittsbalken zu erhalten?

Es gibt dazu die Option -g für dd, tar und rsync. Die Option sollte nur
genutzt werden wenn man *raspiBackup* manuell startet.


<a name="faq24"></a>
### 24) *raspiBackup* meldet einen Fehler `ACL_TYPE_ACCESS, Operation not supported` bei der Benutzung des Backuptypen rsync

Die Fehlermeldung sieht in etwas wie folgt aus:

```
??? RBK0024E: Backupprogramm rsync hat einen Fehler bekommen.
rsync: set_acl: sys_acl_set_file(media/pi, ACL_TYPE_ACCESS): Operation not supported (95)
```

Die Ursache liegt darin, dass NFS4 mit rsync keine Posix ACLs
unterstützt. Diese sind aber auch in 99% der Fälle nicht notwendig. Die
folgende Zeile in der `/etc/mke2fs.conf`

```
default_mntopts = acl,user_xattr
```

bewirkt, dass jeder mount immer die ACL für eine Partition einschaltet. Das
trifft dann auch für die Backuppartition von *raspiBackup* zu, die
standardmäßig auf /backup gemounted wird. Somit wird immer versucht, ACL
Daten zu schreiben, was von rsync nicht unterstützt wird.

Hinweis: Synology unterstützt keine ACLs mit NFS3 as of 13.5.2022.

Hinweis: Mit folgendem Befehl findet mal alle Dateien mit ACLs: sudo
getfacl -Rs /Der Befehl braucht Zeit, bis er fertig ist.

Mögliche Lösungen:

1. Füge die folgende Zeile

   ```
   DEFAULT_RSYNC_BACKUP_OPTIONS="-aHx --delete --force --sparse"
   ```
   (kein großes A) in `/usr/local/etc/raspiBackup.conf`
   ein und damit sichert *rsync* keine ACLs mehr.

1. Nutze *tar* und nicht *rsync*

1. Benutze ein lokal angeschlossenes Gerät welches mit *ext4* formatiert ist

1. Benutze *NFS* version2 oder version3. Lies dazu [diesen Artikel](https://www.linux-tips-and-tricks.de/de/faq/2-uncategorised/605-wie-kann-man-acls-mit-rsync-auf-nfs-gemounteten-partitionen-sichern). Diese
   Option funktioniert aber nicht mit einer Synology.

1. Benutze `raspiBackupWrapper.sh`, in dem sich Code befindet, der ein Loop
   Device welches ein mit *ext4* formatiertes Image als Backuppartition
   benutzt und somit ACLs speichern kann.  (Nur für erfahrene Benutzer).

In Bullseye hat Debian persistentes Journaling eingeführt und somit
existiert /var/log/journal mit ACLs auf dem System. Wer *raspiBackup* Release
0.6.6 oder früher nutzt muss mindestens auf Release 0.6.6.1 upgraden oder
den Workaround, der auf *GitHub* in [Issue 393](https://github.com/framps/raspiBackup/issues/393) beschrieben ist, anwenden.


<a name="faq25"></a>
### 25) Fehlermeldung `dev/... has unsupported feature(s): metadata_csum E2FSCK: Get a newer version of e2fsck`

Lösung:
Vor dem Restore die `/etc/mke2fs.conf` editieren und bei beiden ext4 Optionen
das metadata_csum entfernen. Dann den Restore mit *raspiBackup* durchführen.

[.workaround]: _ "Probleme beim Syntax-Highlighting in vim-markdown bei non-balanced-underlines"


<a name="faq26"></a>
### 26) Wieso bekommen ich die die Meldung `??? RBK0160E: Ziel /dev/sda mit xx GiB ist kleiner als die Backupquelle mit yy GiB` obwohl beide SD-Karten gleich gross sind?

SD-Karten die mit einer bestimmten Größe angegeben sind (z.B. 16GB) sind
trotzdem unterschiedlich groß. Mit dem Befehl `sudo fdisk -l /dev/mmcblk0`
erhält man z.B. folgende Ausgabe die einem genau die Größe mitteilt:

```
sudo fdisk -l /dev/mmcblk0

Disk /dev/mmcblk0: 15.5 GB, 15548284928 bytes
Bei einer anderen ebenfalls 16GB grossen SD-Karte erhält man z.B.
Disk /dev/mmcblk0: 15.9 GB, 15931539456 bytes
```

Man kann also das erste Image auf die zweite SD-Karte bringen aber nicht umgekehrt.

Lösung:

- Eine größere SD-Karte nehmen
- Das Quellimage verkleinern. Das Tool pishrink eignet sich dazu.
- Das Backup mit dem Parameter
  DEFAULT_DD_BACKUP_SAVE_USED_PARTITIONS_ONLY erstellen (Siehe dazu
  auch FAQ16)
- Vor dem Erstellen des Backups die Rootpartition mit *gparted* etwas
  verkleinern (Mehrere hundert MB oder gleich 1 GB). Dann passt der
  Backup auch auf SD-Karten die etwas kleiner sind.


<a name="faq27"></a>
### 27) Ich habe ein tar oder rsync Backup und möchte das in ein dd Backup umwandeln. Geht das?

Es gibt ein Script [raspiBackupRestore2Image.sh](https://raw.githubusercontent.com/framps/raspiBackup/refs/heads/master/helper/raspiBackupRestore2Image.sh).
Damit kann man im Backupverzeichnis ein dd aus einem tar
oder rsync Backup erzeugen.


<a name="faq28"></a>
### 28) Wieso verschwinden Dateiänderungen nach einem Reboot wieder von einem zurückgespieltem Backup?

Die SD-Karte ist unglücklicherweise an der Stelle defekt, wo das Filesystem
Änderungen ablegt (Superblock). Da dieser im Hauptspeicher gehalten wird,
bemerkt man den Fehler nur nach einem Reboot.

Lösung:
Das Backup muss noch einmal auf eine neue fehlerfreie SD-Karte
zurückgespielt werden.


<a name="faq29"></a>
### 29) Ich bekomme die Meldung rsync: chown "(datei-fad)" failed: Operation not permitted (1). Wie kann ich das lösen?

Kurt hat dieses Problem bekommen, die Lösung gefunden und freundlicherweise
mitgeteilt. DougieLawson hat die [Lösung des Problems beschrieben](https://www.raspberrypi.org/forums/viewtopic.php?t=122066#p831840) .

Letztendlich musste der folgende Eintrag in der /etc/fstab

```
192.168.2.203:/data/raspi /media/nas nfs defaults 0 0
```

wie folgt geändert werden

```
192.168.2.203:/data/raspi /media/nas nfs defaults,noatime,noauto,x-systemd.automount 0 0
```

BastiFanta hat einen anderen Grund dafür gefunden:

> Ich musste den NFS-Share mit der Option no_root_squash erstellen, siehe
> für weitere Details: <https://www.selflinux.org/selflinux/html/nfs03.html>


<a name="faq30"></a>
### 30) Mir gefällt *raspiBackup* und ich möchte die Entwicklung und den Support honorieren. Wie kann ich das tun?

Zum Beispiel ein [Trinkgeld](introduction.md#donation) geben.


<a name="faq31"></a>
### 31) Ich bekomme eine Fehlermeldung von *raspiBackup*. Was kann ich tun um sie zu beseitgen?

Es gibt eine Seite wo alle häufigsten Fehlermeldungen von *raspiBackup*
genauer beschrieben sind inklusive Aktionen, mit denen man sie beseitigen
kann. Besuche dazu [diese Seite](error-messages.md).


<a name="faq32"></a>
### 32) Nach dem Upgrade auf v0.6.3.2 bekomme ich Fehlermeldungen RBK0021E: Backupprogramm des Typs tar beendete sich mit RC 1 oder RBK0021E: Backupprogramm des Typs rsync beendete sich mit RC 23.

Diese Fehler wurden in vorhergehenden Versionen ignoriert. Da dadurch aber
inkonsistente Backups erstellt werden können werden sie nicht mehr
ignoriert.

Folgende Optionen existieren, um das Problem zu beseitigen:

  - Stoppe den Service der die Datei während des Backups ändert. Das kann
    man entweder mit dem Installer vornehmen (M3->C6) sofern es ein System
    Service ist oder man muss manuell in der Konfigurationsdatei die beiden
    Optionen DEFAULT_STOPSERVICES und DEFAULT_STARTSERVICES um die Befehle
    erweitern, um den Service zu stoppen und zu starten.
    Tipp: Mit der Option --systemstatus erhält man im Debuglog eine Liste
    der aktiven Services und ihrer offenen Dateien. Damit kann man
    herausfinden welcher Service eine Datei während des Backups
    modifiziert.

  - Mit der option DEFAULT_EXCLUDE_LIST kann man die Dateien die sich
    während des Backups ändern vom Backup ausnehmen Achtung: Wenn diese
    Dateien wichtige Dateien einer Anwendung sind dann wird die restorte
    Anwendung nicht mehr starten. Also dringend vorher prüfen ob sich
    wichtig ist und gründlich testen ob die restorte Anwendung wieder
    startet wenn die Dateien fehlen..

  - inotifywait -m -e delete -e create -e move -e modify -e attrib <Verzeichnis>

U.U. muss noch die Option -r zugefügt werden, damit auch alle
Unterverzeichnisse überwacht werden.

  - Nutze die Configurationsoptionen `RSYNC_IGNORE_ERRORS` bzw
    `TAR_IGNORE_ERRORS` um den Fehler zu irgnorieren. Details dazu stehen
    [hier](#faq59)

<a name="faq33"></a>
### 33) Ich habe einen Cubieboard, Banana Pi, Odroid, Hummingboard, oder Beagle Board. Kann *raspiBackup* diese auch sichern?

Prinzipiell sollte das gehen bzw. geht es schon für bestimmte nicht
Raspberry Hardware. Einfach ausprobieren. *raspiBackup* wird aber [nur für
RaspbianOS und Raspberry HW](supported-hardware-and-software.md) unterstützt. D.h. wenn es funktioniert, sei
glücklich. Wenn es nicht funktioniert, frage aber nicht nach Support. :-)

Beim Aufruf muss dann noch die Option `--unsupportedEnvironment` mitgegeben werden.


<a name="faq34"></a>
### 34) Ich möchte mein 16GB dd Backup zurückspielen und bekommen die Meldung dass die Ziel SDKarte zu klein ist. Wieso?

SD-Karten haben zwar eine bestimmte Größe wie z.B. 16GB aber sie SD-Karten
haben nie genau diese Größe sondern es gibt kleine Abweichungen nach unten
und oben. Da das dd Backup genauso groß ist wie die SD-Karte kann das dd
Backup nicht zurückgeschrieben werden wenn man eine geringfügig kleinere
SD-Karte erwischt. Deshalb sollte man bei einem DD Backup die letzte
Partition immer etwas kleiner als maximal möglich erstellen. Siehe dazu
auch [FAQ16](#faq16). Man kann aber mit [pishrink](https://github.com/Drewsif/PiShrink) das dd Image verkleinern und danach
mit *raspiBackup* zurücksichern.


<a name="faq35"></a>
### 35) Ich möchte mein Rootfilesystem auf eine USB Platte verschieben. Kann ich das mit *raspiBackup* beim Restore machen?

Sofern es ein tar oder rsync Backup ist geht das. Einfach bei Restore die
Option -R nutzen.


<a name="faq36"></a>
### 36) Was bedeuten die Returncodes (RC) mit denen *raspiBackup* im Fehlerfalle endet?

  - 101 - Ein Programmfehler wurde festgestellt
  - 102 - Ein Linux Befehl liefert einen Fehler
  - 103 - *raspiBackup* wurde mit CTRLC beendet.
  - 105 - Beim Stoppen von Services gab es Fehler
  - 106 - Beim Starten von Services gab es Fehler
  - 107 - Ein Parameter in einer Option ist fehlerhaft
  - 108 - Es werden Dateien nicht gefunden
  - 109 - Das verwendete Linux Backupprogramm dd, tar oder rsync hat einen Fehler beim Backup bekommen
  - 110 - Ein Link zu einer Datei kann nicht erstellt werden
  - 111 - Beim Sammeln der Partitionsinformationen gibt es Fehler
  - 112 - Beim Restore gibt es Fehler beim Erstellen der Partitionen
  - 114 - Ein dd Image kann nicht erstellt werden
  - 115 - Benötigte Partitionen wurden nicht gefunden
  - 116 - Der Restore wurde vom Benutzer abgebrochen
  - 117 - Das verwendete Backupprogramm dd, tar oder rsync hat einen Fehler beim Wiederherstellen bekommen

  - 118 - Angegebene Geräte wurden nicht gefunden
  - 119 - Ein Verzeichnis kann nicht angelegt werden
  - 120 - Linux Tools fehlen die von *raspiBackup* benötigt werden
  - 121 - Es konnte keine gültige Bootpartition gefunden werden
  - 122 - Die Extension BEFORE_START_SERVICES endete fehlerhaft
  - 123 - Die Extension BEFORE_STOP_SERVICES endete fehlerhaft
  - 124 - Die Emailextension endete fehlerhaft
  - 130 - A file operation failed (chmod, mv, ...)
  - 131 - A mount failed
  - 132 - The environment (HW/SW) is unsupported
  - 133 - Die RESTORE_EXTENSION endet fehlerhaft
  - 134 - Die BACKUP_EXTENSIONa endet Fehlerhaft
  - 135 - Ein Download einer Datei endet fehlerhaft
  - 136 - Ein ungültiges nicht von *raspiBackup* erstelltes Backupverzeichnis wurde angegeben
  - 137 - Ein ungültiges Restoregerät wurde angegeben
  - 138 - Ein ungültiges Bootgerät wurde angegeben
  - 138 - USBMOUNT detected
  - 140 - An error occured during cleanup
  - 143 - Overlayfilesystem entdeckt
  - 144 - Erstellung des Backupordners auf der Backuppartition am Ende des Backup endet fehlerhaft
  - 145 - Resize einer Partition endet fehlerhaft
  - 147 - UUID Update endet fehlerhaft

<a name="faq37"></a>
### 37) Der eMail Betreff hat manchmal am Anfang einen Smiley. Was bedeutet er?

| smiley | Bedeutung |
| ------ | --------- |
| ;-)    | Es gibt eine neuere Release von *raspiBackup*. Ein Upgrade sollte mit der Option -U vorgenommen werden. Zurückgehen kann man wieder mit der Option -V. |
| :-D    | Es existiert eine Betaversion der nächsten *raspiBackup* Release. Beta Tester sind willkommen und können mit der Option -U die Beta installieren. Nach dem Test kann man auf die aktuelle Version wieder mit der Option -V zurückgehen. |
| O.o    | Eine Warnmeldung wurde geschrieben. |
| :-(    |Die *raspiBackup* Release ist veraltet und enthält einen schwerwiegenden Fehler. Sie sollte dringend durch die aktuelle Release mit der Option -U ersetzt werden. |


<a name="faq38"></a>
### 38) Wo kann ich Fragen stellen und Hilfe bekommen zu Linuxfragen und -problemen die im eigentlichen Sinne nichts mit *raspiBackup* zu tun haben?

*raspiBackup* wurde entwickelt, um auch Linux Einsteigern das Sichern ihrer
Raspberry schnell möglichst einfach zu ermöglichen. Allerdings sind dazu trotzdem gewisse
Linux-Kenntnisse notwendig. Häufige Probleme mit *raspiBackup* sind bei Linux
Einsteigern einfache Linux-Probleme. Solche Fragen werden nicht in den
Kontaktkanälen beantwortet. Dazu gibt es Foren mit
kompetenten Mitgliedern, die gerne helfen. Ein empfehlenswertes Forum ist das
[deutsche Raspberry Pi Forum](https://forum-raspberrypi.de/forum/).
Ein anderes ist das [englische Raspberryforum](https://forums.raspberrypi.com/).

<a name="faq39"></a>
### 39) Wo finde ich das Debuglog von raspiBackup?

Siehe [FAQ41](#faq41)

<a name="faq40"></a>
### 40) Wie kann ich meine Konfiguration nach einem Versionsupdate auf den neuesten Stand bringen?

Dieses wird von *raspiBackup* beim Upgrade automatisch erledigt. Siehe dazu
[Konfigurationsupdate bei einem Upgrade auf eine neue Version](configuration-update-when-upgrading-to-a-new-version.md).

<a name="faq41"></a>
### 41) Wo finde ich das Debuglog von raspiBackup?

Das Debuglog heißt `raspiBackup.log` beim Backup und `raspiBackup.logr` beim
Restore.

- Wenn *raspiBackup* erfolgreich endet, steht das Logfile im Backupverzeichnis
- Wenn *raspiBackup* nicht erfolgreich endet, steht das Logfile im Heimverzeichnis des Aufrufers
    - Wenn *raspiBackup* über die Konsole gestartet wurde, steht das Logfile entweder in `/home/<user>` oder `/root`
    - Wenn *raspiBackup* über Cron oder systemd im Hintergrund gestartet wurde, steht das Logfile in `/root`
- Wenn *raspiBackup* unerwartet endet oder mit kill gestoppt wurde, findet sich das Logfile in `/tmp`
- Das Logfile beim Restore steht entweder in `/home/<user>` oder `/root`

<a name="faq42"></a>
### 42) Wo können die /boot und /root Partition liegen ?

*raspiBackup* unterstützt folgende Konfigurationen im normalen
Backupmodus, wobei immer nur die `/boot`
und `/root` gesichert werden. Weitere Partitionen werden ignoriert.

- `/boot` und `/root` auf SD-Karte oder einem anderen Gerät (Platte, SSD, ...)
- `/boot` auf SD-Karte und `/root` auf eine anderen Gerät (Platte, SSD, ...)
  Dieses ist notwendig, wenn eine ältere Raspberry vorliegt, die noch
  keine USB Boot unterstützt, man aber trotzdem die Rootpartition nicht mehr
  auf der SD-Karte haben möchte.

<a name="faq43"></a>
### 43) Wie finde ich alle Dokumentationsseiten zu *raspiBackup* bzw. Seiten zu einem speziellen Thema?

Initial befand sich alle Doku zu *raspiBackup* auf
[dieser Seite](https://www.linux-tips-and-tricks.de).

Jetzt befindet sich alles auf dieser Webseite.

<a name="faq44"></a>
### 44) Warum startet das Image mit dem restorten Backup nicht?

Siehe [FAQ49](#faq49)

<a name="faq45"></a>
### 45) Wie kann ich Optionen temporär im Aufruf an- und ausschalten?

Viele Optionen dienen dazu etwas ein- oder auszuschalten. Normalerweise
wird die die Optionen einmal in der Konfigurationsdatei definiert und gut ist.
Möchte man aber kurzzeitig Optionen der Konfigurationsdatei überschreiben
kann man die Option mit einem `+` für einschalten und `-` für ausschalten
benutzen. Beispiel: Hat man standardmäßig das Zippen von dd Backups
eingeschaltet kann man das temporär mit der Option `-z-` ausschalten.

<a name="faq46"></a>
### 46) Warum ist es nicht zu empfehlen den Backuptyp dd zu benutzen?

Siehe dazu [diesen Artikel](why-shouldn-t-you-use-dd-as-backup-type.md).


<a name="faq47"></a>
### 47) Wo bekomme ich Hilfe bei reinen Linux-Fragen oder -Problemen, die nichts mit *raspiBackup* im eigentlichen Sinne zu tun haben?

Siehe [FAQ38](#faq38)

<a name="faq48"></a>
### 48) Kann ich den Backup auf ein laufendes System zurückspielen?

Technisch geht das aber das Ergebnis ist alles andere als ein laufendes
System. Deshalb bricht *raspiBackup* sofort ab wenn man das versucht.
Ein Restore muss immer auf eine weitere SD-Karte oder ein weiteres Gerät,
welches an die Raspberry angeschlossen ist, vorgenommen werden.

<a name="faq49"></a>
### 49) Mein Backup welches ich auf eine SD-Karte restored habe startet nicht. Warum nicht?

In 99.9% der Fälle ist die SD-Karte auf die restored wird defekt. Wenn man
auf eine andere, möglichst neue, SD-Karte restored tritt das Problem
üblicherweise nicht mehr auf. Es gibt auch die Option -C die man beim
Restore nutzen kann um die SD-Karte auf Bad Blocks beim Formatieren zu
prüfen. Dadurch dauert aber der Restoreprozess wesentlich länger. Siehe
auch [diese Seite](why-shouldn-t-you-use-dd-as-backup-type.md) zu Problemen eines dd Backups.


<a name="faq50"></a>
### 50) Mein Backup oder restore dauert ewig. Woran kann das liegen?

Die Backup- wie auch Restorezeit ist abhängig von der Größe der zu
sichernden Daten wie auch der Performance der Backuppartition. Wird über
das Netz per SMB oder NFS gesichert dauert es noch einmal länger. Beim
rsync dauert der erste Backup länger da das erste Backup ein Vollbackup
ist. Erst die folgenden Backups sind nur noch inkrementelle Backups und
deshalb i.d.R. schneller.

Es kann vorkommen, dass der Backup- oder Restorelauf nicht endet bzw. extrem
lange dauert. Das liegt i.d.R. daran, dass Fehler bei der Sicherung
auftreten - Schreib- oder Lesefehler, die von den  genutzten Linux
Backuptools `dd`, `tar` oder `rsync` gemeldet werden.

Bei `rsync` kann es auch daran liegen, dass ACLs gesichert werden sollen, aber
dazu die Berechtigung nicht existiert oder ACLs nicht von der
Backuppartition unterstützt werden. Letzteres trifft zu für NFS und SMB
gemountete Backuppartitionen. Siehe dazu [FAQ24](#faq24).

Falls die mount Option `sync` genutzt wird, sollte diese durch die Option `async`
ersetzt werden.

Option --timestamps hilft den Schritt zu finden, wo *raspiBackup* so lange
braucht. Danach hilft das Debuglog weiter.


<a name="faq51"></a>
### 51) Wie werden die Statistiken der Fortschrittsanzeige berechnet ?

*raspiBackup* berechnet nichts. Stattdessen werden die Optionen der
angebotenen Fortschrittsanzeige genutzt. Bei dd ist es die Option
status=progress und bei rsync die Option info=progress2. tar hat keine
eigene Fortschrittsanzeige und es wird deshalb der Datenstrom durch pv
gestreamt. Die Details der jeweiligen Fortschrittsanzeige sind in der
Dokumentation den Optionen in den jeweiligen Tools und sowie dem Linux Tool
pv erklärt.


<a name="faq52"></a>
### 52) Wie kann ich eine Testversion oder einen temporären Fix von aus dem *GitHub* downloaden und ausführen?

Dazu gibt es ein [Script bei *GitHub*](https://github.com/framps/raspiBackup/blob/master/scripts/raspiBackupDownloadFromGit.sh). Dieses muss man wie folgt aufrufen:

```
curl -s https://raw.githubusercontent.com/framps/raspiBackup/master/scripts/raspiBackupDownloadFromGit.sh | sudo bash -s -- <Branchname>
```

Dabei muss <Branchname> der *GitHub* Branch sein, von dem man sich
`raspiBackup.sh` downloaden möchte. Danach ruft man diese *raspiBackup* Version
wie folgt auf (**Achtung:** Auf den führenden Punkt achten !)

```
sudo ./raspiBackup.sh <Optionen>
```


<a name="faq53"></a>
### 53) Was sind *raspiBackup* Snapshots?

*raspiBackup* Snapshots sind spezielle Backups mit zwei besonderen
Eigenschaften:

- Sie werden nicht beim Backuprecycle berücksichtigt und müssen somit
  manuell im Backupverzeichnis gelöscht werden
- Sie haben eine Beschreibung im Backupverzeichnisnamen anhand derer ein
  *raspiBackup* Snapshot leicht zu erkennen ist und mit dem man eine
  sprechende Beschreibung dem Snapshot geben kann damit er leicht zu
  erkennen ist.

Ein Snapshot wird mit der Option -M erstellt und kann sehr gut dazu genutzt
werden beim Neuaufsetzen oder Änderungen am System zu bestimmten
Zeitpunkten einen Snapshot zu ziehen damit man im Fehlerfalle zurückgehen
kann. Anhand der Beschreibung kann man erkennen welchen Stand man mit dem
Snapshot gesichert hat.


<a name="faq54"></a>
### 54) Wie kann ich auf die boot Partitionsdateien im Backupverzeichnis zugreifen?

*raspiBackup* speichert die Bootpartitionsdaten in einem Imagefile. Mit den
folgenden Befehlen kann man auf die Dateien in diesem Image zugreifen:

```
sudo losetup -f <hostname>-backup.img
sudo mount /dev/loop0 /mnt
```


<a name="faq55"></a>
### 55) Warum habe ich plötzlich PARTUUIDs doppelt auf meinem System?

Während des Restores eine Backups wird die PARTUUID der Originalsystems für
die Partitionen wieder genutzt. Wenn dieses restorte System an dem
Originalsystem gemounted wird tauchen die PARTUUIDs doppelt auf und es wird
i.d.R. Probleme beim Booten des Originalsystems geben. Für diese Fälle gibt
es die Option `-updateUUIDs` beim Restore wodurch nicht dieselbe PARTUUID
beim restorten System genutzt wird. Ab der Release 0.6.9 wird immer eine
neue PARTUUID generiert. Will man das nicht muss mit der Option
`-updateUUIDs-` dieses ausgeschaltet werden.


<a name="faq56"></a>
### 56) Wie kann ich *raspiBackup* auf einem unsupporteten System automatisch starten lassen?

Dazu muss die Datei /etc/systemd/system/raspiBackup.service geändert
werden:

Ändere die Zeile ExecStart=/usr/local/bin/raspiBackup.sh in

ExecStart=/usr/local/bin/raspiBackup.sh --unsupportedEnvironment.


<a name="faq57"></a>
### 57) Wie kann ich *raspiBackup* auf ein neues Release updaten?

*raspiBackup* meldet wenn eine neue Release oder eine Beta verfügbar ist. Ein
Update wird mit der Option `-U` gestartet. Mit der Option `-V` kann man wieder
auf eine vorhergehende Release zurückgehen. Beta-Versionen werden oft mehrere Male
erneuert. Um dann den neuesten Stand zu installieren müssen die Optionen
`-U` und `-S` genutzt werden.


<a name="faq58"></a>
### 58) Was muß ich beachten, wenn ich mit rsync auf eine NFS gemountete Backuppartition sichern will?

Die Partition muss vom NFS Server mit `no_root_squash` exportiert werden.


<a name="faq59"></a>
### 59) rsync meldet dass Dateien während des Backuprozesses am System verschwunden sind und bricht mit Returncode 24 ab. Wie kann ich das verhindern?

Es gibt folgende Möglichkeiten:

- Der Service der die Datei löscht wird vor dem Backup gestoppt und wieder gestartet
- Die Datei oder auch das Verzeichnis in der sich die Datei befindet wird vom Backup excluded
- Wenn das alles nicht genutzt werden kann gibt es noch die Option
  DEFAULT_RSYNC_IGNORE_ERRORS="24" mit dem *raspiBackup* den RC24 ignoriert.

Achtung:  Es gibt seltene Umstände, in denen ein rsync RC 24 ein nicht zu
ignorierender Fehler ist. Siehe dazu [hier bei bugzilla.samba.org](https://bugzilla.samba.org/show_bug.cgi?id=3653#c12).
D.h. man sollte möglichst versuchen, den Fehler mit Möglichkeit 1 oder 2 zu beseitigen.

[.status]: translated
[.source]: https://linux-tips-and-tricks.de/de/faq

