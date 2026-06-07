#! /usr/bin/env python3


class Plant:
    """Class of a plant in the garden."""

    def __init__(self, name: str) -> None:
        self.name: str = name
        self._heigh: float = 0.0
        self._agee: int = 0
        print("Plant created: ", end="")
        self.show()

    def show(self) -> None:
        print(f"{self.name}: {self._heigh}cm, {self._agee} days old")

    def grow(self, growth: float) -> None:
        self._heigh += growth

    def age(self, days: int) -> None:
        self._agee += days

    def set_height(self, heigh: float) -> None:
        if float(heigh) >= 0.0:
            self._heigh = heigh
            print(f"Height updated: {self._heigh}cm")
        else:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, agee: int) -> None:
        if int(agee) >= 0:
            self._agee = agee
            print(f"Age updated: {self._agee} days")
        else:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")

    def get_height(self) -> float:
        return self._heigh

    def get_age(self) -> int:
        return self._agee

    def get_data(self) -> None:
        print("Current state: ", end="")
        self.show()


def main() -> None:
    print("=== Garden Security System ===")
    plant1 = Plant("Rose")
    plant1.set_height(25.0)
    plant1.set_age(30)

    plant1.set_height(-5.0)  # Invalid height
    plant1.set_age(-10)      # Invalid age

    plant1.get_data()


if __name__ == "__main__":
    main()
