# Backup introduction

In normal backup mode, *raspiBackup* always creates a complete backup of the system. 
This includes the first two partitions only (/boot and /root).
In partition-oriented backup mode, any number of partitions can be backed up. 
Which partitions to be back up can be chosen but the first two partitions have to be 
included all the time.

If *raspiBackup* has just been installed and configured, it's recommended
to create and test the first backups from the command line.
Only then should the automatic backup be configured.

When configuring the notifications by e-mail or the other push services
it is very helpful to use the `-F` option, as this does not create a backup, but only sends the notifications.
This means that misconfiguration can be detected quickly and
can be fixed without always having to wait for a longer backup run to be completed.

[.status]: translated
