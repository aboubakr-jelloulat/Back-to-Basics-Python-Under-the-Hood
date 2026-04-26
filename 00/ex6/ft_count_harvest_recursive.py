
def foo(n: int) -> None:
    if n == 0:
        return 
    foo(n - 1)
    print(f'Day {n}')

def ft_count_harvest_recursive() -> None:
    n = int(input("Days until harvest: "))
    foo(n);
    print("Harvest time!")


# ft_count_harvest_recursive()