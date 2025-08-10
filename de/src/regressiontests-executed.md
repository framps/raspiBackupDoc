# Regressionstests vor einem neuen Release

Jede neue Version von *raspiBackup* wird vor der Veröffentlichung einem
Regressionstest unterzogen. Bedingt durch die vielen Optionen und möglichen
Hardware- und Softwareumgebungen ist leider kein vollständiger Regressionstest
möglich. Es wird aber dadurch sichergestellt, dass die Primärfunktionalität
von *raspiBackup*, für die verschiedenen Backuptypen und -modi ein
Backup zu erstellen, definitiv erfolgreich durchläuft. Auch werden alle
neuen Features, obwohl sie natürlich schon beim Entwickeln getestet wurden, noch
einmal getestet.

Der Regressionstest wird in einer virtualisierten Umgebung auf einem Linux
Desktop, in der eine [Raspi per Qemu](https://linux-tips-and-tricks.de/de/raspberryd/22-wie-kann-man-raspberry-pi-unter-kvm-emulieren) simuliert wird, durchgeführt.
(Siehe [Entwicklungsumgebung](development-environment.md).)

Als Basis wird ein *RaspbianOS Lite* genommen.
Dieses wird mit den Standardoptionen von *raspiBackup* per
`dd`, `tar` und `rsync` im normalen Modus gesichert, sowohl für ein reines SD
Kartensystem als auch für ein reines USB Bootsystem. Außerdem wird ein `tar` und
`rsync` Backup im partitionsorientierten Modus erstellt.

Danach werden alle jeweiligen Backups mit *raspiBackup* wieder restored, diese
Images per Qemu gestartet und die folgenden Tests durchgeführt:

  - `/boot/cmdline.txt` wird aus der VM per `scp` auf den Host downloaded und geprüft
  - `/etc/fstab` wird aus der VM per `scp` auf den Host downloaded und geprüft
  - IP-Adresse 8.8.8.8 wird in der VM gepinged und getestet, ob der ping erfolgreich war
  - Die Anzahl der aktiven Services des Original Images wird mit verifiziert `service --status-all`

[.status]: review-comment "Sollte das nicht besser an das aktuelle systemd/systemctl angepasst werden??"

Jedem Benutzer von *raspiBackup*, der darüber hinausgehende Optionen benutzt, wird
dringend nahegelegt, nach einem Versionsupgrade von *raspiBackup* Backup und
Restore erneut sorgfältig zu testen. Es wird in diesem Kontext auf den
[Haftungsausschluss](introduction.md#haftungsausschluss) hingewiesen.


[.status]: rst
[.source]: https://www.linux-tips-and-tricks.de/de/raspibackupcategoried/509-raspibackup-ausgefuehrte-regressiontests
[.source]: https://www.linux-tips-and-tricks.de/en/raspibackupcategorye/510-raspibackup-regressiontests-executed
