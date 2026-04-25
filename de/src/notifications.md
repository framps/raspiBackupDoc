# Benachrichtigungen

**raspiBackup** kann Benachrichtigungen beim Starten und Stoppen eines Backups schicken. Diese enthalten alle Meldungen, die **raspiBackup** schreibt und der Titel der Benachrichtigung
weist auf den Beendigungsstatus hin. Ebenso kann Ende eines Backuplaufs eine Benachrichtigung geschickt werden.

Folgende Benachrichtigungsziele sind möglich:

1) eMail - [Beispielkonfigurationen](http://localhost:3000/msmtp-configuration-for-web-de-account.md)
2) Pushover - [Konfigurationsoptionen](general-config-options.html?highlight=pushover#default_pushover_.md) beschrieben
3) Telegram - [Konfigurationsoptionen](general-config-options.html#default_telegram_.md)
4) Slack - [Konfigurationsoptionen](general-config-options.html#default_slack_.md)
5) Jeder beliebige andere Dienst vermittels der eMailErweiterung oder der Benachrichtigungserweiterung.

Die hauptsächlichen Optionen für die Benachrichtigungen sind [hier](general-config-options.html.md) beschrieben. Die eMail Erweiterung sowie die Benachrichtigungserweiterung ist [hier](hooks-for-own-scripts.md) beschrieben.

[!NOTE]
> Benachrichtigungen werden nur geschickt wenn **raspiBackup** im Hintergrund läuft, also nicht direkt auf der Konsole gestartet wird.
> Will man die Benachrichtigung sowie dessen Einstellungen testen, kann die Option -Fi genutzt werden, die ein Backuplauf nur simuliert, also kein Backup erstellt wird,sowie Benachrichtigungen geschickt werden.

Außerdem besteht die Möglichkeit, Benachrichtigungen nur zu bekommen, wenn **raspiBackup** einen Fehler bekommt. Dabei ist zu berücksichtigen, dass ein harter Abbruch von **raspiBackup** u.U. nicht mehr dazu kommt, eine eMail zu schicken.

[.status]: rft "ready for translation. Later: translated"
