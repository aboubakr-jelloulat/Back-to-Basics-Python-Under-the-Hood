# 🌱 Python Exceptions — Garden Guardian Guide

A clean reference on how Python handles errors — what exceptions are, how to use them, and when each type appears.

---

## Table of Contents

- [What is an Exception?](#what-is-an-exception)
- [The Four Keywords](#the-four-keywords)
  - [try](#try)
  - [except](#except)
  - [finally](#finally)
  - [raise](#raise)
- [Exception Types](#exception-types)
- [The Exception Hierarchy](#the-exception-hierarchy)
- [Real Example — Garden Sensor](#real-example--garden-sensor)

---

## What is an Exception?

An **exception** is an error that occurs while a program is running. Without handling it, the program crashes and stops entirely.

```python
int("abc")   #  Crashes the program
```

With exception handling, you can **catch** the error, respond to it, and **keep running**.

```python
try:
    int("abc")
except ValueError:
    print("Bad input!")   #  Program continues
```

---

## The Four Keywords

### `try`

Wraps code that **might fail**. Python runs it and jumps to `except` if an error occurs.

```python
try:
    result = int("abc")   # This will fail
```

---

### `except`

Catches the error. You can target **specific types** or chain multiple blocks.

```python
try:
    result = int("abc")
except ValueError as e:
    print(f"Caught it: {e}")
```

Chaining multiple error types:

```python
try:
    ...
except ValueError:
    print("Bad value")
except TypeError:
    print("Wrong type")
except Exception as e:
    print(f"Unexpected error: {e}")   # Fallback for anything else
```

> **Tip:** Always catch specific exceptions first. Use `Exception` only as a last-resort fallback — it can hide bugs if overused.

---

### `finally`

Runs **no matter what** — whether an error occurred or not. Ideal for cleanup.

```python
try:
    f = open("data.txt")
    data = f.read()
except FileNotFoundError:
    print("File not found!")
finally:
    print("This always runs.")   # Cleanup, logging, etc.
```

---

### `raise`

Manually **triggers** an exception. Useful to signal invalid states in your own code.

```python
def set_temperature(temp: int) -> None:
    if temp > 100:
        raise ValueError("Temperature too high for a garden sensor!")
```

You can also **re-raise** an already-caught exception:

```python
try:
    int("abc")
except ValueError:
    print("Logging the error...")
    raise   # Re-raises the same ValueError upward
```

---

## Exception Types

| Exception | Raised When | Example |
|---|---|---|
| `ValueError` | Right type, wrong value | `int("abc")` |
| `TypeError` | Wrong type entirely | `1 + "hello"` |
| `ZeroDivisionError` | Dividing by zero | `5 / 0` |
| `FileNotFoundError` | File does not exist | `open("ghost.txt")` |
| `KeyError` | Dictionary key missing | `d = {}; d["x"]` |
| `IndexError` | List index out of range | `lst = [1]; lst[9]` |
| `AttributeError` | Object has no such method/attribute | `"hi".explode()` |
| `Exception` | Base class — catches everything | General fallback |

---

### `ValueError`

Raised when the **value** is inappropriate for the operation, even if the type is correct.

```python
int("abc")       #  "abc" is a string, but not a valid number
int("3.14")      #  Works in float(), not int()
int("25")        #  Fine
```

---

### `TypeError`

Raised when an operation is applied to an **incompatible type**.

```python
1 + "hello"      #  Can't add int and string
len(42)          #  int has no length
```

---

### `ZeroDivisionError`

Raised when dividing or performing modulo by **zero**.

```python
10 / 0           #  ZeroDivisionError
10 % 0           #  Also ZeroDivisionError
```

---

### `FileNotFoundError`

Raised when trying to open a file that **does not exist**.

```python
open("sensor_data.txt")   #  If the file doesn't exist
```

> A subclass of `OSError`. You can also catch it with `except OSError`.

---

### `KeyError`

Raised when accessing a **dictionary key** that doesn't exist.

```python
data = {"temp": 25}
data["humidity"]   #  KeyError: 'humidity'
```

Use `.get()` to avoid it:

```python
data.get("humidity", 0)   #  Returns 0 if key is missing
```

---

### `IndexError`

Raised when accessing a **list index** that is out of range.

```python
readings = [20, 22, 19]
readings[10]   #  IndexError
```

---

### `AttributeError`

Raised when accessing a **method or attribute** that doesn't exist on an object.

```python
"hello".explode()   #  str has no method explode()
None.upper()        #  NoneType has no method upper()
```

---

### `Exception`

The **base class** for all built-in exceptions. Catches anything, but use it carefully.

```python
try:
    ...
except ValueError:
    ...              # Handle expected errors first
except Exception as e:
    print(f"Unexpected: {e}")   # Last resort only
```

---

## The Exception Hierarchy

All exceptions inherit from `Exception`. This means catching a parent class catches all its children.

```
Exception
├── ValueError
├── TypeError
├── ZeroDivisionError
├── AttributeError
├── OSError
│   └── FileNotFoundError
└── LookupError
    ├── KeyError
    └── IndexError
```

> Catching `LookupError` catches both `KeyError` and `IndexError`.  
> Catching `OSError` catches `FileNotFoundError` and other file-related errors.

---

## Real Example — Garden Sensor

```python
def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")                    # ValueError
    elif operation_number == 1:
        1 / 0                         # ZeroDivisionError
    elif operation_number == 2:
        open("nonexistent_file.txt")  # FileNotFoundError
    elif operation_number == 3:
        1 + "hello"                   # TypeError


def test_error_types() -> None:
    print("=== Garden Error Types ===\n")

    for i in range(4):
        try:
            garden_operations(i)
        except ValueError as e:
            print(f"[{i}] ValueError       — Bad data provided: {e}")
        except ZeroDivisionError as e:
            print(f"[{i}] ZeroDivisionError — Cannot divide by zero: {e}")
        except FileNotFoundError as e:
            print(f"[{i}] FileNotFoundError — File not found: {e}")
        except TypeError as e:
            print(f"[{i}] TypeError         — Incompatible types: {e}")

    print("\nAll tests completed — program didn't crash!")


test_error_types()
```

**Output:**

```
=== Garden Error Types ===

[0] ValueError        — Bad data provided: invalid literal for int() with base 10: 'abc'
[1] ZeroDivisionError — Cannot divide by zero: division by zero
[2] FileNotFoundError — File not found: [Errno 2] No such file or directory: 'nonexistent_file.txt'
[3] TypeError         — Incompatible types: unsupported operand type(s) for +: 'int' and 'str'

All tests completed — program didn't crash!
```

---

*Garden Guardian — Data Engineering for Smart Agriculture*
