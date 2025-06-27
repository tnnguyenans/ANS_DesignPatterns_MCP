# Bridge Design Pattern

**Intent:**\
Lets you split a large class or a set of closely related classes into two separate hierarchies—abstraction and implementation—which can be developed independently of each other.
---

## Python
```python
"""
Bridge Design Pattern

Intent: Lets you split a large class or a set of closely related classes into
two separate hierarchies—abstraction and implementation—which can be developed
independently of each other.

              A
           /     \                        A         N
         Aa      Ab        ===>        /     \     / \
        / \     /  \                 Aa(N) Ab(N)  1   2
      Aa1 Aa2  Ab1 Ab2

              A
           /     \                        A         N
         Aa      Ab        ===>        /     \     / \
        / \     /  \                 Aa(N) Ab(N)  1   2
      Aa1 Aa2  Ab1 Ab2
"""

from __future__ import annotations
from abc import ABC, abstractmethod

class Abstraction:
    """
The Abstraction defines the interface for the "control" part of the two
    class hierarchies. It maintains a reference to an object of the
    Implementation hierarchy and delegates all of the real work to this object.

    def __init__(self, implementation: Implementation) -> None:
        self.implementation = implementation

    def operation(self) -> str:
        return (f"Abstraction: Base operation with:\n"
                f"{self.implementation.operation_implementation()}")

class ExtendedAbstraction(Abstraction):
    """
You can extend the Abstraction without changing the Implementation
    classes.

    def operation(self) -> str:
        return (f"ExtendedAbstraction: Extended operation with:\n"
                f"{self.implementation.operation_implementation()}")

class Implementation(ABC):
    """
The Implementation defines the interface for all implementation classes.
    It doesn't have to match the Abstraction's interface. In fact, the two
    interfaces can be entirely different. Typically the Implementation interface
    provides only primitive operations, while the Abstraction defines higher-
    level operations based on those primitives.

    @abstractmethod
    def operation_implementation(self) -> str:
        pass

"""
Each Concrete Implementation corresponds to a specific platform and
implements the Implementation interface using that platform's API.

class ConcreteImplementationA(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationA: Here's the result on the platform A."

class ConcreteImplementationB(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationB: Here's the result on the platform B."

def client_code(abstraction: Abstraction) -> None:
    """
Except for the initialization phase, where an Abstraction object gets
    linked with a specific Implementation object, the client code should only
    depend on the Abstraction class. This way the client code can support any
    abstraction-implementation combination.

    # ...

    print(abstraction.operation(), end="")

    # ...

if __name__ == "__main__":
    """
The client code should be able to work with any pre-configured
    abstraction-implementation combination.

    implementation = ConcreteImplementationA()
    abstraction = Abstraction(implementation)
    client_code(abstraction)

    print("\n")

    implementation = ConcreteImplementationB()
    abstraction = ExtendedAbstraction(implementation)
    client_code(abstraction)

# text output
# Abstraction: Base operation with:
# ConcreteImplementationA: Here's the result on the platform A.
# ExtendedAbstraction: Extended operation with:
# ConcreteImplementationB: Here's the result on the platform B.
```
---

## C++
```cpp
#include <iostream>
#include <string>

/**
 *Bridge Design Pattern
 * Intent: Lets you split a large class or a set of closely related classes into
 * two separate hierarchies—abstraction and implementation—which can be
 * developed independently of each other.
 *               A
 *            /     \                        A         N
 *          Aa      Ab        ===>        /     \     / \
 *         / \     /  \                 Aa(N) Ab(N)  1   2
 *       Aa1 Aa2  Ab1 Ab2
 */

/**
 *The Implementation defines the interface for all implementation classes.
 * It doesn't have to match the Abstraction's interface. In fact, the two
 * interfaces can be entirely different. Typically the Implementation interface
 * provides only primitive operations, while the Abstraction defines higher-
 * level operations based on those primitives.
 */

class Implementation {
 public:
  virtual ~Implementation() {}
  virtual std::string OperationImplementation() const = 0;
};

/**
 *Each Concrete Implementation corresponds to a specific platform and
 * implements the Implementation interface using that platform's API.
 */
class ConcreteImplementationA : public Implementation {
 public:
  std::string OperationImplementation() const override {
    return "ConcreteImplementationA: Here's the result on the platform A.\n";
  }
};
class ConcreteImplementationB : public Implementation {
 public:
  std::string OperationImplementation() const override {
    return "ConcreteImplementationB: Here's the result on the platform B.\n";
  }
};

/**
 *The Abstraction defines the interface for the "control" part of the two
 * class hierarchies. It maintains a reference to an object of the
 * Implementation hierarchy and delegates all of the real work to this object.
 */

class Abstraction {
  /**
     * @var Implementation
     */
 protected:
  Implementation* implementation_;

 public:
  Abstraction(Implementation* implementation) : implementation_(implementation) {
  }

  virtual ~Abstraction() {
  }

  virtual std::string Operation() const {
    return "Abstraction: Base operation with:\n" +
           this->implementation_->OperationImplementation();
  }
};
/**
 *You can extend the Abstraction without changing the Implementation
 * classes.
 */
class ExtendedAbstraction : public Abstraction {
 public:
  ExtendedAbstraction(Implementation* implementation) : Abstraction(implementation) {
  }
  std::string Operation() const override {
    return "ExtendedAbstraction: Extended operation with:\n" +
           this->implementation_->OperationImplementation();
  }
};

/**
 *Except for the initialization phase, where an Abstraction object gets
 * linked with a specific Implementation object, the client code should only
 * depend on the Abstraction class. This way the client code can support any
 * abstraction-implementation combination.
 */
void ClientCode(const Abstraction& abstraction) {
  // ...
  std::cout << abstraction.Operation();
  // ...
}
/**
 *The client code should be able to work with any pre-configured
 * abstraction-implementation combination.
 */

int main() {
  Implementation* implementation = new ConcreteImplementationA;
  Abstraction* abstraction = new Abstraction(implementation);
  ClientCode(*abstraction);
  std::cout << std::endl;
  delete implementation;
  delete abstraction;

  implementation = new ConcreteImplementationB;
  abstraction = new ExtendedAbstraction(implementation);
  ClientCode(*abstraction);

  delete implementation;
  delete abstraction;

  return 0;
}

//text output
//Abstraction: Base operation with:
//ConcreteImplementationA: Here's the result on the platform A.
//ExtendedAbstraction: Extended operation with:
//ConcreteImplementationB: Here's the result on the platform B.
```
---

## When to Use

- Implementation of the Bridge design pattern
- When you need the specific functionality provided by this pattern

---

## References

- [Refactoring Guru: Bridge Pattern](https://refactoring.guru/design-patterns/bridge)
- [Wikipedia: Bridge Pattern](https://en.wikipedia.org/wiki/Bridge_pattern)
- [GitHub: Design Patterns C++](https://github.com/RefactoringGuru/design-patterns-cpp.git)
- [GitHub: Design Patterns Python](https://github.com/RefactoringGuru/design-patterns-python.git)
---

> This work is licensed under a [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](https://creativecommons.org/licenses/by-nc-nd/4.0/).
