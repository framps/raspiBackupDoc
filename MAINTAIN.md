# Maintainer, Repo-Owner, Webserver-Admin

Zum Aufbau der Markdown-Dateien siehe [EDIT.md](EDIT.md)

## Arbeitsablauf bei automatischer Generierung bei z.B. *GitHub Pages*

  1. Editieren von Markdown-Datei(en), lokal oder im Browser
  1. commit + push
  1. ca. 30 Sekunden warten, bis die neue Doku generiert und deployed wurde

Die generierte Dokumentation ist über folgenden Links (GitHub Pages) zu erreichen:

  - https://framps.github.io/raspiBackupDoc/
  - https://framps.github.io/raspiBackupDoc/de/

Die automatische Generierung wird durch die im Repository enthaltene Datei
`.github/workflows/mdbook.yml` initiiert und gesteuert.

Bei GitHub muss dazu noch in den Einstellungen des Repositories unter
"Build and deployment" ausgewählt werden: "GitHub Actions":

![github-pages-settings](readme-images/m1-github-pages-settings.png)

**Hinweis**: Manchmal (selten) kommt es beim Build in *GitHub Actions* zu einem Abbruch,
der nicht durch Fehler in den Markdown-Dateien zu erklären bzw. durch deren
Behebung zu beseitigen ist. Dann ist es oft hilfreich,
manuell die Caches bei *GitHub Actions* zu löschen.
Der erste dann folgende Build dauert dann natürlich ein paar Minuten länger...

## Ablauf bei Veröffentlichung auf einem (normalen) Webserver


> [!IMPORTANT]
> Voraussetzungen beim lokalen Generieren:
> Die Rust-Umgebung inkl. Compiler `rustc`, `mdbook` und Präprozessoren für `mdbook` müssen installiert sein.
> Siehe [INSTALL.md](INSTALL.md).

  1. lokales Editieren von Markdown-Datei(en)
  1. lokales Generieren der Webseite(n)
     (Zielverzeichnis ist jeweils `book` in den Sprachverzeichnissen.)

     Die Angabe von "en/de" ist erforderlich, weil in diesem Projekt
     die Dokumentation in mehreren Sprachen erzeugt wird,
     deren Quelltexte in eben diesen beiden Unterverzeichnissen liegen.

         mdbook build en     # "en" ist Default und Fallback
         mdbook build de     # "de" ist eine von evtl. mehreren zusätzlichen Übersetzungen

     Testen geht mit einem lokalen Development-Webservice im Browser: http://localhost:3000  
     Da `mdbook serve` bei jeder Änderung der Quelldateien intern ein 'build' aufruft,
     kann **lokal nur jede Sprache einzeln** getestet werden.

         mdbook serve en

     beziehungsweise

         mdbook serve de

  1. Hochladen der Webseite zu einem Webserver

     Hier eine mögliche Variante mit `lftp`:

     **Hinweis**: Beim Upload die Reihenfolge und Zielverzeichnisse der Sprachen beachten, "en" ist Default und damit Erster!

         lftp sftp://${WEBSERVER} -e "cd ${WEBSERVER_ROOTDIR} ; rm -r raspiBackupDoc; mirror -R en/book raspiBackupDoc; cd raspiBackupDoc ; mirror -R de/book de ; put data/htaccess -o .htaccess ; dir ; quit"

     Details zur Konfiguration des Webservers am Beispiel *Apache* siehe [README-apache.md](README-apache.md)

  1. commit + push


> [!TIP]
> Zur Vereinfachung ist ein einfaches `Makefile` im Repository enthalten.
>
> This Makefile has the following targets:
>
>  - push   : build locally to check and if successful push to GitHub for deployment
>  - all    : build locally and then upload to webserver
>
>  - build  : build the docs locally
>  - upload : upload the locally built docs to webserver
>
>  - check  : check if files are synced and in SUMMARY.md
>             optionally check Markdown links (requires an additional tool)
>
>  - serveDe: build locally; and serve 'de' version via browser
>  - serveEn: build locally; and serve 'en' version via browser

> [!TIP]
> Wenn unbedingt nötig, geht es auch ohne lokales Generieren:  
> Man kann aus dem *GitHub Actions Workflow* die automatisch gebauten Artifacts herunterladen und auspacken.
> Das ist dann die generierte Webseite.
>
> Dann ist allerdings obiger Aufruf von `lftp` noch anzupassen, weil die Webseite schon in finaler Struktur vorliegt.


**TODO**: URL der generierten Dokumentation besprechen und hier nachtragen.

