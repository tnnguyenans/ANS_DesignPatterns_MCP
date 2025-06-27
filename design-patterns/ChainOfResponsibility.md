# ChainOfResponsibility Design Pattern

**Intent:**\
Lets you pass requests along a chain of handlers. Upon receiving a request, each handler decides either to process the request or to pass it to the next handler in the chain.
---

## Python
```python
"""
Chain of Responsibility Design Pattern

Intent: Lets you pass requests along a chain of handlers. Upon receiving a
request, each handler decides either to process the request or to pass it to the
next handler in the chain.

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional

class Handler(ABC):
    """
The Handler interface declares a method for building the chain of
    handlers. It also declares a method for executing a request.

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass

class AbstractHandler(Handler):
    """
The default chaining behavior can be implemented inside a base handler
    class.

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        #Returning a handler from here will let us link handlers in a
        # convenient way like this:
        # monkey.set_next(squirrel).set_next(dog)

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None

"""
All Concrete Handlers either handle a request or pass it to the next handler
in the chain.

class MonkeyHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Banana":
            return f"Monkey: I'll eat the {request}"
        else:
            return super().handle(request)

class SquirrelHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Nut":
            return f"Squirrel: I'll eat the {request}"
        else:
            return super().handle(request)

class DogHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "MeatBall":
            return f"Dog: I'll eat the {request}"
        else:
            return super().handle(request)

def client_code(handler: Handler) -> None:
    """
The client code is usually suited to work with a single handler. In most
    cases, it is not even aware that the handler is part of a chain.

    for food in ["Nut", "Banana", "Cup of coffee"]:
        print(f"\nClient: Who wants a {food}?")
        result = handler.handle(food)
        if result:
            print(f"  {result}", end="")
        else:
            print(f"  {food} was left untouched.", end="")

if __name__ == "__main__":
    monkey = MonkeyHandler()
    squirrel = SquirrelHandler()
    dog = DogHandler()

    monkey.set_next(squirrel).set_next(dog)

    #The client should be able to send a request to any handler, not just
    # the first one in the chain.

    print("Subchain: Squirrel > Dog")
    client_code(squirrel)

# text output
# Chain: Monkey > Squirrel > Dog
# Client: Who wants a Nut?
#   Squirrel: I'll eat the Nut
# Client: Who wants a Banana?
#   Monkey: I'll eat the Banana
# Client: Who wants a Cup of coffee?
#   Cup of coffee was left untouched.
# Subchain: Squirrel > Dog
# Client: Who wants a Nut?
#   Squirrel: I'll eat the Nut
# Client: Who wants a Banana?
#   Banana was left untouched.
# Client: Who wants a Cup of coffee?
#   Cup of coffee was left untouched.
```
---

## C++
```cpp
#include <iostream>
#include <string>
#include <vector>

/**
 *Chain of Responsibility Design Pattern
 * Intent: Lets you pass requests along a chain of handlers. Upon receiving a
 * request, each handler decides either to process the request or to pass it to
 * the next handler in the chain.
 */
/**
 *The Handler interface declares a method for building the chain of
 * handlers. It also declares a method for executing a request.
 */
class Handler {
 public:
  virtual Handler *SetNext(Handler *handler) = 0;
  virtual std::string Handle(std::string request) = 0;
};
/**
 *The default chaining behavior can be implemented inside a base handler
 * class.
 */
class AbstractHandler : public Handler {
  /**
     * @var Handler
     */
 private:
  Handler *next_handler_;

 public:
  AbstractHandler() : next_handler_(nullptr) {
  }
  Handler *SetNext(Handler *handler) override {
    this->next_handler_ = handler;
    //Returning a handler from here will let us link handlers in a
    // convenient way like this:
    // $monkey->setNext($squirrel)->setNext($dog);

    return {};
  }
};
/**
 *All Concrete Handlers either handle a request or pass it to the next
 * handler in the chain.
 */
class MonkeyHandler : public AbstractHandler {
 public:
  std::string Handle(std::string request) override {
    if (request == "Banana") {
      return "Monkey: I'll eat the " + request + ".\n";
    } else {
      return AbstractHandler::Handle(request);
    }
  }
};
class SquirrelHandler : public AbstractHandler {
 public:
  std::string Handle(std::string request) override {
    if (request == "Nut") {
      return "Squirrel: I'll eat the " + request + ".\n";
    } else {
      return AbstractHandler::Handle(request);
    }
  }
};
class DogHandler : public AbstractHandler {
 public:
  std::string Handle(std::string request) override {
    if (request == "MeatBall") {
      return "Dog: I'll eat the " + request + ".\n";
    } else {
      return AbstractHandler::Handle(request);
    }
  }
};
/**
 *The client code is usually suited to work with a single handler. In most
 * cases, it is not even aware that the handler is part of a chain.
 */
void ClientCode(Handler &handler) {
  std::vector<std::string> food = {"Nut", "Banana", "Cup of coffee"};
  for (const std::string &f : food) {
    std::cout << "Client: Who wants a " << f << "?\n";
    const std::string result = handler.Handle(f);
    if (!result.empty()) {
      std::cout << "  " << result;
    } else {
      std::cout << "  " << f << " was left untouched.\n";
    }
  }
}
/**
 *The other part of the client code constructs the actual chain.
 */
int main() {
  MonkeyHandler *monkey = new MonkeyHandler;
  SquirrelHandler *squirrel = new SquirrelHandler;
  DogHandler *dog = new DogHandler;
  monkey->SetNext(squirrel)->SetNext(dog);

  /**
     *The client should be able to send a request to any handler, not just the
     * first one in the chain.
     */
  std::cout << "Chain: Monkey > Squirrel > Dog\n\n";
  ClientCode(*monkey);
  std::cout << "\n";
  std::cout << "Subchain: Squirrel > Dog\n\n";
  ClientCode(*squirrel);

  delete monkey;
  delete squirrel;
  delete dog;

  return 0;
}

//text output
//Chain: Monkey > Squirrel > Dog
//Client: Who wants a Nut?
//  Squirrel: I'll eat the Nut.
//Client: Who wants a Banana?
//  Monkey: I'll eat the Banana.
//Client: Who wants a Cup of coffee?
//  Cup of coffee was left untouched.
//Subchain: Squirrel > Dog
//Client: Who wants a Nut?
//  Squirrel: I'll eat the Nut.
//Client: Who wants a Banana?
//  Banana was left untouched.
//Client: Who wants a Cup of coffee?
//  Cup of coffee was left untouched.
```
---

## When to Use

- Implementation of the ChainOfResponsibility design pattern
- When you need the specific functionality provided by this pattern

---

## References

- [Refactoring Guru: ChainOfResponsibility Pattern](https://refactoring.guru/design-patterns/chainofresponsibility)
- [Wikipedia: ChainOfResponsibility Pattern](https://en.wikipedia.org/wiki/ChainOfResponsibility_pattern)
- [GitHub: Design Patterns C++](https://github.com/RefactoringGuru/design-patterns-cpp.git)
- [GitHub: Design Patterns Python](https://github.com/RefactoringGuru/design-patterns-python.git)
---

> This work is licensed under a [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](https://creativecommons.org/licenses/by-nc-nd/4.0/).
