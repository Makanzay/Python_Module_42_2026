#! /usr/bin/env python3


class Plant:
    """Class of a plant in the garden."""

    def __init__(self, name: str, heigh: float, agee: int) -> None:
        self.name: str = name
        self.heigh: float = heigh
        self.agee: int = agee
        print("Plant created: ", end="")
        self.show()

    def show(self) -> None:
        print(f"{self.name}: {self.heigh}cm, {self.agee} days old")

    def grow(self, growth: float) -> None:
        self.heigh += growth

    def age(self, days: int) -> None:
        self.agee += days


def main() -> None:
    """ making a plants factory and print their details."""

    plants_data: list[tuple[str, float, int]] = [
        ("Rose", 25.0, 30),
        ("Tulip", 15.0, 20),
        ("Sunflower", 50.0, 40),
        ("Daisy", 10.0, 15),
        ("Lily", 20.0, 25),
    ]
    plants: list[Plant] = []
    print("=== Plant Factory Output ===")
    for name, heigh, agee in plants_data:
        plant = Plant(name, heigh, agee)
        plants.append(plant)


if __name__ == "__main__":
    main()
