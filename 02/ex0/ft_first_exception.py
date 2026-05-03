
def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def  test_temperature() -> None:
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

    print("\nAll tests completed - program didn't crash!")

if __name__ == "__main__" :
    test_temperature()