# Updates

From time to time a new version of *raspiBackup* is made available for download.
which contains new functions, extensions and small fixes.

This is indicated by *raspiBackup* when it is invoked and in any notification.
You can then use the `-U` parameter to download and activate the latest version.
The current version is saved and can be reactivated at any time using the `-V` parameter.

In the case of minor changes, no new release is made available and you are not notified of the change.
With the options `-U -S` the current code is always
downloaded and activated. Such an update is generally not necessary and should only be carried out
if explicitly requested to do so.

**Note**:
No backup of the currently active *raspiBackup* is created in this case.

Before updating, you should read which changes and new features are included in the new
are included in the new version. This information can be found in the
[Version history](https://github.com/framps/raspiBackup/releases).
Should a serious error be discovered, a new version will be
a new version will be made available immediately.

Each new version is [regression tested before release](regressiontests-executed.md).

## Configuration update

If new options have been introduced in a new release, the
configuration file `/usr/local/etc/raspiBackup.conf` is automatically updated with the new options.
automatically. The details are described [here](configuration-update-when-upgrading-to-a-new-version.md).

[.status]: translated
[.source]: https://linux-tips-and-tricks.de/de/raspibackup#updatestrategie
[.source]: https://linux-tips-and-tricks.de/de/raspibackupcategoried/432-raspibackup-versionshistorie


