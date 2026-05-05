import sys

print("=== Command Quest ===")

print(f"Program name: {sys.argv[0]}")
arguments_len = len(sys.argv) - 1
if arguments_len == 0:
    print("No arguments provided!")
else:
    print("Arguments received:", arguments_len)
    for i in range(1, len(sys.argv)):
        print(f"Argument {i}: {sys.argv[i]}")

print(f"Total arguments: {len(sys.argv)}")
