# Entscheidungsbaum für Backuptypen

Es gibt verschiedene Backuptypen und eine jede hat ihre Vor- und Nachteile.
Es können unterschiedliche Backuptypen kombiniert werden. Z.B. kann alle
Monate ein Vollbackup mit `tar` erstellt werden und dazwischen wöchentlich ein `rsync` Delta Backup.
Das erfordert aber eine manuelle Konfiguration von *Systemd* Timern und erfordert
gute *Systemd*-Kenntnisse. Der *raspiBackupInstaller* konfiguriert nur genau einen
Backuptypen.

Sämtliche Backuptypen können mit *raspiBackup* vollständig wiederhergestellt
werden.

Ein `dd` Backup erstellt ein in sich konsistentes binäres Abbild des Systems.
Dabei wird immer das ganze Gerät mit dem System gelesen und gesichert. Das bedeutet, dass
auch Daten gesichert werden, die sich nicht geändert haben. Auch bedeutet es,
dass zum Restore das Restoregerät wieder wenigstens so groß sein muss wie das Originalsystem.
Es wird keine Partition in der Größe angepasst. Das bereitet besonders
bei SD-Karten immer wieder Probleme, da die SD-Karten - obwohl z.B. 32GB groß - doch immer
leichte Unterschiede haben und somit ein Restore eines 32GB Systems auf eine andere 32GB SD-Karte
nicht erfolgreich sein kann, da die SD-Karte geringfügig kleiner ist.

Ein `dd` Backup kann unter Windows mit entsprechenden Tools wiederhergestellt werden.

Aber es wird **nicht** empfohlen, den Backuptyp `dd` zu nutzen.
Erklärungen dazu sind in [Warum sollte man dd als Backuptyp besser nicht benutzen?](why-shouldn-t-you-use-dd-as-backup-type.md)
im Detail beschrieben.

Ein `ddz` Backup sichert wie ein `dd` Backup das gesamte System. Diese Methode
belastet die CPU stark, da die Datenmenge reduziert wird. (Es ist ein `dd` Backup
mit eingeschaltetem Zippen mit `-z`). Ein Restore mit Windowstools ist nicht möglich.

Ein `tar` Backup sichert alle auf dem Systemgerät gespeicherten Daten, wobei allerdings das Backup nicht
so groß ist, wie bei einem `dd` Backup, da nur die Daten gesichert werden, die
tatsächlich existieren. Deshalb kann auch ein `tar` Backup auf Geräten
restored werden, die kleiner ist als das Originalgerät. Natürlich nur, sofern alle
gesicherten Daten auf das neue Device passen.

Ein `tgz` Backup sichert das gesamte System, wie ein `tar` Backup. Diese Methode
belastet die CPU stark, da die Datenmenge reduziert wird. (Es ist ein `tar` Backup
mit eingeschaltetem Zippen mit `-z`)

Ein `rsync` Backup sichert außer beim ersten Mal nur die Daten, die sich zum
letzten Backup geändert haben. Durch die Hardlinks des *ext3*/*ext4* Dateisystems
wird dafür gesorgt, dass trotzdem ein konsistenter Stand des Backups vorliegt.
Allerdings werden die Daten nicht komprimiert. Das hat aber wiederum den
Vorteil, dass man sehr gezielt einzelne Dateien ganz einfach per copy aus dem
Backup zurückholen kann. Diese Methode ist sehr schnell, wenn bereits ein
initiales Backup erstellt wurde.

| Typ    | Vollbackup | Backupzeit | Backupgröße | Datenkompression | CPU belastet | Karte belastet | Selektiver Restore möglich | Dateisystem |
|--------|------------|------------|-------------|------------------|--------------|----------------|----------------------------|-------------|
| dd     | ja         | lang       | groß        | nein             | mittel       | hoch           | nein                       | alle, fat32 nur bis 4GB |
| ddz    | ja         | lang       | kleiner     | ja               | ja           | hoch           | nein                       | alle, fat32 nur bis 4GB |
| tar    | ja         | mittel     | mittel      | nein             | nein         | mittel         | ja                         | alle, fat32 nur bis 4GB |
| tgz    | ja         | mittel     | mittel      | ja               | ja           | mittel         | ja                         | alle, fat32 nur bis 4GB |
| rsync  | ja         | kurz mit Hardlinks | klein mit Hardlinks | nein | nein     | kaum           | ja                         | ext3/ext4 |


<a name="decisiontree"></a>

![Entscheidungsbaum](images/decisiontree_de.dia.jpg)

``` admonish info title="Filesysteme"
Die [Vor- und Nachteile der möglichen Filesysteme](which-filesystem-can-be-used-on-the-backup-partition.md) sind zu beachten.

[.status]: rft
[.source]: https://www.linux-tips-and-tricks.de/de/raspibackup#vornach
