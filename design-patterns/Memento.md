# Memento Design Pattern

**Intent:**\
Lets you save and restore the previous state of an object without revealing the details of its implementation.
---

## Python
```python
"""
Memento Design Pattern

Intent: Lets you save and restore the previous state of an object without
revealing the details of its implementation.

from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime
from random import sample
from string import ascii_letters

class Originator:
    """
The Originator holds some important state that may change over time. It
    also defines a method for saving the state inside a memento and another
    method for restoring the state from it.

    _state = None
    """
For the sake of simplicity, the originator's state is stored inside a
    single variable.

    def __init__(self, state: str) -> None:
        self._state = state
        print(f"Originator: My initial state is: {self._state}")

    def do_something(self) -> None:
        """
The Originator's business logic may affect its internal state.
        Therefore, the client should backup the state before launching methods
        of the business logic via the save() method.

        print("Originator: I'm doing something important.")
        self._state = self._generate_random_string(30)
        print(f"Originator: and my state has changed to: {self._state}")

    @staticmethod
    def _generate_random_string(length: int = 10) -> str:
        return "".join(sample(ascii_letters, length))

    def save(self) -> Memento:
        """
Saves the current state inside a memento.

        return ConcreteMemento(self._state)

    def restore(self, memento: Memento) -> None:
        """
Restores the Originator's state from a memento object.

        self._state = memento.get_state()
        print(f"Originator: My state has changed to: {self._state}")

class Memento(ABC):
    """
The Memento interface provides a way to retrieve the memento's metadata,
    such as creation date or name. However, it doesn't expose the Originator's
    state.

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_date(self) -> str:
        pass

class ConcreteMemento(Memento):
    def __init__(self, state: str) -> None:
        self._state = state
        self._date = str(datetime.now())[:19]

    def get_state(self) -> str:
        """
The Originator uses this method when restoring its state.

    def get_name(self) -> str:
        """
The rest of the methods are used by the Caretaker to display
        metadata.

        return f"{self._date} / ({self._state[0:9]}...)"

    def get_date(self) -> str:
        return self._date

class Caretaker:
    """
The Caretaker doesn't depend on the Concrete Memento class. Therefore,
    it doesn't have access to the originator's state, stored inside the memento.
    It works with all mementos via the base Memento interface.

    def __init__(self, originator: Originator) -> None:
        self._mementos = []
        self._originator = originator

    def backup(self) -> None:
        print("\nCaretaker: Saving Originator's state...")
        self._mementos.append(self._originator.save())

    def undo(self) -> None:
        if not len(self._mementos):
            return

        memento = self._mementos.pop()
        print(f"Caretaker: Restoring state to: {memento.get_name()}")
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()

    def show_history(self) -> None:
        print("Caretaker: Here's the list of mementos:")
        for memento in self._mementos:
            print(memento.get_name())

if __name__ == "__main__":
    originator = Originator("Super-duper-super-puper-super.")
    caretaker = Caretaker(originator)

    caretaker.backup()
    originator.do_something()

    caretaker.backup()
    originator.do_something()

    caretaker.backup()
    originator.do_something()

    print()
    caretaker.show_history()

    print("\nClient: Now, let's rollback!\n")
    caretaker.undo()

    print("\nClient: Once more!\n")
    caretaker.undo()

# text output
# Originator: My initial state is: Super-duper-super-puper-super.
# Caretaker: Saving Originator's state...
# Originator: I'm doing something important.
# Originator: and my state has changed to: wQAehHYOqVSlpEXjyIcgobrxsZUnat
# Caretaker: Saving Originator's state...
# Originator: I'm doing something important.
# Originator: and my state has changed to: lHxNORKcsgMWYnJqoXjVCbQLEIeiSp
# Caretaker: Saving Originator's state...
# Originator: I'm doing something important.
# Originator: and my state has changed to: cvIYsRilNOtwynaKdEZpDCQkFAXVMf
# Caretaker: Here's the list of mementos:
# 2019-01-26 21:11:24 / (Super-dup...)
# 2019-01-26 21:11:24 / (wQAehHYOq...)
# 2019-01-26 21:11:24 / (lHxNORKcs...)
# Client: Now, let's rollback!
# Caretaker: Restoring state to: 2019-01-26 21:11:24 / (lHxNORKcs...)
# Originator: My state has changed to: lHxNORKcsgMWYnJqoXjVCbQLEIeiSp
# Client: Once more!
# Caretaker: Restoring state to: 2019-01-26 21:11:24 / (wQAehHYOq...)
# Originator: My state has changed to: wQAehHYOqVSlpEXjyIcgobrxsZUnat
```
---

## C++
```cpp
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <string>
#include <vector>

/**
 *Memento Design Pattern
 * Intent: Lets you save and restore the previous state of an object without
 * revealing the details of its implementation.
 */

/**
 *The Memento interface provides a way to retrieve the memento's metadata,
 * such as creation date or name. However, it doesn't expose the Originator's
 * state.
 */
class Memento {
 public:
  virtual ~Memento() {}
  virtual std::string GetName() const = 0;
  virtual std::string date() const = 0;
  virtual std::string state() const = 0;
};

/**
 *The Concrete Memento contains the infrastructure for storing the
 * Originator's state.
 */
class ConcreteMemento : public Memento {
 private:
  std::string state_;
  std::string date_;

 public:
  ConcreteMemento(std::string state) : state_(state) {
    this->state_ = state;
    std::time_t now = std::time(0);
    this->date_ = std::ctime(&now);
  }
  /**
     *The Originator uses this method when restoring its state.
     */
  std::string state() const override {
    return this->state_;
  }
  /**
     *The rest of the methods are used by the Caretaker to display
     * metadata.
     */
  std::string GetName() const override {
    return this->date_ + " / (" + this->state_.substr(0, 9) + "...)";
  }
  std::string date() const override {
    return this->date_;
  }
};

/**
 *The Originator holds some important state that may change over time. It
 * also defines a method for saving the state inside a memento and another
 * method for restoring the state from it.
 */
class Originator {
  /**
     *@var string For the sake of simplicity, the originator's state is
     * stored inside a single variable.
     */
 private:
  std::string state_;

  std::string GenerateRandomString(int length = 10) {
    const char alphanum[] =
        "0123456789"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "abcdefghijklmnopqrstuvwxyz";
    int stringLength = sizeof(alphanum) - 1;

    std::string random_string;
    for (int i = 0; i < length; i++) {
      random_string += alphanum[std::rand() % stringLength];
    }
    return random_string;
  }

 public:
  Originator(std::string state) : state_(state) {
    std::cout << "Originator: My initial state is: " << this->state_ << "\n";
  }
  /**
     *The Originator's business logic may affect its internal state.
     * Therefore, the client should backup the state before launching methods of
     * the business logic via the save() method.
     */
  void DoSomething() {
    std::cout << "Originator: I'm doing something important.\n";
    this->state_ = this->GenerateRandomString(30);
    std::cout << "Originator: and my state has changed to: " << this->state_ << "\n";
  }

  /**
     *Saves the current state inside a memento.
     */
  Memento *Save() {
    return new ConcreteMemento(this->state_);
  }
  /**
     *Restores the Originator's state from a memento object.
     */
  void Restore(Memento *memento) {
    this->state_ = memento->state();
    std::cout << "Originator: My state has changed to: " << this->state_ << "\n";
    delete memento;
  }
};

/**
 *The Caretaker doesn't depend on the Concrete Memento class. Therefore, it
 * doesn't have access to the originator's state, stored inside the memento. It
 * works with all mementos via the base Memento interface.
 */
class Caretaker {
  /**
     * @var Memento[]
     */
 private:
  std::vector<Memento *> mementos_;

  /**
     * @var Originator
     */
  Originator *originator_;

 public:
     Caretaker(Originator* originator) : originator_(originator) {
     }

     ~Caretaker() {
         for (auto m : mementos_) delete m;
     }

  void Backup() {
    std::cout << "\nCaretaker: Saving Originator's state...\n";
    this->mementos_.push_back(this->originator_->Save());
  }
  void Undo() {
    if (!this->mementos_.size()) {
      return;
    }
    Memento *memento = this->mementos_.back();
    this->mementos_.pop_back();
    std::cout << "Caretaker: Restoring state to: " << memento->GetName() << "\n";
    try {
      this->originator_->Restore(memento);
    } catch (...) {
      this->Undo();
    }
  }
  void ShowHistory() const {
    std::cout << "Caretaker: Here's the list of mementos:\n";
    for (Memento *memento : this->mementos_) {
      std::cout << memento->GetName() << "\n";
    }
  }
};
/**
 *Client code.
 */

void ClientCode() {
  Originator *originator = new Originator("Super-duper-super-puper-super.");
  Caretaker *caretaker = new Caretaker(originator);
  caretaker->Backup();
  originator->DoSomething();
  caretaker->Backup();
  originator->DoSomething();
  caretaker->Backup();
  originator->DoSomething();
  std::cout << "\n";
  caretaker->ShowHistory();
  std::cout << "\nClient: Now, let's rollback!\n\n";
  caretaker->Undo();
  std::cout << "\nClient: Once more!\n\n";
  caretaker->Undo();

  delete originator;
  delete caretaker;
}

int main() {
  std::srand(static_cast<unsigned int>(std::time(NULL)));
  ClientCode();
  return 0;
}

//text output
//Originator: My initial state is: Super-duper-super-puper-super.
//Caretaker: Saving Originator's state...
//Originator: I'm doing something important.
//Originator: and my state has changed to: uOInE8wmckHYPwZS7PtUTwuwZfCIbz
//Caretaker: Saving Originator's state...
//Originator: I'm doing something important.
//Originator: and my state has changed to: te6RGmykRpbqaWo5MEwjji1fpM1t5D
//Caretaker: Saving Originator's state...
//Originator: I'm doing something important.
//Originator: and my state has changed to: hX5xWDVljcQ9ydD7StUfbBt5Z7pcSN
//Caretaker: Here's the list of mementos:
//Sat Oct 19 18:09:37 2019
// / (Super-dup...)
//Sat Oct 19 18:09:37 2019
// / (uOInE8wmc...)
//Sat Oct 19 18:09:37 2019
// / (te6RGmykR...)
//Client: Now, let's rollback!
//Caretaker: Restoring state to: Sat Oct 19 18:09:37 2019
// / (te6RGmykR...)
//Originator: My state has changed to: te6RGmykRpbqaWo5MEwjji1fpM1t5D
//Client: Once more!
//Caretaker: Restoring state to: Sat Oct 19 18:09:37 2019
// / (uOInE8wmc...)
//Originator: My state has changed to: uOInE8wmckHYPwZS7PtUTwuwZfCIbz
```
---

## When to Use

- Implementation of the Memento design pattern
- When you need the specific functionality provided by this pattern

---

## References

- [Refactoring Guru: Memento Pattern](https://refactoring.guru/design-patterns/memento)
- [Wikipedia: Memento Pattern](https://en.wikipedia.org/wiki/Memento_pattern)
- [GitHub: Design Patterns C++](https://github.com/RefactoringGuru/design-patterns-cpp.git)
- [GitHub: Design Patterns Python](https://github.com/RefactoringGuru/design-patterns-python.git)
---

> This work is licensed under a [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](https://creativecommons.org/licenses/by-nc-nd/4.0/).
