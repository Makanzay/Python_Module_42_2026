#!/usr/bin/env python3


def secure_archive(
        filename: str,
        mode: str = "read",
        content: str = ""
) -> tuple[bool, str]:

    try:
        if mode == "read":

            with open(filename, "r") as file:
                return (True, file.read())

        elif mode == "write":

            with open(filename, "w") as file:
                file.write(content)

            return (True, "Content successfully written to file")

        return (False, "Invalid mode")

    except Exception as error:
        return (False, str(error))


def main() -> None:
    print("=== Cyber Archives Security ===")
    try:
        filename: str = input("Enter filename to read: ")
        success, result = secure_archive(filename, "read")
        if success:
            print("---")
            print(result, end="")
            print("\n---")
        else:
            print(f"Error reading file '{filename}': {result}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as error:
        print(f"An unexpected error occurred: {error}")


def test_secure_archive() -> None:
    print("=== Cyber Archives Security Test ===", end="\n\n")
    print("Using 'secure_archive' with non-existent file:")
    print(secure_archive("non_existent_file.txt", "read"))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("testBond", "read"))

    print("\nUsing 'secure_archive' to read from a regular file:")
    print(secure_archive("ex3/test.txt", "read"))
    content_to_write: str = secure_archive("ex3/test.txt", "read")[1]

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(secure_archive("test_secured_file.txt", "write", content_to_write))


if __name__ == "__main__":
    try:
        test_secure_archive()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
