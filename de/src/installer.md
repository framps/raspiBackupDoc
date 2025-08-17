# Installer Aufruf und Optionen

## Aufruf

Wird der Installer `raspiBackupInstallUI` ohne Optionen aufgerufen startet der Installer
mit einem Menu und erlaubt menugesteuert *raspiBackup* zu installieren und zu konfigurieren.

```
sudo raspiBackupInstallUI
```

## Optionen

Mit folgenden Optionen kann der Installer bestimmte Funktionen direkt ohne Menuführung vornehmen:

* -i: Re/Installation von *raspiBackup*
* -e: Re/Installation von den *raspiBackup* Beispielerweiterungen
* -h: Anzeige eines Hilfetextes
* -U: Update vom Installer `raspiBackupInstallUI`
* -u: Deinstallation von *raspiBackup* inklusive Installer
* -t: Nutzung von entweder crond oder systemd als Backuptimer bei Option -i, Default ist systemd

## Deinstallation

Der Installer kann auch wieder deinstalliert werden.
Entweder benutzt man den Installer zum Deinstallieren oder folgenden Befehl:

```
sudo raspiBackupInstallUI -u
```

**Hinweis:**
Dabei wird der Installer wie auch *raspiBackup* mit all seinen Dateien gelöscht.

## Aufruf des Installers ohne Menus direkt von der Befehlszeile

Wer keine menugesteuerte Installation haben möchte kann die Installation von *raspiBackup*,
den Beispielextensions oder die Deinstallation von *raspiBackup*
von der Befehlszeile direkt aufrufen. Dabei wird die Standardkonfiguration installiert.
Der Aufruf dazu ist

```
curl https://raspibackup.linux-tips-and-tricks.de/install | sudo bash -s -- -i
```

Jedwede Änderungen an der Konfiguration können nun manuell mit einem Editor
vorgenommen werden.
Ebenso das Einschalten des wöchentlichen Backup per systemd Timer.
Man kann aber auch den Installer mit seinen Menus benutzen, um die
Konfiguration der primären Optionen anzupassen sowie den regulären Backup ein-
oder auszuschalten.

## Menudetails

<a name="backupversionen"></a>
### Backupversionen - Menu C3

*raspiBackup* bietet zwei verschiedene Möglichkeiten an, Backupversionen
vorzuhalten:

1. Eine *maximale Anzahl von Backups* die für jeden Backuptyp behalten wird (Option -k).
   In der Konfigurationsdatei kann für jeden Backuptyp noch einmal die Anzahl
   definiert werden (Option --keep\<Type\>).
   Wird die Anzahl überschritten wird das älteste Backup gelöscht.

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

*raspiBackup* bietet die Möglichkeit vor dem Backup Services automatisch zu stoppen und anschließend
wieder zu starten. Alle im Installer vorselektierten Services sollten immer gestoppt werden.
Da nicht auszuschliessen ist, dass auch weitere Services auf dem System wichtige Daten
im Speicher halten und vor dem Backup gestoppt werden sollten, muss die Liste der nicht
vorselektierten aber aktiven Services aufmerksam kontrolliert werden und im Bedarfsfall diese
Services auch noch selektiert werden damit sie vor dem Backup gestoppt werden.

Nach der Selektion der Services, die gestoppt werden sollen, muss noch die Reihenfolge
definiert werde in der sie gestoppt werden sollen. I.A. spielt die Reihenfolge
keine Rolle, aber wenn ein Service Abhängigkeiten zu einem anderen Service hat sollte
der Service erst nach dem abhängigen Service gestoppt werden. Beispielsweise
sollten alle Services, die mit einer Datenbank arbeiten, vor dem Stoppen der Datenbank
gestoppt werden, damit sie noch offene Transaktionen beenden können.

<a name="regularbackup"></a>
### Regelmäßiger Backup - Menu C9

*raspiBackup* bietet die Möglichkeit regelmäßig automatisch Backups zu erstellen.
Dieses erfolgt standardmäßig per systemd, kann aber auch mit der Option `-t`
beim Installieren des Installers auf cron umgestellt werden.

Im Installer kann der Wochentag definiert werden an dem ein Backup erstellt
werden soll oder auch täglich. Außerdem muss die Zeit des Backups in Stunde
und Minute definiert werden. Der Standard ist Sonntag um 05:00 Uhr.

[.status]: rst
