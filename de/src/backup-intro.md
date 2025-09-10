# Backup Einführung

*raspiBackup* erstellt im normalen Backupmodus immer ein vollständiges Backup des Systems.
Beim partitionsorientierten Backupmodus können die zu sichernden Partitionen gewählt werden.

Wurde *raspiBackup* gerade frisch installiert und konfiguriert, wird empfohlen,
die ersten Backups von der Befehlszeile zu erstellen und zu testen.
Erst danach sollte der automatische Backup konfiguriert werden.

Bei der Konfiguration der Benachrichtigungen per eMail oder den anderen Pushdiensten
hilft es sehr, die Option `-F` zu nutzen, denn dadurch wird kein Backup erzeugt, sondern
es werden nur die Benachrichtigungen geschickt. So sind Fehlkonfigurationen schnell zu erkennen und
können behoben werden, ohne immer auf die Beendigung eines längeren Backuplaufes
warten zu müssen.

[.status]: rft
