
def garden_operations(operation_number: int) -> None:
    
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        1 / 0
    elif operation_number == 2:
        open("nonexistent_file.txt")
    elif operation_number == 3:
        1337 + " Coding School"


def test_error_types() -> None:
    print("=== Garden Error Types ===\n")
    
    for i in range(4):
        try:
            garden_operations(i)

        except ValueError as e:
            print(f"Testing operation {i}...\nValueError - Bad data provided: {e}")
        except ZeroDivisionError as e:
            print(f"Testing operation {i}...\nZeroDivisionError - Cannot divide by zero: {e}")
        except FileNotFoundError as e:
            print(f"Testing operation {i}...\nFileNotFoundError - File not found: {e}")
        except TypeError as e:
            print(f"Testing operation {i}...\nTypeError - Mixed incompatible types: {e}")
    print ("Operation completed successfully")

    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_error_types()