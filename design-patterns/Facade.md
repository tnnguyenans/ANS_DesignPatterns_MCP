# Facade Design Pattern

**Intent:**\
Provides a simplified interface to a library, a framework, or any other complex set of classes.
---

## Python
```python
"""
Facade Design Pattern

Intent: Provides a simplified interface to a library, a framework, or any other
complex set of classes.

from __future__ import annotations

class Facade:
    """
The Facade class provides a simple interface to the complex logic of one
    or several subsystems. The Facade delegates the client requests to the
    appropriate objects within the subsystem. The Facade is also responsible for
    managing their lifecycle. All of this shields the client from the undesired
    complexity of the subsystem.

    def __init__(self, subsystem1: Subsystem1, subsystem2: Subsystem2) -> None:
        """
Depending on your application's needs, you can provide the Facade
        with existing subsystem objects or force the Facade to create them on
        its own.

        self._subsystem1 = subsystem1 or Subsystem1()
        self._subsystem2 = subsystem2 or Subsystem2()

    def operation(self) -> str:
        """
The Facade's methods are convenient shortcuts to the sophisticated
        functionality of the subsystems. However, clients get only to a fraction
        of a subsystem's capabilities.

        results = []
        results.append("Facade initializes subsystems:")
        results.append(self._subsystem1.operation1())
        results.append(self._subsystem2.operation1())
        results.append("Facade orders subsystems to perform the action:")
        results.append(self._subsystem1.operation_n())
        results.append(self._subsystem2.operation_z())
        return "\n".join(results)

class Subsystem1:
    """
The Subsystem can accept requests either from the facade or client
    directly. In any case, to the Subsystem, the Facade is yet another client,
    and it's not a part of the Subsystem.

    def operation1(self) -> str:
        return "Subsystem1: Ready!"

    # ...

    def operation_n(self) -> str:
        return "Subsystem1: Go!"

class Subsystem2:
    """
Some facades can work with multiple subsystems at the same time.

    def operation1(self) -> str:
        return "Subsystem2: Get ready!"

    # ...

    def operation_z(self) -> str:
        return "Subsystem2: Fire!"

def client_code(facade: Facade) -> None:
    """
The client code works with complex subsystems through a simple interface
    provided by the Facade. When a facade manages the lifecycle of the
    subsystem, the client might not even know about the existence of the
    subsystem. This approach lets you keep the complexity under control.

    print(facade.operation(), end="")

if __name__ == "__main__":
    #The client code may have some of the subsystem's objects already
    # created. In this case, it might be worthwhile to initialize the Facade
    # with these objects instead of letting the Facade create new instances.

# text output
# Facade initializes subsystems:
# Subsystem1: Ready!
# Subsystem2: Get ready!
# Facade orders subsystems to perform the action:
# Subsystem1: Go!
# Subsystem2: Fire!
```
---

## C++
```cpp
#include <iostream>
#include <string>

/**
 *Facade Design Pattern
 * Intent: Provides a simplified interface to a library, a framework, or any
 * other complex set of classes.
 */

/**
 *The Subsystem can accept requests either from the facade or client
 * directly. In any case, to the Subsystem, the Facade is yet another client,
 * and it's not a part of the Subsystem.
 */
class Subsystem1 {
 public:
  std::string Operation1() const {
    return "Subsystem1: Ready!\n";
  }
  // ...
  std::string OperationN() const {
    return "Subsystem1: Go!\n";
  }
};
/**
 *Some facades can work with multiple subsystems at the same time.
 */
class Subsystem2 {
 public:
  std::string Operation1() const {
    return "Subsystem2: Get ready!\n";
  }
  // ...
  std::string OperationZ() const {
    return "Subsystem2: Fire!\n";
  }
};

/**
 *The Facade class provides a simple interface to the complex logic of one
 * or several subsystems. The Facade delegates the client requests to the
 * appropriate objects within the subsystem. The Facade is also responsible for
 * managing their lifecycle. All of this shields the client from the undesired
 * complexity of the subsystem.
 */
class Facade {
 protected:
  Subsystem1 *subsystem1_;
  Subsystem2 *subsystem2_;
  /**
     *Depending on your application's needs, you can provide the Facade
     * with existing subsystem objects or force the Facade to create them on its
     * own.
     */
 public:
  /**
     *In this case we will delegate the memory ownership to Facade Class
     */
  Facade(
      Subsystem1 *subsystem1 = nullptr,
      Subsystem2 *subsystem2 = nullptr) {
    this->subsystem1_ = subsystem1 ?: new Subsystem1;
    this->subsystem2_ = subsystem2 ?: new Subsystem2;
  }
  ~Facade() {
    delete subsystem1_;
    delete subsystem2_;
  }
  /**
     *The Facade's methods are convenient shortcuts to the sophisticated
     * functionality of the subsystems. However, clients get only to a fraction
     * of a subsystem's capabilities.
     */
  std::string Operation() {
    std::string result = "Facade initializes subsystems:\n";
    result += this->subsystem1_->Operation1();
    result += this->subsystem2_->Operation1();
    result += "Facade orders subsystems to perform the action:\n";
    result += this->subsystem1_->OperationN();
    result += this->subsystem2_->OperationZ();
    return result;
  }
};

/**
 *The client code works with complex subsystems through a simple interface
 * provided by the Facade. When a facade manages the lifecycle of the subsystem,
 * the client might not even know about the existence of the subsystem. This
 * approach lets you keep the complexity under control.
 */
void ClientCode(Facade *facade) {
  // ...
  std::cout << facade->Operation();
  // ...
}
/**
 *The client code may have some of the subsystem's objects already created.
 * In this case, it might be worthwhile to initialize the Facade with these
 * objects instead of letting the Facade create new instances.
 */

int main() {
  Subsystem1 *subsystem1 = new Subsystem1;
  Subsystem2 *subsystem2 = new Subsystem2;
  Facade *facade = new Facade(subsystem1, subsystem2);
  ClientCode(facade);

  delete facade;

  return 0;
}

//text output
//Facade initializes subsystems:
//Subsystem1: Ready!
//Subsystem2: Get ready!
//Facade orders subsystems to perform the action:
//Subsystem1: Go!
//Subsystem2: Fire!
```
---

## When to Use

- Implementation of the Facade design pattern
- When you need the specific functionality provided by this pattern

---

## References

- [Refactoring Guru: Facade Pattern](https://refactoring.guru/design-patterns/facade)
- [Wikipedia: Facade Pattern](https://en.wikipedia.org/wiki/Facade_pattern)
- [GitHub: Design Patterns C++](https://github.com/RefactoringGuru/design-patterns-cpp.git)
- [GitHub: Design Patterns Python](https://github.com/RefactoringGuru/design-patterns-python.git)
---

> This work is licensed under a [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](https://creativecommons.org/licenses/by-nc-nd/4.0/).
