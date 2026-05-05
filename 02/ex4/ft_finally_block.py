
class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)

class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)

class WaterError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:

    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
    print("Testing valid plants...")
    try:
        print("Opening watering system")
        for name in ["Tomato", "Lettuce", "Carrots"]:
            water_plant(name)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return 
    finally:
        print("Closing watering system")


    print("\nTesting invalid plants...")
    try:
        print("Opening watering system")
        for name in ["Tomato", "lettuce", "Carrots"]:   # "lettuce" is wrong
            water_plant(name)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    test_watering_system()
    print("\nCleanup always happens, even with errors!")