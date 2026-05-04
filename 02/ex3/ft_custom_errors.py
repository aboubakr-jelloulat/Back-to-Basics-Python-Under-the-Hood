
class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)

class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)
    
class WaterError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)
    

def check_plant(name: str) -> None:
    if name == "tomato":
        raise PlantError("The tomato plant is wilting!")


def check_water(tank: int) -> None:
    if tank < 5:
        raise WaterError("Not enough water in the tank!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        check_plant("tomato")
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")

    print("Testing WaterError...")
    try:
        check_water(2)
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")
    

    print("Testing catching all garden errors...")
    try:
        check_plant("tomato")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    
    try:
        check_water(3)
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("\nAll custom error types work correctly!")