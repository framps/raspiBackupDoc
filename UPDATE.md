# Update der vorhandenen Tools mdbook*


## Was ist aktuell installiert (an Crates)?

```
$ cargo install --list

cargo-about v0.6.1:
    cargo-about
mdbook v0.4.52:
    mdbook
mdbook-admonish v1.20.0:
    mdbook-admonish
mdbook-toc v0.15.3:
    mdbook-toc
```



## Was ist der **aktuelle** Stand von `mdbook`?

```
$ cargo search mdbook

mdbook = "0.5.2"                    # Creates a book from markdown files
mdbook-latex = "0.1.24"             # An mdbook backend for generating LaTeX and PDF documents.
mdbook-lang = "0.1.2"               # A mdbook preprocessor enables multiple programming languages playground.
mdbook-lint = "0.14.3"              # A fast markdown linter and preprocessor for mdBook
mdbook-theme = "0.1.6"              # A preprocessor and a backend to config theme for mdbook, especially creating a pagetoc on t…
mdbook-pandoc = "0.11.0"            # A pandoc-powered mdbook backend
mdbook-tectonic = "0.3.0-beta.4"    # An mdbook backend for generating LaTeX and PDF documents.
mdbook-exercises = "0.1.5"          # An mdBook preprocessor for interactive exercises with hints, solutions, and test execution
fifthtry-mdbook = "0.4.8"           # fork of mdbook, only for ft-cli
mdbook-admonish = "1.20.0"          # A preprocessor for mdbook to add Material Design admonishments.
... and 668 crates more (use --limit N to see more)
note: to learn more about a package, run `cargo info <name>`

```


```
$ cargo info mdbook

    Updating crates.io index
mdbook #book #gitbook #rustbook #markdown
Creates a book from markdown files
version: 0.5.2
license: MPL-2.0
rust-version: 1.88.0
documentation: https://rust-lang.github.io/mdBook/index.html
repository: https://github.com/rust-lang/mdBook
crates.io: https://crates.io/crates/mdbook/0.5.2
features:
 +default = [watch, serve, search]
  search  = [mdbook-html/search]
  serve   = [dep:futures-util, dep:tokio, dep:axum, dep:tower-http]
  watch   = [dep:notify, dep:notify-debouncer-mini, dep:ignore, dep:pathdiff, dep:walkdir]
```




## Auf die aktuelle Version updaten (installieren)

```
$ cargo install mdbook

    Updating crates.io index
  Installing mdbook v0.5.2
    Updating crates.io index
     Locking 232 packages to latest compatible versions
      Adding generic-array v0.14.7 (available: v0.14.9)
      Adding matchit v0.8.4 (available: v0.8.6)
      Adding toml v0.9.12+spec-1.1.0 (available: v1.1.2+spec-1.1.0)
  Downloaded serde_spanned v1.1.1
  Downloaded toml_parser v1.1.2+spec-1.1.0
  Downloaded toml_writer v1.1.1+spec-1.1.0
  ...
   Compiling mdbook v0.5.2
    Finished `release` profile [optimized] target(s) in 1m 20s
   Replacing /home/chris/.cargo/bin/mdbook
    Replaced package `mdbook v0.4.52` with `mdbook v0.5.2` (executable `mdbook`)
```



## Auch das verwendete Crate `mdbook-toc` updaten

```
$ cargo install mdbook-toc
```


## Für `mdbook 0.5` wird hier im Project `mdbook-admonish` nicht mehr benötigt, also deinstallieren

```
$ cargo uninstall mdbook-admonish

    Removing /home/chris/.cargo/bin/mdbook-admonish
```



## Was ist aktuell installiert?

```
$ cargo install --list

cargo-about v0.6.1:
    cargo-about
mdbook v0.5.2:
    mdbook
mdbook-toc v0.15.3:
    mdbook-toc
```




## Um eventuell wieder auf eine ältere (die letzte 0.4.x) zu wechseln:

```
$ cargo install --version=0.4.52 mdbook

  Downloaded mdbook v0.4.52
  Downloaded 1 crate (1.4MiB) in 0.31s
    Updating crates.io index
  Installing mdbook v0.4.52
    Updating crates.io index
   ...
   Compiling shlex v1.3.0
   Compiling mdbook v0.4.52

Finished `release` profile [optimized] target(s) in 1m 26s
Replacing /home/chris/.cargo/bin/mdbook
    Replaced package `mdbook v0.5.2` with `mdbook v0.4.52` (executable `mdbook`)
```

## Und das abhängige Crate `mdbook-toc` ebenfalls neu installieren

```
$ cargo install mdbook-toc
```



