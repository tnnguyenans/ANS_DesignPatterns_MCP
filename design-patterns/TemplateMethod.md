# TemplateMethod Design Pattern

**Intent:**\
Defines the skeleton of an algorithm in the superclass but lets subclasses override specific steps of the algorithm without changing its structure.
---

## Python
```python
"""
Template Method Design Pattern

Intent: Defines the skeleton of an algorithm in the superclass but lets
subclasses override specific steps of the algorithm without changing its
structure.

from abc import ABC, abstractmethod

class AbstractClass(ABC):
    """
The Abstract Class defines a template method that contains a skeleton of
    some algorithm, composed of calls to (usually) abstract primitive
    operations.

    Concrete subclasses should implement these operations, but leave the
    template method itself intact.

    def template_method(self) -> None:
        """
The template method defines the skeleton of an algorithm.

        self.base_operation1()
        self.required_operations1()
        self.base_operation2()
        self.hook1()
        self.required_operations2()
        self.base_operation3()
        self.hook2()

    #These operations already have implementations.

    def base_operation1(self) -> None:
        print("AbstractClass says: I am doing the bulk of the work")

    def base_operation2(self) -> None:
        print("AbstractClass says: But I let subclasses override some operations")

    def base_operation3(self) -> None:
        print("AbstractClass says: But I am doing the bulk of the work anyway")

    #These operations have to be implemented in subclasses.

    @abstractmethod
    def required_operations1(self) -> None:
        pass

    @abstractmethod
    def required_operations2(self) -> None:
        pass

    #These are "hooks." Subclasses may override them, but it's not
    # mandatory since the hooks already have default (but empty) implementation.
    # Hooks provide additional extension points in some crucial places of the
    # algorithm.

    def hook1(self) -> None:
        pass

    def hook2(self) -> None:
        pass

class ConcreteClass1(AbstractClass):
    """
Concrete classes have to implement all abstract operations of the base
    class. They can also override some operations with a default implementation.

    def required_operations1(self) -> None:
        print("ConcreteClass1 says: Implemented Operation1")

    def required_operations2(self) -> None:
        print("ConcreteClass1 says: Implemented Operation2")

class ConcreteClass2(AbstractClass):
    """
Usually, concrete classes override only a fraction of base class'
    operations.

    def required_operations1(self) -> None:
        print("ConcreteClass2 says: Implemented Operation1")

    def required_operations2(self) -> None:
        print("ConcreteClass2 says: Implemented Operation2")

    def hook1(self) -> None:
        print("ConcreteClass2 says: Overridden Hook1")

def client_code(abstract_class: AbstractClass) -> None:
    """
The client code calls the template method to execute the algorithm.
    Client code does not have to know the concrete class of an object it works
    with, as long as it works with objects through the interface of their base
    class.

    # ...
    abstract_class.template_method()
    # ...

if __name__ == "__main__":
    print("Same client code can work with different subclasses:")
    client_code(ConcreteClass1())
    print("")

    print("Same client code can work with different subclasses:")
    client_code(ConcreteClass2())

# text output
# Same client code can work with different subclasses:
# AbstractClass says: I am doing the bulk of the work
# ConcreteClass1 says: Implemented Operation1
# AbstractClass says: But I let subclasses override some operations
# ConcreteClass1 says: Implemented Operation2
# AbstractClass says: But I am doing the bulk of the work anyway
# Same client code can work with different subclasses:
# AbstractClass says: I am doing the bulk of the work
# ConcreteClass2 says: Implemented Operation1
# AbstractClass says: But I let subclasses override some operations
# ConcreteClass2 says: Overridden Hook1
# ConcreteClass2 says: Implemented Operation2
# AbstractClass says: But I am doing the bulk of the work anyway
```
---

## C++
```cpp
#include <iostream>

/**
 *Template Method Design Pattern
 * Intent: Defines the skeleton of an algorithm in the superclass but lets
 * subclasses override specific steps of the algorithm without changing its
 * structure.
 */
/**
 *The Abstract Class defines a template method that contains a skeleton of
 * some algorithm, composed of calls to (usually) abstract primitive operations.
 * Concrete subclasses should implement these operations, but leave the template
 * method itself intact.
 */
class AbstractClass {
  /**
     *The template method defines the skeleton of an algorithm.
     */
 public:
  void TemplateMethod() const {
    this->BaseOperation1();
    this->RequiredOperations1();
    this->BaseOperation2();
    this->Hook1();
    this->RequiredOperation2();
    this->BaseOperation3();
    this->Hook2();
  }
  /**
     *These operations already have implementations.
     */
 protected:
  void BaseOperation1() const {
    std::cout << "AbstractClass says: I am doing the bulk of the work\n";
  }
  void BaseOperation2() const {
    std::cout << "AbstractClass says: But I let subclasses override some operations\n";
  }
  void BaseOperation3() const {
    std::cout << "AbstractClass says: But I am doing the bulk of the work anyway\n";
  }
  /**
     *These operations have to be implemented in subclasses.
     */
  virtual void RequiredOperations1() const = 0;
  virtual void RequiredOperation2() const = 0;
  /**
     *These are "hooks." Subclasses may override them, but it's not
     * mandatory since the hooks already have default (but empty)
     * implementation. Hooks provide additional extension points in some crucial
     * places of the algorithm.
     */
  virtual void Hook1() const {}
  virtual void Hook2() const {}
};
/**
 *Concrete classes have to implement all abstract operations of the base
 * class. They can also override some operations with a default implementation.
 */
class ConcreteClass1 : public AbstractClass {
 protected:
  void RequiredOperations1() const override {
    std::cout << "ConcreteClass1 says: Implemented Operation1\n";
  }
  void RequiredOperation2() const override {
    std::cout << "ConcreteClass1 says: Implemented Operation2\n";
  }
};
/**
 *Usually, concrete classes override only a fraction of base class'
 * operations.
 */
class ConcreteClass2 : public AbstractClass {
 protected:
  void RequiredOperations1() const override {
    std::cout << "ConcreteClass2 says: Implemented Operation1\n";
  }
  void RequiredOperation2() const override {
    std::cout << "ConcreteClass2 says: Implemented Operation2\n";
  }
  void Hook1() const override {
    std::cout << "ConcreteClass2 says: Overridden Hook1\n";
  }
};
/**
 *The client code calls the template method to execute the algorithm.
 * Client code does not have to know the concrete class of an object it works
 * with, as long as it works with objects through the interface of their base
 * class.
 */
void ClientCode(AbstractClass *class_) {
  // ...
  class_->TemplateMethod();
  // ...
}

int main() {
  std::cout << "Same client code can work with different subclasses:\n";
  ConcreteClass1 *concreteClass1 = new ConcreteClass1;
  ClientCode(concreteClass1);
  std::cout << "\n";
  std::cout << "Same client code can work with different subclasses:\n";
  ConcreteClass2 *concreteClass2 = new ConcreteClass2;
  ClientCode(concreteClass2);
  delete concreteClass1;
  delete concreteClass2;
  return 0;
}

//text output
//Same client code can work with different subclasses:
//AbstractClass says: I am doing the bulk of the work
//ConcreteClass1 says: Implemented Operation1
//AbstractClass says: But I let subclasses override some operations
//ConcreteClass1 says: Implemented Operation2
//AbstractClass says: But I am doing the bulk of the work anyway
//Same client code can work with different subclasses:
//AbstractClass says: I am doing the bulk of the work
//ConcreteClass2 says: Implemented Operation1
//AbstractClass says: But I let subclasses override some operations
//ConcreteClass2 says: Overridden Hook1
//ConcreteClass2 says: Implemented Operation2
//AbstractClass says: But I am doing the bulk of the work anyway
```
---

## When to Use

- Implementation of the TemplateMethod design pattern
- When you need the specific functionality provided by this pattern

---

## References

- [Refactoring Guru: TemplateMethod Pattern](https://refactoring.guru/design-patterns/templatemethod)
- [Wikipedia: TemplateMethod Pattern](https://en.wikipedia.org/wiki/TemplateMethod_pattern)
- [GitHub: Design Patterns C++](https://github.com/RefactoringGuru/design-patterns-cpp.git)
- [GitHub: Design Patterns Python](https://github.com/RefactoringGuru/design-patterns-python.git)
---

> This work is licensed under a [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](https://creativecommons.org/licenses/by-nc-nd/4.0/).
