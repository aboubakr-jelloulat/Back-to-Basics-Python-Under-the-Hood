# Encapsulation = hiding internal data and controlling access (by convention in Python)
# Inheritance = class reuses and extends another class
# Polymorphism = same method name, different behavior (mainly via overriding)


class Root:
    def __init__(self, topic: str) -> None:
        self._topic = topic

    def show(self) -> None:
        print(f"TOPIC : {self._topic}")

    # Class Method = receives class (cls) instead of instance (self)
    @classmethod
    def anonymous(cls) -> "Root":
        return cls("class method is powerful")
    
    # Nested Class A class defined INSIDE another class. 
    class Meta:
        def __init__(self, outer, author: str) -> None:
            self._author = author
            self.outer = outer
        #outer reference to Root instance
        
        def show(self) -> None:
            print(f"Author: {self._author}")
            print(f"TOPIC : {self.outer._topic}")
            # print(self._topic)  # ERROR : A nested class in Python does NOT automatically have access to the outer class instance or its attributes. 
            # so You must pass the outer object explicitly



class Child(Root):
    def __init__(self, about: str, topic: str) -> None:
        super().__init__(topic)
        self._about = about

    # Polymorphism (method overriding)
    def show(self) -> None:
        print(f"ABOUT : {self._about}")
        super().show()

    # static method is: A function that lives inside a class but does NOT use self or cls
    @staticmethod
    def add(a: int, b: int) -> int:
        return a + b


def main():
    r = Root("Why Linux does not natively support Visual Studio IDE")
    r.show()

    print("\n**** Polymorphism ****\n")
    ch = Child("AI", "Will AI replace developers?")
    ch.show()

    print("\n**** Static Method ****\n")
    a = 10
    b = 20
    print(f"{a} + {b} = {Child.add(a, b)}")

    print("\n**** Class Method ****\n")
    unknown = Root.anonymous()
    unknown.show()

    print("\n**** Nested Class ****\n")
    meta = Root.Meta(r, "Xi Auth")
    meta.show()



if __name__ == "__main__":
    main()