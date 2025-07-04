# FactoryMethod Design Pattern

**Intent:**\
Provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created.
---

## Python
```python
"""
Factory Method Design Pattern

Intent: Provides an interface for creating objects in a superclass, but allows
subclasses to alter the type of objects that will be created.

from __future__ import annotations
from abc import ABC, abstractmethod

class Creator(ABC):
    """
The Creator class declares the factory method that is supposed to return
    an object of a Product class. The Creator's subclasses usually provide the
    implementation of this method.

    @abstractmethod
    def factory_method(self):
        """
Note that the Creator may also provide some default implementation
        of the factory method.

    def some_operation(self) -> str:
        """
Also note that, despite its name, the Creator's primary
        responsibility is not creating products. Usually, it contains some core
        business logic that relies on Product objects, returned by the factory
        method. Subclasses can indirectly change that business logic by
        overriding the factory method and returning a different type of product
        from it.

        #Call the factory method to create a Product object.

        #Now, use the product.

        return result

"""
Concrete Creators override the factory method in order to change the
resulting product's type.

class ConcreteCreator1(Creator):
    """
Note that the signature of the method still uses the abstract product
    type, even though the concrete product is actually returned from the method.
    This way the Creator can stay independent of concrete product classes.

    def factory_method(self) -> Product:
        return ConcreteProduct1()

class ConcreteCreator2(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct2()

class Product(ABC):
    """
The Product interface declares the operations that all concrete products
    must implement.

    @abstractmethod
    def operation(self) -> str:
        pass

"""
Concrete Products provide various implementations of the Product interface.

class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct1}"

class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"

def client_code(creator: Creator) -> None:
    """
The client code works with an instance of a concrete creator, albeit
    through its base interface. As long as the client keeps working with the
    creator via the base interface, you can pass it any creator's subclass.

    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.some_operation()}", end="")

if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Launched with the ConcreteCreator2.")
    client_code(ConcreteCreator2())

# text output
# App: Launched with the ConcreteCreator1.
# Client: I'm not aware of the creator's class, but it still works.
# Creator: The same creator's code has just worked with {Result of the ConcreteProduct1}
# App: Launched with the ConcreteCreator2.
# Client: I'm not aware of the creator's class, but it still works.
# Creator: The same creator's code has just worked with {Result of the ConcreteProduct2}
```
---

## C++
```cpp
#include <iostream>
#include <string>

/**
 *Factory Method Design Pattern
 * Intent: Provides an interface for creating objects in a superclass, but
 * allows subclasses to alter the type of objects that will be created.
 */

/**
 *The Product interface declares the operations that all concrete products
 * must implement.
 */

class Product {
 public:
  virtual ~Product() {}
  virtual std::string Operation() const = 0;
};

/**
 *Concrete Products provide various implementations of the Product
 * interface.
 */
class ConcreteProduct1 : public Product {
 public:
  std::string Operation() const override {
    return "{Result of the ConcreteProduct1}";
  }
};
class ConcreteProduct2 : public Product {
 public:
  std::string Operation() const override {
    return "{Result of the ConcreteProduct2}";
  }
};

/**
 *The Creator class declares the factory method that is supposed to return
 * an object of a Product class. The Creator's subclasses usually provide the
 * implementation of this method.
 */

class Creator {
  /**
     *Note that the Creator may also provide some default implementation of
     * the factory method.
     */
 public:
  virtual ~Creator(){};
  virtual Product* FactoryMethod() const = 0;
  /**
     *Also note that, despite its name, the Creator's primary
     * responsibility is not creating products. Usually, it contains some core
     * business logic that relies on Product objects, returned by the factory
     * method. Subclasses can indirectly change that business logic by
     * overriding the factory method and returning a different type of product
     * from it.
     */

  std::string SomeOperation() const {
    //Call the factory method to create a Product object.

/**
 *Concrete Creators override the factory method in order to change the
 * resulting product's type.
 */
class ConcreteCreator1 : public Creator {
  /**
     *Note that the signature of the method still uses the abstract product
     * type, even though the concrete product is actually returned from the
     * method. This way the Creator can stay independent of concrete product
     * classes.
     */
 public:
  Product* FactoryMethod() const override {
    return new ConcreteProduct1();
  }
};

class ConcreteCreator2 : public Creator {
 public:
  Product* FactoryMethod() const override {
    return new ConcreteProduct2();
  }
};

/**
 *The client code works with an instance of a concrete creator, albeit
 * through its base interface. As long as the client keeps working with the
 * creator via the base interface, you can pass it any creator's subclass.
 */
void ClientCode(const Creator& creator) {
  // ...
  std::cout << "Client: I'm not aware of the creator's class, but it still works.\n"
            << creator.SomeOperation() << std::endl;
  // ...
}

/**
 *The Application picks a creator's type depending on the configuration or
 * environment.
 */

int main() {
  std::cout << "App: Launched with the ConcreteCreator1.\n";
  Creator* creator = new ConcreteCreator1();
  ClientCode(*creator);
  std::cout << std::endl;
  std::cout << "App: Launched with the ConcreteCreator2.\n";
  Creator* creator2 = new ConcreteCreator2();
  ClientCode(*creator2);

  delete creator;
  delete creator2;
  return 0;
}

//text output
//App: Launched with the ConcreteCreator1.
//Client: I'm not aware of the creator's class, but it still works.
//Creator: The same creator's code has just worked with {Result of the ConcreteProduct1}
//App: Launched with the ConcreteCreator2.
//Client: I'm not aware of the creator's class, but it still works.
//Creator: The same creator's code has just worked with {Result of the ConcreteProduct2}
```
---

## When to Use

- Implementation of the FactoryMethod design pattern
- When you need the specific functionality provided by this pattern

---

## References

- [Refactoring Guru: FactoryMethod Pattern](https://refactoring.guru/design-patterns/factorymethod)
- [Wikipedia: FactoryMethod Pattern](https://en.wikipedia.org/wiki/FactoryMethod_pattern)
- [GitHub: Design Patterns C++](https://github.com/RefactoringGuru/design-patterns-cpp.git)
- [GitHub: Design Patterns Python](https://github.com/RefactoringGuru/design-patterns-python.git)
---

> This work is licensed under a [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](https://creativecommons.org/licenses/by-nc-nd/4.0/).
