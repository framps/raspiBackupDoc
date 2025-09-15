# Exim4 configuration

The following variables are used in the description:

  - eMail Domain: MYDOMAIN (e.g. dummy.de)
  - Hostname of the server: HOSTNAME (e.g. myserver)
  - smtp Hostname to deliver emails: SMTP_PROVIDER_HOST (e.g. mail.your-server.de)
  - Userid to send emails: SMTP_INPUT_USERNAME
  - Password to send emails: SMTP_INPUT_PASSWORD

## Changes or additions:

  - `/etc/aliases`: root: HOSTNAME@MYDOMAIN, then `sudo newaliases`
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

To send e.g. status mails from *raspiBackup* as root, *nullmailer* can be used.


[.status]: translated
[.source]: https://www.linux-tips-and-tricks.de/de/raspibackupcategoried/573-exim4-konfigurieren



