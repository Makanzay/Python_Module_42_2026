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
            new_filename: str = input("Enter new file name (or empty): ")
            if new_filename:
                new_file: typing.IO[str] = open(new_filename, "w")
                new_file.write(add_archive_symbol(content))
                print(f"Saving data to '{new_filename}'...")
                print(f"Data saved in file '{new_filename}'.")
                new_file.close()
            else:
                print("Not saving data.")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
        except Exception as error:
            print(f"Error saving file '{new_filename}': {error}")
    except Exception as error:
        print(f"Error opening file '{filename}': {error}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
