# Aufruf und Optionen

*raspiBackup* muss als Benutzer *root* oder per `sudo` aufgerufen werden.

    raspiBackup Option1 Option2 Option3 ... Backupverzeichnis

Alle Optionen, die etwas ein- oder ausschalten, können durch
ein angehängtes `+` oder `-` beim Aufruf von raspiBackup gezielt ein oder ausgeschaltet werden.

Beispiel: Die Option `-z` sowie die Option `-z+` schaltet die Backupcompression ein.
Mit der Option `-z-` wird dagegen die Backupcompression ausgeschaltet. Unabhängig davon,
was in der Konfigurationsdatei in dem Parameter `DEFAULT_ZIP_BACKUP` steht. Damit kann eine
Option in der Befehlszeile ausgeschaltet werden, obwohl sie in der
Konfigurationsdatei eingeschaltet ist.

Zu den meisten Aufrufoptionen gibt es zugehörige Optionen in der Konfigurationsdatei(en)
`/usr/local/etc/raspiBackup.conf`. Ausserdem können weitere Konfigurationsdateien
genutzt werden um selektiv bestimmte Optionen zu setzen oder zu überschreiben.

## Konfigurationsdateien

<a name="configfiles"></a>
Neben `/usr/local/etc/raspiBackup.conf` gibt es weitere Konfigurationsdateien,
die, sofern vorhanden, gelesen werden. Die höchste Priorität haben die Optionen,
die bei dem Aufruf mitgegeben werden.

Die Priorität der Optionsquellen ist aus folgender Tabelle ersichtlich:

| Priorität | Quelle |
|-----------|--------|
| 1         | Aufrufoptionen |
| 2         | -f <configFile> |
| 3         | $(pwd)/.raspiBackup.conf |
| 4         | ~/.raspiBackup.conf |
| 5         | /usr/local/etc/raspiBackup.conf |


**Hinweis:** Optionen in der Konfigdatei, die ja/an oder nein/aus als Parameter
benötigen, müssen 0 für nein und 1 für ja sein.
Kein Eintrag in der Standardspalte bedeutet der Standard ist `""`

[.status]: restructured
