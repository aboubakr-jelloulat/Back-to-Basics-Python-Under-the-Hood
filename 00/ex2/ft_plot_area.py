def calcul_area(length: int, width: int) -> int:
    return length * width

def ft_plot_area() -> None:
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))
    print(f"Plot area: {calcul_area(length, width)}")