# Benachrichtigungen

**raspiBackup** kann Benachrichtigungen beim Starten und Stoppen eines Backups schicken. Diese enthalten alle Meldungen, die **raspiBackup** schreibt, und der Titel der Benachrichtigung
weist auf den Beendigungsstatus hin. Ebenso kann am Ende eines Backuplaufs eine Benachrichtigung geschickt werden.

Folgende Benachrichtigungsziele sind möglich:

1) eMail - [Beispielkonfigurationen](msmtp-configuration-for-web-de-account.md)
2) Pushover - [Konfigurationsoptionen](general-config-options.md)
3) Telegram - [Konfigurationsoptionen](general-config-options.md)
4) Slack - [Konfigurationsoptionen](general-config-options.md)
5) Jeder beliebige andere Dienst mittels der eMail Erweiterung oder der Benachrichtigungserweiterung

Die hauptsächlichen Optionen für die Benachrichtigungen sind [hier](general-config-options.md) beschrieben. Die eMail Erweiterung sowie die Benachrichtigungserweiterung sind [hier](hooks-for-own-scripts.md) beschrieben.

> [!NOTE]
> Benachrichtigungen werden nur geschickt, wenn **raspiBackup** im Hintergrund läuft, also nicht direkt auf der Konsole gestartet wird.
> Will man die Benachrichtigung sowie deren Einstellungen testen, kann die Option `-F` genutzt werden, die einen Backuplauf nur simuliert, d.h. es wird kein Backup erstellt, aber die Benachrichtigungen werden geschickt.

Außerdem besteht die Möglichkeit, Benachrichtigungen nur zu bekommen, wenn **raspiBackup** auf einen Fehler stößt. Dabei ist zu berücksichtigen, dass **raspiBackup** bei einem harten Abbruch u.U. nicht mehr dazu kommt, eine eMail zu schicken.

[.status]: translated
