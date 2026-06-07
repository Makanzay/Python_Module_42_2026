#!/usr/bin/env python3

import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    filename: str = sys.argv[1]

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

    except Exception as error:
        print(f"Error opening file '{filename}': {error}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
