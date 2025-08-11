
``` admonish info title="Nutzungshinweise"
Oben auf den Seiten befinden sich zwei Icon-Gruppen zur Bedienung
der Dokumentation:

![Menü-links](images/mdbook-icons-left.png)

  - Ein-/Ausblenden eines Inhaltsverzeichnisses
  - Auswahl eines Themes
  - Suchfunktion

![Menü-rechts](images/mdbook-icons-right.png)

  - Sprachauswahl (Deutsch/Englisch)
  - Drucken
  - *GitHub*-Seite des Dokumentationsprojektes
  - Änderungen an der aktuellen Seite im *GitHub* vorschlagen

Eintippen eines `?` blendet eine kleine Tastatur-Navigationshilfe ein.
```

<center>     <!-- The blank line before the image definition is required! -->

![Icon](images/icons/Icon_rot_blau_final_128.png)
</center>

---

Themen auf dieser Seite:

<!-- toc -->

---

# Einführung

Eine regelmäßige Sicherung von Raspberry Pis ist wichtig, um im Falle eines
Ausfalls des Systemspeichergerätes (SD-Karte, USB Disk, SSD, NVMe ...) oder auch von
unbeabsichtigten Änderungen, durch die das System nicht mehr oder fehlerhaft bootet,
das System wieder auf einen vorherigen Zustand zurücksetzen zu können.

*raspiBackup* erstellt eine Systemsicherung einer Raspberry Pi **bei laufendem System**.
Das kann manuell oder automatisch in regelmäßigen Abständen geschehen.
Ein Backup enthält immer das gesamte System, d.h. Systemdaten sowie Nutzerdaten.
Deshalb bootet das System sofort wieder, wenn es zurückgespielt wurde.

Backups können auf alle Geräte, die an Linux gemounted werden können, gesichert
werden. Dazu gehören SD-Karten, USB Sticks, USB Platten, SSDs und NVMe SSDs.
Auch Netzlaufwerke, die per NFS, SMB, SSHFS, FtpFS und WebDAV gemounted werden,
können als Ziel für Backups genutzt werden.

Ein Backup kann auf anderen Geräten zurückgespielt werden, als auf das Gerät, von
dem ein Backup erstellt wurde. Zum Beispiel kann ein Backup einer SD-Karte auf
einer SSD zurückgespielt werden.

Die Anzahl der vorzuhaltenden Backups ist konfigurierbar oder es wird das
[Großvater-Vater-Sohn Generationenprinzip](https://www.framp.de/raspiBackupDoc/de/smart-recycle.md) genutzt.
Außerdem können manuell sogenannte *raspiBackup* [Snapshots](snapshots.md) erstellt werden. Dieses sind Backups, die
nicht automatisch gelöscht werden und dazu dienen, bei Systemupgrades Zwischenschritte zu sichern
um jederzeit bei Fehlern beim Upgrade wieder auf vorherige Stände zurückgehen zu können.

Es gibt zwei [Backupmodi](normal-or-partition-backup.md):
Der **normale Backupmodus** sichert nur die Boot- und Rootpartition.
Der **partitionsorientierte Modus** sichert beliebig viele Partitionen.

Folgende Linux Backuptools können genutzt werden:
`dd`und `tar`, beides auch gezipped, die immer ein Vollbackup erstellen
und `rsync`mit [Hardlinknutzung](how-do-hardlinks-work-with-rsync.md),
um relativ schnell ein Deltabackup zu erstellen.
Die einzelnen Backuptypen sind im Detail [hier](backup-types.md) beschrieben.
Dort befindet sich auch ein [Entscheidungsbaum](backup-types.md#decisiontree),
um schnell den richtigen Backuptyp zu finden.

Zur **Installation und Konfiguration** von *raspiBackup* gibt es einen
[Installer](installation-in-5-minutes.md), mit dem menügesteuert einfach und schnell die wichtigsten
Optionen von *raspiBackup* konfiguriert werden können, vergleichbar mit `raspi-config`.
Speziellere Einstellungen lassen sich in einer Konfigurationsdatei vornehmen.

Für Entwickler bietet *raspiBackup* verschiedene [Erweiterungspunkte](hooks-for-own-scripts.md),
um eigenen Code ausführen zu lassen.

Weiterhin existieren verschiedene [Scripts](https://github.com/framps/raspiBackup/tree/master/helper),
die die Funktionalität von *raspiBackup* erweitern und entweder unverändert genutzt
oder an eigene Anforderungen angepasst werden können.

Am Ende eines Backuplaufes kann *raspiBackup*, wenn gewünscht, eine Benachrichtigung per eMail,
*Telegram*, *Slack* oder *Pushover* senden.

Alle Funktionen und Einsatzgebiete von *raspiBackup* sind tabellarisch in der
[Funktionsübersicht](function-overview.md) zusammengetragen.

## Einführungsvideo und Youtube-Channel

Es gibt ein [Einführungsvideo zu raspiBackup](https://youtu.be/PuK_FNK674s) auf Youtube.

Behandelte Themen sind

  * Vorstellung von *raspiBackup* mit seinen wichtigsten Fähigkeiten
  * Besuch der wichtigsten Webseiten zu *raspiBackup*
  * Vorstellung von *GitHub* als Fragen- und Probleminteraktionstool
  * Liveinstallation von *raspiBackup* mit dem menügesteuerten Installer

Die dort verwendeten Slides können zum Lesen [hier](https://raspibackup.linux-tips-and-tricks.de/wp-content/uploads/simple-file-list/raspiBackup_de.pdf) heruntergeladen werden.

Viele weitere Videos zu allen möglichen Themen zu *raspiBackup* finden sich im [raspiBackup-Channel](https://www.youtube.com/@raspiBackup).

<a name="kontakt"></a>
## Kontaktmöglichkeiten

* Klicke [![GitHub](images/icons/GitHub-Mark-32px.png)](https://github.com/framps/raspiBackup/issues),
  um auf *GitHub* Fragen oder Probleme zu *raspiBackup* als "Issues" zu erstellen.
  Die Issues können gerne auch in Deutsch erstellt werden.
  So lassen sich Fragen und Problemberichte tracken und man bekommt eine Benachrichtigung über Antworten.

* Klicke [![Facebook](images/icons/FB-f-Logo__blue_29.png)](https://www.facebook.com/raspiBackup/),
  um auf Facebook aktuelle Aktivitäten und Randinformationen zu *raspiBackup* zu erfahren.
  Fragen zu *raspiBackup* sind auch möglich. Probleme bitte nur im [*GitHub*](https://github.com/framps/raspiBackup/issues) melden.

* Klicke [![Twitter](images/icons/Twitter-f-Logo__blue_29.png)](https://www.twitter.com/linuxframp),
  um *raspiBackup* auf Twitter zu folgen.

* Klicke [![RaspberryForum](images/icons/RaspberryForumSmall.png)](https://forum-raspberrypi.de/forum/board/153-backup/),
  um im deutschen RaspberryForum Fragen zu Raspberry Backups im Allgemeinen und *raspiBackup* im Speziellen zu stellen oder existierende Threads zu *raspiBackup* zu lesen.

* Klicke [![Reddit](images/icons/reddit-icon.png)](https://www.reddit.com/r/raspiBackup/),
  um *raspiBackup* auf Reddit zu folgen.

``` admonish info title="Hinweis"
Jegliche anderen Kommunikationswege wie z.B. eMails, die leider gerne genutzt werden, werden ignoriert!
```

<a name="donation"></a>
## Trinkgeld

Eine Anerkennung des Entwicklungs- und Wartungsaufwands sowie Supports für
*raspiBackup* ist gerne gesehen und wie folgt möglich:

1. Werde ein [*GitHub* Sponsor](https://github.com/sponsors/framps) für *raspiBackup*
2. Paypal: Die eMail `framp att linux-tips-and-tricks dott de` ist PayPal bekannt
   und ein jeder kann mit einem PayPal Konto an diese eMail ein Trinkgeld geben.
3. Keines von beidem: Einfach bei der o.g. eMail nachfragen. Es findet sich
   gewiss eine Alternative. Z.B. wurde Trinkgeld schon mehrmals auf die
   gute alte Art per Brief zugeschickt :-)

Das Trinkgeld wird primär dazu genutzt, Verbrauchsmaterialien wie SD-Karten, Adapter, Kabel etc.,
die für das Entwickeln und Testen benötigt werden, zu kaufen. Sofern das Trinkgeld ausreicht,
wird damit auch neue Hardware gekauft, um in *raspiBackup* den notwendigen
Hardwaresupport einzubauen und die korrekte Funktionalität
auf der neuen Hardware zu verifizieren.

## Danksagungen

Es haben im Laufe der Zeit sehr viele Leute aus der Community durch Kommentare,
Erweiterungsvorschläge und Beta- und Fixtests zu *raspiBackup* beigetragen.
In Anbetracht der großen Anzahl ist es leider nicht möglich, jeden einzelnen aufzuführen.

Daher einfach: Vielen Dank an alle Unterstützer!

**Besonderer Dank** geht an [simonz](https://github.com/rpi-simonz) für den Aufbau
dieses *raspiBackup* Dokumentationsrepositories in *GitHub*, den Transfer aller
*raspiBackup* Seiten von [framps Homepage](https://www.linux-tips-and-tricks.de)
in dieses Repository und die intensive Unterstützung bei der Überarbeitung
der Seiten mit Rat und Tat sowie mit sehr hilfreichen Tools.

## Lizenz und *GitHub*-Link

Der Code von *raspiBackup* steht unter der GPL auf [*GitHub*](https://github.com/framps/raspiBackup) zur Verfügung.

## Haftungsausschluss

*raspiBackup* wurde für den persönlichen Gebrauch erstellt und, da es sich als sehr nützlich erwies,
der Allgemeinheit zur Verfügung gestellt.

Es wird im Rahmen des Möglichen die korrekte Funktionalität getestet
aber es kann nicht ausgeschlossen werden, dass durch Fehler in
*raspiBackup* die erwartete Funktionalität nicht gewährleistet ist.
Jeder, der *raspiBackup* benutzt, tut das auf sein eigenes Risiko.

Der Ersteller von *raspiBackup* ist in keiner Weise haftbar für
irgendwelche Fehlfunktionen des Scripts.

[.source]: https://www.linux-tips-and-tricks.de/de/raspibackup
[.source]: https://www.linux-tips-and-tricks.de/en/backup
[.source]: https://linux-tips-and-tricks.de/de/trinkgeld
[.status]: rst
