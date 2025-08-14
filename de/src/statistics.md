# Statistiken

 *raspiBackup* prüft bei jedem Start, maximal aber einmal pro Tag, ob es ein neues
 Release oder eine Beta gibt und weist dann mit einer Meldung darauf hin, so
 dass ein Upgrade geplant und durchgeführt werden kann. Bei dieser Prüfung
 werden auch ein paar Informationen übermittelt, die es ermöglichen, allgemeine
 Nutzungsdaten von *raspiBackup* zu ermitteln und sich einen Überblick über die
 jeweilige Nutzung zu verschaffen.

Die Informationen, die übertragen werden, sind

  - Release
  - Backuptyp
  - Backupmodus
  - Backup- oder Restoreaufruf
  - Keep
  - Parameter der intelligenten Rotationsstrategie, sofern sie genutzt wird
  - OS: *Raspberry Pi OS* oder *Ubuntu*

Das Senden dieser o.g. Informationen kann mit der Option

```
DEFAULT_SEND_STATS=0
```

in der Konfigurationsdatei `/usr/local/etc/raspiBackup.conf` ausgeschaltet werden.

[.status]: rst
[.source]: https://www.linux-tips-and-tricks.de/de/raspibackup#stats

