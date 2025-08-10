# Aufruf und Optionen

[.status]: review-comment "Der Dateiname 'details.md' ist zu nichtssagend"

*raspiBackup* muss als Benutzer *root* oder per `sudo` aufgerufen werden.

```
raspiBackup Option1 Option2 Option3 ... Backupverzeichnis
```

Alle Optionen, die etwas ein- oder ausschalten, können durch
ein angehängtes `+` oder `-` beim Aufruf von *raspiBackup* gezielt ein- oder ausgeschaltet werden.

Beispiel: Die Option `-z` sowie die Option `-z+` schaltet die Backupcompression ein.
Mit der Option `-z-` wird dagegen die Backupcompression ausgeschaltet, und zwar unabhängig davon,
was in der Konfigurationsdatei in dem Parameter `DEFAULT_ZIP_BACKUP` steht. Damit kann eine
Option in der Befehlszeile ausgeschaltet werden, obwohl sie in der
Konfigurationsdatei eingeschaltet ist.

Zu den meisten Aufrufoptionen gibt es zugehörige Optionen in der Konfigurationsdatei
`/usr/local/etc/raspiBackup.conf`. Außerdem können weitere Konfigurationsdateien
genutzt werden, um selektiv bestimmte Optionen zu setzen oder zu überschreiben.

<a name="configFiles"></a>
## Konfigurationsdateien

<a name="configfiles"></a>
Neben `/usr/local/etc/raspiBackup.conf` gibt es weitere Konfigurationsdateien,
die, sofern vorhanden, gelesen werden. Die höchste Priorität haben die Optionen,
die bei dem Aufruf mitgegeben werden.

Die Priorität der Optionsquellen ist aus folgender Tabelle ersichtlich:

```
| Priorität | Quelle |
|-----------|--------|
| 1         | Aufrufoptionen |
| 2         | -f \<configFile\> |
| 3         | $(pwd)/.raspiBackup.conf |
| 4         | ~/.raspiBackup.conf |
| 5         | /usr/local/etc/raspiBackup.conf |
```

**Hinweis:**
Optionen in der Konfigurationsdatei, die ja/an oder nein/aus als Parameter
benötigen, müssen 0 für nein und 1 für ja sein.
Kein Eintrag in der Standardspalte bedeutet, der Standard ist `""`

**Hinweis:**
Bei einem Versionsupgrade wird nur die Standardkonfigurationsdatei
`/usr/local/etc/raspiBackup.conf` mit
neuen Konfigurationsoptionen aktualisiert. Alle anderen Konfigurationsdateien
müssen gegebenenfalls manuell aktualisiert werden.

Es existieren für den Backup- und Restore-Aufruf verschiedene Optionen:

1. Aufrufoptionen sowie deren Konfigurationsoption ([Backup](backup.md) / [Restore](restore.md)).
   Die Konfigurationsoptionen können durch die entsprechenden Aufrufoptionen temporär
   überschrieben werden
1. Reine Konfigurationsoptionen, die nicht per Aufrufoption überschrieben werden können
   ([Backup](backup-config-options.md) / [Restore](restore-config-options.md))
1. Allgemeine Aufruf- und Konfigurationsoptionen sowohl für den Backup
   als auch den Restore ([Aufrufoptionen](general.md))

## Hilfetext auf der Konsole

Sofern man sich auf der Konsole bewegt, kann eine Liste der
verfügbaren Aufrufoptionen sowie deren aktuellen Status mit den
Optionen `-h` oder `--help` ausgegeben werden.

## Thematische Liste von Aufruf-Optionen

Eine Liste der Aufruf-Optionen ist auch [thematisch sortiert vorhanden](options-by-topic.md).

[.status]: rst
