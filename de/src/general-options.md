# Allgemeine Optionen

<div class="table-wrapper-for-options">

------------------

<!-- toc -->

------------------

<a name="parm_A"></a>
### -A: Das Laufzeitlog wird bei der eMail Benachrichtigung mitgeschickt

Das Laufzeitlog wird bei der eMail Benachrichtigung mitgeschickt.

| Optionsname | Standard | Im Installer | Konfigurationsname |
|-------------|----------|--------------|--------------------|
| -A | aus |  | DEFAULT_APPEND_LOG |

<a name="parm_coloring"></a>
### --coloring: Kolorierungseinstellungen bei eMails und Konsolmeldungen

Die Meldungen in der eMail sowie auf der Konsole können
koloriert werden. Mögliche Werte sind `C` für Konsole und/oder `M` für eMail.
Falls Postfix als eMail Client genutzt wird, siehe auch Option --eMailColoring.

| Optionsname | Standard | Im Installer | Konfigurationsname |
|-------------|----------|--------------|--------------------|
| --coloring | automatisch |  | DEFAULT_COLORING |

<a name="parm_e"></a>
### -e: eMailAdresse, an die die Benachrichtigung geschickt wird

email Addresse, die eine Status-email sowie die Meldungen des Backuplaufs
zugesendet bekommt

**Achtung**: Die Benachrichtigungsemail wird vom *root* Nutzer gesendet.
D.h. der eMailClient auf dem System muss so konfiguriert werden, dass mit

```
echo "eMail-Text" | sudo mail -s "Betreff" "Empfänger eMail"
```

die eMail erfolgreich gesendet wird.

Mit der Konfigurationsoption DEFAULT_SENDER_EMAIL kann die
Standardsenderadresse  "root@$(hostname)" bei Bedarf geändert werden.

**Hinweis:** Die eMail Benachrichtigung funktioniert nur, wenn ein MTA wie z.B.
nullmailer, msmtp, Postfix oder Exim4 entsprechend korrekt konfiguriert wurde.
Für einige eMailClients gibt es [Konfigurationsanleitungen](configuration-examples.md).
Ansonsten ist [FAQ38](faq.md#faq38) zu berücksichtigen.
Die eMailfunktion kann relativ einfach mit der "Fake"-Option -F
getestet werden. Außerdem sind weitere Benachrichtigungsmöglichkeiten wie
*Pushover*, *Slack* oder *Telegram* unterstützt.

| Optionsname | Standard | Im Installer | Konfigurationsname |
|-------------|----------|--------------|--------------------|
| -e | keine | konfigurierbar | DEFAULT_EMAIL |

<a name="parm_E"></a>
### -E: Optionale Parameter für die eMailClientProgramme

Optionale weitere Parameter, die im eMail-Programmaufruf mitgegeben werden. Für
sendEmail muss er z.B. wie folgt aussehen: "-f absender.mail@absenderdomain -s
smtp-server:587 -xu Username -xp Password".

**Achtung**: Die Parameter für `-E` müssen in Anführungszeichen `"` eingeschlossen
sein. Speziell zum Testen der eMail Benachrichtigungsfunktion ist der Parameter
`-F` hilfreich.

**Achtung**: Wenn der Parameter `-l 1` benutzt wird, steht das Password im Log und
sollte vor Verschicken des Logs manuell maskiert werden.

| Optionsname | Standard | Im Installer | Konfigurationsname |
|-------------|----------|--------------|--------------------|
| -E | keine |  | DEFAULT_EMAIL_PARMS |

<a name="parm_eMailColoring"></a>
### --eMailColoring: Steuerung, wo der genutzte eMailClient Colorierungnsinformationen akzeptiert

Standardmäßig wird das eMailColoring über die "Subject" Zeile gesteuert, da
dieser Weg von den meisten eMail Clients genutzt wird. Wenn man aber *Postfix*
als eMail Client benutzt, muss man OPTION als Parameter mitgeben, da *Postfix* das
Coloring mit einer separaten Option steuert.

| Optionsname | Standard | Im Installer | Konfigurationsname |
|-------------|----------|--------------|--------------------|
| --eMailColoring | SUBJECT |  | DEFAULT_EMAIL_COLORING |


<a name="parm_f"></a>
### -f: Angabe einer Konfigurationsdatei

Angabe einer Konfigurationsdatei, die eingelesen wird. Siehe
[alle möglichen Konfigurationsdateien und ihre Einlesereihenfolge](details.md#configFiles).

| Optionsname | Standard | Im Installer | Konfigurationsname |
|-------------|----------|--------------|--------------------|
| -f | None |  | None |

<a name="parm_g"></a>
### -g: Fortschrittsanzeige

Mit dieser Option wird beim Backup und Restore eine Fortschrittsanzeige
angezeigt. Beim `tar` Backup steht keine  Fortschrittsanzeige zur Verfügung.

| Optionsname | Standard | Im Installer | Konfigurationsname |
|-------------|----------|--------------|--------------------|
| -g | None |  | None |

<a name="parm_G"></a>
### -G: Sprache der Meldungen

Festlegung der Sprache der Meldungen. Standard ist die
Systemsprache sofern sie unterstützt wird.
Ansonsten sind alle Meldungen in Englisch.

Eine Liste der unterstützten Sprachen findet sich [hier](language-support.md#supported-languages).

Wer helfen möchte, *raspiBackup* eine weitere Sprache zu geben, ist herzlich eingeladen,
dieses zu tun. Details dazu finden sich [in dieser englischsprachigen Beschreibung](../local-language-support-for-languages-other-than-de-and-en-l10n.md).

| Optionsname | Standard | Im Installer | Konfigurationsname |
|-------------|----------|--------------|--------------------|
| -G | Systemsprache oder EN | konfigurierbar | DEFAULT_LANGUAGE |

<a name="parm_h"></a>
### -h: Hilfe

Ausgabe der Aufrufsyntax mit seinen Parametern

| Optionsname | Standard | Im Installer | Konfigurationsname |
|-------------|----------|--------------|--------------------|
| -h | None |  | None |


<a name="parm_l"></a>
### -l: Loglevel

Definiert, ob ein Debuglog erstellt wird:

- off  -> Es wird kein Debuglog erstellt
- debug -> Es wird ein Debuglog erstellt

**Achtung**: Die Logausgabe kann sensitive Informationen enthalten.
*raspiBackup* maskiert z.B. externe statische IP Adressen, eMailAdressen, Kennwörter für
mount Befehle oder email Server, u.V.m. Es  können aber immer noch sensitive Informationen
im Debuglog enthalten sein, die noch manuell maskiert werden sollten.
Das Debuglog wird immer im Backupverzeichnis abgelegt.
Falls es Fehler gibt und das Backupverzeichnis wieder gelöscht werden wird,
wird das Log vorher in das Home-Verzeichnis des Aufrufers gesichert.

| Optionsname | Standard | Im Installer | Konfigurationsname |
|-------------|----------|--------------|--------------------|
| -l | on |  | DEFAULT_LOG_LEVEL |


<a name="parm_L"></a>
### -L: Verzeichnis wo das Debuglog sowie die Laufzeitmeldungen gespeichert werden

Definiert das Ziel der Logdatei `raspiBackup.log`.

- varlog: Die Logdatei wird in `/var/log/` geschrieben
- backup: Die Logdatei wird in das erzeugte Backup geschrieben
- current: Die Logdatei wird in das aktuelle Verzeichnis geschrieben.
- <Dateiprefix>:  Das Debuglog wird dort mit der Extension `.log` und die
  Messagedatei mit der Extension `.msg` abgelegt.

Beispiel: `/home/pi/raspiBackup`

Am Ende existieren `/home/pi/raspiBackup.log` sowie `/home/pi/raspiBackup.msg`

Im Backupverzeichnis werden keine Logs abgelegt.

| Optionsname | Standard | Im Installer | Konfigurationsname |
|-------------|----------|--------------|--------------------|
| -L | backup |  | DEFAULT_LOG_OUTPUT |

<a name="parm_m"></a>
### -m: Meldungsdetails

Meldungsdetails

- minimal: Nur wichtige Meldungen werden ausgegeben
- detailed: Viele Meldungen über den Fortschritt werden ausgegeben

| Optionsname | Standard | Im Installer | Konfigurationsname |
|-------------|----------|--------------|--------------------|
| -m | minimal | konfigurierbar | DEFAULT_MSG_LEVEL |

<a name="parm_s"></a>
### -s: eMailClientProgramm welches benutzt wird, um die eMail zu verschicken

email Programm, welches benutzt wird {mail|sendEmail|ssmtp|msmtp}.
Für *Postfix* und *nullmailer* muss mail benutzt werden und die mailtools installiert werden.
Für *sendEmail* muss der Parameter -E zusätzlich genutzt werden für weitere
obligatorische Parameter (Siehe [Parameter -E Beschreibung](#parm_E) für Details).

Es kann auch ein eMailPlugin benutzt werden, um eMails zu verschicken. Damit
können beliebige weitere eMailClients in *raspiBackup* eingebunden werden. Der `-s`
Parameter muss dann "mailext" sein. Details zum eMailPlugin siehe [diese Seite](hooks-for-own-scripts.md).

| Optionsname | Standard | Im Installer | Konfigurationsname |
|-------------|----------|--------------|--------------------|
| -s | mail |  | DEFAULT_MAIL_PROGRAM |

<a name="parm_S"></a>
### -S: Unbedingtes Update

Ein Update mit der Option `-U` wird auch vorgenommen, wenn die Versionen
übereinstimmen. Sie bewirkt, dass sowohl eine lokale Betaversion wie auch eine
lokale normale Version mit dem aktuellen Codestand ersetzt wird. Primär ist
sie dafür gedacht, den Codestand einer existierenden lokalen Betaversion zu
aktualisieren.

| Optionsname | Standard | Im Installer | Konfigurationsname |
|-------------|----------|--------------|--------------------|
| -S | aus |  |  |

<a name="parm_timestamps"></a>
### --timestamps: Alle Meldungen werden mit einem führenden Zeitstempel ausgegeben

Durch diese Option wird vor jeder Meldung ein Zeitstempel ausgegeben.

| Optionsname | Standard | Im Installer | Konfigurationsname |
|-------------|----------|--------------|--------------------|
| --timestamps | aus |  | DEFAULT_TIMESTAMPS |

<a name="parm_U"></a>
### -U: Update von *raspiBackup*

Die lokale *raspiBackup* Version wird durch die letzte aktuelle Version ersetzt,
sofern eine neue Version existiert. Die vorherige Version wird als
`raspiBackup.sh.n.m` gesichert, wobei `n` und `m` die Versionsnummer von *raspiBackup*
ist. Siehe Parameter `-V`, um eine vorhergehende Version wiederherzustellen.

**Achtung**: Vorher sollte man [diese Seite](version-history.md) lesen
und sich über die Änderungen und Neuerungen informieren.

Zusätzlich gibt es noch die Option `-S`, mit der Betaversionen auf den letzten
Stand gebracht werden können.

Mit der Option `-V` kann auf eine ältere Version zurückgegangen werden.

| Optionsname | Standard | Im Installer | Konfigurationsname |
|-------------|----------|--------------|--------------------|
| -U | aus |  |  |

<a name="parm_updateConfig"></a>
### --updateConfig: Update der *raspiBackup* Konfiguration

Mit dieser Option kann man ein Update der Konfiguration
erzwingen, falls sie nicht bei einem normalen Update mit der
Option `-U` vorgenommen wurde.

| Optionsname | Standard | Im Installer | Konfigurationsname |
|-------------|----------|--------------|--------------------|
| --updateConfig | aus |  |  |

<a name="parm_unsupportedEnvironment"></a>
### --unsupportedEnvironment: Nicht unterstützte HW und SW wird akzeptiert

Wird *raspiBackup* auf nicht [unterstützten Umgebungen](supported-hardware-and-software.md)
gestartet, ist diese Option anzugeben.

| Optionsname | Standard | Im Installer | Konfigurationsname |
|-------------|----------|--------------|--------------------|
| --unsupportedEnvironment | aus |  |  |

<a name="parm_version"></a>
### --version: Anzeige der Versionsinformation

Die Version von *raspiBackup* wird im folgenden Format ausgegeben:

```
Version: 0.6.3.2 CommitSHA: 8fbcd1a CommitDate: 2018-02-19 CommitTime: 19:18:31#
```

| Optionsname | Standard | Im Installer | Konfigurationsname |
|-------------|----------|--------------|--------------------|
| --version | aus |  |  |

<a name="parm_v"></a>
### -v: Alle Meldungen des verwendeten Backuptools werden protokolliert

Die verwendeten Backuptools `tar` und `rsync` zeigen detaillierte Informationen an
(Verbose mode). Die Option ist besonders nützliche bei initialen manuellen
Backuptests, um den Backupfortschritt verfolgen zu können.

| Optionsname | Standard | Im Installer | Konfigurationsname |
|-------------|----------|--------------|--------------------|
| -v | aus |  | DEFAULT_VERBOSE |


<a name="parm_V"></a>
### -V: Reaktivierung einer vorhergehenden *raspiBackup* Version

Es wird eine Liste aller existierenden Vorgängerversionen angezeigt und man
kann die Version auswählen, die wiederhergestellt werden soll. Die aktuelle
Version wird gesichert und kann dann auch mit dieser Option später
wiederhergestellt werden (Siehe auch `-U` Parameter)

| Optionsname | Standard | Im Installer | Konfigurationsname |
|-------------|----------|--------------|--------------------|
| -V | None |  | None |

<a name="parm_y"></a>
### -y: Kopie der aktuellen *raspiBackup* Version auf vordefinierte lokale Hosts per scp

Mit dieser Option wird das aktuelle Script auf alle Hosts kopiert, die in der
Konfigurationsdatei definiert sind. Der Zugriff muss per `authorized_keys` ohne
Kennwort möglich sein. Somit lässt sich *raspiBackup* schnell auf einer größeren
Menge von Hosts nach einem Versionsupdate verteilen.

| Optionsname | Standard | Im Installer | Konfigurationsname |
|-------------|----------|--------------|--------------------|
| -y | None |  | DEFAULT_DEPLOYMENT_HOSTS |

</div>

[.status]: rst
