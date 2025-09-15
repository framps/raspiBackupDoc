# nullmailer configuration

To send e.g. status mails from *raspiBackup* as root, *nullmailer* can be used.

The following variables are used in the description (provider is Hetzner):

  - eMail Domain: MYDOMAIN (e.g. dummy.de)
  - Hostname of the server: HOSTNAME (e.g. myserver)
  - smtp Hostname to deliver emails: SMTP_PROVIDER_HOST (e.g. mail.your-server.de)
  - Userid to send emails: SMTP_INPUT_USERNAME
  - Password to send emails: SMTP_INPUT_PASSWORD


## Changes or additions:

- Installation of mail: `sudo apt install mailutils -y`
- `/etc/nullmailer/remotes`:
  ```
  SMTP_PROVIDER_HOST smtp --auth-login --user=SMTP_INPUT_USER --pass=SMTP_INPUT_PASSWORD --ssl
  ```

If the host name is not a valid host name at the e-mail provider, the following steps are necessary:

- Install and configure [Nullmailer Rewrite Wrapper](https://github.com/JsBergbau/nullmailer-Rewrite-Wrapper).
   Set `NULLMAILER_USER=SMTP_INPUT_USER` and `NULL_MAILER_HOST=MYDOMAIN` in "sendmail".
- `sudo chown 700 /usr/sbin/sendmail`



[.status]: translated
[.source]: https://www.linux-tips-and-tricks.de/de/raspibackupcategoried/675-nullmailer-konfigurieren


