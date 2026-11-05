# Multiple backup tasks

Normally, it is sufficient to use one backup task that can be configured with the installer.
However, there are also scenarios in which several different backups have to be
executed at different times with different retention values.

The *raspiBackup* installer only allows one backup task to be configured. Further
backup tasks must then be configured manually. When configuring the *raspiBackup*
options, an additional configuration file can be created and used. If only a few
options are different, these options should be passed at runtime. Otherwise
every configuration update caused by an update of the *raspiBackup* version has to be applied manually.
In the following, the name raspiBackup2 is used for the second backup task.

## Configuration of the first backup task

First you configure the first backup task with the installer, and further configuration options
must then be adapted in the configuration file. This configuration serves as a template
for the second backup task.

## Configuration of the second backup task

For the second backup task, the following files must be duplicated in the same directory with the name raspiBackup2:

* /etc/systemd/system/raspiBackup.timer
* /etc/systemd/system/raspiBackup.service
* Optional /usr/local/etc/raspiBackup.conf

The files must then be adapted:

Change `raspiBackup.service` to `raspiBackup2.service` in file `raspiBackup2.timer`:

```
[Timer]
OnCalendar=Sat *-*-* 01:00:00
Unit=raspiBackup2.service
```
The line `OnCalendar` must be defined according to the desired rhythm and time.
Make sure that the syntax corresponds to the Systemd timer format.

The following changes must then be made in `raspiBackup2.service`:

Either another configuration file is specified as follows with the `-f` option
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

The second backup task must then be activated. To do this,
the following commands must be executed:

```
sudo systemctl enable raspiBackup2.timer
sudo systemctl start raspiBackup2.timer
```

**Note**:
If different backup types are used, no other backup directory is required.

[.status]: translated
