# Typische Restore Anwendungsbeispiele

Hier werden verschiedene Anwendungsbeispiele von
*raspiBackup* vorgestellt wie man ein Backup zum Restore nutzen kann.
Eine Übersicht aller Optionen findet sich
im Kapitel [Wiederherstellen/Restore](restore.md).

*Hinweis*
In den folgenden Beispielen wird /dev/sda als das Gerät genommen, auf welches restored werden soll.

<!-- toc -->

## Ein System startete nicht mehr weil eine SD Karte unbrauchbar wurde

In diesem Falle muss das gesamte Backup auf eine neue SD Karte restored werden

```
sudo raspiBackup -d /dev/sda <backup>
```

## Ein System startete nicht mehr weil Änderungen am System vorgenommen wurden

In diesem Falle muss das gesamte Backup restored werden wenn ein normaler Backup erstellt wurde. Liegt ein partitionsorientiertes Backup vor geht die Wiederherstellung auf das Systemgerät viel schneller da keine neue Partitionierung vorgenommen wird.

```
sudo raspiBackup -d /dev/sda -00 <backup>
```

In diesem Falle werden nur die Änderungen seit dem Backup zurückgedreht, d.h. neue Dateien werden gelöscht, geänderte Dateien durch die vorherigen Inhalte ersetzt und gelöschte Dateien wiederhergestellt.

## Es wurde ein neues System aufgesetzt und ein paar Konfigurationsdateien sollen wieder den Stand von einem gesicherten System erhalten

Wenn ein dd oder tar Backup vorliegt müssen die Dateien umständlich aus den Backups extrahiert werden. Wurde ein rsync Backup erstellt kann einfach auf die Dateien zugegriffen und sie aufs neue System kopiert werden. Details wie einzelne Dateien kopiert werden können ist [hier](how-to-retrieve-single-files-or-directories-from-the-backup.md) beschrieben.

## Ein System soll auf ein anderes Medium umgezogen werden. Z.B. von SD Karte auf eine SSD

Dazu wird ein Snapshot erstellt (Option -M) und dann das Backup auf das neue Systemgerät restored werden.

```
sudo raspiBackup -M "Systemumzug" <Backupverzeichnis>
sudo raspiBackup -d /dev/sda <Backupverzeichnis>_Systemumzug
```

## Ein System mit einer separaten Datenpartition bootet nicht mehr

Ein Restore der Datenpartition ist nicht notwendig. Es muss nur die Boot- und Systempartition restored werden.

```
sudo raspiBackup -d /dev/sda -T "1 2"
```

Falls nur wenige Änderungen an der Systempartition vorgenommen wurden kann zusätzlich die Option `-00` genutzt werden.

[.status]: translated
[.source]: https://linux-tips-and-tricks.de/de/konfigurationsbeispiele
[.source]: https://www.linux-tips-and-tricks.de/en/configuration-samples

