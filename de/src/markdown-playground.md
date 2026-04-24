# Testseite

Diese Seite ist gedacht zum Testen von Markdown-Features und -Syntax.

## Unterschied zwischen Codeblock und Inline-Code

Inline-Code mit Single-Backticks stellt Code wie z.B. `print("Good Morning")` innerhalb normalen Textes dar.

`Dies ist eine ganze Zeile mit Inline-Code`

Sie wird anders dargestellt als ein Codeblock:

```
Und dies ein echter Codeblock.
```

## Einrückungen

Text steht linksbündig.

  Um zwei Zeichen eingerückt.

    Um vier Zeichen eingerückt ergibt einen Codeblock!

    print("Hello Markdown")

Codeblock mit Einrückung um 6 Leerzeichen:

      print("Hello Markdown")

Codeblock mit Einrückung um 8 Leerzeichen:

        print("Hello Markdown")


## Tabellen

### Tests bzgl. Wortumbruch

Verschiedene Längen des "Option" Titels mit Leerzeichen ändert nichts:

| Option | Standard| Im Installer setzbar | Konfigurationsname |
|--------|---------|----------------------|--------------------|
| --keep_rsync | Parameter für Option -k | nein | DEFAULT_KEEPBACKUPS_RSYNC |

| Option       | Standard| Im Installer setzbar | Konfigurationsname |
|--------------|---------|----------------------|--------------------|
| --keep_rsync | Parameter für Option -k | nein | DEFAULT_KEEPBACKUPS_RSYNC |

| Option                  | Standard| Im Installer setzbar | Konfigurationsname |
|-------------------------|---------|----------------------|--------------------|
| --keep_rsync | Parameter für Option -k | nein | DEFAULT_KEEPBACKUPS_RSYNC |

Erst das Verlängern des Titels selber hilft:

| Option zum Testen       | Standard| Im Installer setzbar | Konfigurationsname |
|-------------------------|---------|----------------------|--------------------|
| --keep_rsync | Parameter für Option -k | nein | DEFAULT_KEEPBACKUPS_RSYNC |

Hier **eine** Spalte (Installer) zentriert:

| Optionsname             | Standard| Im Installer setzbar | Konfigurationsname |
|-------------------------|---------|:--------------------:|--------------------|
| --keep_rsync | Parameter für Option -k | nein | DEFAULT_KEEPBACKUPS_RSYNC |

... rechtsbündig:

| Optionsname             | Standard| Im Installer setzbar | Konfigurationsname |
|-------------------------|---------| --------------------:|--------------------|
| --keep_rsync | Parameter für Option -k | nein | DEFAULT_KEEPBACKUPS_RSYNC |

... linksbündig:

| Optionsname             | Standard| Im Installer setzbar | Konfigurationsname |
|-------------------------|---------| :------------------- |--------------------|
| --keep_rsync | Parameter für Option -k | nein | DEFAULT_KEEPBACKUPS_RSYNC |

### Tests bzgl. Ausrichtung


#### Normal (Header zentriert, Spalten linksbündig):

| Optionsname | Standard | Im Installer | Konfigurationsname |
|-------------|----------|--------------|--------------------|
| --ignoreMissingPartitions | nein |  | DEFAULT_... |

#### Alles zentriert:


| Optionsname | Standard | Im Installer | Konfigurationsname |
|:-----------:|:--------:|:------------:|:------------------:|
| --ignoreMissingPartitions | nein |  | DEFAULT_... |

#### Alles linksbündig, inkl. Header:


| Optionsname | Standard | Im Installer | Konfigurationsname |
|:------------|:---------|:-------------|:--------------------
| --ignoreMissingPartitions | nein |  | DEFAULT_... |

#### Normal (Header zentriert, Spalten linksbündig):

| Optionsname | Standard | Im Installer | Konfigurationsname |
|-------------|----------|--------------|--------------------|
| --keep_dd    | Parameter für Option -k | konfigurierbar | DEFAULT_KEEPBACKUPS_DD |
| --keep_ddz   | Parameter für Option -k | konfigurierbar | DEFAULT_KEEPBACKUPS_DDZ |
| --keep_rsync | Parameter für Option -k | konfigurierbar | DEFAULT_KEEPBACKUPS_RSYNC |
| --keep_tar   | Parameter für Option -k | konfigurierbar | DEFAULT_KEEPBACKUPS_TAR |
| --keep_tgz   | Parameter für Option -k | konfigurierbar | DEFAULT_KEEPBACKUPS_TGZ |

#### Alles zentriert:

| Optionsname | Standard | Im Installer | Konfigurationsname |
|:-----------:|:--------:|:------------:|:------------------:|
| --keep_dd    | Parameter für Option -k | konfigurierbar | DEFAULT_KEEPBACKUPS_DD |
| --keep_ddz   | Parameter für Option -k | konfigurierbar | DEFAULT_KEEPBACKUPS_DDZ |
| --keep_rsync | Parameter für Option -k | konfigurierbar | DEFAULT_KEEPBACKUPS_RSYNC |
| --keep_tar   | Parameter für Option -k | konfigurierbar | DEFAULT_KEEPBACKUPS_TAR |
| --keep_tgz   | Parameter für Option -k | konfigurierbar | DEFAULT_KEEPBACKUPS_TGZ |

#### Alles linksbündig, inkl. Header:

| Optionsname | Standard | Im Installer | Konfigurationsname |
|:------------|:---------|:-------------|:-------------------|
| --keep_dd    | Parameter für Option -k | konfigurierbar | DEFAULT_KEEPBACKUPS_DD |
| --keep_ddz   | Parameter für Option -k | konfigurierbar | DEFAULT_KEEPBACKUPS_DDZ |
| --keep_rsync | Parameter für Option -k | konfigurierbar | DEFAULT_KEEPBACKUPS_RSYNC |
| --keep_tar   | Parameter für Option -k | konfigurierbar | DEFAULT_KEEPBACKUPS_TAR |
| --keep_tgz   | Parameter für Option -k | konfigurierbar | DEFAULT_KEEPBACKUPS_TGZ |

#### Normal (Header zentriert, Spalten linksbündig):

| Config-Option              | Standard |
|----------------------------|----------|
| DEFAULT_SEND_STATS         | ja       |

#### Alles zentriert:

| Config-Option              | Standard |
|:--------------------------:|:--------:|
| DEFAULT_SEND_STATS         | ja       |

#### Alles linksbündig, inkl. Header:

| Config-Option              | Standard |
|:---------------------------|:---------|
| DEFAULT_SEND_STATS         | ja       |


#### formatiert per CSS und ohne Alignment-":" im Quelltext

100% Breite, linksbündige Header und Daten und Normal-Font im Header

<div class="table-wrapper-for-options">

| Optionsname | Standard | Im Installer | Konfigurationsname |
|-------------|----------|--------------|--------------------|
| --keep_dd    | Parameter für Option -k | konfigurierbar | DEFAULT_KEEPBACKUPS_DD |
| --keep_ddz   | Parameter für Option -k | konfigurierbar | DEFAULT_KEEPBACKUPS_DDZ |
| --keep_rsync | Parameter für Option -k | konfigurierbar | DEFAULT_KEEPBACKUPS_RSYNC |
| --keep_tar   | Parameter für Option -k | konfigurierbar | DEFAULT_KEEPBACKUPS_TAR |
| --keep_tgz   | Parameter für Option -k | konfigurierbar | DEFAULT_KEEPBACKUPS_TGZ |


| Config-Option              | Standard |
|----------------------------|----------|
| DEFAULT_SEND_STATS         | ja       |

</div>


## Fenced Codeblocks per Triple-Backticks

Besser/empfohlen:

Linksbündig:

```
print("Hello Markdown")
```

Um zwei Zeichen eingerückt:

  ```
  print("Hello Markdown")
  ```

Um mindestens vier Zeichen eingerückt erzeugt aber einen Codeblock vom Codeblock:

    ```
    print("Hello Markdown")
    ```

Um sechs Zeichen eingerückt:

      ```
      print("Hello Markdown")
      ```

## Listen

Hier sieht man, warum Codeblocks durch Einrückung nicht mehr empfohlen werden:
Es ist nicht immer eindeutig erkennbar oder sie werden beim Parsen evtl. nicht erkannt!


- Linksbündig
- dito
  - sub 1
    Text in sub 1
  Text
        Um 4 Zeichen eingerückt ergibt hier nur Text

        Um 4 Zeichen eingerückt und per Leerzeile abgesetzt
        ergibt einen Codeblock

  - zwei Zeichen eingerückt
  - dito
      - sub 1
        Text in Sub 1
      Text
            Um 4 Zeichen eingerückt ergibt hier nur Text

            Codeblock 1

            Codeblock 2

Mit fenced Codeblocks (per Triple-Backticks) ist es eindeutig:

  - zwei Zeichen eingerückt
  - dito
      - sub 1
        Text in Sub 1 mit zwei Leerzeichen am Zeilenende  
        ergibt eine neue Zeile und die Codeblocks dürfen
        auch direkt ohne Leerzeile folgen
        (eine Leerzeile schadet aber nicht und erhöht die Lesbarkeit des Quelltextes.)
        ```
        print("")
        ```
          ```
          print("")
          ```
            ```
            print("")
            ```


## Test mit neuem Parser ab mdbook 0.5


Der neue Parser ist bezüglich von in den Markdown Text eingefügtem HTML-Code pingeliger als die Versionen bis 0.4.

Das wird besonders deutlich, wenn keine echte HTML-Formatierung, sondern Pseudo-HTML-Tags verwendet werden.

* Normaler Text

  * mit <b>eingebettetem HTML</b>.
  * Ein pseudo-HTML Tag, der nicht angezeigt wird (nur öffnend: das ergibt eine Parser-Warnung): <parameter>

    ```
    WARN unclosed HTML tag `<parameter>` found in `markdown-playground.md` while exiting Item
    HTML tags must be closed before exiting a markdown element.
    ```

* Als Zitat verhält es sich identisch:

  > Text mit <b>eingebettetem HTML</b>.
  >
  > Ein Pseudo-HTML Tag, nur öffnend, keine Anzeige: <parameter>

* Korrekturversuch mit auch-schließendem Tag ```<parameter/>```:

  * keine Warnung mehr, aber natürlich immer noch keine Anzeige: <parameter/>

* Korrektur per Escape mit Backslash (eher als Workaround zu sehen) ```\<parameter>```:

  * das deaktiviert die HTML-Interpretation und zeigt es endlich an: \<parameter>


Sinnvoller erscheint die Verwendung von Formatierung als *Code* für Pseudo-HTML-Tags:


* In single Backticks: `<parameter>`
* In triple Backticks: ```<parameter>```


* Dieselbe Zeilen in einem eingerückten Codeblock:

      Normaler Text mit <b>eingebettetem HTML</b>.
      Pseudo-HTML Tag, nur öffnend: <parameter>

* Dieselbe Zeilen in einem fenced Codeblock:

  ```
  Normaler Text mit <b>eingebettetem HTML</b>.
  Pseudo-HTML Tag, nur öffnend: <parameter>
  ```

[.status]: z_Markdown_Playground
