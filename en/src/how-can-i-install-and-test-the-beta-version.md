# How can I install and try out a beta version of *raspiBackup*?

From time to time there is a new version of *raspiBackup*, which contains new
features, enhancements and bug fixes.

Each new version undergoes an automated [regression test](regressiontests-executed.md), which tests the
actual backup and restore functionality. Then the new
functions, enhancements and bug fixes that were already tested during development are
tested during development are verified again manually.

The new version is then made generally available as a beta. This
is recognizable by the smiley `:-D` in front of the email subject.
Now every user of *raspiBackup* has the possibility to test the future new
version with the new functions, enhancements and error corrections
and, in the event of an error, to create a problem record so that the problem can be
problem can be fixed.

Since it is not possible to test all possible system environment conditions,
testing the beta version also helps the community to
make sure that no errors will be in the new version.

The following section describes how to install a beta,
uninstall it again and create problem reports.

Installing the beta is relatively simple. You use

```
sudo raspiBackup -U
```

The current *raspiBackup* version is saved so that you can switch back to the previous version at any time.
This is done with

```
sudo raspiBackup.sh -V
```
whereby the version can be selected from a list of previous versions,
which is then reactivated.

If, contrary to expectations, a problem is discovered, a problem record or issue should be created on [*GitHub*](https://github.com/framps/raspiBackup/issues).
It is very important to check the
output of `sudo *raspiBackup*.sh --version` so that it is clear exactly
which code version is used.

When a new version is available, the creator will be
will be informed via *GitHub* and it can be downloaded again with `sudo *raspiBackup*.sh -U -S`
to download it again and verify the fix.

[.status]: translated
[.source]: https://www.linux-tips-and-tricks.de/de/raspibackupcategoried/594-wie-kann-ich-die-betaversion-installieren-und-ausprobieren
[.source]: https://www.linux-tips-and-tricks.de/en/raspibackupcategorye/595-how-can-i-install-and-test-the-beta-version



