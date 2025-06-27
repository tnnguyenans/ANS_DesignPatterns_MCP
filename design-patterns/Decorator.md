# Decorator Design Pattern

**Intent:**\
Lets you attach new behaviors to objects by placing these objects inside special wrapper objects that contain the behaviors.
---

## Python
```python
"""
Decorator Design Pattern

Intent: Lets you attach new behaviors to objects by placing these objects inside
special wrapper objects that contain the behaviors.

class Component():
    """
The base Component interface defines operations that can be altered by
    decorators.

    def operation(self) -> str:
        pass

class ConcreteComponent(Component):
    """
Concrete Components provide default implementations of the operations.
    There might be several variations of these classes.

    def operation(self) -> str:
        return "ConcreteComponent"

class Decorator(Component):
    """
The base Decorator class follows the same interface as the other
    components. The primary purpose of this class is to define the wrapping
    interface for all concrete decorators. The default implementation of the
    wrapping code might include a field for storing a wrapped component and the
    means to initialize it.

    _component: Component = None

    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> Component:
        """
The Decorator delegates all work to the wrapped component.

        return self._component

    def operation(self) -> str:
        return self._component.operation()

class ConcreteDecoratorA(Decorator):
    """
Concrete Decorators call the wrapped object and alter its result in some
    way.

    def operation(self) -> str:
        """
Decorators may call parent implementation of the operation, instead
        of calling the wrapped object directly. This approach simplifies
        extension of decorator classes.

class ConcreteDecoratorB(Decorator):
    """
Decorators can execute their behavior either before or after the call to
    a wrapped object.

    def operation(self) -> str:
        return f"ConcreteDecoratorB({self.component.operation()})"

def client_code(component: Component) -> None:
    """
The client code works with all objects using the Component interface.
    This way it can stay independent of the concrete classes of components it
    works with.

    # ...

    print(f"RESULT: {component.operation()}", end="")

    # ...

if __name__ == "__main__":
    #This way the client code can support both simple components...

    #...as well as decorated ones.
    # Note how decorators can wrap not only simple components but the other
    # decorators as well.

# text output
# Client: I've got a simple component:
# RESULT: ConcreteComponent
# Client: Now I've got a decorated component:
# RESULT: ConcreteDecoratorB(ConcreteDecoratorA(ConcreteComponent))
```
---

## C++
```cpp
#include <iostream>
#include <string>

/**
 *Decorator Design Pattern
 * Intent: Lets you attach new behaviors to objects by placing these objects
 * inside special wrapper objects that contain the behaviors.
 */
/**
 *The base Component interface defines operations that can be altered by
 * decorators.
 */
class Component {
 public:
  virtual ~Component() {}
  virtual std::string Operation() const = 0;
};
/**
 *Concrete Components provide default implementations of the operations.
 * There might be several variations of these classes.
 */
class ConcreteComponent : public Component {
 public:
  std::string Operation() const override {
    return "ConcreteComponent";
  }
};
/**
 *The base Decorator class follows the same interface as the other
 * components. The primary purpose of this class is to define the wrapping
 * interface for all concrete decorators. The default implementation of the
 * wrapping code might include a field for storing a wrapped component and the
 * means to initialize it.
 */
class Decorator : public Component {
  /**
     * @var Component
     */
 protected:
  Component* component_;

 public:
  Decorator(Component* component) : component_(component) {
  }
  /**
     *The Decorator delegates all work to the wrapped component.
     */
  std::string Operation() const override {
    return this->component_->Operation();
  }
};
/**
 *Concrete Decorators call the wrapped object and alter its result in some
 * way.
 */
class ConcreteDecoratorA : public Decorator {
  /**
     *Decorators may call parent implementation of the operation, instead
     * of calling the wrapped object directly. This approach simplifies
     * extension of decorator classes.
     */
 public:
  ConcreteDecoratorA(Component* component) : Decorator(component) {
  }
  std::string Operation() const override {
    return "ConcreteDecoratorA(" + Decorator::Operation() + ")";
  }
};
/**
 *Decorators can execute their behavior either before or after the call to
 * a wrapped object.
 */
class ConcreteDecoratorB : public Decorator {
 public:
  ConcreteDecoratorB(Component* component) : Decorator(component) {
  }

  std::string Operation() const override {
    return "ConcreteDecoratorB(" + Decorator::Operation() + ")";
  }
};
/**
 *The client code works with all objects using the Component interface.
 * This way it can stay independent of the concrete classes of components it
 * works with.
 */
void ClientCode(Component* component) {
  // ...
  std::cout << "RESULT: " << component->Operation();
  // ...
}

int main() {
  /**
 *This way the client code can support both simple components...
 */
  Component* simple = new ConcreteComponent;
  std::cout << "Client: I've got a simple component:\n";
  ClientCode(simple);
  std::cout << "\n\n";
  /**
 *...as well as decorated ones.
 * Note how decorators can wrap not only simple components but the other
 * decorators as well.
 */
  Component* decorator1 = new ConcreteDecoratorA(simple);
  Component* decorator2 = new ConcreteDecoratorB(decorator1);
  std::cout << "Client: Now I've got a decorated component:\n";
  ClientCode(decorator2);
  std::cout << "\n";

  delete simple;
  delete decorator1;
  delete decorator2;

  return 0;
}

//text output
//Client: I've got a simple component:
//RESULT: ConcreteComponent
//Client: Now I've got a decorated component:
//RESULT: ConcreteDecoratorB(ConcreteDecoratorA(ConcreteComponent))
```
---

## When to Use

- Implementation of the Decorator design pattern
- When you need the specific functionality provided by this pattern

---

## References

- [Refactoring Guru: Decorator Pattern](https://refactoring.guru/design-patterns/decorator)
- [Wikipedia: Decorator Pattern](https://en.wikipedia.org/wiki/Decorator_pattern)
- [GitHub: Design Patterns C++](https://github.com/RefactoringGuru/design-patterns-cpp.git)
- [GitHub: Design Patterns Python](https://github.com/RefactoringGuru/design-patterns-python.git)
---

> This work is licensed under a [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](https://creativecommons.org/licenses/by-nc-nd/4.0/).
