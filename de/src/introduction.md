# Einführung

Eine regelmäßige Sicherung von Raspberry Pis ist wichtig, um im Falle eines
Ausfalls des Systemspeichergerätes (SD-Karte, USB Disk, SSD, NVMe ...) oder auch von
unbeabsichtigten Änderungen, durch die das System nicht mehr oder fehlerhaft bootet,
das System wieder auf einen vorherigen Zustand zurücksetzen zu können.

*raspiBackup* erstellt eine Systemsicherung einer Raspberry Pi **bei laufendem System**.
Siehe dazu [Ist ein Backup eines laufenden Systems zuverlässig und sollte nicht das gesamte System vor dem Backup gestoppt werden ?](faq.md#faq1)
Das kann manuell oder automatisch in regelmäßigen Abständen geschehen.
Ein Backup enthält immer das gesamte System, d.h. Systemdaten sowie Nutzerdaten.
Deshalb bootet das System sofort wieder, wenn es zurückgespielt wurde.
Ein Restore kann immer vollständig vorgenommen werden. Der [partitionsorientierte Backup](normal-or-partition-backup.md#partitionlBackup) unterstützt auch einen vollständigen partitionsweisen Restore. Außerdem unterstützt er bei dem rsync Backuptyp ein Deltarestore, d.h. es werden nur die Änderungen vom letzten Backup zurückgenommen. Dadurch reduziert sich die Restorezeit signifikant.

Zur **Installation und Konfiguration** von *raspiBackup* gibt es einen
[Installer](installation-in-5-minutes.md), mit dem menügesteuert einfach und schnell die wichtigsten
Optionen von *raspiBackup* konfiguriert werden können, vergleichbar mit `raspi-config`.
Speziellere Einstellungen lassen sich in einer Konfigurationsdatei vornehmen.

Alle Funktionen und Einsatzgebiete von *raspiBackup* sind gleich im ersten Kapitel
[Funktionsübersicht](function-overview.md) zusammengetragen.


Weitere Themen auf dieser Seite:

<!-- toc -->


## Einführungsvideo und Youtube-Channel

Es gibt ein [Einführungsvideo zu raspiBackup](https://youtu.be/PuK_FNK674s) auf Youtube.

Behandelte Themen sind

  * Vorstellung von *raspiBackup* mit seinen wichtigsten Fähigkeiten
  * Besuch der wichtigsten Webseiten zu *raspiBackup*
  * Vorstellung von *GitHub* als Fragen- und Probleminteraktionstool
  * Liveinstallation von *raspiBackup* mit dem menügesteuerten Installer

Die dort verwendeten Slides können zum Lesen [hier](https://raspibackup.linux-tips-and-tricks.de/wp-content/uploads/simple-file-list/raspiBackup_de.pdf) heruntergeladen werden.

Viele weitere Videos zu allen möglichen Themen zu *raspiBackup* finden sich im [raspiBackup-Channel](https://www.youtube.com/@raspiBackup).

<a name="contact_options"></a>
## Kontaktmöglichkeiten

* Klicke [![GitHub](images/icons/GitHub-Mark-32px.png)](https://github.com/framps/raspiBackup/issues),
  um auf *GitHub* Fragen oder Probleme zu *raspiBackup* als "Issues" zu erstellen.
  Die Issues können gerne auch in Deutsch erstellt werden.
  So lassen sich Fragen und Problemberichte tracken und man bekommt eine Benachrichtigung über Antworten.
  Das ist die präferierte Kontaktmethode.

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

<a name="haftungsausschluss"></a>
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
[.status]: translated

