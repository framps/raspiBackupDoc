# Manual installation and configuration

Installation with the [Installer](installation-in-5-minutes.md) is the fastest method.
You can also install *raspiBackup* very quickly in a standard installation using the command line.
However, if you want to install *raspiBackup* manually for various reasons, you will find the necessary steps below:

Prerequisites: Login as user `pi` to the home directory and an active network connection.

1. the *raspiBackup* installer is downloaded and started in `/usr/local/bin` on the Raspberry
   and called. Thereby *raspiBackup* is installed with its
   installed with its standard options. You can then start *raspiBackup* with
   `sudo raspiBackupInstallUI` and change the default configuration.

   ```
    curl -sSLO https://www.linux-tips-and-tricks.de/raspiBackupInstallUI.sh; sudo bash ./raspiBackupInstallUI.sh -i
    ```

2. you can also download and install *raspiBackup* manually.

   1. download the necessary files:
      ```
      curl -sSLO https://www.linux-tips-and-tricks.de/raspiBackup.sh
      curl -sSLO https://www.linux-tips-and-tricks.de/raspiBackupInstallUI.sh
      curl -sSL https://www.linux-tips-and-tricks.de/raspiBackup_de.conf > raspiBackup.conf
      ```

   2. now the files must be copied into the corresponding directories and ownership and access rights must be adjusted:
      ```
      # Move the files to the correct directories
      sudo mv raspiBackup.sh /usr/local/bin
      sudo mv raspiBackupInstallUI.sh /usr/local/bin
      sudo mv raspiBackup.conf /usr/local/etc

      # Customize ownership and access rights
      sudo chown root:root /usr/local/bin/raspiBackup.sh
      sudo chmod 755 /usr/local/bin/raspiBackup.sh
      sudo chown root:root /usr/local/etc/raspiBackup.conf
      sudo chmod 600 /usr/local/etc/raspiBackup.conf

      # Create the shortcuts without .sh at the end
      sudo ln -s /usr/local/bin/raspiBackup.sh /usr/local/bin/raspiBackup
      sudo ln -s /usr/local/bin/raspiBackupInstallUI.sh /usr/local/bin/raspiBackupInstallUI
      ```

   3. now the installer can be called with `sudo raspiBackupInstallUI` and *raspiBackup* can be configured.

3. a restore of a backup should then be carried out,
   to familiarize yourself with how to restore the backup and to test the backup.
   test the backup. There is nothing more annoying if, at the time when you need the backup
   you need the backup, you realize that the backup does not contain everything or is even
   even unusable.

If you want to install *raspiBackup* on a system that does not have
Internet access, you must run *2.1* on a system that has an Internet connection.
Internet connection. Then copy the files to the target system
and run *2.2* and *2.3* there. However, you must bear in mind that
no notifications can be sent and no notifications from
notifications from *raspiBackup* for new versions.

[.status]: translated
[.source]: https://www.linux-tips-and-tricks.de/de/raspibackupcategoried/538-raspibackup-manuelle-installation
[.source]: https://www.linux-tips-and-tricks.de/en/raspibackupcategorye/539-raspibackup-manual-installation



