# Mehrere Backuptasks

Im Normalfall reicht es, einen Backuptask, der mit dem Installer konfigurierbar ist,
zu nutzen. Es gibt aber auch Szenarien, in denen mehrere verschiedene Backups zu
unterschiedlichen Zeiten mit unterschiedlichen Aufbewahrungswerten ausgeführt werden
müssen.

Der *raspiBackup* Installer erlaubt nur, einen Backuptask zu konfigurieren. Weitere
Backuptasks sind dann manuell zu konfigurieren. Bei der Konfiguration der *raspiBackup*
Optionen kann eine weitere Konfigurationsdatei erstellt und genutzt werden. Sofern nur wenige
Optionen unterschiedlich sind, sollten diese Optionen zur Laufzeit mitgegeben werden. Ansonsten
muss bei jedem Konfigurationsupdate durch einen Update der *raspiBackup* Version dies manuell
nachgezogen werden. Im Folgenden wird für den zweiten Backuptask der Name raspiBackup2 genutzt.

## Konfiguration des ersten Backuptasks

Zuerst konfiguriert man den ersten Backuptask mit dem Installer, und weitere Konfigurationsoptionen
müssen dann in der Konfigurationsdatei angepasst werden. Diese Konfiguration dient als Vorlage
für den zweiten Backuptask.

## Konfiguration des zweiten Backuptasks

Für den weiteren Backuptask sind folgende Dateien im selben Verzeichnis mit dem Namen raspiBackup2 zu duplizieren:

* /etc/systemd/system/raspiBackup.timer
* /etc/systemd/system/raspiBackup.service
* Optional /usr/local/etc/raspiBackup.conf

Danach ist eine Anpassung der Dateien notwendig:

`raspiBackup.service` ändern in `raspiBackup2.service` in der Datei `raspiBackup2.timer`:

```
[Timer]
OnCalendar=Sat *-*-* 01:00:00
Unit=raspiBackup2.service
```
Die Zeile `OnCalendar` muss entsprechend dem gewünschten Rhythmus und Zeit definiert werden.
Dabei ist darauf zu achten, dass die Syntax dem Systemd Timer Format entspricht.

Anschließend sind folgende Änderungen in `raspiBackup2.service` notwendig:

Entweder wird eine weitere Konfigurationsdatei wie folgt mit der Option `-f` angegeben
```
[Service]
Type=simple
ExecStart=/usr/local/bin/raspiBackup.sh -f /usr/local/etc/raspiBackup2.conf
```

oder es werden weitere Optionen direkt im Aufruf definiert. Im folgenden Beispiel wird
der Backuptyp auf tar und die Anzahl Backups auf 42 geändert.

```
[Service]
Type=simple
ExecStart=/usr/local/bin/raspiBackup.sh -t tar -k 42
```

Anschließend ist die Aktivierung des zweiten Backuptasks notwendig. Dazu
sind folgende Befehle auszuführen:

```
sudo systemctl enable raspiBackup2.timer
sudo systemctl start raspiBackup2.timer
```

**Hinweis**:
Sofern unterschiedliche Backuptypen genutzt werden, ist kein anderes Backupverzeichnis notwendig.

[.status]: translated
