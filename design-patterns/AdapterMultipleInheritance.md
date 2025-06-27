# Adapter Design Pattern-MultipleInheritance

**Intent:**\
Provides a unified interface that allows objects with incompatible interfaces to collaborate using multiple inheritance.
---

## Python
```python
"""
Adapter Design Pattern

Intent: Provides a unified interface that allows objects with incompatible
interfaces to collaborate.
"""


class Target:
    """
    The Target defines the domain-specific interface used by the client
    code.
    """

    def request(self) -> str:
        return "Target: The default target's behavior."


class Adaptee:
    """
    The Adaptee contains some useful behavior, but its interface is
    incompatible with the existing client code. The Adaptee needs some
    adaptation before the client code can use it.
    """

    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"


class Adapter(Target, Adaptee):
    """
    The Adapter makes the Adaptee's interface compatible with the Target's
    interface using multiple inheritance. In Python, this allows the adapter
    to inherit from both Target and Adaptee classes.
    """

    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.specific_request()[::-1]}"


def client_code(target: Target) -> None:
    """
    The client code supports all classes that follow the Target interface.
    """

    print(target.request(), end="")


if __name__ == "__main__":
    print("Client: I can work just fine with the Target objects:")
    target = Target()
    client_code(target)
    print("\n")

    adaptee = Adaptee()
    print("Client: The Adaptee class has a weird interface. "
          "See, I don't understand it:")
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

    print("Client: But I can work with it via the Adapter:")
    adapter = Adapter()
    client_code(adapter)

# text output
# Client: I can work just fine with the Target objects:
# Target: The default target's behavior.
# 
# Client: The Adaptee class has a weird interface. See, I don't understand it:
# Adaptee: .eetpadA eht fo roivaheb laicepS
# 
# Client: But I can work with it via the Adapter:
# Adapter: (TRANSLATED) Special behavior of the Adaptee.
```
---

## C++
```cpp
#include <algorithm>
#include <iostream>
#include <string>

/**
 * Adapter Design Pattern
 *
 * Intent: Provides a unified interface that allows objects with incompatible
 * interfaces to collaborate.
 */

/**
 * The Target defines the domain-specific interface used by the client code.
 */
class Target {
 public:
  virtual ~Target() = default;
  virtual std::string Request() const {
    return "Target: The default target's behavior.";
  }
};

/**
 * The Adaptee contains some useful behavior, but its interface is
 * incompatible with the existing client code. The Adaptee needs some adaptation
 * before the client code can use it.
 */
class Adaptee {
 public:
  std::string SpecificRequest() const {
    return ".eetpadA eht fo roivaheb laicepS";
  }
};

/**
 * The Adapter makes the Adaptee's interface compatible with the Target's
 * interface using multiple inheritance.
 */
class Adapter : public Target, public Adaptee {
 public:
  Adapter() {}
  std::string Request() const override {
    std::string to_reverse = SpecificRequest();
    std::reverse(to_reverse.begin(), to_reverse.end());
    return "Adapter: (TRANSLATED) " + to_reverse;
  }
};

/**
 * The client code supports all classes that follow the Target interface.
 */
void ClientCode(const Target *target) {
  std::cout << target->Request();
}

int main() {
  std::cout << "Client: I can work just fine with the Target objects:\n";
  Target *target = new Target;
  ClientCode(target);
  std::cout << "\n\n";
  Adaptee *adaptee = new Adaptee;
  std::cout << "Client: The Adaptee class has a weird interface. See, I don't understand it:\n";
  std::cout << "Adaptee: " << adaptee->SpecificRequest();
  std::cout << "\n\n";
  std::cout << "Client: But I can work with it via the Adapter:\n";
  Adapter *adapter = new Adapter;
  ClientCode(adapter);
  std::cout << "\n";

  delete target;
  delete adaptee;
  delete adapter;

  return 0;
}

//text output
//Client: I can work just fine with the Target objects:
//Target: The default target's behavior.
//
//Client: The Adaptee class has a weird interface. See, I don't understand it:
//Adaptee: .eetpadA eht fo roivaheb laicepS
//
//Client: But I can work with it via the Adapter:
//Adapter: (TRANSLATED) Special behavior of the Adaptee.
```
---

## When to Use

- When you want to use multiple inheritance to create an adapter that inherits from both the target interface and the adaptee
- In C++, when you need the adapter to be both a Target and an Adaptee simultaneously
- When you prefer inheritance over composition for the adapter pattern implementation
- When the adaptee class doesn't have conflicting method signatures with the target class

---

## Key Differences from Composition-based Adapter

- **Multiple Inheritance**: The adapter inherits from both Target and Adaptee classes
- **Direct Access**: Can directly call adaptee methods without composition
- **Memory Efficiency**: No need to store a reference to the adaptee object
- **Language Support**: Works well in C++, also supported in Python

---

## References

- [Refactoring Guru: Adapter Pattern](https://refactoring.guru/design-patterns/adapter)
- [Wikipedia: Adapter Pattern](https://en.wikipedia.org/wiki/Adapter_pattern)
- [GitHub: Design Patterns C++](https://github.com/RefactoringGuru/design-patterns-cpp.git)
- [GitHub: Design Patterns Python](https://github.com/RefactoringGuru/design-patterns-python.git)
---

> This work is licensed under a [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](https://creativecommons.org/licenses/by-nc-nd/4.0/).
