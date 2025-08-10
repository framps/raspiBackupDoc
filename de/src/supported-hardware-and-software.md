# Unterstützte Hardware und Software

<center>

![raspiBackup icon](images/icons/Icon_rot_blau_final_128.png)
</center>

*raspiBackup* wird nur auf Raspberry Pi Hardware mit dem *Raspberry Pi OS* und *Ubuntu*
unterstützt. Es läuft aber auch auf anderer Raspberry Pi kompatibler Hardware und
anderen Linux Distributions erfolgreich. Dabei ist zu beachten, dass *raspiBackup* die
beiden Partitionen `/boot` und `/root` benötigt, wie sie bei *Raspberry Pi OS* existieren.

D.h. man kann *raspiBackup* auf dem jeweiligen Environment ausprobieren und wenn
es erfolgreich läuft, kann man sich freuen und es nutzen. Wenn es aber nicht
läuft bzw. Fehlermeldungen bringt, wird **kein** Support gegeben. Man kann einen
Issue in *GitHub* erstellen und das Debuglog beifügen. So kann *framp* prüfen, ob vielleicht mit ein
paar kleinen Änderungen das Problem beseitigt werden kann. Sind größere Änderungen notwendig,
werden diese nicht vorgenommen und somit kann *raspiBackup* in dem Environment nicht genutzt werden.
Aber auch wenn ein Fix das Problem beseitigt, bleibt das Environment nicht unterstützt.

Insbesondere kann meist ein beliebiges Linux OS auf einer beliebigen Hardware genutzt werden,
um ein Backup zu restoren. Auch hier ist dann die Option `--unsupportedenvironment`
notwendig. Sollte es doch Probleme geben, muss eine Raspberry zum Restore genutzt werden.

Unter der Tatsache, dass **raspiBackup ~~umsonst~~ gratis** ist, ist es zu teuer/zu aufwändig für *framp*,

 1) sich alle mögliche Hardware für die Tests anzuschaffen
 1) alle mögliche Hardware- und Softwaretestkombinationen aufzubauen
 1) jeweils alles bei einer neuen Release zu testen

Also kann *framp* *raspiBackup* nur unter den genannten Voraussetzungen unterstützen.

Es besteht die Möglichkeit der [Donation](introduction.md#donation)
und je nach Aufwand besteht die Chance, dass zukünftig weitere
Environments von *raspiBackup* unterstützt werden.

*raspiBackup* prüft beim Aufruf, ob eine unterstützte Hard- und Software vorliegt
und beendet sich ansonsten. Mit der Option `--unsupportedEnvironment` wird diese
Prüfung nicht vorgenommen und führt u.U. zu Fehlern und Programmabbrüchen.

## Raspberry Pi OS (RaspbianOS) Lite und Desktop

Sowohl *Raspberry Pi OS* (früher *RaspbianOS*) *Lite* als auch *Desktop* werden
von *raspiBackup* unterstützt.
Die Desktop Version sollte wenigstens auf einem RPi4/RPi5 mit 4GB Speicher genutzt werden.

## Ubuntu

Sofern die offizielle Ubuntuversion für Raspberries genutzt wird, ist diese
von *raspiBackup* unterstützt. Es sollte aber wenigstens eine Raspberry Pi 4 mit 4GB, besser noch
mit 8GB Speicher, genutzt werden. Selbiges trifft für einen Raspberry Pi 5 zu. Vermutlich
sind die Anforderungen an ein Ubuntu Server System geringer.

## Raspberry Pi Compute Module (CM)

*raspiBackup* unterstützt Raspberry Pi Computemodule
mit einer SD Karte, eMMC Speicher und NVMe.

Wie man CM4 NVMe Devices auf Linux verfügbar macht, um ein NVMe Backup von *raspiBackup* zu restoren,
ist der [englischsprachigen Seite](https://www.linux-tips-and-tricks.de/en/raspberrye/614-raspberry-compute-module-4-setup-guide) beschrieben.

## Unterstützte Geräte

*raspiBackup* unterstützt folgende Geräte und Speicher

  - SD Karten
  - Platten/HDDs
  - SSDs
  - USB Sticks
  - USB SD Adapter
  - eMMC Speicher
  - NVMe Speicher

Als Backupziel für die Backups kann prinzipiell alles genutzt werden,
was unter Linux mountbar ist. Dazu gehören u.A.

  - SMB Netzwerklaufwerke
  - NFS Netzwerklaufwerke
  - SSHFS Netzwerklaufwerke
  - WebDAV Netzwerklaufwerke
  - FtpFS Netzwerklaufwerke

Auf [Backupziele](backup-targets.md) finden sich Beispiele für SMB, NFS und WebDAV Konfiguration.

[.source]: https://linux-tips-and-tricks.de/de/raspibackupcategoried/608-unterstuetzte-hard-und-software/
[.source]: https://www.linux-tips-and-tricks.de/en/raspibackupcategorye/609-supported-hard-and-software/
[.status]: rst
