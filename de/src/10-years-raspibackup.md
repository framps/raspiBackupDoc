# 10 Jahre *raspiBackup* (Retrospektive von framp)

Heute (07. August 2023) vor 10 Jahren wurde die erste Version von *raspiBackup*
in meinem lokalen cvs abgelegt.

```
revision 1.1
date: 2013-08-07 21:28:14 +0200; author: framp; state: Exp; commitid: 10052029FC71A98602F;
Initial version
=============================================================================
```

Dieses cvs existiert leider nicht mehr, denn es wäre schon interessant zu sehen,
wie sich das Script in den 10 Jahren verändert hat. Initial waren es um die 50
Codezeilen. Jetzt sind es 8000 Codezeilen.

In der [wayback machine](https://web.archive.org/) habe ich auf dieser Webseite 6/2013 eine
initiale Version von *raspiBackup* gefunden. Ich habe sie auf meiner Webseite als [raspiBackup_201306.sh](https://www.linux-tips-and-tricks.de/raspiBackup/raspiBackup_201306.sh) abgelegt.
Es waren nicht 50 sondern 314 lines of code.

Weihnachten 2013 schenkte mir mein Sohn eine Raspberry. Mit Begeisterung begann
ich, mit ihr zu arbeiten und schnell kam eine zweite Raspberry dazu, die dann
auch in Produktion eingesetzt wurde. Da SD Karten leider nur eine beschränkte
Haltbarkeit haben, entstand *raspiBackup*. Erst nur privat genutzt - aber
nachdem es doch sehr gut seinen Dienst verrichtete, wurde es der Community zur
Verfügung gestellt.

Was dadurch an Aufwand dazu kam, hatte ich unterschätzt: Es ist
ein Unterschied, ob man ein kleines Script selbst schreibt und nutzt, oder es von
anderen Usern genutzt wird. Es mussten sehr viele Tests auf falsche Eingaben
und Systemumgebungen zugefügt werden. Dazu mussten dann auch entsprechende
Fehlermeldungen geschrieben werden. Da die Fehlermeldungen nur kurz sind,
entstanden parallel diverse Webseiten, auf denen die Funktionsweise von
*raspiBackup* beschrieben wird, sowie detailliertere Beschreibungen der
Fehlermeldungen und wie die Fehler beseitigt werden können.

Um die initiale Installation zu vereinfachen, entstand dann der Installer. Bald
fanden sich auch Freunde von *raspiBackup*, die halfen, die Sprachunterstützung
für Finnisch, Chinesisch und Französisch zusätzlich zu Deutsch und Englisch
zuzufügen.

Es gab viel Feedback und Vorschläge von *raspiBackup* Nutzern, was noch
nützliche Features in *raspiBackup* wären. Ohne diese Anregungen der
*raspiBackup* Nutzer würde *raspiBackup* immer noch die initiale Funktion haben,
die ich bei mir @home benötige. Es gab und gibt viele Helfer. Initial hatte
ich mal eine Webseite gepflegt, auf der alle Helfer aufgeführt wurden.
Irgendwann wurde es einfach zu viel und ich habe die Webseite vom Netz
genommen.

Durch diese Hilfe entwickelte sich *raspiBackup* über die 10 Jahre fortwährend
in seinem Funktionsumfang weiter. Zuerst kamen alle Feedbacks über die
Kommentarfunktion auf [meiner Webseite](https://www.linux-tips-and-tricks.de). Das erwies sich aber als sehr
umständlich und schließlich wurde der cvs Code in *GitHub* abgelegt. Dadurch
wurde das Erstellen von Featurerequests wesentlich vereinfacht. Zusätzlich ist
seitdem das Berichten von Fehlern und Fragen zur *raspiBackup* Nutzung
wesentlich einfacher.

Relativ schnell hatte ich mich dann in dem [deutschen Raspberry Forum](https://forum-raspberrypi.de/forum/)
angemeldet. Die Mitglieder dort halfen mir sehr, meine Raspberry kennenzulernen
und zu nutzen. Irgendwann fragte ich dann an, ob es nicht Sinn macht, ein Backup
Subforum zu erstellen, was dann auch getan wurde. Seitdem helfe ich in dem Unterforum
bei Fragen zu *raspiBackup*.

Ich halte eigentlich nicht viel von Videos, sondern präferiere textuelle
Beschreibungen, denn darin kann man suchen. Aber im langweiligen Coronazeitraum
erstellte ich dann doch verschiedene Videos zu *raspiBackup* und publizierte
sie auf [Youtube](https://www.youtube.com/channel/UCnFHtfMXVpWy6mzMazqyINg).
Viel Aufwand habe ich dazu nicht getrieben - im Gegensatz zu
anderen Leuten, die sehr fancy Videos auf Youtube publizieren: Ein paar Slides
erstellt und die wurden dann im Präsentationsmodus erklärt. Später habe ich
dann noch ein paar Videos mit praktischer Nutzung von *raspiBackup* auf der
Befehlszeile erstellt. Aber die Zahl der Leute, die sich die Videos ansieht
wächst. Der Aufwand war also nicht unnütz.

Franjo vom Raspberryforum schrieb ein kleines Tool namens [raspiBackupDialog](https://github.com/framps/raspiBackup/blob/master/helper/raspiBackupDialog.sh), mit
welchem der Backup und Restore mit *raspiBackup* dialoggeführt vorgenommen
werden kann.

Irgendwann erstellte ich auch eine [Facebookgruppe zu *raspiBackup*](https://www.facebook.com/raspiBackup). Initial
konnten mich darüber *raspiBackup* Nutzer direkt kontaktieren. Das wurde mir
dann aber irgendwann zu viel, da es letztendlich zu einem unbezahlten 7/24
Hotlinesupport für *raspiBackup* wurde.

Schließlich habe ich mal ein Paypalkonto eingerichtet, auf welches jeder dem
*raspiBackup* gefällt, [spenden kann](introduction.md#donation). Außerdem kann
jeder als [Sponsor](https://github.com/sponsors/framps) über *GitHub* spenden.

Reich werde ich dadurch natürlich nicht, aber es wird damit die Arbeit erkennbar gewürdigt,
die ich in *raspiBackup* Entwicklung und Support reinstecke.

Auch kann ich damit Test-Hardware kaufen, denn
ich kann und will nicht meine Produktivsysteme stilllegen, um *raspiBackup* zu
testen und zu maintainen. Außerdem bin ich nicht mehr bereit, einen Cent
in benötigte HW für *raspiBackup* zu stecken. *raspiBackup* ist kostenlos
verfügbar und Nutzer sollen sich erkenntlich zeigen und die benötigte HW durch Spenden finanzieren.

Zum Beispiel spendete ein Nutzer ein CM4, damit ich NVMe Support in *raspiBackup* einbauen und testen konnte.

Aus den allgemeinen kleinen Spenden konnte ich einen RPi4 mit 8GB Memory erwerben und den Ubuntu Support in *raspiBackup*
einbauen.

Schließlich hat jemand gespendet, damit ich mir einen RPi5 kaufen konnte. Die Spende gab es, da es ein
auf einem RPi4 nicht reproduzierbares Problem mit [rpi-clone](https://github.com/geerlingguy/rpi-clone) gab.
So konnte ich dann final das intermittierende Problem auf der RPi5 nachvollziehen und fixen.
(*rpi-clone* ist ein nützliches Clonetool - kein Backuptool wie *raspiBackup*, aber oft nachgefragt,
auf welches ich auch ein Auge habe.)

Im Mai 2025 hat [simonz](https://github.com/rpi-simonz/) viel Einsatz und Energie in ein neues git Repository [raspiBackupDoc](https://github.com/framps/raspiBackupDoc) gesteckt,
um die bisherige Dokumentation von *raspiBackup* auf meiner Webseite in dieses Repository zu bringen
und die Dokumentation dadurch wesentlich zu verbessern. Sämtliches Tooling wie auch der Transfer und
Anpassung von meinen Webseiten ins Repository ist sein Verdienst. Dieses Repository und die daraus generierte
[raspiBackup Dokumentation](https://framps.github.io/raspiBackupDoc) wird zukünftig die Dokumentation auf meiner Webseite ablösen.

Zusätzlich entstanden viele [kleine Scripte](https://github.com/framps/raspiBackup/tree/master/scripts), die *raspiBackup* in seiner Nutzung
unterstützen.

Hiermit gebe ich eine virtuelle Runde Freibier zur Feier des Tages aus.


[.status]: rst
[.source]: https://www.linux-tips-and-tricks.de/de/raspibackupcategoried/649-10-jahre-raspibackup
[.source]: https://www.linux-tips-and-tricks.de/en/raspibackupcategorye/657-10-years-raspibackup
