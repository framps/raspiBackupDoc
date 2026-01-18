# Development environment

*raspiBackup* is primarily developed on a Linux desktop, but of course
tested on a real Raspberry. For this purpose there are various
Raspberry Pi OS images created in advance, which are first restored with *raspiBackup
and then tested manually with the new or modified code of *raspiBackup*
After successful testing, a new version of
*raspiBackup* will be made generally available.

In the beginning, all possible test variants were always tested manually.
However, this is quite time-consuming and many SD cards are worn out in the process.
For this reason, the [regression tests](regressiontests-executed.md) are now executed in a [simulated Raspberry](https://www.linux-tips-and-tricks.de/de/raspberryd/22-wie-kann-man-raspberry-pi-unter-kvm-emulieren) running on a Raspberry 5. This is much faster and since then SD no longer breaks so often.

All source code is maintained in a *git* repository. New
releases are created in a development branch. When a new release is ready
to be made generally available and all regression tests have been successfully
completed, the new version is made available as a beta.
This allows *raspiBackup* users to test the new version and provide feedback.
In addition, the beta will be used on *framp*s local Raspberries.
After about 4 weeks the new code will be merged into the *main* branch and the new version
will be published.

*raspiBackup* is open source and therefore all releases are synchronized in [*GitHub*](https://github.com/framps/raspiBackup).
This also includes the development branch, which is synchronized from time to time.

*raspiBackup* writes its git code version (commit sha) in the following message RBK0009I

```
--- RBK0009I: raspifix: raspiBackup.sh V0.6.3.2 (5c98a16) started at Sun Jun 3 09:46:08 CEST 2018
```

The hexadecimal number in brackets (5c98a16 in this example) allows you to view the corresponding
code whenever a problem is reported with *raspiBackup*
and the cause of the problem can be found more easily. That is why it is important,
to mention the message RBK0009I in every problem report.
This also makes it possible to build a hotfix on this code version.
This is usually done and the hotfix is verified before it is included in the next release.

Most issues are managed in [*GitHub*](https://github.com/framps/raspiBackup/issues). For each new release
here on *GitHub*](https://github.com/framps/raspiBackup/releases) a summary of the bugfixes and new functionality.


[.status]: translated
[.source]: https://www.linux-tips-and-tricks.de/de/raspibackupcategoried/516-raspibackup-entwicklungsumgebung
[.source]: https://www.linux-tips-and-tricks.de/en/raspibackupcategorye/517-raspibackup-developmentenvironment

