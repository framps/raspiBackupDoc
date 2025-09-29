# Statistics

 *raspiBackup* checks at every startup, but at most once a day, whether there is a new release or a beta available
 and then informs you with a message so that an upgrade can be
 planned and carried out. During this check
 information is also transmitted, which makes it possible to collect general
 usage data of *raspiBackup* and to get an overview of the respective usage.

The information that is transmitted is

  - Release
  - Backup type
  - Backup mode
  - Backup or restore call
  - Keep
  - Parameters of the intelligent rotation strategy, if it is used
  - OS: *Raspberry Pi OS* or *Ubuntu*

Sending the above information can be disabled with the option

```
DEFAULT_SEND_STATS=0
```

in the configuration file `/usr/local/etc/raspiBackup.conf`.

[.status]: translated
[.source]: https://www.linux-tips-and-tricks.de/de/raspibackup#stats

