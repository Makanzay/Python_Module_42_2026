#! /usr/bin/env python3


class Plant:
    """Class of a plant in the garden."""

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self.height: float = height
        self.agee: int = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.agee} days old")

    def grow(self, growth: float) -> None:
        self.height += growth

    def age(self, days: int) -> None:
        self.agee += days

    def get_data(self) -> None:
        print("Current state: ", end="")
        self.show()


class Flower(Plant):
    """Class of a flower in the garden."""

    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color: str = color
        self._bloomed: bool = False

    def bloom(self) -> None:
        self._bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self._bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet.")


class Tree(Plant):
    """Class of a tree in the garden."""

    def __init__(self, name: str, height: float, age: int, t_d: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter: float = t_d

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces shade"
              f" of {self.height}cm long and {self.trunk_diameter}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk Diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    """Class of a vegetable in the garden."""

    def __init__(self, name: str, height: float, age: int, h_s: str, n_v: int) -> None:
        super().__init__(name, height, age)
        self.harvest_season: str = h_s
        self.nutritional_value: int = n_v

    def show(self) -> None:
        super().show()
        print(f"Harvest Season: {self.harvest_season}")
        print(f"Nutritional Value: {self.nutritional_value}")

    def age(self, days: int) -> None:
        super().age(days)
        if self.agee >= 30:
            self.nutritional_value += 10

    def grow(self, growth: float) -> None:
        super().grow(growth)
        if self.height >= 35.0:
            self.nutritional_value += 10


def main() -> None:
    print("=== Garden Plant Types ===")
    print("== Flower")
    flower1 = Flower("Rose", 15.0, 10, "Red")
    flower1.show()
    print("[asking the flower to bloom]")
    flower1.bloom()
    flower1.show()

    print("\n== Tree")
    tree1 = Tree("Oak", 200.0, 365, 5.0)
    tree1.show()
    print("[asking the tree to produce shade]")
    tree1.produce_shade()

    print("\n== Vegetable")
    vegetable1 = Vegetable("Tomato", 5.0, 10, "April", 0)
    vegetable1.show()
    print(f"[make {vegetable1.name} grow and age for 20 days]")
    vegetable1.grow(42.0)
    vegetable1.age(20)
    vegetable1.show()


if __name__ == "__main__":
    main()
