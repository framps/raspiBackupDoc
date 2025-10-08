# Multiple backup tasks

Normally, it is sufficient to use one back-up task that can be configured with the installer,
to use. However, there are also scenarios in which several different backups are
different times with different retention values need to be executed.
must be executed.

The *raspiBackup* installer only allows one backup task to be configured. Further
backup tasks must then be configured manually. When configuring the *raspiBackup*
options, an additional configuration file can be created and used. If only a few
options are different, these options should be added at runtime. Otherwise
configuration must be updated manually each time the *raspiBackup* version is updated.
manually. In the following, the name raspiBackup2 is used for the second backup task.

## Configuration of the first backuptask

First you configure the first backuptask with the installer and further configuration options
must then be adapted in the configuration file. This configuration serves as a template
for the second backuptask.

## Configuration of the second backuptask

For the second backuptask, the following files must be duplicated in the same directory with the name raspiBackup2:

* /etc/systemd/system/raspiBackup.timer
* /etc/systemd/system/raspiBackup.service
* Optional /usr/local/etc/raspiBackup.conf

The files must then be adapted:

`raspiBackup.servicei``change to i`raspiBackup2.service` in `raspiBackup2.timer`:
```
[Timer]
OnCalendar=Sat *-*-* 01:00:00
Unit=raspiBackup2.service
```
The line `OnCalendar` must be defined according to the desired rhythm and time.
Make sure that the syntax corresponds to the Systemd timer format.

The following changes must then be made in `raspiBackup2.service`:

Either another configuration file is specified as follows with the -f option
```
[Service]
Type=simple
ExecStart=/usr/local/bin/raspiBackup.sh -f /usr/local/etc/raspiBackup2.conf
```

or further options are defined directly in the call. In the following example
the backup type is changed to tar and the number of backups to 42.

```
[Service]
Type=simple
ExecStart=/usr/local/bin/raspiBackup.sh -t tar -k 42
```

The second backuptask must then be activated. To do this
the following commands must be executed:

```
sudo systemctl start raspiBackup2.timer
sudo systemctl enable raspiBackup2.timer
```

**Note**:
If different backup types are used, no other backup directory is required.

[.status]: translated
