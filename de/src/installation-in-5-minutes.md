# Schnellstart - Installation in 5 Minuten

Die Dokumentation von *raspiBackup* ist Aufgrund der Fülle an Funktionen
mittlerweile sehr umfangreich geworden.

Um den Einstieg zu erleichtern, wird auf dieser Seite deshalb kurzgefasst
erklärt, wie *raspiBackup* in wenigen Minuten installiert und konfiguriert
und dann Backups der Raspberry erstellt werden können.

Im Kapitel [Konfigurationsbeispiele](configuration-examples.md) sind einige Inspirationen zum Einsatz von *raspiBackup*
aufgeführt. Diese können zum Kennenlernen der Parameter dienen und damit bei der späteren
Konfiguration während der Installation helfen.

Das Wiederherstellen eines Backups ist detailliert [auf einer eigenen Seite](restore-intro.md) beschrieben.
Dort wird auch auf die primären Plattformen (Linux, Mac oder Windows) der Benutzer eingegangen.

**Hinweis:** Von *raspiBackup*-User [Franjo_G](https://forum-raspberrypi.de/user/57610-franjo-g/) gibt es eine weitere
[Anleitung zur Installation, Konfiguration und Nutzung von raspiBackup](https://forum-raspberrypi.de/article/7-raspibackup-installation-grundeinstellungen-erstes-backup-und-restore/).im deutschen Raspberryforum.


## Mit Installer oder ohne?

Es gibt verschiedene Möglichkeiten, *raspiBackup* zu starten.

Sogar eine ["adhoc"-Nutzung](using-raspibackup-without-installation.md) von *raspiBackup* ganz ohne Installation ist möglich.

Hier wird aber nun auf die standardmäßige Installation mit dem Installer eingegangen.

**Hinweis**: Wer sich vor der Installation den Sourcecode von *raspiBackup* und/oder den Installer
*raspiBackupInstallUI* ansehen möchte, kann dies über die folgende Links tun:

  - [Download *raspiBackup*](https://github.com/framps/raspiBackup/blob/master/raspiBackup.sh)
  - [Download raspiBackupInstallUI](https://github.com/framps/raspiBackup/blob/master/installation/raspiBackupInstallUI.sh)


## Der *raspiBackup* Installer

*raspiBackup* hat einen menügeführten UI Installer bzw. Konfigurator,
`raspiBackupInstallUI`, mit dem es sich wie mit `raspi-config` einfach
installieren und in Grundzügen konfigurieren lässt.

Ebenso vorhanden sind Update-Funktionen für den Installer selbst und für *raspiBackup*.

Die Installationsführung erfolgt über Menüs sowie über Auswahllisten. Als
Menüsprachen stehen Deutsch, Englisch, Finnisch, Chinesisch und Französisch zur Verfügung.

In dem [*raspiBackup*-Vorstellungsvideo auf Youtube](https://youtu.be/PuK_FNK674s)
wird eine Demo der Installation gezeigt.


<a name="backup-directory"></a>
## Vorbereitung: Das Backup-Ziel/Backup-Verzeichnis

In der Standardkonfiguration geht *raspiBackup* davon aus, dass es einen
Mountpoint `/backup` gibt, unter dem das Backupverzeichnis gemounted ist.

Dieser Mountpoint sollte schon vor der Installation erstellt und dann dort
das externe Backupverzeichnis/Gerät (USB-Platte, USB-Stick, NFS-Laufwerk, ...)
gemounted werden.

Im folgenden Beispiel wird eine externe USB-Platte bzw. USB-Stick gemountet:

```
sudo mkdir -p /backup
sudo mount /dev/sda1 /backup
```

*raspiBackup* setzt je nach gewünschtem Backuptyp für diese Partition ein gewisses Filesystem voraus.
Dies wird in Kapitel "[Welches Dateisystem kann auf der Backuppartition benutzt werden?](which-filesystem-can-be-used-on-the-backup-partition.md)" erklärt.
Bitte beachten: [Warum sollte man dd als Backuptyp besser nicht benutzen?](why-shouldn-t-you-use-dd-as-backup-type.md).

**Vor** dem ersten Backup ist es sinnvoll, zu prüfen/sicherstellen, dass wirklich das
richtige Backupziel bzw die richtige Backuppartition genutzt wird.

Hilfreich sind dabei folgende Befehle:

```
sudo blkid -o list
mount | grep backup
```


## Download und Installation des Installers

Zum Download, der Installation und Start des *raspiBackup* Installers bitte
folgendes in der Befehlszeile auf der Raspberry eingeben:

```
pushd /tmp
curl -o install -L https://raspibackup.linux-tips-and-tricks.de/install
sudo bash ./install
popd
```

**Hinweis**: Eine manuelle Installation ohne `sudo` Nutzung ist in einer extra
[Anleitung](manual-installation-and-configuration.md) dokumentiert.

Nun kann man die Installation mit Standardkonfiguration wählen und
die wesentlichen Einstellungen im Konfigurationsmenü zu ändern.

![Screenshot Konfiguration (2019)](images/Screenshot_at_2019-04-10_07-52-15.png)

Alle weiterführenden Einstellungen werden in der Konfigurationsdatei
`/usr/local/etc/raspiBackup.conf` mit einem Editor konfiguriert.

Zum Schluss kann die wöchentliche Sicherung mit *raspiBackup* eingeschaltet werden.

Der Installer kann jederzeit wieder in der Befehlszeile mit
`sudo raspiBackupInstallUI` aufgerufen werden, um die Konfiguration
zu ändern.

![Installationsdemovideo](images/raspiBackupInstall_de.gif)


## Systemd zum automatischen regelmäßigen Starten des Backups

Nachdem sowohl Backup als auch Restore erfolgreich getestet und die vor dem Backup
zu stoppenden Services konfiguriert wurden, kann *raspiBackup* per *Systemd timer*
für eine automatische Ausführung im gewünschten Intervall eingeplant werden.

Die Systemd-Konfiguration sollte immer mit dem Installer geändert werden.

Eventuelle manuelle Änderungen in der *Systemd*-Konfigurationsdatei `/etc/systemd/system/raspiBackup.timer`
sollten "vorsichtig" vorgenommen werden. Sie könnten leicht dazu führen,
dass der Installer die Konfigurationsdatei nicht mehr ändern kann.

Sollte es doch einmal ein Problem geben: Vom Installer wird immer ein Debuglog in der Datei
`/root/raspiBackupInstallUI.log` angelegt, welches bei der Suche nach der Ursache hilft.


## Die Benachrichtigung per eMail

Benachrichtigungen per eMail benötigen einen korrekt konfigurierten lokalen MTA
wie *Postfix*, *nullmailer*, *msmtp* oder *Exim4*. Wird *Pushover*, *Slack* oder *Telegram*
genutzt, muss die Konfigurationsdatei von *raspiBackup* vorher manuell
entsprechend mit den benötigten Konfigurationsdaten versehen werden.
Siehe Kapitel [Allgemeine Konfiguration](general-config-options.md).
Ein Benachrichtigungstest kann mit der Option `-F` durchgeführt werden.



## Ein Backup erstellen ...

Nachdem die Backuppartition ja schon unter `/backup` gemountet ist [(s.o.)](#backup-directory),
kann das Backup gestartet werden. Beim ersten Mal vielleicht mit ausführlichen Meldungen:


```
sudo raspiBackup -m detailed
```

Je nach Größe der Installation kann das natürlich etwas länger dauern...


## ... und einen Restore testen!

**Danach sollte unbedingt ein Restoretest durchgeführt werden** ([Link zur
Restoredokumentation](restore.md)), um zu verifizieren, dass ein konsistentes
Backup erstellt wird, und um sich mit der Restoreprozedur vertraut zu machen.

**Denn:
Ein Backup nützt nichts, wenn man in dem Moment, wo man es einspielen möchte,
feststellt, dass es nicht zu gebrauchen ist.**

Der ganze Restoreprozess sollte von Zeit zu Zeit durchexerziert und damit getestet werden,
ob die erstellten Backups in Ordnung sind und sich damit ein System funktionsfähig
restaurieren lässt. *raspiBackup* erinnert in regelmäßigen Abständen daran,
einen Restoretest vorzunehmen. Das Erinnerungsintervall ist konfigurierbar.
Der Standardwert ist 6 Monate.

Besonders wichtig ist das Testen auch, wenn ein neues System mit einem neuen
Betriebssystem wieder mit *raspiBackup* gesichert wird. Es gibt immer wieder
Änderungen bei neuen Betriebssystemversionen, die dazu führen können, dass der
Restore nicht mehr funktioniert.


<a name="next-steps"></a>
## Weitere Schritte

Nachdem das erste Backup erfolgreich erstellt und wiederhergestellt wurde,
sollte man sich in einer ruhigen Stunde über alle weiteren Optionen von
*raspiBackup* informieren und je nach Bedarf einsetzen.

In jedem Falle ist es sinnvoll, sich die [FAQs](faq.md) durchzulesen.

Jede Option kann in der Konfigurationsdatei `/usr/local/etc/raspiBackup.conf` definiert werden,
so dass beim Aufruf keine weitere Optionen angegeben werden müssen.

Details dazu finden sich im Kapitel [Aufruf und Optionen - Backup - Optionen](backup-options.md)
und zu den Optionen, die sich **nur** über die Konfigurationsdatei einstellen lassen
im Kapitel [Aufruf und Optionen - Backup - Konfiguration](backup-config-options.md).

Ebenfalls nützlich: [raspiBackupDialog - ein komfortables Hilfsscript für raspiBackup](raspibackupdialog-a-convenient-helper-script-for-raspibackup.md),
welches die Nutzung und den Aufruf von *raspiBackup* vereinfacht.

## Deinstallation

Sollte sich tatsächlich herausstellen, dass *raspiBackup* nicht den Anforderungen genügt,
steht eine [Deinstallation](installer.md#deinstallation) per *raspiBackup* Installer zur Verfügung.
Über einen der [Kontaktwege](https://framps.github.io/raspiBackupDoc/#contact-options) ist es vorher aber sinnvoll mal nachzufragen ob die vermisste Funktionalität
nicht doch in raspiBackup verfügbar ist.

[.status]: translated
[.source]: https://linux-tips-and-tricks.de/de/installation
