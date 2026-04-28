class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cmcm, {self.age} days old")
    
    def grow(self) -> None:
        self.height += 0.8
    
    def age_up(self) -> None:
        self.age += 1


def main() -> None:
    print("=== Garden Plant Growth ===")

    plant = Plant("Rose", 25.0, 30)
    plant.show()

    init_height = plant.height

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        plant.grow()
        plant.age_up()
        plant.show()

    growth = round(plant.height - init_height, 1)
    print(f"Growth this week: {growth}cm")


if __name__ == "__main__":
    main()