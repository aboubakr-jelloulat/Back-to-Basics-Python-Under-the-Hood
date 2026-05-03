
def temperature_is_reasonable(temp: int) -> bool:
    return 0 <= temp <= 40

def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temperature_is_reasonable(temp):
        return temp
    elif (temp > 40) :
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    else :
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")

def test_temperature() -> None:
    print("=== Garden Temperature === \n")

    nb = 25
    print(f"Input data is {nb}")
    try:
        print(f"Temperature is now {input_temperature(nb)}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    print()

    nb = "abc"
    print(f"Input data is {nb}")
    try:
        print(f"Temperature is now {input_temperature(nb)}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    
    print()

    nb = 100
    print(f"Input data is {nb}")
    try:
        print(f"Temperature is now {input_temperature(nb)}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    
    print()

    nb = -50
    print(f"Input data is {nb}")
    try:
        print(f"Temperature is now {input_temperature(nb)}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    

    print("\nAll tests completed - program didn't crash!")



if __name__ == "__main__":
    test_temperature()