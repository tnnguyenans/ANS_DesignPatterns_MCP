# State Design Pattern

**Intent:**\
Lets an object alter its behavior when its internal state changes. It appears as if the object changed its class.
---

## Python
```python
"""
State Design Pattern

Intent: Lets an object alter its behavior when its internal state changes. It
appears as if the object changed its class.

from __future__ import annotations
from abc import ABC, abstractmethod

class Context:
    """
The Context defines the interface of interest to clients. It also
    maintains a reference to an instance of a State subclass, which represents
    the current state of the Context.

    _state = None
    """
A reference to the current state of the Context.

    def __init__(self, state: State) -> None:
        self.transition_to(state)

    def transition_to(self, state: State):
        """
The Context allows changing the State object at runtime.

        print(f"Context: Transition to {type(state).__name__}")
        self._state = state
        self._state.context = self

    """
The Context delegates part of its behavior to the current State object.

    def request1(self):
        self._state.handle1()

    def request2(self):
        self._state.handle2()

class State(ABC):
    """
The base State class declares methods that all Concrete State should
    implement and also provides a backreference to the Context object,
    associated with the State. This backreference can be used by States to
    transition the Context to another State.

    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context: Context) -> None:
        self._context = context

    @abstractmethod
    def handle1(self) -> None:
        pass

    @abstractmethod
    def handle2(self) -> None:
        pass

"""
Concrete States implement various behaviors, associated with a state of the
Context.

class ConcreteStateA(State):
    def handle1(self) -> None:
        print("ConcreteStateA handles request1.")
        print("ConcreteStateA wants to change the state of the context.")
        self.context.transition_to(ConcreteStateB())

    def handle2(self) -> None:
        print("ConcreteStateA handles request2.")

class ConcreteStateB(State):
    def handle1(self) -> None:
        print("ConcreteStateB handles request1.")

    def handle2(self) -> None:
        print("ConcreteStateB handles request2.")
        print("ConcreteStateB wants to change the state of the context.")
        self.context.transition_to(ConcreteStateA())

if __name__ == "__main__":
    #The client code.

    context = Context(ConcreteStateA())
    context.request1()
    context.request2()

# text output
# Context: Transition to ConcreteStateA
# ConcreteStateA handles request1.
# ConcreteStateA wants to change the state of the context.
# Context: Transition to ConcreteStateB
# ConcreteStateB handles request2.
# ConcreteStateB wants to change the state of the context.
# Context: Transition to ConcreteStateA
```
---

## C++
```cpp
#include <iostream>
#include <typeinfo>
/**
 *State Design Pattern
 * Intent: Lets an object alter its behavior when its internal state changes. It
 * appears as if the object changed its class.
 */

/**
 *The base State class declares methods that all Concrete State should
 * implement and also provides a backreference to the Context object, associated
 * with the State. This backreference can be used by States to transition the
 * Context to another State.
 */

class Context;

class State {
  /**
     * @var Context
     */
 protected:
  Context *context_;

 public:
  virtual ~State() {
  }

  void set_context(Context *context) {
    this->context_ = context;
  }

  virtual void Handle1() = 0;
  virtual void Handle2() = 0;
};

/**
 *The Context defines the interface of interest to clients. It also
 * maintains a reference to an instance of a State subclass, which represents
 * the current state of the Context.
 */
class Context {
  /**
     *@var State A reference to the current state of the Context.
     */
 private:
  State *state_;

 public:
  Context(State *state) : state_(nullptr) {
    this->TransitionTo(state);
  }
  ~Context() {
    delete state_;
  }
  /**
     *The Context allows changing the State object at runtime.
     */
  void TransitionTo(State *state) {
    std::cout << "Context: Transition to " << typeid(*state).name() << ".\n";
    if (this->state_ != nullptr)
      delete this->state_;
    this->state_ = state;
    this->state_->set_context(this);
  }
  /**
     *The Context delegates part of its behavior to the current State
     * object.
     */
  void Request1() {
    this->state_->Handle1();
  }
  void Request2() {
    this->state_->Handle2();
  }
};

/**
 *Concrete States implement various behaviors, associated with a state of
 * the Context.
 */

class ConcreteStateA : public State {
 public:
  void Handle1() override;

  void Handle2() override {
    std::cout << "ConcreteStateA handles request2.\n";
  }
};

class ConcreteStateB : public State {
 public:
  void Handle1() override {
    std::cout << "ConcreteStateB handles request1.\n";
  }
  void Handle2() override {
    std::cout << "ConcreteStateB handles request2.\n";
    std::cout << "ConcreteStateB wants to change the state of the context.\n";
    this->context_->TransitionTo(new ConcreteStateA);
  }
};

void ConcreteStateA::Handle1() {
  {
    std::cout << "ConcreteStateA handles request1.\n";
    std::cout << "ConcreteStateA wants to change the state of the context.\n";

    this->context_->TransitionTo(new ConcreteStateB);
  }
}

/**
 *The client code.
 */
void ClientCode() {
  Context *context = new Context(new ConcreteStateA);
  context->Request1();
  context->Request2();
  delete context;
}

int main() {
  ClientCode();
  return 0;
}

//text output
//Context: Transition to 14ConcreteStateA.
//ConcreteStateA handles request1.
//ConcreteStateA wants to change the state of the context.
//Context: Transition to 14ConcreteStateB.
//ConcreteStateB handles request2.
//ConcreteStateB wants to change the state of the context.
//Context: Transition to 14ConcreteStateA.
```
---

## When to Use

- Implementation of the State design pattern
- When you need the specific functionality provided by this pattern

---

## References

- [Refactoring Guru: State Pattern](https://refactoring.guru/design-patterns/state)
- [Wikipedia: State Pattern](https://en.wikipedia.org/wiki/State_pattern)
- [GitHub: Design Patterns C++](https://github.com/RefactoringGuru/design-patterns-cpp.git)
- [GitHub: Design Patterns Python](https://github.com/RefactoringGuru/design-patterns-python.git)
---

> This work is licensed under a [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](https://creativecommons.org/licenses/by-nc-nd/4.0/).
