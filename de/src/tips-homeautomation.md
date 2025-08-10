# Tipps zur Homeautomation

Auf den folgenden Seiten werden Hinweise zu verschiedenen Anwendungen gegeben:
Ob und welche Services zu stoppen und zu starten sind, welche Besonderheiten zu
berücksichtigen sind, ob und welche Aktionen vor und nach dem Backup und/oder
vor und nach dem Restore vorzunehmen sind.

Diese Seite lebt vom Feedback der *raspiBackup* Nutzer, die sich mit den
jeweiligen Anwendungen auskennen und genau beschreiben können, worauf bei den
jeweiligen Anwendungen zu achten ist. Deshalb ist Feedback auf der [*GitHub* Diskussionsseite](https://github.com/framps/raspiBackupDoc/discussions)
sehr erwünscht. Gerne auch in Deutsch.

## *raspiBackup* Tipps für bestimmte Anwendungen

### OpenHAB

Funktioniert ohne Probleme. Siehe [hier auf der OpenHAB-Webseite](https://community.openhab.org/t/usage-of-raspibackup-within-openhabian/145926).


### ioBroker

ioBroker nutzt ACLs. Wer sein Backup auf eine per NFS angebundene Synology oder QNAP
sichert, muss das Sichern von ACLs ausschalten, damit *rsync* nicht abbricht. Siehe
dazu [FAQ24](faq.md#faq24), wie man das erreichen kann.

Wenn man ein Backup wiederherstellt, lassen sich mit ioBroker fix die
fehlenden ACLs neu erstellen. Außerdem sollte man den ioBroker vor dem
Backup mit `systemctl stop iobroker` stoppen und nach dem Backup mit `systemctl
start iobroker` wieder starten. Das lässt sich entweder direkt in der
*raspiBackup* Konfigurationsdatei bei DEFAULT_START_SERVICES und
DEFAULT_STOP_SERVICES eingeben oder man nutzt den *raspiBackup* Installer und
wählt dort den ioBroker als Service aus, der zu stoppen und zu starten ist. Der
Installer generiert dann die entsprechenden Befehle in der Konfigurationsdatei.

### FHEM

FHEM nutzt keine ACLs.

FHEM läuft als System Service und taucht somit im Installer als Service auf und
kann dort einfach mit M3->C6 ausgewählt werden, so dass FHEM vor dem Backup
gestoppt und am Ende wieder gestartet wird.

Zur manuellen Konfiguration in der Config dienen folgende Kommandos:

```
systemctl stop fhem
```
bei DEFAULT_STOPSERVICES

bzw.
```
systemctl start fhem
```
bei DEFAULT_STARTSERVICES


### SmartHomeNG

SmartHomeNG läuft als System Service und taucht somit im Installer als Service
auf und kann dort einfach mit M3->C6 ausgewählt werden, so dass SmartHomeNG vor
dem Backup gestoppt und am Ende wieder gestartet wird.

Wer es manuell in der Config konfigurieren will, sollte folgende Befehle aufnehmen:
```
systemctl stop smarthome
```
bei DEFAULT_STOPSERVICES

bzw.
```
systemctl start smarthome
```

bei DEFAULT_STARTSERVICES


[.status]: rst
[.source]: https://linux-tips-and-tricks.de/de/anwendungstipps
