# Multiple backup tasks

Normally it is sufficient to use a back-up task that can be configured with the installer,
to use. However, there are also scenarios in which several different backups are
different times with different retention values need to be executed.
must be executed.

The *raspiBackup* installer only allows one backup task to be configured. Further
backup tasks must be configured manually. When configuring the *raspiBackup*
options, an additional configuration file can be created and used. If only a few
options are different, these options should be specified at runtime. Otherwise
configuration must be updated manually each time the *raspiBackup* version is updated.
manually. In the following, the name raspiBackup2 is used for the second backuptask.

## Configuration of the first backup task

First, the first back-up task must be initially configured with the installer and further configuration options
must then be adapted in the configuration file. This configuration serves as a template
for the second backuptask.

## Configuration of the second backup task

The following files must be duplicated in the same directory for the second back-up task:

* /etc/systemd/system/raspiBackup.timer
* /etc/systemd/system/raspiBackup.service
* Optional /usr/local/etc/raspiBackup.conf

The files must then be adapted:

raspiBackup.timer must be changed to raspiBackup2.timer.
```
[Timer]
OnCalendar=Sat *-*-* 01:00:00
Unit=raspiBackup2.service
```
The line `OnCalendar` must be defined according to the desired rhythm and time.
Make sure that the syntax corresponds to the Systemd timer format.

The following must then be changed in raspiBackup2.service:

Either another configuration file is specified as follows with the -f option
```
Service]
Type=simple
ExecStart=/usr/local/bin/raspiBackup.sh -f /usr/local/etc/raspiBackup2.conf
```

or further options are defined directly in the call. In the following example
the backup type is changed to tar and the number of backups to 42.

```
Service]
Type=simple
ExecStart=/usr/local/bin/raspiBackup.sh -t tar -k 42
```

The second back-up task must then be activated. To do this
the following commands must be executed:

```
sudo systemctl start raspiBackup2.timer
sudo systemctl enable raspiBackup2.timer
```

**Note**:
If different backup types are used, no second backup directory is required.


