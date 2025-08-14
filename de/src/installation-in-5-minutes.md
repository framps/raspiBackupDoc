# Schnellstart - Installation in 5 Minuten

**Hinweis:** Es gibt vom *raspiBackup*-User [Franjo_G](https://forum-raspberrypi.de/user/57610-franjo-g/) eine schöne Anleitung,
wie man *raspiBackup* installiert, konfiguriert und ein Backup restored.
Bevor hier alles dupliziert wird: [Seine Anleitung](https://forum-raspberrypi.de/article/7-raspibackup-installation-grundeinstellungen-erstes-backup-und-restore/) im deutschen Raspberryforum.

Die Dokumentation von *raspiBackup* ist durch Erweiterungswünsche von Benutzern
mittlerweile sehr umfangreich geworden. Auf dieser Seite wird deshalb kurz und
knapp Schritt für Schritt erklärt, wie man *raspiBackup* direkt benutzt, um sofort
ein Backup zu erstellen oder in 5 Minuten *raspiBackup* installiert und
konfiguriert und dann ein Backup der Raspberry erstellen kann.

Das Wiederherstellen eines Backups ist detailliert für die unterschiedlichen Benutzer mit
ihren jeweiligen primären Plattformen (Linux, Mac oder Windows) [auf einer eigenen Seite](restore.md) beschrieben.

Nachdem sowohl Backup als auch Restore erfolgreich getestet und die vor dem Backup
zu stoppenden Services konfiguriert wurden, kann *raspiBackup* per *systemd timer*
für eine automatische Ausführung im gewünschten Intervall eingeplant werden.

Danach kann man in einer stillen Stunde sämtliche Möglichkeiten von
*raspiBackup* hier nachlesen und die Konfiguration den speziellen Bedürfnissen
anpassen. In jedem Falle ist es sinnvoll, sich die [FAQs](faq.md) durchzulesen.

Der *raspiBackup* Installer ermöglicht es auch, *raspiBackup* wieder komplett zu
deinstallieren, falls sich nach der Installation und beim Test herausstellen
sollte, dass *raspiBackup* nicht den Anforderungen genügt.

**Hinweis:**  "5 Minuten" braucht jemand, der Basiskenntnisse von Linux hat. Wer diese
nicht hat, braucht vermutlich etwas länger, obwohl der Installer schon hilft,
schnell eine *raspiBackup* Anfangskonfiguration zu erstellen.

Vor der Nutzung von *raspiBackup* bitte erst lesen: [Unterstützte Hard- und Software](supported-hardware-and-software.md)

Die Supportkanäle [sind hier beschrieben](introduction.md#kontakt)


## Anwendungs- und Konfigurationsbeispiele

Auf [dieser Seite](configuration-examples.md) werden verschiedene Beispiele gegeben, wie man *raspiBackup* einsetzen kann.
Diese Beispiele sollten sich vor der eigentlichen Installation angesehen werden,
um bei der Konfiguration während der Installation die richtigen Parameter zu benutzen.


## *raspiBackup* installieren und automatisch regelmäßig ein Backup erstellen

*raspiBackup* hat einen UI installer, mit dem es sich wie mit `raspi-config`
recht einfach installieren und die primären Optionen konfigurieren lässt.

Alle weiteren Optionen werden in der Konfigurationsdatei
`/usr/local/etc/raspiBackup.conf` mit einem Editor konfiguriert.

Außerdem lassen sich jederzeit die primären Optionen durch erneuten Aufruf
von `raspiBackupInstallUI` nachträglich ändern. Dazu gehört auch eine
Updatefunktion für den Installer und für *raspiBackup*. Die
Installationsführung erfolgt über Menüs sowie über Auswahllisten. Die Menüsprache
kann Deutsch, Englisch. Finnisch, Chinesisch oder Französisch sein.

Wer *raspiBackup* einfach nur mit einer Standardkonfiguration ohne individuelle
Konfiguration schnell installieren möchte, kann das mit den Aufrufoptionen `-i` und
`-e` starten (`-h` für Hilfe benutzen).

Danach kann der Installer genutzt werden, um
die Basiskonfiguration von *raspiBackup* vorzunehmen bzw. zu ändern.
Auf Youtube existiert ein Video, auf dem *raspiBackup* vorgestellt wird
sowie am Ende eine Demo der Installation von *raspiBackup* gegeben wird.

[.status]: todo "Youtube Link hier einfügen -> generell YT videos an entsprechenden Stellen verlinken"
[.status]: todo "YT videos auf neue Doc umstellen"

![Screenshot Konfiguration (2019)](images/Screenshot_at_2019-04-10_07-52-15.png)

Zum Download, der Installation und Start des *raspiBackup* Installers bitte
folgendes in der Befehlszeile auf der Raspberry eingeben:

```
cd ~
curl -o install -L https://raspibackup.linux-tips-and-tricks.de/install
sudo bash ./install
```

**Hinweis**: Eine manuelle Installation ohne `sudo` Nutzung ist in einer extra [Anleitung](manual-installation-and-configuration.md)
dokumentiert.

Danach kann man die Installation wählen, bei der eine Standardkonfiguration
benutzt wird. Anschließend ist es möglich, die wesentlichen
Standardkonfigurationsoptionen im Konfigurationsmenü zu ändern. Zum Schluss
kann man die wöchentliche Sicherung mit *raspiBackup* einschalten.

In der Standardkonfiguration geht *raspiBackup* davon aus, dass es einen
Mountpoint `/backup` gibt, unter dem das Backupverzeichnis gemounted ist.
Diesen sollte man mit `sudo mkdir /backup` erstellen und dann dort das externe
Backupverzeichnis mounten.

Der Installer kann jederzeit wieder in der Befehlszeile mit
`sudo raspiBackupInstallUI` aufgerufen werden, um *raspiBackup* Konfigurationen
zu ändern oder auch *raspiBackup* zu deinstallieren.

**Hinweis**: Die *raspiBackup* Systemd Konfigurationsdatei ist
`/etc/systemd/system/raspiBackup.timer`. Die Systemdkonfiguration sollte immer
mit dem Installer geändert werden. Manuelle Änderungen in der Datei sollten
"vorsichtig" vorgenommen werden. Sie könnten leicht dazu führen, dass der Installer die
Konfigurationsdatei nicht mehr ändern kann.

Sollte es Probleme geben: Es wird vom Installer immer ein Debuglog in der Datei
`/root/raspiBackupInstallUI.log` angelegt, welches hilft, die Problemursache zu finden.


## Installationsdemo

**Hinweis**: Das folgende Video zeigt die Installation in Deutsch, da das OS
auf Deutsch konfiguriert war. Ist es auf Finnisch, Französisch, Englisch
oder Chinesisch konfiguriert schreibt der Installer alles in der jeweiligen
Sprache. Die Sprache kann auch im Installer geändert werden.

![Installationsdemovideo](images/raspiBackupInstall_de.gif)

**Hinweis:**
Benachrichtigungen per eMail benötigen einen korrekt konfigurierten lokalen MTA
wie *Postfix*, *nullmailer*, *msmtp* oder *Exim4*. Wird *Pushover*, *Slack* oder *Telegram*
genutzt, muss die Konfigurationsdatei von *raspiBackup* vorher manuell
entsprechend mit den benötigten Konfigurationsdaten versehen werden. Ein
Benachrichtigungstest kann am schnellsten mit der Option `-F` durchgeführt
werden.

**Achtung:**
Ein Backup nützt nichts, wenn man in dem Moment, wo man es einspielen möchte,
feststellt, dass das Backup nicht zu gebrauchen ist. Deshalb macht es Sinn, nach
dem ersten erfolgreichen Backup auch gleich den Restore testen.
Der ganze Restoreprozess sollte von Zeit zu Zeit durchexerziert und damit getestet werden,
ob die erstellten Backups in Ordnung sind und sich damit ein System funktionsfähig
restaurieren lässt. *raspiBackup* erinnert in regelmäßigen Abständen daran,
einen Restoretest vorzunehmen. Das Erinnerungsintervall ist konfigurierbar.
Der Standardwert ist 6 Monate.

Besonders wichtig ist das Testen auch, wenn ein neues System mit einem neuen
Betriebssystem wieder mit *raspiBackup* gesichert wird. Es gibt immer wieder
Änderungen bei neuen Betriebssystemversionen, die dazu beitragen können, dass der
Restore nicht mehr funktioniert.

[.status]: review-comment "Doppelt gemoppelt?"


## Downloadlinks auf *raspiBackup* und den raspiBackupInstaller

Wer sich vor der Installation den Sourcecode von *raspiBackup* und/oder den Installer
*raspiBackupInstallUI* ansehen möchte, kann dies über die folgenden
Downloadlinks tun:

  - [Download *raspiBackup*](https://github.com/framps/raspiBackup/blob/master/raspiBackup.sh)
  - [Download raspiBackupInstallUI](https://github.com/framps/raspiBackup/blob/master/installation/raspiBackupInstallUI.sh)


## Erstellen und Wiederherstellen eines Backups

Nachdem *raspiBackup* installiert wurde, sind folgende Schritte notwendig,
um ein Backup zu erstellen.

Der Standardmountpunkt von *raspiBackup*, wo die Backups abgelegt werden
(Annahme, dass der Standardmountpunkt benutzt wird), wird angelegt mit

```
sudo mkdir /backup
```

Anschließend muss ein externes Gerät (USB Platte, USB Stick, NFS Laufwerk, ...)
auf diesen Mountpoint gemounted werden. Im folgenden Beispiel wird eine externe
USB Platte bzw. ein externer USB Stick gemountet.

```
sudo mount /dev/sda1 /backup
```

Dabei ist zu beachten, dass die Partition je nach gewünschtem Backuptyp ein
gewisses Filesystem voraussetzt. Die Abhängigkeiten sind in "[Welches Dateisystem kann auf der Backuppartition benutzt werden?](which-filesystem-can-be-used-on-the-backup-partition.md)" erklärt.
Außerdem sollte man, wenn es denn nicht unbedingt erforderlich ist, den Backuptyp *dd* vermeiden.
Details dazu finden sich in "[Warum sollte man dd als Backuptyp besser nicht benutzen?](why-shouldn-t-you-use-dd-as-backup-type.md)".

Beim ersten Backup sollte man noch prüfen/sicherstellen, dass man auf das richtige Backupgerät
bzw. die richtige Backuppartition sichert. Hilfreich sind dabei folgende Befehle:

```
sudo blkid -o list
mount | grep backup
```
oder wenn die Backuppartition lokal angeschlossen wurde und sie ein Label hat

```
sudo blkid -o list | grep <label>
```

Danach ist alles fertig konfiguriert, um ein Backup zu erstellen.

Will man den Backup einmal schnell testen, kann wie folgt das Backup mit
*raspiBackup* erstellt werden. Das kann je nach Größe der Installation
länger dauern.

```
sudo raspiBackup -m detailed
```

**Danach sollte unbedingt ein Restoretest durchgeführt werden** ([Link zur
Restoredokumentation](restore.md)), um zu verifizieren, dass ein konsistentes
Backup erstellt wird, und um sich mit der Restoreprozedur vertraut zu machen.



## Standardkonfiguration und Ort der Konfigurationsdatei

Der Installer erstellt folgende Dateien:

  - Konfigurationsdatei `/usr/local/etc/raspiBackup.conf`

    In dieser werden folgende Standardwerte eingestellt und können mit dem
    Installer geändert werden. Alle anderen Optionen müssen mit einem Editor
    geändert werden oder mit einer Aufrufoption überschrieben werden.

    | Option               | Einstellung          |
    |----------------------|----------------------|
    | Backuppfad           | /backup              |
    | Backupmode           | normal               |
    | Backuptyp            | rsync                |
    | Sprache              | Sprache des Systems  |
    | Zip                  | nein                 |
    | Meldungsdetail       | normal               |
    | Backupanzahl         | 3                    |
    | Services start       | keine                |
    | Services stop        | keine                |
    | Wöchentlicher Backup | nein                 |
    | Backuptag            | Sonntag              |
    | Backupzeit           | 05:00 Uhr            |

    [Aufruf und Optionen](backup-options.md) sind ausführlich beschrieben.

<<<<<<< HEAD
2. *Systemd timer* Konfiguration `/etc/systemd/system/raspiBackup.timer`
=======
  - *Systemd timer* Konfiguration `/etc/systemd/system/raspiBackup.timer`
>>>>>>> main

    Diese Datei steuert den Aufruf von *raspiBackup* und im Standardfall ist der
    wöchentliche Backup ausgeschaltet. Er kann aber mit dem Installer eingeschaltet
    werden.

<<<<<<< HEAD
3. *raspiBackup*.sh `/usr/local/bin`

4. *raspiBackupInstallUI.sh* `/usr/local/bin`
=======
  - *raspiBackup*.sh `/usr/local/bin`

  - *raspiBackupInstallUI.sh* `/usr/local/bin`
>>>>>>> main

## Deinstallation

*raspiBackup* kann auch wieder deinstalliert werden.
Entweder benutzt man den Installer zum Deinstallieren oder folgenden Befehl:

```
sudo raspiBackupInstallUI.sh -u
```

## Weitere Schritte

Nachdem das erste Backup erfolgreich erstellt und wiederhergestellt wurde,
sollte man sich in einer ruhigen Stunde über alle weiteren Optionen von
<<<<<<< HEAD
*raspiBackup* hier informieren und je nach Bedarf einsetzen. Eine hilfreiche
Option ist z.B. `-e <eMailAdresse>`. Dadurch schickt *raspiBackup* nach jedem
Backuplauf seine Meldungen per eMail an die angegebene Adresse. Weiterhin lassen
sich Verzeichnisse vom Backup ausschließen sowie `dd` Backups
verkleinern und damit beschleunigen und Diverses mehr.
=======
*raspiBackup* hier informieren und je nach Bedarf einsetzen.
>>>>>>> main

Jede Option kann in der Konfigurationsdatei `/usr/local/etc/raspiBackup.conf` definiert werden,
so dass beim Aufruf keine weitere Optionen angegeben werden müssen.

Es existieren auch Optionen, die sich **nur** über die Konfigurationsdatei einstellen lassen.
Details dazu finden sich auf der [Optionsbeschreibungsseite](backup-options.md).

Ebenfalls nützlich: [raspiBackupDialog - ein komfortables Hilfsscript für raspiBackup](raspibackupdialog-a-convenient-helper-script-for-raspibackup.md),
welches die Nutzung und den Aufruf von *raspiBackup* vereinfacht.

<<<<<<< HEAD
=======
## Deinstallation

Entweder benutzt man den Installer zum Deinstallieren oder folgenden Befehl:

```
sudo raspiBackupInstallUI.sh -u
```


## Aufruf des Installers ohne Menüs direkt von der Befehlszeile

[.status]: review-comment "Doppelt gemoppelt!"

Wer nicht die menügesteuerte Installation nutzen möchte, kann die Installation von *raspiBackup*,
den Beispielextensions oder die Deinstallation direkt von der Befehlszeile aufrufen.
Dabei wird die Standardkonfiguration installiert.

Der Aufruf dazu ist

```
curl https://raspibackup.linux-tips-and-tricks.de/install | sudo bash -s -- -i
```

Änderungen an der Konfiguration können nun manuell mit einem Editor vorgenommen werden.
Ebenso das Einschalten des wöchentlichen Backups per Systemd Timer.
Man kann aber auch den Installer mit seinen Menüs benutzen, um die
Konfiguration der primären Optionen anzupassen sowie den regulären Backup ein-
oder auszuschalten. Der Aufruf dazu lautet

```
sudo raspiBackupInstallUI
```

Weitere Details zu den verschiedenen Funktionen des Installationsskriptes
erfährt man durch den Aufruf der Hilfefunktion:

```
sudo raspiBackupInstallUI -h
```

Zur Auswahl des Daemons, der die regelmäßigen Backups steuert, gibt es die Option `-t`.
Es kann `crond` oder `systemd` (Default) gewählt werden.


>>>>>>> main
## *raspiBackup* soll ohne Installation direkt aufgerufen werden, um sofort ein Backup zu erstellen

1. Download von *raspiBackup*: `curl -sSLO  https://www.linux-tips-and-tricks.de/raspiBackup.sh`

2. Mount der Backuppartition unter `/backup` oder Angabe der Backuppartition als letzten
   Parameter im Aufruf, also z.B. `sudo bash ./raspiBackup.sh /media/pi`

3. Start des Backups:  `sudo bash ./raspiBackup.sh`

Falls kein `rsync` Backup gewünscht wird, muss der Backuptyp `tar` oder `dd` mit Option `-t`
 mitgegeben werden, also `sudo bash ./raspiBackup.sh -t tar` oder `sudo bash ./raspiBackup.sh -t dd`

Kurzinfos zu allen Aufrufoptionen von *raspiBackup* erhält man mit `bash ./raspiBackup.sh -`


## Manuelle Installation und Konfiguration von *raspiBackup*

Siehe im gleichnamigen Kapitel: [Manuelle Installation und Konfiguration](manual-installation-and-configuration.md)

[.status]: review-comment "Doppelt gemoppelt?! Siehe oben und auch in installation.md"


[.status]: rst
[.source]: https://linux-tips-and-tricks.de/de/installation
