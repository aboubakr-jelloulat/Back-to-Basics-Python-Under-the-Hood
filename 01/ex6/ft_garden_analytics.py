

class Plant:

    class PlantStats:
        """Tracks how many times key methods have been called."""

        def __init__(self) -> None:
            """Initialise all counters to zero."""
            self._grow_count: int = 0
            self._age_count: int = 0
            self._show_count: int = 0

        def record_grow(self) -> None:
            """Increment grow counter."""
            self._grow_count += 1

        def record_age(self) -> None:
            """Increment age counter."""
            self._age_count += 1

        def record_show(self) -> None:
            """Increment show counter."""
            self._show_count += 1

        def display(self) -> None:
            """Print the basic statistics line."""
            print(
                f"Stats: {self._grow_count} grow, "
                f"{self._age_count} age, "
                f"{self._show_count} show"
            )

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        growth_rate: float = 1.0,
    ) -> None:
        """Initialise plant data and create a fresh stats tracker."""
        self._name: str = name
        self._growth_rate: float = growth_rate
        self._stats: Plant.PlantStats = Plant.PlantStats()

        self._height: float = float(height) if height >= 0 else 0.0
        self._age: int = age if age >= 0 else 0


    @staticmethod
    def is_older_than_year(age_days: int) -> bool:
        """Return True if age_days is more than 365 days."""
        return age_days > 365

 
    @classmethod
    def anonymous(cls) -> "Plant":
        """Create an anonymous plant with default zero values."""
        return cls("Unknown plant", 0.0, 0)


    def get_height(self) -> float:
        """Return height."""
        return self._height

    def get_age(self) -> int:
        """Return age."""
        return self._age

    def get_name(self) -> str:
        """Return name."""
        return self._name

    def set_height(self, value: float) -> None:
        """Set height with validation."""
        if value < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = float(value)

    def set_age(self, value: int) -> None:
        """Set age with validation."""
        if value < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = value


    def grow(self) -> None:
        """Increase height and record the call."""
        self._height = round(self._height + self._growth_rate, 1)
        self._stats.record_grow()

    def age(self) -> None:
        """Increase age and record the call."""
        self._age += 1
        self._stats.record_age()

    def show(self) -> None:
        """Display plant info and record the call."""
        print(f"{self._name}: {self._height}cm, {self._age} days old")
        self._stats.record_show()



class Flower(Plant):
    """A flowering plant."""

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str,
        growth_rate: float = 1.0,
    ) -> None:
        super().__init__(name, height, age, growth_rate)
        self._color: str = color
        self._blooming: bool = False

    def bloom(self) -> None:
        """Make the flower bloom."""
        self._blooming = True

    def show(self) -> None:
        """Display flower info."""
        super().show()                  # Plant.show() counts the call
        print(f" Color: {self._color}")
        if self._blooming:
            print(f" {self._name} is blooming beautifully!")
        else:
            print(f" {self._name} has not bloomed yet")


class Seed(Flower):
    """A seed-producing flower — extends Flower with a seed count."""

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str,
        seed_count: int = 0,
        growth_rate: float = 1.0,
    ) -> None:
      
        super().__init__(name, height, age, color, growth_rate)
        self._seed_count: int = seed_count

    def bloom(self) -> None:
        """Bloom and set the seed count to the provided value."""
        super().bloom()   # sets self._blooming = True via Flower

    def set_seeds(self, count: int) -> None:
        """Manually set the number of seeds (called after bloom)."""
        self._seed_count = count

    def show(self) -> None:
        """Display flower info plus seed count."""
        super().show()                  # Flower.show() handles everything above
        print(f" Seeds: {self._seed_count}")



class Tree(Plant):
    """A tree with a trunk diameter and extended shade statistics."""


    class TreeStats(Plant.PlantStats):
        """Extends PlantStats with a produce_shade counter."""

        def __init__(self) -> None:
            super().__init__()
            self._shade_count: int = 0

        def record_shade(self) -> None:
            """Increment shade counter."""
            self._shade_count += 1

        def display(self) -> None:
            """Print base stats then shade stats."""
            super().display()
            print(f" {self._shade_count} shade")

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        trunk_diameter: float,
        growth_rate: float = 0.5,
    ) -> None:
        super().__init__(name, height, age, growth_rate)
        self._trunk_diameter: float = trunk_diameter
        # Replace the base PlantStats with the extended TreeStats
        self._stats: Tree.TreeStats = Tree.TreeStats()

    def produce_shade(self) -> None:
        """Produce shade and record the call."""
        print(
            f"Tree {self._name} now produces a shade of "
            f"{self._height}cm long and {self._trunk_diameter}cm wide."
        )
        self._stats.record_shade()

    def show(self) -> None:
        """Display tree info."""
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter}cm")


# ---------------------------------------------------------------------------
# Vegetable
# ---------------------------------------------------------------------------

class Vegetable(Plant):
    """A vegetable that gains nutritional value as it grows and ages."""

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        harvest_season: str,
        growth_rate: float = 2.0,
    ) -> None:
        super().__init__(name, height, age, growth_rate)
        self._harvest_season: str = harvest_season
        self._nutritional_value: int = 0

    def grow(self) -> None:
        """Grow and gain nutritional value."""
        super().grow()
        self._nutritional_value += 1

    def age(self) -> None:
        """Age and gain nutritional value."""
        super().age()
        self._nutritional_value += 1

    def show(self) -> None:
        """Display vegetable info."""
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutritional_value}")


def display_stats(plant: Plant) -> None:
    """Display statistics for any kind of plant via its _stats object."""
    plant._stats.display()



if __name__ == "__main__":
    print("=== Garden statistics ===")

    # Static method demo
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")
    print()

    # Flower
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red", growth_rate=8.0)
    rose.show()
    print("[statistics for Rose]")
    display_stats(rose)

    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    print("[statistics for Rose]")
    display_stats(rose)
    print()

    # Tree
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, trunk_diameter=5.0)
    oak.show()
    print("[statistics for Oak]")
    display_stats(oak)

    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for Oak]")
    display_stats(oak)
    print()

    # Seed
    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow", growth_rate=30.0)
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age()
    sunflower.bloom()
    sunflower.set_seeds(42)
    sunflower.show()
    print("[statistics for Sunflower]")
    display_stats(sunflower)
    print()

    # Anonymous (class method)
    print("=== Anonymous")
    unknown = Plant.anonymous()
    unknown.show()
    print("[statistics for Unknown plant]")
    display_stats(unknown)



