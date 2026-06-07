#!/usr/bin/env python3

import sys
import typing


def add_archive_symbol(content: str) -> str:
    lines: list[str] = content.splitlines()

    result: str = ""

    for line in lines:
        result += line + "#\n"

    return result


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    filename = sys.argv[1]

    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    try:
        file: typing.IO[str] = open(filename, "r")

        print("---")
        content: str = file.read()
        print(content, end="")
        print("\n---")

        file.close()
        print(f"File '{filename}' closed.")

        print("\nTransform data:")
        print("--- ")
        print(add_archive_symbol(content), end="")
        print("\n---")
        try:
            sys.stdout.write("Enter new filename (or empty): ")
            sys.stdout.flush()
            new_filename: str = sys.stdin.readline().strip()
            if new_filename and len(new_filename.split()) == 1:
                print(f"Saving data to '{new_filename}'...")
                new_file: typing.IO[str] = open(new_filename, "w")
                new_file.write(add_archive_symbol(content))
                print(f"Data saved in file '{new_filename}'.")
                new_file.close()
            else:
                print("Not saving data.")
        except KeyboardInterrupt:
            sys.stderr.write("\n[STDERR] Operation cancelled by user.\n")
        except Exception as error:
            sys.stderr.write(
                f"[STDERR] Error saving file '{new_filename}': {error}\n")
    except Exception as error:
        sys.stderr.write(
            f"[STDERR] Error opening file '{filename}': {error}\n")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        sys.stderr.write(f"[STDERR] An unexpected error occurred: {e}\n")
    except KeyboardInterrupt:
        sys.stderr.write("\n[STDERR] Operation cancelled by user.\n")
