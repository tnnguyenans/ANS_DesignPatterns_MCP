# Command Design Pattern

**Intent:**\
Turns a request into a stand-alone object that contains all information about the request.
---

## Python
```python
"""
Command Design Pattern

Intent: Turns a request into a stand-alone object that contains all information
about the request. This transformation lets you parameterize methods with
different requests, delay or queue a request's execution, and support undoable
operations.

from __future__ import annotations
from abc import ABC, abstractmethod

class Command(ABC):
    """
The Command interface declares a method for executing a command.

    @abstractmethod
    def execute(self) -> None:
        pass

class SimpleCommand(Command):
    """
Some commands can implement simple operations on their own.

    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self) -> None:
        print(f"SimpleCommand: See, I can do simple things like printing"
              f"({self._payload})")

class ComplexCommand(Command):
    """
However, some commands can delegate more complex operations to other
    objects, called "receivers."

    def __init__(self, receiver: Receiver, a: str, b: str) -> None:
        """
Complex commands can accept one or several receiver objects along
        with any context data via the constructor.

        self._receiver = receiver
        self._a = a
        self._b = b

    def execute(self) -> None:
        """
Commands can delegate to any methods of a receiver.

        print("ComplexCommand: Complex stuff should be done by a receiver object", end="")
        self._receiver.do_something(self._a)
        self._receiver.do_something_else(self._b)

class Receiver:
    """
The Receiver classes contain some important business logic. They know
    how to perform all kinds of operations, associated with carrying out a
    request. In fact, any class may serve as a Receiver.

    def do_something(self, a: str) -> None:
        print(f"\nReceiver: Working on ({a}.)", end="")

    def do_something_else(self, b: str) -> None:
        print(f"\nReceiver: Also working on ({b}.)", end="")

class Invoker:
    """
The Invoker is associated with one or several commands. It sends a
    request to the command.

    _on_start = None
    _on_finish = None

    """
Initialize commands.

    def set_on_start(self, command: Command):
        self._on_start = command

    def set_on_finish(self, command: Command):
        self._on_finish = command

    def do_something_important(self) -> None:
        """
The Invoker does not depend on concrete command or receiver classes.
        The Invoker passes a request to a receiver indirectly, by executing a
        command.

        print("Invoker: Does anybody want something done before I begin?")
        if isinstance(self._on_start, Command):
            self._on_start.execute()

        print("Invoker: ...doing something really important...")

        print("Invoker: Does anybody want something done after I finish?")
        if isinstance(self._on_finish, Command):
            self._on_finish.execute()

if __name__ == "__main__":
    """
The client code can parameterize an invoker with any commands.

    invoker = Invoker()
    invoker.set_on_start(SimpleCommand("Say Hi!"))
    receiver = Receiver()
    invoker.set_on_finish(ComplexCommand(
        receiver, "Send email", "Save report"))

    invoker.do_something_important()

# text output
# Invoker: Does anybody want something done before I begin?
# SimpleCommand: See, I can do simple things like printing (Say Hi!)
# Invoker: ...doing something really important...
# Invoker: Does anybody want something done after I finish?
# ComplexCommand: Complex stuff should be done by a receiver object
# Receiver: Working on (Send email.)
# Receiver: Also working on (Save report.)
```
---

## C++
```cpp
#include <iostream>
#include <string>

/**
 *Command Design Pattern
 * Intent: Turns a request into a stand-alone object that contains all
 * information about the request. This transformation lets you parameterize
 * methods with different requests, delay or queue a request's execution, and
 * support undoable operations.
 */
/**
 *The Command interface declares a method for executing a command.
 */
class Command {
 public:
  virtual ~Command() {
  }
  virtual void Execute() const = 0;
};
/**
 *Some commands can implement simple operations on their own.
 */
class SimpleCommand : public Command {
 private:
  std::string pay_load_;

 public:
  explicit SimpleCommand(std::string pay_load) : pay_load_(pay_load) {
  }
  void Execute() const override {
    std::cout << "SimpleCommand: See, I can do simple things like printing (" << this->pay_load_ << ")\n";
  }
};

/**
 *The Receiver classes contain some important business logic. They know how
 * to perform all kinds of operations, associated with carrying out a request.
 * In fact, any class may serve as a Receiver.
 */
class Receiver {
 public:
  void DoSomething(const std::string &a) {
    std::cout << "Receiver: Working on (" << a << ".)\n";
  }
  void DoSomethingElse(const std::string &b) {
    std::cout << "Receiver: Also working on (" << b << ".)\n";
  }
};

/**
 *However, some commands can delegate more complex operations to other
 * objects, called "receivers."
 */
class ComplexCommand : public Command {
  /**
     * @var Receiver
     */
 private:
  Receiver *receiver_;
  /**
     *Context data, required for launching the receiver's methods.
     */
  std::string a_;
  std::string b_;
  /**
     *Complex commands can accept one or several receiver objects along
     * with any context data via the constructor.
     */
 public:
  ComplexCommand(Receiver *receiver, std::string a, std::string b) : receiver_(receiver), a_(a), b_(b) {
  }
  /**
     *Commands can delegate to any methods of a receiver.
     */
  void Execute() const override {
    std::cout << "ComplexCommand: Complex stuff should be done by a receiver object.\n";
    this->receiver_->DoSomething(this->a_);
    this->receiver_->DoSomethingElse(this->b_);
  }
};

/**
 *The Invoker is associated with one or several commands. It sends a
 * request to the command.
 */
class Invoker {
  /**
     * @var Command
     */
 private:
  Command *on_start_;
  /**
     * @var Command
     */
  Command *on_finish_;
  /**
     *Initialize commands.
     */
 public:
  ~Invoker() {
    delete on_start_;
    delete on_finish_;
  }

  void SetOnStart(Command *command) {
    this->on_start_ = command;
  }
  void SetOnFinish(Command *command) {
    this->on_finish_ = command;
  }
  /**
     *The Invoker does not depend on concrete command or receiver classes.
     * The Invoker passes a request to a receiver indirectly, by executing a
     * command.
     */
  void DoSomethingImportant() {
    std::cout << "Invoker: Does anybody want something done before I begin?\n";
    if (this->on_start_) {
      this->on_start_->Execute();
    }
    std::cout << "Invoker: ...doing something really important...\n";
    std::cout << "Invoker: Does anybody want something done after I finish?\n";
    if (this->on_finish_) {
      this->on_finish_->Execute();
    }
  }
};
/**
 *The client code can parameterize an invoker with any commands.
 */

int main() {
  Invoker *invoker = new Invoker;
  invoker->SetOnStart(new SimpleCommand("Say Hi!"));
  Receiver *receiver = new Receiver;
  invoker->SetOnFinish(new ComplexCommand(receiver, "Send email", "Save report"));
  invoker->DoSomethingImportant();

  delete invoker;
  delete receiver;

  return 0;
}

//text output
//Invoker: Does anybody want something done before I begin?
//SimpleCommand: See, I can do simple things like printing (Say Hi!)
//Invoker: ...doing something really important...
//Invoker: Does anybody want something done after I finish?
//ComplexCommand: Complex stuff should be done by a receiver object.
//Receiver: Working on (Send email.)
//Receiver: Also working on (Save report.)
```
---

## When to Use

- Implementation of the Command design pattern
- When you need the specific functionality provided by this pattern

---

## References

- [Refactoring Guru: Command Pattern](https://refactoring.guru/design-patterns/command)
- [Wikipedia: Command Pattern](https://en.wikipedia.org/wiki/Command_pattern)
- [GitHub: Design Patterns C++](https://github.com/RefactoringGuru/design-patterns-cpp.git)
- [GitHub: Design Patterns Python](https://github.com/RefactoringGuru/design-patterns-python.git)
---

> This work is licensed under a [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](https://creativecommons.org/licenses/by-nc-nd/4.0/).
