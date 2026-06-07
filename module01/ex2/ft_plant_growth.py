#! /usr/bin/env python3


class Plant:
    """Class of a plant in the garden."""

    def __init__(self, name: str, heigh: float, agee: int) -> None:
        self.name: str = name
        self.heigh: float = heigh
        self.agee: int = agee

    def show(self) -> None:
        print(f"{self.name}: {self.heigh}cm, {self.agee} days old")

    def grow(self, growth: float) -> None:
        self.heigh += growth

    def age(self, days: int) -> None:
        self.agee += days


def main() -> None:
    """Store  plant in the garden and print their details."""

    plant1 = Plant("Rose", 25.0, 30)
    start_height: float = plant1.heigh
    print("=== Garden Plant Growth ===")
    plant1.show()
    for day in range(1, 8):
        plant1.grow(0.5)
        plant1.age(1)
        print(f"=== Day {day} ===")
        plant1.show()
    print(f"Growth this week: {round(plant1.heigh - start_height, 2)}cm")


if __name__ == "__main__":
    main()
