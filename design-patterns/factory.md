# Factory Pattern

**Intent:**\
Define an interface for creating an object, but let subclasses decide which class to instantiate. Factory Method lets a class defer instantiation to subclasses.
---

## Python

```python
from abc import ABC, abstractmethod

# Product interface
class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass

# Concrete Products
class ConcreteProductA(Product):
    def operation(self) -> str:
        return "Result of ConcreteProductA"

class ConcreteProductB(Product):
    def operation(self) -> str:
        return "Result of ConcreteProductB"

# Creator
class Creator(ABC):
    @abstractmethod
    def factory_method(self) -> Product:
        pass
    
    def some_operation(self) -> str:
        # Call the factory method to create a Product object
        product = self.factory_method()
        # Use the product
        return f"Creator: The same creator's code has just worked with {product.operation()}"

# Concrete Creators
class ConcreteCreatorA(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductA()

class ConcreteCreatorB(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductB()

# Usage example:
def client_code(creator: Creator) -> None:
    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.some_operation()}")

# Client code
if __name__ == "__main__":
    print("App: Launched with ConcreteCreatorA.")
    client_code(ConcreteCreatorA())
    print("\n")
    
    print("App: Launched with ConcreteCreatorB.")
    client_code(ConcreteCreatorB())
```

---

## C++

```cpp
#include <iostream>
#include <string>

// Product interface
class Product {
public:
    virtual ~Product() {}
    virtual std::string Operation() const = 0;
};

// Concrete Products
class ConcreteProductA : public Product {
public:
    std::string Operation() const override {
        return "Result of ConcreteProductA";
    }
};

class ConcreteProductB : public Product {
public:
    std::string Operation() const override {
        return "Result of ConcreteProductB";
    }
};

// Creator
class Creator {
public:
    virtual ~Creator() {}
    virtual Product* FactoryMethod() const = 0;
    
    std::string SomeOperation() const {
        // Call the factory method to create a Product object
        Product* product = this->FactoryMethod();
        // Use the product
        std::string result = "Creator: The same creator's code has just worked with " + 
                             product->Operation();
        delete product;
        return result;
    }
};

// Concrete Creators
class ConcreteCreatorA : public Creator {
public:
    Product* FactoryMethod() const override {
        return new ConcreteProductA();
    }
};

class ConcreteCreatorB : public Creator {
public:
    Product* FactoryMethod() const override {
        return new ConcreteProductB();
    }
};

// Client code
void ClientCode(const Creator& creator) {
    std::cout << "Client: I'm not aware of the creator's class, but it still works.\n"
              << creator.SomeOperation() << std::endl;
}

int main() {
    std::cout << "App: Launched with ConcreteCreatorA.\n";
    Creator* creator = new ConcreteCreatorA();
    ClientCode(*creator);
    delete creator;
    
    std::cout << "\nApp: Launched with ConcreteCreatorB.\n";
    creator = new ConcreteCreatorB();
    ClientCode(*creator);
    delete creator;
    
    return 0;
}
```

---

## When to Use

- When a class can't anticipate the class of objects it must create
- When a class wants its subclasses to specify the objects it creates
- When you want to provide users of your library or framework with a way to extend its internal components
- When you need to reduce tight coupling between classes

---

## References

- [Refactoring Guru: Factory Method Pattern](https://refactoring.guru/design-patterns/factory-method)
- [Wikipedia: Factory Method Pattern](https://en.wikipedia.org/wiki/Factory_method_pattern)
- [GitHub: Design Patterns C++](https://github.com/RefactoringGuru/design-patterns-cpp.git)
- [GitHub: Design Patterns Python](https://github.com/RefactoringGuru/design-patterns-python.git)

---

> This work is licensed under a [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](https://creativecommons.org/licenses/by-nc-nd/4.0/).
