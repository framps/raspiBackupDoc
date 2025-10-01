# Tips for home automation

The following pages provide information on various applications:
Whether and which services should be stopped and started, which special features should be
to be taken into account, whether and which actions should be taken before and after the backup and/or
before and after the restore.

This page is based on feedback from *raspiBackup* users who are familiar with the
respective applications and can describe exactly what to look out for with the
the respective applications. Therefore, feedback on the [*GitHub* discussion page](https://github.com/framps/raspiBackupDoc/discussions)
is very welcome.

## *raspiBackup* Tips for specific applications

### OpenHAB

Works without problems. See [here on the OpenHAB website](https://community.openhab.org/t/usage-of-raspibackup-within-openhabian/145926).


### ioBroker

ioBroker uses ACLs. If you are backing up to a Synology or QNAP connected via NFS,
you must switch off the saving of ACLs so that *rsync* does not abort. See
FAQ24](faq.md#faq24) on how to do this.

If you restore a backup, you can use ioBroker to recreate the missing
ACLs again. You should also stop the ioBroker before the
backup with `systemctl stop iobroker` and restart it after the backup with `systemctl
start iobroker` after the backup. This can be done either directly in the
*raspiBackup* configuration file at DEFAULT_START_SERVICES and
DEFAULT_STOP_SERVICES or you can use the *raspiBackup* installer
and select the ioBroker as the service to be stopped and started. The
installer then generates the corresponding commands in the configuration file.

### FHEM

FHEM does not use ACLs.

FHEM runs as a system service and thus appears in the installer as a service and can be
can simply be selected there with M3->C6, so that FHEM is stopped before the backup
is stopped and restarted at the end.

The following commands are used for manual configuration in the Config:

```
systemctl stop fhem
```
for DEFAULT_STOPSERVICES

resp.
```
systemctl start fhem
```
for DEFAULT_STARTSERVICES


### SmartHomeNG

SmartHomeNG runs as a system service and therefore appears in the installer as a service
and can simply be selected there with M3->C6, so that SmartHomeNG is stopped before
is stopped before the backup and restarted at the end.

If you want to configure it manually in the Config, you should include the following commands:
```
systemctl stop smarthome
```
for DEFAULT_STOPSERVICES

resp.
```
systemctl start smarthome
```

for DEFAULT_STARTSERVICES


[.status]: translated
[.source]: https://linux-tips-and-tricks.de/de/anwendungstipps


