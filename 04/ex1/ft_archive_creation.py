import sys

def main() -> None:

    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return 
    
    print("=== Cyber Archives Recovery & Preservation ===")

    path = sys.argv[1]
    print(f"Accessing file '{path}'")

    content = ""
    try:
        with open(path) as f:
            print("---\n")
            content = f.read()
            print(content)
            print("\n---")
            print(f"File '{path}' closed.")

    except Exception as ex:
        print(f"Error opening file '{path}': {ex}")
        return 

    print("\nTransform data:")
    print("---\n")

    lines = content.splitlines()
    transformed_lines = [line + "#" for line in lines]
    new_content = "\n".join(transformed_lines)
    print(new_content)

    print("\n---")

    new_file = input("Enter new file name (or empty): ")
    if new_file == "":
        print("Not saving data.")
        return

    print(f"Saving data to '{new_file}'")
    with open(new_file, "w") as f:
        f.write(new_content + "\n")

    print(f"Data saved in file '{new_file}'.")



if __name__ == "__main__" :
    main()