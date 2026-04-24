# Für Entwickler

Entwickler, die die Dokumentation (auch) lokal generieren möchten, benötigen ein paar Tools.

<a name="rust-compiler"></a>
## Rust-Compiler

Ein Rust-Compiler ist Grundlage, da die weiteren Tools in Rust programmiert sind,
und zumindest teilweise compiliert werden müssen.

Dabei ist zu beachten, dass die Rust-Version ziemlich aktuell sein sollte,
damit das aktuelle *mdbook* kompilierbar ist (siehe unten).

> mdBook currently requires at least Rust version 1.82.

Zum Beispiel beim aktuellen *Raspberry Pi OS* *Bookworm* ist *rustc* Version 1.63 in den Repositories, also zu alt.

Zur Installation von *Rust* siehe:

  - https://www.rust-lang.org/tools/install
  - https://www.rust-lang.org/learn/get-started

Am Einfachsten geht die Installation von Rust folgendermaßen:

```
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

Das bitte **ohne** `sudo` aufrufen, da es eine benutzerspezifische Installation ist!


## Generator - mdbook

Das Wichtigste ist der "Generator", der die Markdown-Textdateien einliest und nach HTML umwandelt.

Ich habe *mdbook* gewählt.

Dieses Tools kommt aus dem Rust-Umfeld und wird auch für die Rust-Dokumentation selbst eingesetzt.
Siehe <https://rust-lang.github.io/mdBook>

### Installation

Siehe <https://rust-lang.github.io/mdBook/guide/installation.html>

Kurzfassung hier:

#### Binaries

Für Apple, Windows und x86_64-Linux gibt es zwar fertige Binaries zum Herunterladen.

Da aber die weiteren erforderlichen Tool auf jeden Fall compiliert werden müssen,
macht es Sinn, auch *mdbook* zu compilieren:

<a name="compile-from-sources"></a>
#### Compilation aus den Quelltexten

Alle benötigten Tools lassen sich auch aus den Sourcen selbst kompilieren.
<https://rust-lang.github.io/mdBook/guide/installation.html#build-from-source-using-rust>

Dafür ist ein Rust-Compiler mit der entsprechenden Umgebung erforderlich.

Wenn der Compiler `rustc` dann installiert ist ([s.o.](#rust-compiler)), wird *mdbook* compiliert und installiert:

    cargo install mdbook

Dann kommt noch ein Präprozessor zur Erzeugung lokaler Inhaltsverzeichnisse dazu:

    cargo install mdbook-toc

Das ganze Prozedere inklusive *Rust* dauert selbst auf einem Pi5 nur wenige Minuten!
