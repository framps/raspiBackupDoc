# General options

<div class="table-wrapper-for-options">

------------------

<!-- toc -->

------------------

<a name="parm_A"></a>
### -A: The runtime log is sent with the eMail notification

The runtime log is sent with the eMail notification.

| Option name | Default | In Installer | Configuration name |
|-------------|----------|--------------|--------------------|
| -A | off | no | DEFAULT_APPEND_LOG |

<a name="parm_coloring"></a>
### --coloring: Coloring settings for eMails and console messages

The messages in the eMail and on the console can
be colored. Possible values are `C` for console and/or `M` for eMail.
If Postfix is used as eMail client, see also option `--eMailColoring`.

| Option name | Default | In Installer | Configuration name |
|-------------|----------|--------------|--------------------|
| --coloring | automatic | no | DEFAULT_COLORING |

<a name="parm_e"></a>
### -e: eMail address to which the notification will be sent

eMail address that receives a status eMail and the messages of the backup run.

**Attention**: The notification eMail is sent by the *root* user.
I.e. the eMail client on the system must be configured so that with

```
echo "eMail-Text" | sudo mail -s "Subject" "Recipient eMail"
```

the eMail is sent successfully.

With the configuration option DEFAULT_SENDER_EMAIL the default sender address
"root@$(hostname)" can be changed if required.

**Note:** The eMail notification only works if an MTA such as
nullmailer, msmtp, Postfix or Exim4 has been configured correctly.
For some eMail clients there are [configuration instructions](configuration-examples.md).
Otherwise [FAQ38](faq.md#faq38) should be taken into account.
The eMail function can be tested relatively easily with the "Fake"
option `-F`. In addition, other notification options such as
*Pushover*, *Slack* or *Telegram* are supported.

| Option name | Default | In Installer | Configuration name |
|-------------|----------|--------------|--------------------|
| -e | none | configurable | DEFAULT_EMAIL |

<a name="parm_E"></a>
### -E: Optional parameters for the eMail client programs

Optional additional parameters that are specified in the eMail program call. For
sendEmail, for example, it must look like this: "-f sender.mail@senderdomain -s
smtp-server:587 -xu Username -xp Password".

**Attention**: The parameters for `-E` must be enclosed in quotation marks `"`.
Especially for testing the eMail notification function, the parameter
`-F` is helpful.

**Attention**: If the parameter `-l 1` is used, the password is in the log and
should be masked manually before sending the log.

| Option name | Default | In Installer | Configuration name |
|-------------|----------|--------------|--------------------|
| -E | none | no | DEFAULT_EMAIL_PARMS |

<a name="parm_eMailColoring"></a>
### --eMailColoring: Control where the used eMail client accepts coloring information

By default, eMailColoring is controlled via the "Subject" line, as this
way is used by most eMail clients. However, if you use *Postfix*
as an eMail client, you must specify OPTION as a parameter, as *Postfix* controls the
coloring with a separate option.

| Option name | Default | In Installer | Configuration name |
|-------------|----------|--------------|--------------------|
| --eMailColoring | SUBJECT | no | DEFAULT_EMAIL_COLORING |


<a name="parm_f"></a>
### -f: Specification of a configuration file

Specification of a configuration file that is read in. See
[all possible configuration files and their reading sequence](invocation-options.md#configFiles).

| Option name | Default | In Installer | Configuration name |
|-------------|----------|--------------|--------------------|
| -f | none | no | |

<a name="parm_g"></a>
### -g: Progress bar

This option displays a progress bar during backup and restore.
No progress bar is available for `tar` backups.

| Option name | Default | In Installer | Configuration name |
|-------------|----------|--------------|--------------------|
| -g | none | no | |

<a name="parm_G"></a>
### -G: Language of the messages

Specifies the language of the messages. The default is the
system language if it is supported.
Otherwise, all messages are in English.

A list of supported languages can be found [here](language-support.md#supported-languages).

If you want to help to give *raspiBackup* another language, you are welcome to do so,
Details can be found [in this description](../local-language-support-for-languages-other-than-de-and-en-l10n.md).

| Option name | Default | In Installer | Configuration name |
|-------------|----------|--------------|--------------------|
| -G | System language or EN | configurable | DEFAULT_LANGUAGE |

<a name="parm_h"></a>
### -h: Help

Output of the invocation syntax with its parameters

| Option name | Default | In Installer | Configuration name |
|-------------|----------|--------------|--------------------|
| -h | none | no | |


<a name="parm_l"></a>
### -l: Loglevel

Defines whether a debug log is created:

- off -> No debug log is created
- debug -> A debug log is created

**Caution**: The log output may contain sensitive information.
*raspiBackup* masks e.g. external static IP addresses, eMail addresses, passwords for
mount commands or eMail servers, and much more. However, there may still be sensitive information
contained in the debug log, which should be masked manually.
The debug log is always stored in the backup directory.
If there are errors and the backup directory is deleted again,
the log is saved beforehand in the home directory of the caller.

| Option name | Default | In Installer | Configuration name |
|-------------|----------|--------------|--------------------|
| -l | on | no | DEFAULT_LOG_LEVEL |


<a name="parm_L"></a>
### -L: Directory where the debug log and runtime messages are stored

Defines the destination of the log file `raspiBackup.log`.

- varlog: The log file is written to `/var/log/`
- backup: The log file is written to the backup created
- current: The log file is written to the current directory.
- \<file prefix\>: The debug log is written there with the extension `.log` and the
  message file with the extension `.msg`.

Example: `/home/pi/raspiBackup`

At the end there are `/home/pi/raspiBackup.log` and `/home/pi/raspiBackup.msg`.

No logs are stored in the backup directory.

| Option name | Default | In Installer | Configuration name |
|-------------|----------|--------------|--------------------|
| -L | backup | no | DEFAULT_LOG_OUTPUT |

<a name="parm_m"></a>
### -m: Message details

Message details

- minimal: Only important messages are displayed
- detailed: Many messages about the progress are output

| Option name | Default | In Installer | Configuration name |
|-------------|----------|--------------|--------------------|
| -m | minimal | configurable | DEFAULT_MSG_LEVEL |

<a name="parm_s"></a>
### -s: eMail client program which is used to send the eMail

eMail program which is used {mail|sendEmail|ssmtp|msmtp}.
For *Postfix* and *nullmailer*, mail must be used and mailtools must be installed.
For *sendEmail* the parameter `-E` must also be used for additional
mandatory parameters (see [Parameter -E description](#parm_E) for details).

An eMail extension can also be used to send eMails. With this,
any other eMail clients can be integrated into *raspiBackup*. The `-s`
parameter must then be "mailext". For details on the eMail extension see [this page](hooks-for-own-scripts.md).

| Option name | Default | In Installer | Configuration name |
|-------------|----------|--------------|--------------------|
| -s | mail | no | DEFAULT_MAIL_PROGRAM |

<a name="parm_S"></a>
### -S: Unconditional update

An update with the `-U` option is also carried out if the versions
match. It has the effect that both a local beta version and a
local normal version are replaced with the current code version. It is primarily
intended to update the code version of an existing local beta version.

| Option name | Default | In Installer | Configuration name |
|-------------|----------|--------------|--------------------|
| -S | off | no | |

<a name="parm_timestamps"></a>
### --timestamps: All messages are output with a leading timestamp

This option causes a timestamp to be output before each message.

| Option name | Default | In Installer | Configuration name |
|-------------|----------|--------------|--------------------|
| --timestamps | off | no | DEFAULT_TIMESTAMPS |

<a name="parm_U"></a>
### -U: Update of *raspiBackup*

The local *raspiBackup* version is replaced by the latest version,
if a new version exists. The previous version is saved as
`raspiBackup.sh.n.m`, where `n` and `m` are the version number of *raspiBackup*.
See parameter `-V` to restore a previous version.

**Attention**: You should first read [this page](version-history.md)
and inform yourself about the changes and new features.

There is also the option `-S`, with which beta versions can be updated to the latest
version.

The `-V` option can be used to revert to an older version.

| Option name | Default | In Installer | Configuration name |
|-------------|----------|--------------|--------------------|
| -U | off | no | |

<a name="parm_updateConfig"></a>
### --updateConfig: Update the *raspiBackup* configuration

With this option you can force an update of the configuration
if it has not been updated during a normal update with the
option `-U`.

| Option name | Default | In Installer | Configuration name |
|-------------|----------|--------------|--------------------|
| --updateConfig | off | no | |

<a name="parm_unsupportedEnvironment"></a>
### --unsupportedEnvironment: Unsupported HW and SW are accepted

If *raspiBackup* is started in non-[supported environments](supported-hardware-and-software.md),
this option must be specified.

| Option name | Default | In Installer | Configuration name |
|-------------|----------|--------------|--------------------|
| --unsupportedEnvironment | off | no | |

<a name="parm_version"></a>
### --version: Display the version information

The version of *raspiBackup* is displayed in the following format:

```
Version: 0.6.3.2 CommitSHA: 8fbcd1a CommitDate: 2018-02-19 CommitTime: 19:18:31#
```

| Option name | Default | In Installer | Configuration name |
|-------------|----------|--------------|--------------------|
| --version | off | no | |

<a name="parm_v"></a>
### -v: All messages from the backup tool used are logged

The backup tools `tar` and `rsync` used display detailed information
(verbose mode). This option is particularly useful for initial manual backup tests
in order to be able to track the backup progress.

| Option name | Default | In Installer | Configuration name |
|-------------|----------|--------------|--------------------|
| -v | off | no | DEFAULT_VERBOSE |


<a name="parm_V"></a>
### -V: Reactivation of a previous *raspiBackup* version

A list of all existing previous versions is displayed and you can select the
version to be restored. The current
version is backed up and can then be restored later using this option
(see also `-U` parameter).

| Option name | Default | In Installer | Configuration name |
|-------------|----------|--------------|--------------------|
| -V | none| no | |

<a name="parm_y"></a>
### -y: Copy the current *raspiBackup* version to predefined local hosts via scp

This option copies the current script to all hosts defined in the configuration file.
Access must be possible via `authorized_keys` without a
password. This means that *raspiBackup* can be quickly distributed to a large
number of hosts after a version update.

| Option name | Default | In Installer | Configuration name |
|-------------|----------|--------------|--------------------|
| -y | none | no | DEFAULT_DEPLOYMENT_HOSTS |

</div>

[.status]: translated


