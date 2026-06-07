#!/usr/bin/env python3


class Plant:
    """Class of a plant in the garden."""

    def __init__(self, name: str, heigh: float, age: int) -> None:
        self.name: str = name
        self.heigh: float = heigh
        self.age: int = age

    def show(self):
        print(f"{self.name.capitalize()}: {self.heigh}cm, {self.age} days old")


def main() -> None:
    """Store 3 plants in the garden and print their details."""

    plant1 = Plant("rose", 20.5, 30)
    plant2 = Plant("sunflower", 80.0, 45)
    plant3 = Plant("Cactus", 15.0, 120)

    print("=== Garden Plant Registry ===")
    plant1.show()
    plant2.show()
    plant3.show()


if __name__ == "__main__":
    main()
