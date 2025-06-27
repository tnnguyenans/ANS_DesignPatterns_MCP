# Strategy Design Pattern

**Intent:**\
Lets you define a family of algorithms, put each of them into a separate.
---

## Python
```python
"""
Strategy Design Pattern

Intent: Lets you define a family of algorithms, put each of them into a separate
class, and make their objects interchangeable.

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Context():
    """
The Context defines the interface of interest to clients.

    def __init__(self, strategy: Strategy) -> None:
        """
Usually, the Context accepts a strategy through the constructor, but
        also provides a setter to change it at runtime.

        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        """
The Context maintains a reference to one of the Strategy objects.
        The Context does not know the concrete class of a strategy. It should
        work with all strategies via the Strategy interface.

        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        """
Usually, the Context allows replacing a Strategy object at runtime.

        self._strategy = strategy

    def do_some_business_logic(self) -> None:
        """
The Context delegates some work to the Strategy object instead of
        implementing multiple versions of the algorithm on its own.

        # ...

        print("Context: Sorting data using the strategy (not sure how it'll do it)")
        result = self._strategy.do_algorithm(["a", "b", "c", "d", "e"])
        print(",".join(result))

        # ...

class Strategy(ABC):
    """
The Strategy interface declares operations common to all supported
    versions of some algorithm.

    The Context uses this interface to call the algorithm defined by Concrete
    Strategies.

    """

    @abstractmethod
    def do_algorithm(self, data: List):
        pass

"""
Concrete Strategies implement the algorithm while following the base
Strategy interface. The interface makes them interchangeable in the Context.

class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data: List) -> List:
        return sorted(data)

class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data: List) -> List:
        return reversed(sorted(data))

if __name__ == "__main__":
    #The client code picks a concrete strategy and passes it to the
    # context. The client should be aware of the differences between strategies
    # in order to make the right choice.

    context = Context(ConcreteStrategyA())
    print("Client: Strategy is set to normal sorting.")
    context.do_some_business_logic()
    print()

    print("Client: Strategy is set to reverse sorting.")
    context.strategy = ConcreteStrategyB()
    context.do_some_business_logic()

# text output
# Client: Strategy is set to normal sorting.
# Context: Sorting data using the strategy (not sure how it'll do it)
# a,b,c,d,e
# Client: Strategy is set to reverse sorting.
# Context: Sorting data using the strategy (not sure how it'll do it)
# e,d,c,b,a
```
---

## C++
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

/**
 *Strategy Design Pattern
 * Intent: Lets you define a family of algorithms, put each of them into a
 * separate class, and make their objects interchangeable.
 */

/**
 *The Strategy interface declares operations common to all supported
 * versions of some algorithm.
 * The Context uses this interface to call the algorithm defined by Concrete
 * Strategies.
 */
class Strategy
{
public:
    virtual ~Strategy() = default;
    virtual std::string doAlgorithm(std::string_view data) const = 0;
};

/**
 *The Context defines the interface of interest to clients.
 */

class Context
{
    /**
     *@var Strategy The Context maintains a reference to one of the
     * Strategy objects. The Context does not know the concrete class of a
     * strategy. It should work with all strategies via the Strategy interface.
     */
private:
    std::unique_ptr<Strategy> strategy_;
    /**
     *Usually, the Context accepts a strategy through the constructor, but
     * also provides a setter to change it at runtime.
     */
public:
    explicit Context(std::unique_ptr<Strategy> &&strategy = {}) : strategy_(std::move(strategy))
    {
    }
    /**
     *Usually, the Context allows replacing a Strategy object at runtime.
     */
    void set_strategy(std::unique_ptr<Strategy> &&strategy)
    {
        strategy_ = std::move(strategy);
    }
    /**
     *The Context delegates some work to the Strategy object instead of
     * implementing +multiple versions of the algorithm on its own.
     */
    void doSomeBusinessLogic() const
    {
        if (strategy_) {
            std::cout << "Context: Sorting data using the strategy (not sure how it'll do it)\n";
            std::string result = strategy_->doAlgorithm("aecbd");
            std::cout << result << "\n";
        } else {
            std::cout << "Context: Strategy isn't set\n";
        }
    }
};

/**
 *Concrete Strategies implement the algorithm while following the base
 * Strategy interface. The interface makes them interchangeable in the Context.
 */
class ConcreteStrategyA : public Strategy
{
public:
    std::string doAlgorithm(std::string_view data) const override
    {
        std::string result(data);
        std::sort(std::begin(result), std::end(result));

        return result;
    }
};
class ConcreteStrategyB : public Strategy
{
    std::string doAlgorithm(std::string_view data) const override
    {
        std::string result(data);
        std::sort(std::begin(result), std::end(result), std::greater<>());

        return result;
    }
};
/**
 *The client code picks a concrete strategy and passes it to the context.
 * The client should be aware of the differences between strategies in order to
 * make the right choice.
 */

void clientCode()
{
    Context context(std::make_unique<ConcreteStrategyA>());
    std::cout << "Client: Strategy is set to normal sorting.\n";
    context.doSomeBusinessLogic();
    std::cout << "\n";
    std::cout << "Client: Strategy is set to reverse sorting.\n";
    context.set_strategy(std::make_unique<ConcreteStrategyB>());
    context.doSomeBusinessLogic();
}

int main()
{
    clientCode();
    return 0;
}

//text output
//Client: Strategy is set to normal sorting.
//Context: Sorting data using the strategy (not sure how it'll do it)
//abcde
//Client: Strategy is set to reverse sorting.
//Context: Sorting data using the strategy (not sure how it'll do it)
//edcba
```
---

## When to Use

- Implementation of the Strategy design pattern
- When you need the specific functionality provided by this pattern

---

## References

- [Refactoring Guru: Strategy Pattern](https://refactoring.guru/design-patterns/strategy)
- [Wikipedia: Strategy Pattern](https://en.wikipedia.org/wiki/Strategy_pattern)
- [GitHub: Design Patterns C++](https://github.com/RefactoringGuru/design-patterns-cpp.git)
- [GitHub: Design Patterns Python](https://github.com/RefactoringGuru/design-patterns-python.git)
---

> This work is licensed under a [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](https://creativecommons.org/licenses/by-nc-nd/4.0/).
