# Exim4 Konfiguration

Folgende Variablen werden in der Beschreibung genutzt:

  - eMail Domain: MYDOMAIN (z.B. dummy.de)
  - Hostname des Servers: HOSTNAME (z.B. myserver)
  - smtp Hostname, um eMails abzuliefern: SMTP_PROVIDER_HOST (z.B. mail.your-server.de)
  - Userid, um emails zu senden: SMTP_INPUT_USERNAME
  - Password, um emails zu senden: SMTP_INPUT_PASSWORD

## Änderungen bzw. Einfügungen:

  - `/etc/aliases`: root: HOSTNAME@MYDOMAIN, dann `sudo newaliases`
  - `/etc/mailname`: MYDOMAIN
  - `/etc/hostname`: HOSTNAME.MYDOMAIN
  - `/etc/email-addresses`: root: HOSTNAME@MYDOMAIN
  - `/etc/hosts`: hosts:127.0.1.1 HOSTNAME HOSTNAME.MYDOMAIN
  - `/etc/exim4/update-exim4.conf.conf`

    ```
    dc_eximconfig_configtype='internet'
    dc_other_hostnames='localhost'
    dc_local_interfaces='127.0.0.1 ; ::1'
    dc_readhost='HOSTNAME.MYDOMAIN'
    dc_relay_domains=''
    dc_minimaldns='false'
    dc_relay_nets=''
    dc_smarthost='SMTP_PROVIDER_HOST'
    CFILEMODE='644'
    dc_use_split_config='false'
    dc_hide_mailname='true'
    dc_mailname_in_oh='true'
    dc_localdelivery='mail_spool'
    keep_environment=
    ```

  - `/etc/exim4/passwd.client`

    ```
    SMTP_PROVIDER_HOST:SMTP_INPUT_USERNAME:SMTP_INPUT_PASSWORD
    ```

Um z.B. Statusmails von *raspiBackup* als root zu versenden, kann *nullmailer* eingesetzt werden.


[.status]: rst
[.source]: https://www.linux-tips-and-tricks.de/de/raspibackupcategoried/573-exim4-konfigurieren

