## Weitere Optionen (nur in der Konfigurationsdatei)

<!-- toc -->

**Hinweis:** Optionen in der Konfigdatei, die ja/an oder nein/aus als Parameter
benötigen, müssen 0 für nein und 1 für ja sein. Kein Eintrag in
der Standardspalte bedeutet der Standard ist `""`

<div class="table-wrapper-for-options">

### DEFAULT_BEFORE_STOPSERVICES / DEFAULT_AFTER_STARTSERVICES

Ab Version 0.6.4.3: Die hier definierten Befehle werden vor bzw nach dem Backup
vor bzw nach dem Stoppen von Systemservices (Option -a und -o) ausgeführt.

| Config-Option               | Standard |
|-----------------------------|----------|
| DEFAULT_BEFORE_STOPSERVICES |          |
| DEFAULT_AFTER_STARTSERVICES |          |



### DEFAULT_COLOR_CODES

Ab Version 0.6.7 können die html und VT100 Colorcodes definiert werden. Default
ist gelb für Warnungen und Rot für Fehler. Das erste Pärchen der Definition legt
die Codes für Warnung das zweite Pärchen die Definition für Fehler fest. Dabei
ist die erste Definition der HTML Colorocde und die zweite Definition der VT100
Colorcode.

| Config-Option              | Standard |
|----------------------------|----------|
| DEFAULT_COLOR_CODES        | ("#FF8000 33" "#FF0000 31")  |



### DEFAULT_DD_BACKUP_SAVE_USED_PARTITIONS_ONLY

dd Backups sichern nur den von definierten Partitionen belegten Platz. Dadurch
benötigt eine 32GB SD Karte, die nur eine 8GB Partition definiert hat, für den
Backup nur 8GB und nicht 32GB. Dazu muss aber vermittels gparted oder resize2fs
die root Partition entsprechend verkleinert werden, denn üblicherweise füllt
die root Partition den gesamten Rest der SD Karte aus.

Siehe dazu auch [FAQ16](faq.md#faq16).

| Config-Option              | Standard |
|----------------------------|----------|
| DEFAULT_DD_BACKUP_SAVE_USED_PARTITIONS_ONLY |          |



### DEFAULT_LINK_BOOTPARTITIONFILES

Sich selten ändernde Bootparition Backups werden mit Hardlinks verknüpft, um
Backupspace zu sparen. Voraussetzung: Der Backupspace unterstützt Hardlinks
(ext3/ext4 Filesystem).

| Config-Option              | Standard |
|----------------------------|----------|
| DEFAULT_LINK_BOOTPARTITIONFILES |          |



### DEFAULT_MAIL_ON_ERROR_ONLY

Nur im Fehlerfalle wird eine eMailbenachrichtigung gesendet. Hinweis: Sollte
*raspiBackup* wegen aussergewöhnlicher Umstände abstürzen, kann es durchaus sein,
dass keine eMail gesendet wird.

| Config-Option              | Standard |
|----------------------------|----------|
| DEFAULT_MAIL_ON_ERROR_ONLY |          |



### DEFAULT_PUSHOVER_*

Ab Version 0.6.8 können Benachrichtigungen per Pushover geschickt werden. Dazu
ist es notwendig, sich auf <https://pushover.net/> registriert zu haben und eine
application eingerichtet haben muss.

Mit den Notifications definiert man ob man in Erfolgs- und/oder Fehlerfalle
benachrichtigt werden will. Mögliche Optionen sind "S" für Erfolg (Success)
und/oder "F" für den Fehlerfall (Failure). Mit "M" werden die raspiBackup
Meldungen als Datei geschickt.. Es können die Optionen beliebig kombiniert
werden. Beispiel: "SF" oder "SM".

Die Prioritäten entsprechen den verfügbaren Pushover Prioritäten.

Die Klänge entsprechen den verfügbaren Pushoverklängen.

| Config-Option              | Standard | Bemerkung |
|----------------------------|----------|-----------|
| DEFAULT_PUSHOVER_TOKEN     |          |  |
| DEFAULT_PUSHOVER_USER      |          |  |
| DEFAULT_PUSHOVER_NOTIFICATIONS |      |  |
| DEFAULT_PUSHOVER_SOUND_SUCCESS |      |  |
| DEFAULT_PUSHOVER_SOUND_FAILURE |      |  |
| DEFAULT_PUSHOVER_PRIORITY_SUCCESS |   |  |
| DEFAULT_PUSHOVER_PRIORITY_FAILURE |   |  |
| DEFAULT_PUSHOVER_ADDITIONAL_OPTIONS | |  ab Release 0.7.0 |
| DEFAULT_PUSHOVER_DEVICE             | |  ab Release 0.7.0 |

### DEFAULT_RESTORE_EXTENSIONS

Ab Version 0.6.7 gibt es auch für den Restore wie beim Backup die Möglichkeit,
auch pre und post Exits zu konfigurieren, um vor und nach dem Restore noch
irgendwelche Aktionen vorzunehmen. Die Syntax ist genauso wie für die Backup
Extensions.

| Config-Option              | Standard |
|----------------------------|----------|
| DEFAULT_RESTORE_EXTENSIONS |          |


### DEFAULT_REBOOT_SYSTEM

Mit dieser Option kann ein Reboot des gesicherten Systems am Ende des Backups
konfiguriert werden. 

**Hinweis**: Die Services, die vor dem Backup gestoppt wurdeni, werden nicht wieder
gestartet. Das ist unnötig da sie sowieso beim Neustart gestartet werden.

| Config-Option              | Standard |
|----------------------------|----------|
| DEFAULT_REBOOT_SYSTEM      |    0     |

 

### DEFAULT_RESTORE_REMINDER_INTERVAL

Backup Restore Test Reminder Intervall (Einheit: Monate)

| Config-Option              | Standard |
|----------------------------|----------|
| DEFAULT_RESTORE_REMINDER_INTERVAL | 6 |



### DEFAULT_RESTORE_REMINDER_REPEAT

Anzahl der Erinnerungen, einen Backup Restore Test durchzuführen.

| Config-Option              | Standard |
|----------------------------|----------|
| DEFAULT_RESTORE_REMINDER_REPEAT | 3   |



### DEFAULT_RSYNC_BACKUP_ADDITIONAL_OPTIONS

Backupoptionen, die beim rsync Backup zusätzlich genutzt werden.

**Benutzung auf eigene Gefahr!**

| Config-Option              | Standard |
|----------------------------|----------|
| DEFAULT_RSYNC_BACKUP_ADDITIONAL_OPTIONS |          |




### DEFAULT_RSYNC_BACKUP_OPTIONS

Backupoptionen, die beim rsync Backup genutzt werden.

**Benutzung auf eigene Gefahr!**

| Config-Option              | Standard |
|----------------------------|----------|
| DEFAULT_RSYNC_BACKUP_OPTIONS | --delete -aHAx |



### DEFAULT_SEND_STATS

Ab Version 0.6.6.1 vom 13.2.2022: Es werden beim Versionscheck ein paar *raspiBackup*
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

Ab Version 0.6.8 können Benachrichtigungen per Slack geschickt werden.

Mit den Notifications definiert man ob man in Erfolgs- und/oder Fehlerfalle
benachrichtigt werden will. Mögliche Optionen sind "S" für Erfolg (Success)
und/oder "F" für den Fehlerfall (Failure). Mit "M" werden die raspiBackup
Meldungen als Datei geschickt. Es können die Optionen beliebig kombiniert
werden. Beispiel: "SF" oder "SM".

| Config-Option               | Standard |
|-----------------------------|----------|
| DEFAULT_SLACK_WEBHOOK_URL   |          |
| DEFAULT_SLACK_NOTIFICATIONS |          |

### DEFAULT_TELEGRAM_*

Ab Version 0.6.8 können Benachrichtigungen per TelegraTelegramm geschickt werden.

Mit den Notifications definiert man ob man in Erfolgs- und/oder Fehlerfalle
benachrichtigt werden will. Mögliche Optionen sind "S" für Erfolg (Success)
und/oder "F" für den Fehlerfall (Failure). Mit "M" werden die raspiBackup
Meldungen als Datei geschickt. Es können die Optionen beliebig kombiniert
werden. Beispiel: "SF" oder "SM".

| Config-Option               | Standard |
|-----------------------------|----------|
| DEFAULT_TELEGRAM_TOKEN      |          |
| DEFAULT_TELEGRAM_CHATID     !          |
| DEFAULT_TELEGRAM_NOTIFICATIONS |        | 
| DEFAULT_TELEGRAM_THREADID      |          | ab Release 7.1.1 |


### DEFAULT_TAR_BACKUP_ADDITIONAL_OPTIONS

Backupoptionen, die beim tar Backup zusätzlich genutzt werden.

**Benutzung auf eigene Gefahr!**

| Config-Option              | Standard |
|----------------------------|----------|
| DEFAULT_TAR_BACKUP_ADDITIONAL_OPTIONS |          |



### DEFAULT_TAR_BACKUP_OPTIONS

Backupoptionen, die beim tar Backup genutzt werden.

**Benutzung auf eigene Gefahr!**

| Config-Option              | Standard |
|----------------------------|----------|
| DEFAULT_TAR_BACKUP_OPTIONS | -cpi     |

</div>

[.status]: review-needed
