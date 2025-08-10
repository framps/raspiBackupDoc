# Entwicklungsumgebung

*raspiBackup* wird primär auf einem Linux Desktop entwickelt, aber
natürlich auf einer richtigen Raspberry getestet. Dazu gibt es verschiedene
vorab erstellte RaspbianOS Images, die zuerst mit *raspiBackup* restored
und dann mit den neuen bzw. geänderten Funktionen von *raspiBackup*
manuell getestet werden. Nach erfolgreichen Test steht eine neue Version von
*raspiBackup* an, allgemein verfügbar gemacht zu werden.

Zu Anfang wurden immer alle möglichen Testvarianten zu Fuß durchgetestet.
Allerdings ist das ziemlich zeitaufwändig und es werden dabei viele SD Karten
verschlissen. Deshalb werden die [Regressionstests](regressiontests-executed.md) nun in einer auf dem Desktop
[simulierten Raspberry](https://www.linux-tips-and-tricks.de/de/raspberryd/22-wie-kann-man-raspberry-pi-unter-kvm-emulieren) vorgenommen. Das geht wesentlich schneller und seitdem
geht auch nicht mehr so häufig eine SD kaputt.

Sämtlicher Sourcecode wird in einem lokalen *git*-Repository gewartet. Neue
Releases entstehen in einem Development-Branch. Wenn ein neues Release fertig
ist, um es allgemein verfügbar zu machen und alle Regressionstests erfolgreich
durchgelaufen sind, wird die neue Version als Beta verfügbar gemacht.
So  können *raspiBackup* Benutzer die neue Version testen und Feedback geben.
Außerdem wird die Beta auf meinen (*framp*) lokalen Raspberries eingesetzt.
Nach ca. 4 Wochen wird der neue Code in den *main* Branch übernommen und die neue Version
veröffentlicht.

*raspiBackup* ist Open Source und deshalb werden alle Releases im [*GitHub*](https://github.com/framps/raspiBackup) synchronisiert.
Dazu gehört auch der Developmentzweig, der von Zeit zu Zeit synchronisiert wird.

*raspiBackup* schreibt seine git Codeversion (commit sha) in die folgenden Meldung RBK0009I

```
--- RBK0009I: raspifix: raspiBackup.sh V0.6.3.2 (5c98a16) started at Sun Jun  3 09:46:08 CEST 2018
```

Die hexadezimale Zahl in Klammern (5c98a16 in diesem Beispiel) erlaubt, den
dazugehörigen Code anzusehen, wann immer ein Problem mit *raspiBackup* berichtet
wird und die Problemursache kann leichter gefunden werden. Darum ist es wichtig,
die Meldung RBK0009I in jedem Problembericht zu erwähnen.
Außerdem ist es dadurch möglich, auf diesem Codestand einen Hotfix zu bauen.
Das wird in der Regel getan und der Hotfix verifiziert, bevor er in das nächste Release
einfließt.

Die meisten Probleme werden in [*GitHub*](https://github.com/framps/raspiBackup/issues) verwaltet. Für jedes neue Release gibt
es [hier auf *GitHub*](https://github.com/framps/raspiBackup/releases) eine Zusammenfassung der Bugfixes und neuer Funktionalität.


[.status]: rst
[.source]: https://www.linux-tips-and-tricks.de/de/raspibackupcategoried/516-raspibackup-entwicklungsumgebung
[.source]: https://www.linux-tips-and-tricks.de/en/raspibackupcategorye/517-raspibackup-developmentenvironment
