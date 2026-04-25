# Notifications 

**raspiBackup** can send notifications when a backup starts or stops. These notifications include all messages logged by **raspiBackup**, and the notification title
indicates the completion status. A notification can also be sent when a backup job finishes.

The following notification destinations are available:

1) eMail - [Sampleconfigurationen](msmtp-configuration-for-web-de-account.md)
2) Pushover - [Configurationoptions](general-config-options.md)
3) Telegram - [Configurationsoptions](general-config-options.md)
4) Slack - [Configurationoptions](general-config-options.md)
5) Any other service via the email extension or the notification extension

The main options for notifications are described [here](general-config-options.md). The email extension and the notification extension are described [here](hooks-for-own-scripts.md).

> [!NOTE]
> Notifications are only sent when **raspiBackup** is running in the background, meaning it is not launched directly from the console.
> If you want to test the notification and its settings, you can use the -F option, which only simulates a backup run—meaning no backup is actually created—but notifications are still sent.

You also have the option to receive notifications only when **raspiBackup** encounters an error. Keep in mind that if **raspiBackup** crashes, it may not be able to send an email.

[.status]: rft "ready for translation. Later: translated"
