# Language support for languages other than DE and EN (L10N)

*raspiBackupInstallUI* and *raspiBackup* initially printed messages in German and English only.
But both are able to print messages in any language from a coding point of view (I18N).
Anybody who is willing to help to add support for a yet unsupported language is welcome
to translate *raspiBackup* messages.

``` admonish info title="Note"
Don't hesitate if you're willing to add a new language to *raspiBackup* even you don't have any programming experience.
You don't have to fiddle with the programming stuff. You have only
to translate all messages into your native language. You even don't have
to create a PR to get the new language into *raspiBackup*. All this programming stuff will be handled by *raspiBackup* developers for you.
```

Just add your interest in an [issue on *GitHub*](https://github.com/framps/raspiBackup/issues) and
you will immediate get individual support to add new messages in your native language
to raspiBackupInstallUI and *raspiBackup*.

Right now following languages are supported:

  - ZH - Chinese
  - EN - English
  - FI - Finnish
  - FR - French
  - DE - German

## Basic activities to add a new language to *raspiBackup*

There exist two files printing messages: `raspiBackup` and `raspiBackupInstallUI`.

Following steps have to be done to support a new language to them:

1. For every message a new line for the new language has to be added to the code. Example for FI:

   ```
   MSG_RUNASROOT=2
   MSG_EN[$MSG_RUNASROOT]="RBK0002E: $MYSELF has to be started as root. Try 'sudo %s%s'."
   MSG_DE[$MSG_RUNASROOT]="RBK0002E: $MYSELF muss als root gestartet werden. Benutze 'sudo %s%s'."
   MSG_FI[$MSG_RUNASROOT]="RBK0002E: $MYSELF tulee käynnistää root-oikeuksin. Suorita 'sudo %s%s'."
   ```

   The line starting with `MSG_FI` was added in order to support Finnish.
   `FI` are the first two characters of the variable $LANG on a system which uses `FI` as system language.

   Example for a German system:
   ```
   echo $LANG
   de_DE.UTF-8
   ```
   and that's why `MSG_DE` is used.

1. The help text in *raspiBackup* may optionally also be translated.
   For every language a bash function `usageLL()` may be created which has to follow bash syntax.
   Just use the existing function `usageEN` as a template.

1. To enable the new language the following line in the code has to be updated:
   ```
   SUPPORTED_LANGUAGES=("EN" "DE")
   ```
   To enable Finnish the line has to be changed changed to
   ```
   SUPPORTED_LANGUAGES=("EN" "DE" "FI")
   ```

[.de]: ../../de/src/local-language-support-for-languages-other-than-de-and-en-l10n.md

[.source]: https://linux-tips-and-tricks.de/en/raspibackupcategoried/603-raspibackup-local-language-support-for-languages-other-than-de-and-en-l10n
[.source]: https://linux-tips-and-tricks.de/de/raspibackupcategoried/603-raspibackup-local-language-support-for-languages-other-than-de-and-en-l10n
