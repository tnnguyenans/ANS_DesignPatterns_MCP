# Observer Design Pattern

**Intent:**\
Lets you define a subscription mechanism to notify multiple objects about any events that happen to the object they're observing.
---

## Python
```python
"""
Observer Design Pattern

Intent: Lets you define a subscription mechanism to notify multiple objects
about any events that happen to the object they're observing.

Note that there's a lot of different terms with similar meaning associated with
this pattern. Just remember that the Subject is also called the Publisher and
the Observer is often called the Subscriber and vice versa. Also the verbs
"observe", "listen" or "track" usually mean the same thing.

"""

from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List

class Subject(ABC):
    """
The Subject interface declares a set of methods for managing
    subscribers.

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
Attach an observer to the subject.

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
Detach an observer from the subject.

    @abstractmethod
    def notify(self) -> None:
        """
Notify all observers about an event.

class ConcreteSubject(Subject):
    """
The Subject owns some important state and notifies observers when the
    state changes.

    _state: int = None
    """
For the sake of simplicity, the Subject's state, essential to all
    subscribers, is stored in this variable.

    _observers: List[Observer] = []
    """
List of subscribers. In real life, the list of subscribers can be stored
    more comprehensively (categorized by event type, etc.).

    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    """
The subscription management methods.

    def notify(self) -> None:
        """
Trigger an update in each subscriber.

        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:
        """
Usually, the subscription logic is only a fraction of what a Subject
        can really do. Subjects commonly hold some important business logic,
        that triggers a notification method whenever something important is
        about to happen (or after it).

        print("\nSubject: I'm doing something important.")
        self._state = randrange(0, 10)

        print(f"Subject: My state has just changed to: {self._state}")
        self.notify()

class Observer(ABC):
    """
The Observer interface declares the update method, used by subjects.

    @abstractmethod
    def update(self, subject: Subject) -> None:
        """
Receive update from subject.

"""
Concrete Observers react to the updates issued by the Subject they had been
attached to.

class ConcreteObserverA(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state < 3:
            print("ConcreteObserverA: Reacted to the event")

class ConcreteObserverB(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state == 0 or subject._state >= 2:
            print("ConcreteObserverB: Reacted to the event")

if __name__ == "__main__":
    #The client code.

    subject = ConcreteSubject()

    observer_a = ConcreteObserverA()
    subject.attach(observer_a)

    observer_b = ConcreteObserverB()
    subject.attach(observer_b)

    subject.some_business_logic()
    subject.some_business_logic()

    subject.detach(observer_a)

    subject.some_business_logic()

# text output
# Subject: Attached an observer.
# Subject: Attached an observer.
# Subject: I'm doing something important.
# Subject: My state has just changed to: 0
# Subject: Notifying observers...
# ConcreteObserverA: Reacted to the event
# ConcreteObserverB: Reacted to the event
# Subject: I'm doing something important.
# Subject: My state has just changed to: 5
# Subject: Notifying observers...
# ConcreteObserverB: Reacted to the event
# Subject: I'm doing something important.
# Subject: My state has just changed to: 0
# Subject: Notifying observers...
# ConcreteObserverB: Reacted to the event
```
---

## C++
```cpp
/**
 *Observer Design Pattern
 * Intent: Lets you define a subscription mechanism to notify multiple objects
 * about any events that happen to the object they're observing.
 * Note that there's a lot of different terms with similar meaning associated
 * with this pattern. Just remember that the Subject is also called the
 * Publisher and the Observer is often called the Subscriber and vice versa.
 * Also the verbs "observe", "listen" or "track" usually mean the same thing.
 */

#include <iostream>
#include <list>
#include <string>

class IObserver {
 public:
  virtual ~IObserver(){};
  virtual void Update(const std::string &message_from_subject) = 0;
};

class ISubject {
 public:
  virtual ~ISubject(){};
  virtual void Attach(IObserver *observer) = 0;
  virtual void Detach(IObserver *observer) = 0;
  virtual void Notify() = 0;
};

/**
 *The Subject owns some important state and notifies observers when the
 * state changes.
 */

class Subject : public ISubject {
 public:
  virtual ~Subject() {
    std::cout << "Goodbye, I was the Subject.\n";
  }

  /**
     *The subscription management methods.
     */
  void Attach(IObserver *observer) override {
    list_observer_.push_back(observer);
  }
  void Detach(IObserver *observer) override {
    list_observer_.remove(observer);
  }
  void Notify() override {
    std::list<IObserver *>::iterator iterator = list_observer_.begin();
    HowManyObserver();
    while (iterator != list_observer_.end()) {
      (*iterator)->Update(message_);
      ++iterator;
    }
  }

  void CreateMessage(std::string message = "Empty") {
    this->message_ = message;
    Notify();
  }
  void HowManyObserver() {
    std::cout << "There are " << list_observer_.size() << " observers in the list.\n";
  }

  /**
     *Usually, the subscription logic is only a fraction of what a Subject
     * can really do. Subjects commonly hold some important business logic, that
     * triggers a notification method whenever something important is about to
     * happen (or after it).
     */
  void SomeBusinessLogic() {
    this->message_ = "change message message";
    Notify();
    std::cout << "I'm about to do some thing important\n";
  }

 private:
  std::list<IObserver *> list_observer_;
  std::string message_;
};

class Observer : public IObserver {
 public:
  Observer(Subject &subject) : subject_(subject) {
    this->subject_.Attach(this);
    std::cout << "Hi, I'm the Observer \"" << ++Observer::static_number_ << "\".\n";
    this->number_ = Observer::static_number_;
  }
  virtual ~Observer() {
    std::cout << "Goodbye, I was the Observer \"" << this->number_ << "\".\n";
  }

  void Update(const std::string &message_from_subject) override {
    message_from_subject_ = message_from_subject;
    PrintInfo();
  }
  void RemoveMeFromTheList() {
    subject_.Detach(this);
    std::cout << "Observer \"" << number_ << "\" removed from the list.\n";
  }
  void PrintInfo() {
    std::cout << "Observer \"" << this->number_ << "\": a new message is available --> " << this->message_from_subject_ << "\n";
  }

 private:
  std::string message_from_subject_;
  Subject &subject_;
  static int static_number_;
  int number_;
};

int Observer::static_number_ = 0;

void ClientCode() {
  Subject *subject = new Subject;
  Observer *observer1 = new Observer(*subject);
  Observer *observer2 = new Observer(*subject);
  Observer *observer3 = new Observer(*subject);
  Observer *observer4;
  Observer *observer5;

  subject->CreateMessage("Hello World! :D");
  observer3->RemoveMeFromTheList();

  subject->CreateMessage("The weather is hot today! :p");
  observer4 = new Observer(*subject);

  observer2->RemoveMeFromTheList();
  observer5 = new Observer(*subject);

  subject->CreateMessage("My new car is great! ;)");
  observer5->RemoveMeFromTheList();

  observer4->RemoveMeFromTheList();
  observer1->RemoveMeFromTheList();

  delete observer5;
  delete observer4;
  delete observer3;
  delete observer2;
  delete observer1;
  delete subject;
}

int main() {
  ClientCode();
  return 0;
}

//text output
//Hi, I'm the Observer "1".
//Hi, I'm the Observer "2".
//Hi, I'm the Observer "3".
//There are 3 observers in the list.
//Observer "1": a new message is available --> Hello World! :D
//Observer "2": a new message is available --> Hello World! :D
//Observer "3": a new message is available --> Hello World! :D
//Observer "3" removed from the list.
//There are 2 observers in the list.
//Observer "1": a new message is available --> The weather is hot today! :p
//Observer "2": a new message is available --> The weather is hot today! :p
//Hi, I'm the Observer "4".
//Observer "2" removed from the list.
//Hi, I'm the Observer "5".
//There are 3 observers in the list.
//Observer "1": a new message is available --> My new car is great! ;)
//Observer "4": a new message is available --> My new car is great! ;)
//Observer "5": a new message is available --> My new car is great! ;)
//Observer "5" removed from the list.
//Observer "4" removed from the list.
//Observer "1" removed from the list.
//Goodbye, I was the Observer "5".
//Goodbye, I was the Observer "4".
//Goodbye, I was the Observer "3".
//Goodbye, I was the Observer "2".
//Goodbye, I was the Observer "1".
//Goodbye, I was the Subject.
```
---

## When to Use

- Implementation of the Observer design pattern
- When you need the specific functionality provided by this pattern

---

## References

- [Refactoring Guru: Observer Pattern](https://refactoring.guru/design-patterns/observer)
- [Wikipedia: Observer Pattern](https://en.wikipedia.org/wiki/Observer_pattern)
- [GitHub: Design Patterns C++](https://github.com/RefactoringGuru/design-patterns-cpp.git)
- [GitHub: Design Patterns Python](https://github.com/RefactoringGuru/design-patterns-python.git)
---

> This work is licensed under a [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](https://creativecommons.org/licenses/by-nc-nd/4.0/).
