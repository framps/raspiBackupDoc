# nullmailer Konfiguration

Um z.B. Statusmails von *raspiBackup* als root zu versenden, kann *nullmailer* eingesetzt werden.

Folgende Variablen werden in der Beschreibung genutzt (Provider ist Hetzner):

  - eMail Domain: MYDOMAIN (z.B. dummy.de)
  - Hostname des Servers: HOSTNAME (z.B. myserver)
  - smtp Hostname, um eMails abzuliefern: SMTP_PROVIDER_HOST (z.B. mail.your-server.de)
  - Userid, um emails zu senden: SMTP_INPUT_USERNAME
  - Password, um emails zu senden: SMTP_INPUT_PASSWORD


## Änderungen bzw. Einfügungen:

- Installation von mail: `sudo apt install mailutils -y`
- `/etc/nullmailer/remotes`:
  ```
  SMTP_PROVIDER_HOST smtp --auth-login --user=SMTP_INPUT_USER --pass=SMTP_INPUT_PASSWORD --ssl
  ```

Falls der Hostname kein gültiger Hostname beim eMailProvider ist, sind noch folgende Schritte nötig:

- [Nullmailer Rewrite Wrapper](https://github.com/JsBergbau/nullmailer-Rewrite-Wrapper) installieren und konfigurieren.
   Dabei `NULLMAILER_USER=SMTP_INPUT_USER` und `NULL_MAILER_HOST=MYDOMAIN` in "sendmail" setzen.
- `sudo chown 700 /usr/sbin/sendmail`



[.status]: rst
[.source]: https://www.linux-tips-and-tricks.de/de/raspibackupcategoried/675-nullmailer-konfigurieren
