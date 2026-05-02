class Plant:
    def __init__(self, name: str, height: float, age: int, growth_rate: float = 0.1):
        self.name = name
        self.growth_rate = growth_rate

        if height > 0:
            self.height = height
        else:
            print(f"{name}: Error, height can't be negative")
            self.height = 0.0

        if age >= 0:
            self.age = age
        else:
            print(f"{name}: Error, age can't be negative")
            self.age = 0

    # Getters
    def get_name(self) -> str:
        return self.name

    def get_height(self) -> float:
        return self.height

    def get_age(self) -> int:
        return self.age

    # Setters
    def set_age(self, age: int) -> None:
        if age >= 0:
            self.age = age
        else:
            print(f"{self.name}: Error, age can't be negative")
            print("age update rejected")

    def set_height(self, height: float) -> None:
        if height > 0:
            self.height = height
        else:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")

    def grow(self) -> None:
        self.height = round(self.height + self.growth_rate, 1)

    # renamed to avoid conflict with attribute "age"
    def grow_older(self) -> None:
        self.age += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str, growth_rate: float = 1.0):
        super().__init__(name, height, age, growth_rate)
        self.color = color
        self.blooming = False

    def bloom(self) -> None:
        self.blooming = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.blooming:
            print(f"{self.name} is blooming")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, trunk_diameter: float, growth_rate: float = 1.0):
        super().__init__(name, height, age, growth_rate)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(
            f"Tree {self.name} now produces shade of "
            f"{self.height}cm tall and {self.trunk_diameter}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int, harvest_season: str, growth_rate: float = 1.0):
        super().__init__(name, height, age, growth_rate)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")

    def grow(self) -> None:
        super().grow()
        self.nutritional_value += 1

    def grow_older(self) -> None:
        super().grow_older()
        self.nutritional_value += 1


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")

    # Flower
    print("=== Flower ===")
    rose = Flower("Rose", 15.0, 10, "red", growth_rate=8.0)
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print()

    # Tree
    print("=== Tree ===")
    oak = Tree("Oak", 200.0, 365, trunk_diameter=5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print()

    # Vegetable
    print("=== Vegetable ===")
    tomato = Vegetable("Tomato", 5.0, 10, "April", growth_rate=2.1)
    tomato.show()

    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.grow()
        tomato.grow_older()

    tomato.show()
    