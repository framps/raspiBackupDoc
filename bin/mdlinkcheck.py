#!/usr/bin/env python3
"""Simple link checker for project-internal Markdown links

Links to external targets are not checked. There are other tools for that.
But they can be listed with option `--show-external-links`.

Usually Markdown files in the current directory and subdirectories are checked.

If a directory (or more) are given as arguments that ones are checked instead.


## Installation

Copy the script into one of your PATH's directories and make it executable.


-------------------------------------------------------------------------------

## Usage for project 'raspiBackupDoc'

Option `--raspiBackupDoc` enables the handling of the following asymmetry
in that project (https://github.com/framps/raspiBackupDoc):

The source files are in a **symmetric** directory structure:

    de/src/
    en/src/

but the generated HTML structure is **asymmetric**:
English as root and other language(s) as subdirectories:

    <files in English>
    ...
    de/<files in German>

-------------------------------------------------------------------------------
"""

import argparse
import re
from pathlib import Path
from typing import List


def check_anchor_in_target_file(target: Path,
                                anchor, is_local_anchor,
                                file: Path, line_number) -> None:
    """Check if given anchor is in target file

     - as an html anchor "<a name="...">
     - as Markdown heading "# ..."
    """
    content = target.read_text()

    m_anchor_quoted = re.search(f'<a name="{anchor}">', content)
    m_anchor_unquoted = re.search(f'<a name={anchor}[^"]', content)
    m_title = re.search(f'^##* {anchor}', content,
                        re.IGNORECASE | re.MULTILINE)

    if is_local_anchor:
        if m_anchor_unquoted:
            # print(m_anchor_unquoted.start())
            target_line = content[:m_anchor_unquoted.start()].count("\n")+1
            print(f"{file.as_posix()}:{line_number}:"
                  f" Anchor name '{anchor}' is not quoted"
                  f" in line {target_line}!")
        else:
            if m_anchor_quoted or m_title:
                return
            print(f"{file.as_posix()}:{line_number}:"
                  f" Anchor not found: '{anchor}'")
    else:
        if m_anchor_unquoted:
            target_line = content[:m_anchor_unquoted.start()].count("\n")+1
            print(f"{file.as_posix()}:{line_number}:"
                  f" Anchor name '{anchor}' is not quoted"
                  f" in target file '{target.as_posix()}:{target_line}'!")
        else:
            if m_anchor_quoted or m_title:
                return
            print(f"{file.as_posix()}:{line_number}:"
                  f" Anchor not found"
                  f" in target file '{target.as_posix()}':"
                  f" '{anchor}'")


def check_markdown_file(root: Path, file: Path,
                        raspibackupdoc=False,
                        external_links=None) -> None:
    """Check Markdown file for broken project-internal links

    Collect possible external links in list external_links
    as [(file.as_posix(), line_number, target), ...]
    """

    with file.open() as f:
        lines = f.readlines()

    for line_number, line in enumerate(lines, start=1):
        line = line.strip()
        m = re.search(r"\[.*?\]\((.*?)\)", line)
        if not m:
            continue

        target = m.groups()[0]

        if re.match(r"https*://", target):
            external_links.append((file.as_posix(), line_number, target))
            continue

        try:
            target, anchor = target.split("#")
        except ValueError:
            anchor = ""

        if target == "":   # the current file itself
            target_path = file
            is_local_anchor = True
        else:
            is_local_anchor = False

            if raspibackupdoc:
                # special handling for raspiBackupDoc
                if target.startswith("../"):
                    target = "../../en/src/" + target[3:]
                elif target.startswith("de/"):
                    target = "../../de/src/" + target[3:]
                # end special handling

            target_path = root / target

        if not target_path.exists():
            print(f"{file.as_posix()}:{line_number}:"
                  f" Target file not found: '{target_path.as_posix()}'")
            continue

        if anchor:
            check_anchor_in_target_file(target_path,
                                        anchor, is_local_anchor,
                                        file, line_number)


def walk_dir(directory: Path, raspibackupdoc=False,
             external_links=None, verbose=False) -> None:
    """Traverse given directory and check Markdown files """

    for root, _, files in Path(directory).walk(on_error=print):
        if verbose:
            print(">>> Checking directory", root)
        for f in files:
            file = root / f
            if file.suffix not in (".md", ".mkd", ".markdown"):
                continue
            if verbose:
                print(">>> Checking file", file)
            check_markdown_file(root, file,
                                raspibackupdoc=raspibackupdoc,
                                external_links=external_links)


def print_external_links(links):
    """Print the list of external - unchecked - links """

    print("\n\n*** Info: Not checked external link(s) ***\n")
    for linkdata in sorted(links):
        (filename, line_number, target) = linkdata
        print(f"{filename}:{line_number}: {target}")


def main(args):
    """The main checker ;-) """

    print("*** Check project-internal links ***\n")

    external_links: List[tuple] = []

    for srcdir in args.pathes:
        walk_dir(srcdir, raspibackupdoc=args.raspiBackupDoc,
                 external_links=external_links, verbose=args.verbose)

    if external_links and args.show_external_links:
        print_external_links(external_links)

    print("")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
                    prog='mdlinkcheck.py',
                    formatter_class=argparse.RawDescriptionHelpFormatter,
                    description=__doc__)

    parser.add_argument('pathes', nargs='*', default=["."], metavar='path')
    parser.add_argument('--raspiBackupDoc',
                        help='special handling regarding directory structure',
                        action='store_true')
    parser.add_argument('--show-external-links',
                        action='store_true')
    parser.add_argument('--verbose',
                        action='store_true')

    main(parser.parse_args())
