
class Plant:
    def __init__(self, name: str, height: float, age: int, growth_rate: float = 0.1) :
        self.name = name
        self.growth_rate = growth_rate

        if height > 0:
            self.height = height
        else :
            print(f"{name}: Error, height can't be negative")
            self.height = 0.0

        if age > 0:
            self.age = age
        else :
            print(f"{name}: Error, age can't be negative")
            self.age = age
    
    def get_name() -> str :
        return name
    
    def get_height() -> float :
        return height
    
    def get_age() -> int :
        return age

    def set_age(self, age: int) -> None:
        if age > 0 :
            self.age = age
        else :
            print(f"{self.name}: Error, age can't be negative")
            print("age update rejected")
    
    def set_height(self, height: float) -> None:
        if height > 0 :
            self.height = height
        else :
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
    
    def grow(self) -> None:
        self.height = round(self.height + self.growth_rate, 1)
    
    def add_one_day(self) -> None:
        self.age += 1
    
    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")



def main() -> None:
    print("=== Garden Security System ===")

    rose = Plant("Rose", 15.0, 10)
    print("Plant created: ", end="")
    rose.show()
    print()

    # Valid updates
    rose.set_height(25)
    rose.set_age(30)
    rose.show()
    print()

    # Invalid updates 
    rose.set_height(-42)
    rose.set_age(-1337)
    rose.show()
    print()

    print("Current state: ", end="")
    rose.show()



if __name__ == "__main__" :
    main()
