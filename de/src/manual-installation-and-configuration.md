# Manuelle Installation und Konfiguration

Die Installation mit dem [Installer](installation-in-5-minutes.md) ist die schnellste Methode.
Man kann auch per Befehlszeile *raspiBackup* sehr schnell in einer Standardinstallation installieren.
Wer *raspiBackup* aber aus verschiedenen Gründen manuell installieren möchte, findet im Folgenden die notwendigen Schritte:

Voraussetzungen: Login als Benutzer `pi` ins Home-Verzeichnis und eine aktive Netzwerkverbindung.

1. Der *raspiBackup* Installer wird in `/usr/local/bin` auf der Raspberry
   downloaded und aufgerufen. Dabei wird *raspiBackup* mit seinen
   Standardoptionen installiert. Anschließend kann man *raspiBackup* mit
   `sudo raspiBackupInstallUI` aufrufen und die Standardkonfiguration ändern.

   [.status]: todo "Stimmt das so bzgl. /usr/local/bin???"
   [.status]: todo "Und wieso steht das überhaupt hier im Abschnitt zur manuellen Installation???"

   ```
    curl -sSLO https://www.linux-tips-and-tricks.de/raspiBackupInstallUI.sh; sudo bash ./raspiBackupInstallUI.sh -i
    ```

2. *raspiBackup* kann man auch manuell downloaden und installieren.

   1. Download der notwendigen Dateien:
      ```
      curl -sSLO https://www.linux-tips-and-tricks.de/raspiBackup.sh
      curl -sSLO https://www.linux-tips-and-tricks.de/raspiBackupInstallUI.sh
      curl -sSL https://www.linux-tips-and-tricks.de/raspiBackup_de.conf > raspiBackup.conf
      ```

   2. Jetzt müssen die Dateien in die entsprechenden Verzeichnisse kopiert und Ownership und Zugriffsrechte angepasst werden:
      ```
      # Verschieben der Dateien in die richtigen Verzeichnisse
      sudo mv raspiBackup.sh /usr/local/bin
      sudo mv raspiBackupInstallUI.sh /usr/local/bin
      sudo mv raspiBackup.conf /usr/local/etc

      # Anpassen der Ownership und Zugriffsrechte
      sudo chown root:root /usr/local/bin/raspiBackup.sh
      sudo chmod 755 /usr/local/bin/raspiBackup.sh
      sudo chown root:root /usr/local/etc/raspiBackup.conf
      sudo chmod 600 /usr/local/etc/raspiBackup.conf

      # Erstellen der Shortcuts ohne .sh am Ende
      sudo ln -s /usr/local/bin/raspiBackup.sh /usr/local/bin/raspiBackup
      sudo ln -s /usr/local/bin/raspiBackupInstallUI.sh /usr/local/bin/raspiBackupInstallUI
      ```

   3. Nun kann der Installer mit `sudo raspiBackupInstallUI` aufgerufen werden und *raspiBackup* konfiguriert werden.

3. Anschließend sollte ein Restore eines Backups vorgenommen werden,
   um sich mit der Art, wie das Backup zu restoren ist, vertraut zu machen und das
   Backup zu testen. Es ist nichts ärgerlicher, wenn man zu dem Zeitpunkt, wenn
   man das Backup benötigt, feststellt, das das Backup nicht alles enthält oder
   sogar nicht brauchbar ist.

Will man *raspiBackup* auf einem System installieren, welches keinen
Internetzugang hat, muss man *2.1* auf einem System ausführen, welches eine
Internetverbindung hat. Danach sind die Dateien auf das Zielsystem zu kopieren
und dort *2.2* und *2.3* auszuführen. Allerdings muss man berücksichtigen, dass dann
keine Benachrichtigungen geschickt werden können wie auch keine
Benachrichtigungen von *raspiBackup* bei neuen Versionen erhalten werden.

[.status]: rst
[.source]: https://www.linux-tips-and-tricks.de/de/raspibackupcategoried/538-raspibackup-manuelle-installation
[.source]: https://www.linux-tips-and-tricks.de/en/raspibackupcategorye/539-raspibackup-manual-installation

