# msmtp Konfiguration für einen web.de Account

Der Nutzer *gNeadr* von *raspiBackup* hatte Probleme, die eMail-Benachrichtigung
für seinen web.de Account einzurichten. Nachdem es ihm
erfolgreich gelungen war, alles richtig zu konfigurieren, bot er
erfreulicherweise an, seine Installations- und Konfigurationsschritte hier zu
veröffentlichen, damit andere *raspiBackup* Nutzer es leichter haben,
die eMailKonfiguration für *raspiBackup* vorzunehmen.

In *raspiBackup* ist nicht viel zu konfigurieren.
Die Schwierigkeit ist, den eMailClient richtig zu konfigurieren.

Anbei die Installations- und Konfigurationsschritte von *gNeandr* -
noch einmal sehr herzlichen Dank für die Bereitstellung.

[.status]: review-comment "Das Folgende würde ich deutlich kürzen und auf den Mailteil beschränken."


```
Raspberry Installation 2023-08-20
====================================================
SDCard 64GB microSDXC
 ext4 formatiert mit gparded auf LX
 Label: RXXXX
```


## Install Raspberry Pi OS with Raspberry Pi Imager v.1.7.4

OS: Raspberry PI OS Lite (32-bit) Bullseye vom 2023-05-03

SD-Karte: Generic STORAGE_DEVICE (RXXXX) - 63.8GB

Erweiterte Einstellungen:

- Hostname: rasp1
- SSH aktiviert, Name: rasp1 PW: [siehe keypass]
- Wifi: SSID: [ssid] PW: [siehe keypass]
- Wifi Land: DE
- Spracheinstellung: Berlin Tastatur: de

Speichern ==> SCHREIBEN


## Setup for Static LAN with Fritzbox

(see also https://learn.sparkfun.com/tutorials/headless-raspberry-pi-setup/ethernet-with-static-ip-address)

Mit LX Terminal auf der SDCard (im CardLeser) die IF-Datei anpassen:

```
$ ls -lt /media/xxxxx/rootfs/etc/dhcpcd.conf
```

```
interface eth0
static ip_address=192.123.123.xx/24
static routers=192.123.123.1
static domain_name_servers=192.123.123.1
```

Erfordert Zugriff mit:
```
sudo nano /media/xxxxx/rootfs/etc/dhcpcd.conf
```

Danach im LX Dateimanager SDCard auswerfen.


## Raspberry starten und konfigurieren

Danach SD Karte in Raspberry installieren und diesen starten/Netzadapter anschliessen.

Mit Fritzbox kontrollieren, ggf. Namen des 'raspberry' ändern.

Raspberry per SSH starten mit:

```
ssh pi@192.123.123.7X (ip des Raspberry wie oben konfiguriert)
```

## Raspberry/RASPIAN OS Konfigurieren & Update/Upgrade

Zur Sicherheit das Password ändern ...
(see also https://www.raspberrypi.org/documentation/configuration/security.md)
... dies erfolgt mit dem Raspberry Config tool:

```
$ sudo raspi-config
```

Einstellung z.B.:

```
│ 1 Change User Password Change password for the 'pi' user │
│ 2 Network Options Configure network settings │
--> Name eingeben zB 'raspellX'
│ 3 Boot Options Configure options for start-up │
--> B2 Wait for network
│ 4 Localisation Options Set up language and regional settings to match your │
--> Locales: de_DE.UTF-8 UTF-8
--> default : en_GB.UTF-8
--> Timezone
--> Keyboard
│ 5 Interfacing Options Configure connections to peripherals │
--> P2 SSH
│ 6 Overclock Configure overclocking for your Pi │
│ 7 Advanced Options Configure advanced settings │
--> A1 Expand Filesystem
│ 8 Update Update this tool to the latest version │
--> update the tool
│ 9 About raspi-config Information about this configuration tool |
```

```
$ sudo apt-get update
$ sudo apt-get upgrade
```

## mSMTP für Versand von EMail zB. aus *raspiBackup*

Diese Zusammenstellung basiert auf: <https://goneuland.de/raspberry-pi-e-mails-versenden-mit-msmtp/>

### Installation

```
$ sudo apt-get install msmtp msmtp-mta mailutils
```
```
$ msmtp --version

msmtp version 1.8.11
Platform: arm-unknown-linux-gnueabihf
TLS/SSL library: GnuTLS
Authentication library: GNU SASL; oauthbearer: built-in
Supported authentication methods:
plain scram-sha-1 external gssapi cram-md5 digest-md5 login ntlm oauthbearer
IDN support: enabled
NLS: enabled, LOCALEDIR is /usr/share/locale
Keyring support: Gnome
System configuration file name: /etc/msmtprc <<===
User configuration file name: /home/pi/.msmtprc <<===
Copyright (C) 2020 Martin Lambers and others.
This is free software. You may redistribute copies of it under the terms of
the GNU General Public License <http://www.gnu.org/licenses/gpl.html>.
There is NO WARRANTY, to the extent permitted by law.
```

Die mit `<<===` bezeichneten Zeilen sind wichtig für die weitere mSMTP Konfiguration!


### Config Datei erstellen (bzw anpassen) für Versand mit WEB.de

```
$ sudo nano /etc/msmtprc
```

Das nachfolgende Listing von "/etc/msmtprc" zeigt die Einstellungen für den Versand über einen
existierenden EMail Account bei WEB.de

Für den eigenen Einsatz müssen die Zeilen, die auf "# Anpassen" folgen mit den eigenen Werten geändert werden.

Im Abschnitt "# Authentifizierungs-Methoden." sind verschiedene Formate für die Passwort Angabe möglich.
Die einfachste Art (wie im Beispiel) ist der direkte Eintrag des PW des Mail Account ... ABER
das ist nicht die sicherste Methode!
Siehe auch: # https://marlam.de/msmtp/msmtp.html#Authentication

```
$ sudo cat /etc/msmtprc

# Set default values for all following accounts.
defaults
# Use the mail submission port 587 instead of the SMTP port 25.
port 587
# Always use TLS.
tls on
# Mail account
# Hier wird jetzt alles für den E-Mail Account konfiguriert
# Einen beliebigen Namen verwenden
account raspi
# Host name of the SMTP server
# Anpassen
host smtp.web.de
# Envelope-from address
# Anpassen
from yyyyyy@web.de
# Authentifizierungs-Methoden. Mehr Informationen dazu findet man in der Dokumentation zu msmtp:
# https://marlam.de/msmtp/msmtp.html#Authentication
auth on
# Anpassen
user yyyyyy@web.de
# Anpassen
password PxxxxxxxxW
# Set a default account
# Name von oben hier wieder eintragen
account default: raspi
```


### Rechte / Zugriff Anpassen

Die nächsten Schritte passen die Rechte der Datei an.

```
$ sudo chmod 600 /etc/msmtprc
```

Festlegen des E-Mail Programms mit "set sendmail":

```
$ sudo nano /etc/mail.rc
```
```
set sendmail="/usr/bin/msmtp -t"
```
```
$ sudo chown pi:pi /etc/msmtprc
$ ls -lt /etc/msmtprc

-rw------- 1 pi pi 566 Aug 19 19:55 /etc/msmtprc
```

### Test von mSMTP für WEB.de

```
$ sudo echo "E-Mail Test" | mail -s "E-Mail Betreff" yyyyyy@web.de
```

Damit empfängt der WEB.de Mail Account diese Nachricht:

```
Betreff: E-Mail Betreff: mSMTP TEST
Datum: Sun, 20 Aug 2023 14:40:18 +0200
Von: yyyyyy@web.de
An: yyyyyy@web.de
E-Mail Test
```

## *raspiBackup* Konfiguration für EMail Versand mit mSMTP

### Anpassung

Die Konfigurationsdatei "raspiBackup.conf" wird an die vorstehende mSMTP Einrichtung
angepasst für *raspiBackup* EMail Benachrichtigungen mit:

```
$ sudo nano /usr/local/etc/raspiBackup.conf
```
```
# email to send completion status
DEFAULT_EMAIL="yyyyyy@web.de"
# Sender emailadresse die mit ssmtp und msmtp benutzt wird
DEFAULT_SENDER_EMAIL="yyyyyy@web.de"
# Additional parameters for email program (optional)
DEFAULT_EMAIL_PARMS=""
# mailprogram
DEFAULT_MAIL_PROGRAM="mail"
```

### Test EMail-Benachrichtung von *raspiBackup* mit mSMTP für WEB.de

```
$ sudo *raspiBackup* -m detailed -F
```

Console Ausgabe:

```
--- RBK0009I: rasp8: *raspiBackup*.sh V0.6.8 - 2023-08-18 (cbfe5e8) Sun 20 Aug 15:42:40 CEST 2023 gestartet.
--- RBK0116I: Konfigurationsdatei /usr/local/etc/raspiBackup.conf wird benutzt.
!!! RBK0124W: Simulationsmodus an.
--- RBK0151I: Backuppfad /media/backup8 mit Partitionstyp ext4 wird benutzt.
!!! RBK0157W: Keine Systemd Services sind zu stoppen.
--- RBK0081I: Backup vom Typ rsync wird in /media/backup8/rasp8/rasp8-rsync-backup-20230820-154237 erstellt.
--- RBK0078I: Backupzeit: 00:00:01.
--- RBK0033I: Bitte warten bis aufgeräumt wurde.
--- RBK0159I: 5 Backups werden für den Backuptyp rsync aufbewahrt. Bitte Geduld.
--- RBK0017I: Backup erfolgreich beendet.
--- RBK0010I: rasp8: *raspiBackup*.sh V0.6.8 - 2023-08-18 (cbfe5e8) Sun 20 Aug 15:42:49 CEST 2023 beendet mit Returncode 0.
--- RBK0167I: Eine eMail wird versendet.
--- RBK0026I: Debug Logdatei wurde in /home/pi/raspiBackup.log gesichert.
```


Der WEB.de Mail Account empfängt diese Nachricht:

```
Betreff: rasp8: Backup erfolgreich beendet.
Datum: Sun, 20 Aug 2023 15:42:50 +0200
Von: yyyyyy@web.de
An: yyyyyy@web.de
--- RBK0009I: rasp8: *raspiBackup*.sh V0.6.8 - 2023-08-18 (cbfe5e8) Sun 20 Aug 15:42:40 CEST 2023 gestartet.
--- RBK0116I: Konfigurationsdatei /usr/local/etc/raspiBackup.conf wird benutzt.
!!! RBK0124W: Simulationsmodus an.
--- RBK0151I: Backuppfad /media/backup8 mit Partitionstyp ext4 wird benutzt.
!!! RBK0157W: Keine Systemd Services sind zu stoppen.
--- RBK0081I: Backup vom Typ rsync wird in /media/backup8/rasp8/rasp8-rsync-backup-20230820-154237 erstellt.
--- RBK0078I: Backupzeit: 00:00:01.
--- RBK0033I: Bitte warten bis aufgeräumt wurde.
--- RBK0159I: 5 Backups werden für den Backuptyp rsync aufbewahrt. Bitte Geduld.
--- RBK0017I: Backup erfolgreich beendet.
--- RBK0010I: rasp8: *raspiBackup*.sh V0.6.8 - 2023-08-18 (cbfe5e8) Sun 20 Aug 15:42:49 CEST 2023 beendet mit Returncode 0.
--- RBK0167I: Eine eMail wird versendet.
```

[.status]: rst
[.source]: https://www.linux-tips-and-tricks.de/de/raspibackupcategoried/650-konfiguration-von-raspibackup-mit-msmtp-fuer-einen-web-de-account

