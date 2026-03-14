# mdbook - Eine kurze Einführung

Offizielle Dokumentation:

  - <https://rust-lang.github.io/mdBook/index.html>
  - <https://rust-lang.github.io/mdBook/guide/creating.html>


**Hinweis**: Folgende Beschreibung bezieht sich allgemein auf das Arbeiten mit *mdbook*.
Bei *raspiBackupDoc* werden mehrere Zielsprachen erstellt, daher ist dort die
Aufteilung der Quelldateien und der Aufruf der Tools etwas anders.
Die Sprachen liegen dort in Unterverzeichnissen je Sprache, was den Tools mitgeteilt werden muss.
Siehe [EDIT.md](EDIT.md) und [MAINTAIN.md](MAINTAIN.md).

Für die Arbeit an einem neuen Dokument/Buch wird ein neues Verzeichnis angelegt

    $ mkdir ~/mein_buch

*mdbook* gibt eine gewisse - einfache - Verzeichnis-/Dateistruktur vor und legt diese auch an.
(Inklusive der Datei `book.toml`, die ein paar Verwaltungsdaten enthält.)

Hier der Ablauf der Einrichtung eines neuen "Buches" in einem ursprünglich leeren Arbeitsverzeichnis:

    $ cd ~/mein_buch

    $ mdbook init

        Do you want a .gitignore to be created? (y/n)
        y
        What title would you like to give the book?
        Mein erstes Buch
        2025-05-26 13:04:56 [INFO] (mdbook::book::init): Creating a new book with stub content

        All done, no errors...

Das Ergebnis:

    $ tree

        .
        ├── book
        ├── book.toml
        └── src
            ├── chapter_1.md
            └── SUMMARY.md

        3 directories, 3 files

mit diesem Inhalt in der `book.toml`:

    $ cat book.toml

        [book]
        authors = []
        language = "en"
        src = "src"
        title = "Mein erstes Buch"


Die Sprachangabe in der Datei sollte dann noch den zukünftigen Inhalten angepasst werden,
damit der Browser des Lesers korrekt damit umgehen kann.


## Editieren/Erstellen des Inhalts

Im Unterverzeichnis `src/` stehen die Inhalte in Markdown-formatierten Dateien.
Die `SUMMARY.md` gibt den Aufbau und das Inhaltsverzeichnis wieder.

Beispiel:

    # Mein erstes Buch

    [Vorwort](introduction.md)

    - [Erstes Kapitel](chapter_1.md)

Hier in `src/` können auch Bilder, Icons etc. untergebracht werden, sinnvollerweise
in passend benannten Unterverzeichnissen.


## Generieren der Webseite

Mit dem Aufruf von

        mdbook build

wird anhand der `SUMMARY.md` eine Webseite im Verzeichnis `book/` generiert.


## Lokaler Webserver während der Entwicklung des Buches

Zum lokalen Ansehen im Browser unter der Adresse <http://localhost:3000> gibt es das Kommando

    mdbook serve


welches einen kleinen lokalen Webserver startet.

    2025-05-26 13:24:48 [INFO] (mdbook::book): Book building has started
    2025-05-26 13:24:48 [INFO] (mdbook::book): Running the html backend
    2025-05-26 13:24:49 [INFO] (mdbook::cmd::serve): Serving on: http://localhost:3000
    2025-05-26 13:24:49 [INFO] (mdbook::cmd::watch::poller): Watching for changes...
    2025-05-26 13:24:49 [INFO] (warp::server): Server::run; addr=[::1]:3000
    2025-05-26 13:24:49 [INFO] (warp::server): listening on http://[::1]:3000

Dieser Webserver bemerkt Änderungen an Dateien im Verzeichnis `src/` und generiert dann automatisch neu,
so dass der lokale Browser synchron ist (manchmal ist allerdings ein Auffrischen - F5 erforderlich).


## Veröffentlichung

Wenn nun das Ergebnis im lokalen Webserver/Browser zufriedenstellend ist,
kann die Webseite, also die generierte Sammlung von HTML- und anderen Dateien im Verzeichnis `book/`,
natürlich noch veröffentlicht werden.

Dies kann z.B. durch Hochladen zu einem Webserver/Webhoster o.Ä. geschehen.
Oder per *GitHub Pages*.



# Mögliche Fehlermeldungen

Es kann natürlich sein, dass beim `mdbook build` Fehler auftreten.

 - Falls der Präprozessor `mdbook-admonish` nicht installiert ist:

        2025-05-27 02:53:49 [INFO] (mdbook::book): Book building has started
        2025-05-27 02:53:49 [WARN] (mdbook::preprocess::cmd): The command wasn't found, is the "admonish" preprocessor installed?
        2025-05-27 02:53:49 [WARN] (mdbook::preprocess::cmd): 	Command: mdbook-admonish

   Siehe dazu bei [Compilation aus den Quelltexten](INSTALL.md#compile-from-sources)

