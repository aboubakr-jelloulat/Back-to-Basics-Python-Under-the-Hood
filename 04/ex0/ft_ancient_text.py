import sys

if len(sys.argv) != 2:
    print("Usage: ft_ancient_text.py <file>")
else:
    print("=== Cyber Archives Recovery ===")

    path = sys.argv[1]
    print(f"Accessing file '{path}'")

    try:
        with open(path) as f:
            print("---\n")
            txt = f.read()
            print(txt)
            print("\n---")
            print(f"File '{path}' closed.")

    except Exception as ex:
        print(f"Error opening file '{path}': {ex}")




# What is the type of the data returned by open()?
    # It returns a file object, specifically something like: _io.TextIOWrapper
