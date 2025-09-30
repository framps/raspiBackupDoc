# General configuration options

------------------

<!-- toc -->

------------------

**Note:** Options in the config file that require yes/on or no/off as parameters
must be 0 for no and 1 for yes. No entry in the
in the default column means the default is `""`

<div class="table-wrapper-for-options">

<a name="backuppath"></a>
### DEFAULT_BACKUPPATH

This configuration variable defines the directory in which the backups are
are stored.

| config option | default |
|----------------------------|----------|
| DEFAULT_BACKUPATH | /backup |

This option can be overwritten when invoking *raspiBackup*
with the option [-p](backup-options.md#parm_p) or by specifying a directory at the end
a directory is specified at the end. (See [invocation and options](invocation-options.md)).

### DEFAULT_COLOR_CODES

The html and VT100 color codes can be defined here. Default
is yellow for warnings and red for errors. The first pair of the definition defines
the codes for warnings and the second pair the definition for errors. Here
the first definition is the HTML color code and the second definition is the VT100
Colorcode.

| Config option | Standard |
|----------------------------|----------|
| DEFAULT_COLOR_CODES | ("#FF8000 33" "#FF0000 31") |

See [ANSI Colorcodes](https://en.wikipedia.org/wiki/ANSI_escape_code)

### DEFAULT_PUSHOVER_*

*raspiBackup* can send notifications via *pushover*. For this
it is necessary to have registered at <https://pushover.net/> and to have set up an
application set up.

With the notifications you define whether you want to be notified in case of success and/or error.
want to be notified. Possible options are "S" for success
and/or "F" in the event of an error (Failure). With "M" the *raspiBackup*
messages are sent as a file. The options can be combined as desired.
can be combined as desired. Example: "SF" or "SM".

The priorities correspond to the available *Pushover* priorities.

The sounds correspond to the available *pushover* sounds.

| Config option | Standard |
|----------------------------|----------|
| DEFAULT_PUSHOVER_TOKEN | none |
| DEFAULT_PUSHOVER_USER | none |
| DEFAULT_PUSHOVER_NOTIFICATIONS | none |
| DEFAULT_PUSHOVER_SOUND_SUCCESS | none |
| DEFAULT_PUSHOVER_SOUND_FAILURE | none |
| DEFAULT_PUSHOVER_PRIORITY_SUCCESS | none |
| DEFAULT_PUSHOVER_PRIORITY_FAILURE | none |
| DEFAULT_PUSHOVER_ADDITIONAL_OPTIONS | none |
| DEFAULT_PUSHOVER_DEVICE | none |


### DEFAULT_SEND_STATS

During the version check, a few *raspiBackup*
options that are used for [statistics purposes](statistics.md).

| config option | default |
|----------------------------|----------|
| DEFAULT_SEND_STATS | yes |

### DEFAULT_SENDER_EMAIL

The e-mail address of the sender can be specified for ssmtp and msmtp.

| Config-Option | Default |
|----------------------------|----------|
| DEFAULT_SENDER_EMAIL | root@$(hostname) |


### DEFAULT_SLACK_*

*raspiBackup* can send notifications via *Slack*.

With the notifications you define whether you want to be notified in case of success and/or error.
you want to be notified. Possible options are "S" for success
and/or "F" for failure. With "M" the *raspiBackup*
messages are sent as a file. The options can be combined as desired.
be combined as desired. Example: "SF" or "SM".

| Config option | Standard |
|-----------------------------|----------|
| DEFAULT_SLACK_WEBHOOK_URL | none |
| DEFAULT_SLACK_NOTIFICATIONS | none |

### DEFAULT_TELEGRAM_*

*raspiBackup* can send notifications via *Telegram*.

With the notifications you define whether you want to be notified in case of success and/or error.
you want to be notified. Possible options are "S" for success (Success)
and/or "F" for failure. With "M" the *raspiBackup*
messages are sent as a file. The options can be combined as desired.
be combined as desired. Example: "SF" or "SM".

| Config option | Standard |
|-----------------------------|----------|
| DEFAULT_TELEGRAM_TOKEN | none |
| DEFAULT_TELEGRAM_CHATID | none |
| DEFAULT_TELEGRAM_NOTIFICATIONS | none |
| DEFAULT_TELEGRAM_THREADID | none | as of Release 7.1.1 |


</div>

[.status]: translated


