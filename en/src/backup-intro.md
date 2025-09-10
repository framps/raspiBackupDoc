# Backup introduction

In normal backup mode, *raspiBackup* always creates a complete backup of the system.
In partition-oriented backup mode, the partitions to be backed up can be selected.

If *raspiBackup* has just been installed and configured, we recommend
create and test the first backups from the command line.
Only then should the automatic backup be configured.

When configuring the notifications by e-mail or the other push services
it is very helpful to use the `-F` option, as this does not create a backup, but only sends the notifications.
only the notifications are sent. This means that misconfigurations can be recognized quickly and
can be rectified without always having to wait for a longer backup run to be completed.
always having to wait for a longer backup run to complete.

[.status]: translated
