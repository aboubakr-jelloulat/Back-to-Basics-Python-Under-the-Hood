class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")
    
    def grow(self) -> None:
        self.height += 0.8
    
    def age_up(self) -> None:
        self.age += 1


def create_plants_object() -> list:
    return [
        Plant("Rose", 25.0, 30),
        Plant("Sunflower", 80.0, 45),
        Plant("Cactus", 15.0, 120),
        Plant("Tulip", 20.0, 15),
        Plant("Bamboo", 150.0, 200)
    ]

def main() -> None:
    print("=== Plant Factory Output ===")

    plants = create_plants_object()

    for p in plants:
        p.show()
    


if __name__ == "__main__":
    main()