# Allgemeine Konfigurationsoptionen

------------------

<!-- toc -->

------------------

**Hinweis:** Optionen in der Konfigdatei, die ja/an oder nein/aus als Parameter
benötigen, müssen 0 für nein und 1 für ja sein. Kein Eintrag in
der Standardspalte bedeutet, der Standard ist `""`

<div class="table-wrapper-for-options">

<a name="backuppath"></a>
### DEFAULT_BACKUPPATH

Diese Konfigurationsvariable definiert das Verzeichnis, in dem die Backups
abgelegt werden.

| Config-Option              | Standard |
|----------------------------|----------|
| DEFAULT_BACKUPATH          | /backup  |

Diese Option kann beim Aufruf von *raspiBackup* überschrieben werden
mit der Option [-p](backup-options.md#parm_p) oder indem am Ende
ein Verzeichnis angegeben wird. (Siehe [Aufruf und Optionen](invocation-options.md)).

### DEFAULT_COLOR_CODES

Hiermit können die html und VT100 Colorcodes definiert werden. Default
ist gelb für Warnungen und Rot für Fehler. Das erste Pärchen der Definition legt
die Codes für Warnung das zweite Pärchen die Definition für Fehler fest. Dabei
ist die erste Definition der HTML Colorcode und die zweite Definition der VT100
Colorcode.

| Config-Option              | Standard |
|----------------------------|----------|
| DEFAULT_COLOR_CODES        | ("#FF8000 33" "#FF0000 31")  |

Siehe [ANSI Colorcodes](https://en.wikipedia.org/wiki/ANSI_escape_code)

### DEFAULT_PUSHOVER_*

*raspiBackup* kann Benachrichtigungen per *Pushover* schicken. Dazu
ist es notwendig, sich auf <https://pushover.net/> registriert zu haben und eine
Application eingerichtet zu haben.

Mit den Notifications definiert man, ob man in Erfolgs- und/oder Fehlerfalle
benachrichtigt werden will. Mögliche Optionen sind "S" für Erfolg (Success)
und/oder "F" für den Fehlerfall (Failure). Mit "M" werden die *raspiBackup*
Meldungen als Datei geschickt.. Es können die Optionen beliebig kombiniert
werden. Beispiel: "SF" oder "SM".

Die Prioritäten entsprechen den verfügbaren *Pushover* Prioritäten.

Die Klänge entsprechen den verfügbaren *Pushover* Klängen.

| Config-Option              | Standard |
|----------------------------|----------|
| DEFAULT_PUSHOVER_TOKEN     | keiner   |
| DEFAULT_PUSHOVER_USER      | keiner   |
| DEFAULT_PUSHOVER_NOTIFICATIONS | keiner |
| DEFAULT_PUSHOVER_SOUND_SUCCESS | keiner     |
| DEFAULT_PUSHOVER_SOUND_FAILURE | keiner     |
| DEFAULT_PUSHOVER_PRIORITY_SUCCESS | keiner  |
| DEFAULT_PUSHOVER_PRIORITY_FAILURE | keiner  |
| DEFAULT_PUSHOVER_ADDITIONAL_OPTIONS | keiner|
| DEFAULT_PUSHOVER_DEVICE             | keiner |


### DEFAULT_SEND_STATS

Es werden beim Versionscheck ein paar *raspiBackup*
Optionen übermittelt, die für [Statistikzwecke](statistics.md) genutzt werden.

| Config-Option              | Standard |
|----------------------------|----------|
| DEFAULT_SEND_STATS         | ja       |

### DEFAULT_SENDER_EMAIL

Die eMailAdresse des Versenders kann bei ssmtp und msmtp angegeben werden.

| Config-Option              | Standard |
|----------------------------|----------|
| DEFAULT_SENDER_EMAIL | root@$(hostname) |


### DEFAULT_SLACK_*

*raspiBackup* kann Benachrichtigungen per *Slack* schicken.

Mit den Notifications definiert man, ob man in Erfolgs- und/oder Fehlerfalle
benachrichtigt werden will. Mögliche Optionen sind "S" für Erfolg (Success)
und/oder "F" für den Fehlerfall (Failure). Mit "M" werden die *raspiBackup*
Meldungen als Datei geschickt. Es können die Optionen beliebig kombiniert
werden. Beispiel: "SF" oder "SM".

| Config-Option               | Standard |
|-----------------------------|----------|
| DEFAULT_SLACK_WEBHOOK_URL   |  keiner  |
| DEFAULT_SLACK_NOTIFICATIONS |  keiner  |

### DEFAULT_TELEGRAM_*

*raspiBackup* kann Benachrichtigungen per *Telegram* schicken.

Mit den Notifications definiert man, ob man in Erfolgs- und/oder Fehlerfalle
benachrichtigt werden will. Mögliche Optionen sind "S" für Erfolg (Success)
und/oder "F" für den Fehlerfall (Failure). Mit "M" werden die *raspiBackup*
Meldungen als Datei geschickt. Es können die Optionen beliebig kombiniert
werden. Beispiel: "SF" oder "SM".

| Config-Option               | Standard |
|-----------------------------|----------|
| DEFAULT_TELEGRAM_TOKEN      | keiner   |
| DEFAULT_TELEGRAM_CHATID     | keiner  |
| DEFAULT_TELEGRAM_NOTIFICATIONS | keiner |
| DEFAULT_TELEGRAM_THREADID      | keiner   | ab Release 7.1.1 |


</div>

[.status]: translated
