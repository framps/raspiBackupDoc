# Installer - Aufruf und Optionen

## Aufruf

```
sudo raspiBackupInstallUI {Optionen}
```

Es existieren zwei verschiedene Möglichkeiten den *raspiBackup* Installer `raspiBackupInstallUI`
aufzurufen:

1.  Aufruf ohne Optionen oder mit Option `-t`
    Der Installer startet mit einem Menu über welches *raspiBackup* konfiguriert werden kann.
    Option `-t` steuert ob crond oder systemd genutzt wird.
1.  Aufruf mit Optionen
    Sofern eine andere Option als `-t`genutzt wird führt der Installer die gewählte Funktion
    sofort ohne Menu aus.

## Optionen

Mit folgenden Optionen kann der Installer bestimmte Funktionen direkt ohne Menüführung vornehmen:

* -i: Re/Installation von *raspiBackup*
* -e: Re/Installation von den *raspiBackup* Beispielerweiterungen
* -h: Anzeige eines Hilfetextes
* -U: Update vom Installer `raspiBackupInstallUI`
* -u: Deinstallation von *raspiBackup* inklusive Installer
* -t: Nutzung von entweder crond oder systemd als Backuptimer bei Option -i, Default ist systemd

## Deinstallation

*raspiBackup* und der Installer können auch wieder deinstalliert werden:

```
sudo raspiBackupInstallUI -u
```

**Hinweis:**
Dabei wird der Installer wie auch *raspiBackup* mit all seinen Dateien gelöscht!



## Details zu einigen Menüpunkten

<a name="backupversionen"></a>
### Backupversionen - Menu C3

*raspiBackup* bietet zwei verschiedene Möglichkeiten an, Backupversionen
vorzuhalten:

1. Eine *maximale Anzahl von Backups*, die für jeden Backuptyp behalten wird (Option -k).
   In der Konfigurationsdatei kann für jeden Backuptyp die Anzahl
   definiert werden (Option --keep\<Type\>).
   Wird die Anzahl überschritten, wird das älteste Backup gelöscht.

1. Nutzung der *intelligenten Backupstrategie*. Dabei werden nach einer bestimmten Regel Backups
   der letzten Tage, Wochen, Monate und Jahre vorgehalten. Ältere Backups
   werden jeweils gelöscht. Im Installer wird die Zahl der
   jeweils vorzuhaltenden Backups mit 4 Zahlen definiert. Der Standard ist
   `7 4 12 3`.
 
   1. tägliche Backups (7)
   1. wöchentliche Backups (4)
   1. monatliche Backups (12)
   1. jährliche Backups (3)

   Die intelligente Backupstrategie ist im Detail [hier](smart-recycle.md) beschrieben.


<a name="services"></a>
### Zu stoppende und startenden Services - Menu C6

Da *raspiBackup* keine Speicherinhalte sichert sollten alle Services, die wichtige Informationen
im Speicher halten, vor dem Backup gestoppt werden.

*raspiBackup* bietet die Möglichkeit, vor dem Backup Services automatisch zu stoppen und anschließend
wieder zu starten. Alle im Installer vorselektierten Services sollten immer gestoppt werden.
Da nicht auszuschließen ist, dass auch weitere Services auf dem System wichtige Daten
im Speicher halten und vor dem Backup gestoppt werden sollten, muss die Liste der nicht
vorselektierten aber aktiven Services aufmerksam kontrolliert werden und im Bedarfsfall diese
Services auch noch selektiert werden, damit sie vor dem Backup gestoppt werden.

Nach der Selektion der Services, die gestoppt werden sollen, muss noch die Reihenfolge
definiert werden, in der sie gestoppt werden sollen. I.A. spielt die Reihenfolge
keine Rolle, aber wenn ein Service Abhängigkeiten zu einem anderen Service hat, sollte
der Service erst nach dem abhängigen Service gestoppt werden. Beispielsweise
sollten alle Services, die mit einer Datenbank arbeiten, vor dem Stoppen der Datenbank
gestoppt werden, damit sie noch offene Transaktionen beenden können.


<a name="regularbackup"></a>
### Regelmäßiger Backup - Menu C9

*raspiBackup* bietet die Möglichkeit, regelmäßig automatisch Backups zu erstellen.
Dieses erfolgt standardmäßig per *Systemd*, kann aber auch mit der Option `-t`
beim Installieren des Installers auf *Cron* umgestellt werden.

Im Installer kann der Wochentag definiert werden, an dem ein Backup erstellt
werden soll. Oder auch eine tägliche Sicherung.
Außerdem wird die Zeit des Backups in Stunde und Minute definiert.
Der Standard ist Sonntag um 05:00 Uhr.


## Standardkonfiguration und Ort der Konfigurationsdatei

Der Installer erstellt folgende Dateien:

  - Konfigurationsdatei `/usr/local/etc/raspiBackup.conf`

    In dieser werden folgende Standardwerte eingestellt und können mit dem
    Installer geändert werden. Alle anderen Optionen müssen mit einem Editor
    geändert werden oder mit einer Aufrufoption überschrieben werden.

    | Option               | Einstellung          |
    |----------------------|----------------------|
    | Backuppfad           | /backup              |
    | Backupmode           | normal               |
    | Backuptyp            | rsync                |
    | Sprache              | Sprache des Systems  |
    | Zip                  | nein                 |
    | Meldungsdetail       | normal               |
    | Backupanzahl         | 3                    |
    | Services start       | keine                |
    | Services stop        | keine                |
    | Wöchentlicher Backup | nein                 |
    | Backuptag            | Sonntag              |
    | Backupzeit           | 05:00 Uhr            |

    [Aufruf und Optionen](backup-options.md) sind ausführlich beschrieben.

  - *Systemd timer* Konfiguration `/etc/systemd/system/raspiBackup.timer`

    Diese Datei steuert den Aufruf von *raspiBackup* und im Standardfall ist der
    wöchentliche Backup ausgeschaltet. Er kann aber mit dem Installer eingeschaltet
    werden.

  - *raspiBackup*.sh `/usr/local/bin`

  - *raspiBackupInstallUI.sh* `/usr/local/bin`



## Aufruf der Installation ohne Installer direkt von der Befehlszeile - online

Wer keine menügesteuerte Installation nutzen möchte, kann die Installation von *raspiBackup*
und den Beispielextensions oder die Deinstallation direkt von der Befehlszeile aufrufen.

(Bei dieser Installation wird die Standardkonfiguration installiert.)

```
curl https://raspibackup.linux-tips-and-tricks.de/install | sudo bash -s -- -i
```

Statt `-i` kann jede andere Installeroption mitgegeben werden.

Änderungen an der Konfiguration können nun manuell mit einem Editor vorgenommen werden.
Siehe dazu [Aufruf und Optionen](invocation-options.md). 

Man kann aber auch den Installer mit seinen Menüs benutzen, um die Konfiguration
der primären Optionen anzupassen sowie den regulären Backup ein- oder auszuschalten.

[.status]: rst
