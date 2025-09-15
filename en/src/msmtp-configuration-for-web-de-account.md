# msmtp configuration for a web.de account

The user *gNeadr* from *raspiBackup* had problems setting up the e-mail notification
for his web.de account. After he
successfully managed to configure everything correctly, he fortunately
fortunately offered to publish his installation and configuration steps here
to make it easier for other *raspiBackup* users,
the email configuration for *raspiBackup*.

There is not much to configure in *raspiBackup*.
The difficulty is to configure the eMailClient correctly.

Enclosed are the installation and configuration steps for *gNeandr* -
Once again, thank you very much for providing it.

```
Raspberry Installation 2023-08-20
====================================================
SDCard 64GB microSDXC
 ext4 formatted with gparded on LX
 Label: RXXXX
```


## Install Raspberry Pi OS with Raspberry Pi Imager v.1.7.4

OS: Raspberry PI OS Lite (32-bit) Bullseye from 2023-05-03

SD card: Generic STORAGE_DEVICE (RXXXX) - 63.8GB

Advanced settings:

- Hostname: rasp1
- SSH enabled, name: rasp1 PW: [see keypass]
- Wifi: SSID: [ssid] PW: [see keypass]
- Wifi country: DE
- Language setting: Berlin Keyboard: de

Save ==> WRITE


## Setup for Static LAN with Fritzbox

(see also https://learn.sparkfun.com/tutorials/headless-raspberry-pi-setup/ethernet-with-static-ip-address)

Customize the IF file with LX Terminal on the SDCard (in the card reader):

```
$ ls -lt /media/xxxxx/rootfs/etc/dhcpcd.conf
```

```
interface eth0
static ip_address=192.123.123.xx/24
static routers=192.123.123.1
static domain_name_servers=192.123.123.1
```

Requires access with:
```
sudo nano /media/xxxxx/rootfs/etc/dhcpcd.conf
```

Then eject SDCard in the LX file manager.


## Start and configure Raspberry

Then install the SD card in the Raspberry and start it/connect the power adapter.

Check with Fritzbox, change the name of the 'raspberry' if necessary.

Start Raspberry via SSH with :

```
ssh pi@192.123.123.7X (ip of the Raspberry as configured above)
```

## Configure and update/upgrade Raspberry/RASPIAN OS

To be on the safe side, change the password ...
(see also https://www.raspberrypi.org/documentation/configuration/security.md)
... this is done with the Raspberry Config tool:

```
$ sudo raspi-config
```

Setting e.g:

```
│ 1 Change User Password Change password for the 'pi' user │
│ 2 Network Options Configure network settings │
--> Enter name e.g. 'raspellX'
│ 3 Boot Options Configure options for start-up │
--> B2 Wait for network
│ 4 Localization Options Set up language and regional settings to match your │
--> Locales: de_DE.UTF-8 UTF-8
--> default : en_GB.UTF-8
--> Timezone
--> Keyboard
│ 5 Interfacing Options Configure connections to peripherals │
--> P2 SSH
│ 6 Overclock Configure overclocking for your Pi │
│ 7 Advanced Options Configure advanced settings │
--> A1 Expand Filesystem
│ 8 Update Update this tool to the latest version │
--> update the tool
│ 9 About raspi-config Information about this configuration tool |
```

```
$ sudo apt-get update
$ sudo apt-get upgrade
```

## mSMTP for sending email e.g. from *raspiBackup*

This compilation is based on: <https://goneuland.de/raspberry-pi-e-mails-versenden-mit-msmtp/>

### Installation

```
$ sudo apt-get install msmtp msmtp-mta mailutils
```
```
$ msmtp --version

msmtp version 1.8.11
Platform: arm-unknown-linux-gnueabihf
TLS/SSL library: GnuTLS
Authentication library: GNU SASL; oauthbearer: built-in
Supported authentication methods:
plain scram-sha-1 external gssapi cram-md5 digest-md5 login ntlm oauthbearer
IDN support: enabled
NLS: enabled, LOCALEDIR is /usr/share/locale
Keyring support: Gnome
System configuration file name: /etc/msmtprc <<===
User configuration file name: /home/pi/.msmtprc <<===
Copyright (C) 2020 Martin Lambers and others.
This is free software. You may redistribute copies of it under the terms of
the GNU General Public License <http://www.gnu.org/licenses/gpl.html>.
There is NO WARRANTY, to the extent permitted by law.
```

The lines marked with `<<===` are important for the further mSMTP configuration!


### Create (or adapt) config file for sending with WEB.de

```
$ sudo nano /etc/msmtprc
```

The following listing of "/etc/msmtprc" shows the settings for sending via an
existing EMail account at WEB.de

For your own use, the lines following "# Customize" must be changed with your own values.

In the section "# Authentication methods." different formats are possible for the password specification.
The simplest way (as in the example) is the direct entry of the PW of the mail account ... BUT
this is not the most secure method!
See also: # https://marlam.de/msmtp/msmtp.html#Authentication

```
$ sudo cat /etc/msmtprc

# Set default values for all following accounts.
defaults
# Use the mail submission port 587 instead of the SMTP port 25.
port 587
# Always use TLS.
tls on
# Mail account
# Everything is now configured here for the e-mail account
# Use a name of your choice
account raspi
# Host name of the SMTP server
# Customize
host smtp.web.de
# Envelope-from address
# Customize
from yyyyyy@web.de
# Authentication methods. More information can be found in the msmtp documentation:
# https://marlam.de/msmtp/msmtp.html#Authentication
auth on
# Customize
user yyyyyy@web.de
# Customize
password PxxxxxxxxxxW
# Set a default account
# Enter name from above here again
account default: raspi
```


### Customize rights / access

The next steps adjust the rights of the file.

```
$ sudo chmod 600 /etc/msmtprc
```

Set the e-mail program with "set sendmail":

```
$ sudo nano /etc/mail.rc
```
```
set sendmail="/usr/bin/msmtp -t"
```
```
$ sudo chown pi:pi /etc/msmtprc
$ ls -lt /etc/msmtprc

-rw------- 1 pi pi 566 Aug 19 19:55 /etc/msmtprc
```

### Test of mSMTP for WEB.de

```
$ sudo echo "E-Mail Test" | mail -s "E-Mail Subject" yyyyyy@web.de
```

The WEB.de mail account will then receive this message:

```
Subject: E-Mail Subject: mSMTP TEST
Date: Sun, 20 Aug 2023 14:40:18 0200
From: yyyyyy@web.de
To: yyyyyy@web.de
E-mail test
```

## *raspiBackup* Configuration for sending e-mails with mSMTP

### Customization

The configuration file "raspiBackup.conf" is adapted to the above mSMTP setup
for *raspiBackup* email notifications with:

```
$ sudo nano /usr/local/etc/raspiBackup.conf
```
```
# email to send completion status
DEFAULT_EMAIL="yyyyyy@web.de"
# sender email address used with ssmtp and msmtp
DEFAULT_SENDER_EMAIL="yyyyyy@web.de"
# Additional parameters for email program (optional)
DEFAULT_EMAIL_PARMS=""
# mailprogram
DEFAULT_MAIL_PROGRAM="mail"
```

### Test email notification from *raspiBackup* with mSMTP for WEB.de

```
$ sudo *raspiBackup* -m detailed -F
```

Console output:

```
--- RBK0009I: rasp8: *raspiBackup*.sh V0.6.8 - 2023-08-18 (cbfe5e8) Sun 20 Aug 15:42:40 CEST 2023 started.
--- RBK0116I: Configuration file /usr/local/etc/raspiBackup.conf is used.
!!! RBK0124W: Simulation mode on.
--- RBK0151I: Backup path /media/backup8 with partition type ext4 is used.
!!! RBK0157W: No systemd services are to be stopped.
--- RBK0081I: Backup of type rsync is created in /media/backup8/rasp8/rasp8-rsync-backup-20230820-154237.
--- RBK0078I: Backup time: 00:00:01.
--- RBK0033I: Please wait until cleanup is complete.
--- RBK0159I: 5 backups are kept for the backup type rsync. Please be patient.
--- RBK0017I: Backup completed successfully.
--- RBK0010I: rasp8: *raspiBackup*.sh V0.6.8 - 2023-08-18 (cbfe5e8) Sun 20 Aug 15:42:49 CEST 2023 finished with return code 0.
--- RBK0167I: An e-mail is sent.
--- RBK0026I: Debug log file was saved in /home/pi/raspiBackup.log.
```


The WEB.de mail account receives this message:

```
Subject: rasp8: Backup completed successfully.
Date: Sun, 20 Aug 2023 15:42:50 0200
From: yyyyyy@web.de
To: yyyyyy@web.de
--- RBK0009I: rasp8: *raspiBackup*.sh V0.6.8 - 2023-08-18 (cbfe5e8) Sun 20 Aug 15:42:40 CEST 2023 started.
--- RBK0116I: Configuration file /usr/local/etc/raspiBackup.conf is used.
!!! RBK0124W: Simulation mode on.
--- RBK0151I: Backup path /media/backup8 with partition type ext4 is used.
!!! RBK0157W: No systemd services are to be stopped.
--- RBK0081I: Backup of type rsync is created in /media/backup8/rasp8/rasp8-rsync-backup-20230820-154237.
--- RBK0078I: Backup time: 00:00:01.
--- RBK0033I: Please wait until cleanup is complete.
--- RBK0159I: 5 backups are kept for the backup type rsync. Please be patient.
--- RBK0017I: Backup completed successfully.
--- RBK0010I: rasp8: *raspiBackup*.sh V0.6.8 - 2023-08-18 (cbfe5e8) Sun 20 Aug 15:42:49 CEST 2023 finished with return code 0.
--- RBK0167I: An e-mail is sent.
```

[.status]: translated
[.source]: https://www.linux-tips-and-tricks.de/de/raspibackupcategoried/650-konfiguration-von-raspibackup-mit-msmtp-fuer-einen-web-de-account

