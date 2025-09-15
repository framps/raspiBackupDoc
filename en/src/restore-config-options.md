# Restore configuration options

Most of the invocation options can also be defined in the configuration file
configuration file. See [Restore options](restore-options.md).

<div class="table-wrapper-for-options">

------------------

<!-- toc -->

------------------

### DEFAULT_RESTORE_EXTENSIONS

As with the backup, *raspiBackup* offers the option of configuring pre and post exits for the restore,
pre and post exits to perform actions before and after the restore.
actions before and after the restore. The syntax is the same as for the backup extensions.

| Config option | Standard |
|----------------------------|----------|
| DEFAULT_RESTORE_EXTENSIONS | none |


### DEFAULT_RESTORE_REMINDER_INTERVAL

Backup Restore Test Reminder Interval (unit: months)

| Config option | Default |
|----------------------------|----------|
| DEFAULT_RESTORE_REMINDER_INTERVAL | 6 |

### DEFAULT_RESTORE_REMINDER_REPEAT

Number of reminders to perform a backup restore test.

| Config option | Default |
|----------------------------|----------|
| DEFAULT_RESTORE_REMINDER_REPEAT | 3 |

### DEFAULT_YES_NO_DEVICES

The call option `-Y` can be used to suppress the yes/no
queries can be suppressed during the restore.

However, as this can cause unintentional deletion of
devices, this option must be used to
by means of a regular expression
to define which restored devices
may be overwritten without a query.

| Config-Option | Default |
|----------------------------|----------|
| DEFAULT_YES_NO_DEVICES | loop |

</div>

[.status]: translated 



