# Weitere nützliche Hilfsprogramme

Mittlerweile sind verschiedene Hilfsprogramme zu *raspiBackup* entstanden. Diese
sind nicht offiziell unterstützt und als Beispiele für eigene Hilfsprogramme
gedacht und für eigene Anforderungen angepasst werden können.

Sie stehen auf [*GitHub*](https://github.com/framps/raspiBackup/tree/master/helper) zum Download zur Verfügung:

1. **raspiBackupWrapper.sh**: Damit kann man vor und nach dem Aufruf von
   *raspiBackup* verschiedene Dinge erledigen lassen. Der Code mounted schon die
   Backuppartition und unmounted sie, falls sie vorher nicht gemounted war. Es
   ist etwas bash Script Kenntnis notwendig, um das Script dem eigenen Bedarf
   anzupassen.

   **Hinweis**
   Dieses Script entstand, als *raspiBackup* noch keine Erweiterungspunkte hatte. Normalerweise
   reicht es, die vorhandenen [Erweiterungspunkte](hooks-for-own-scripts.md)
   zu nutzen, um die Funktionalität von *raspiBackup* für die eigenen Bedürfnisse zu erweitern.

2. **raspiBackupNfsWrapper.sh**: Es wird von dem Script geprüft, ob ein NFS Server
   verfügbar ist und nur dann *raspiBackup* gestartet. Außer ein paar
   Definitionen des NFS Servers ist nichts anzupassen.

3. **raspiBackupRestore2Image.sh**: Mit diesem Script kann ein tar oder rsync
   Backup, welches in normalen Backupmodus erstellt wurde, in ein dd Backup
   umgewandelt werden. Außerdem wird pishrink benutzt, um die Größe des dd Images
   soweit wie möglich zu minimieren. kmbach hat die Erstellung des Scripts angeregt.
   Das Script erfordert keine Änderungen.

4. **raspiImageMail.sh**: Dieses Script wurde von dem *raspiBackup* Benutzer kmbach
   erstellt, weil er am Ende vom Aufruf von raspiBackupRestore2Image.sh eine eMail
   erhalten wollte. Dazu werden die *raspiBackup* eMail Konfigurationsparameter benutzt.
   Das Script erfordert keine Änderungen.

5. **raspiBackupAndClone.sh**: Dieses Script erstellt eine Backupversion mit *raspiBackup*
   und restored anschließend das aktuelle Backup auf ein angeschlossenes Device. Somit hat
   man nach dem Backup immer ein aktuelles Backupsystem, von welchem man booten kann,
   wenn das Systemdevice korrupt wurde. Nimmt man den partitionsorientierten Backup mit rsync,
   ist der Restore nur eine Synchronisation der Änderungen zum vorherigen Stand und das geht
   wesentlich schneller als ein Vollrestore mit tar oder dd.

   **Hinweis**: Falls das System durch irgendwelche Fehlkonfiguration nicht mehr bootet, hilft das geclonte Backup
   natürlich nicht, denn darin befindet sich dieselbe Fehlkonfiguration. In diesem Falle muss man ein
   älteres noch funktionierendes Backup manuell restoren.

6. **raspiBackupAndJSON.sh**: Wer die von *raspiBackup* erzeugten Meldungen nach dem Backup untersuchen will,
   kann mit diesem Script die Meldungen im JSON Format erzeugen lassen
   und sie dadurch wesentlich einfacher parsen, z.B. mit `jq`.

7. **raspiBackupDialog.sh**: Dieses von [Franjo](https://github.com/franjo-G) erstellte Script ist ein *raspiBackup* vorgeschaltetes
   Script, mit welchem einfacher Backups erstellt und auch restored werden können.
   Details dazu finden sich im Kapitel [raspiBackupDialog - ein komfortables Hilfsscript für raspiBackup](raspibackupdialog-a-convenient-helper-script-for-raspibackup.md).

## Nutzergeschriebene Extensions

Des weiteren gibt es [Extensions](https://github.com/framps/raspiBackup/tree/master/extensions_userprovided),
die von *raspiBackup* Nutzern geschrieben wurden und zur allgemeinen
Verfügung in das *raspiBackup* Repository per PR eingestellt wurden.
Weitere eigene Extensions werden gerne per PR aufgenommen.

[.status]: rst
[.source]: https://www.linux-tips-and-tricks.de/de/raspibackupcategoried/507-raspibackup-nuetzliche-hilfsprogramme
[.source]: https://www.linux-tips-and-tricks.de/en/raspibackupcategorye/508-raspibackup-nuetzliche-hilfsprogramme-2

