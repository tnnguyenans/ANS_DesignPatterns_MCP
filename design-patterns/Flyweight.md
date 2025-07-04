# Flyweight Design Pattern

**Intent:**\
Lets you fit more objects into the available amount of RAM by sharing common parts of state between multiple objects, instead of keeping all of the data in each object.
---

## Python
```python
"""
Flyweight Design Pattern

Intent: Lets you fit more objects into the available amount of RAM by sharing
common parts of state between multiple objects, instead of keeping all of the
data in each object.

import json
from typing import Dict

class Flyweight():
    """
The Flyweight stores a common portion of the state (also called
    intrinsic state) that belongs to multiple real business entities. The
    Flyweight accepts the rest of the state (extrinsic state, unique for each
    entity) via its method parameters.

    def __init__(self, shared_state: str) -> None:
        self._shared_state = shared_state

    def operation(self, unique_state: str) -> None:
        s = json.dumps(self._shared_state)
        u = json.dumps(unique_state)
        print(f"Flyweight: Displaying shared ({s}) and unique ({u}) state.", end="")

class FlyweightFactory():
    """
The Flyweight Factory creates and manages the Flyweight objects. It
    ensures that flyweights are shared correctly. When the client requests a
    flyweight, the factory either returns an existing instance or creates a new
    one, if it doesn't exist yet.

    _flyweights: Dict[str, Flyweight] = {}

    def __init__(self, initial_flyweights: Dict) -> None:
        for state in initial_flyweights:
            self._flyweights[self.get_key(state)] = Flyweight(state)

    def get_key(self, state: Dict) -> str:
        """
Returns a Flyweight's string hash for a given state.

        return "_".join(sorted(state))

    def get_flyweight(self, shared_state: Dict) -> Flyweight:
        """
Returns an existing Flyweight with a given state or creates a new
        one.

        key = self.get_key(shared_state)

        if not self._flyweights.get(key):
            print("FlyweightFactory: Can't find a flyweight, creating new one.")
            self._flyweights[key] = Flyweight(shared_state)
        else:
            print("FlyweightFactory: Reusing existing flyweight.")

        return self._flyweights[key]

    def list_flyweights(self) -> None:
        count = len(self._flyweights)
        print(f"FlyweightFactory: I have {count} flyweights:")
        print("\n".join(map(str, self._flyweights.keys())), end="")

def add_car_to_police_database(
    factory: FlyweightFactory, plates: str, owner: str,
    brand: str, model: str, color: str
) -> None:
    print("\n\nClient: Adding a car to database.")
    flyweight = factory.get_flyweight([brand, model, color])
    #The client code either stores or calculates extrinsic state and passes
    # it to the flyweight's methods.

if __name__ == "__main__":
    """
The client code usually creates a bunch of pre-populated flyweights in
    the initialization stage of the application.

    factory = FlyweightFactory([
        ["Chevrolet", "Camaro2018", "pink"],
        ["Mercedes Benz", "C300", "black"],
        ["Mercedes Benz", "C500", "red"],
        ["BMW", "M5", "red"],
        ["BMW", "X6", "white"],
    ])

    factory.list_flyweights()

    add_car_to_police_database(
        factory, "CL234IR", "James Doe", "BMW", "M5", "red")

    add_car_to_police_database(
        factory, "CL234IR", "James Doe", "BMW", "X1", "red")

    print("\n")

    factory.list_flyweights()

# text output
# FlyweightFactory: I have 5 flyweights:
# Camaro2018_Chevrolet_pink
# C300_Mercedes Benz_black
# C500_Mercedes Benz_red
# BMW_M5_red
# BMW_X6_white
# Client: Adding a car to database.
# FlyweightFactory: Reusing existing flyweight.
# Flyweight: Displaying shared (["BMW", "M5", "red"]) and unique (["CL234IR", "James Doe"]) state.
# Client: Adding a car to database.
# FlyweightFactory: Can't find a flyweight, creating new one.
# Flyweight: Displaying shared (["BMW", "X1", "red"]) and unique (["CL234IR", "James Doe"]) state.
# FlyweightFactory: I have 6 flyweights:
# Camaro2018_Chevrolet_pink
# C300_Mercedes Benz_black
# C500_Mercedes Benz_red
# BMW_M5_red
# BMW_X6_white
# BMW_X1_red
```
---

## C++
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>

/**
 *Flyweight Design Pattern
 * Intent: Lets you fit more objects into the available amount of RAM by sharing
 * common parts of state between multiple objects, instead of keeping all of the
 * data in each object.
 */

struct SharedState
{
    std::string brand_;
    std::string model_;
    std::string color_;

    SharedState(const std::string &brand, const std::string &model, const std::string &color)
        : brand_(brand), model_(model), color_(color)
    {
    }

    friend std::ostream &operator<<(std::ostream &os, const SharedState &ss)
    {
        return os << "[ " << ss.brand_ << " , " << ss.model_ << " , " << ss.color_ << " ]";
    }
};

struct UniqueState
{
    std::string owner_;
    std::string plates_;

    UniqueState(const std::string &owner, const std::string &plates)
        : owner_(owner), plates_(plates)
    {
    }

    friend std::ostream &operator<<(std::ostream &os, const UniqueState &us)
    {
        return os << "[ " << us.owner_ << " , " << us.plates_ << " ]";
    }
};

/**
 *The Flyweight stores a common portion of the state (also called intrinsic
 * state) that belongs to multiple real business entities. The Flyweight accepts
 * the rest of the state (extrinsic state, unique for each entity) via its
 * method parameters.
 */
class Flyweight
{
private:
    SharedState *shared_state_;

public:
    Flyweight(const SharedState *shared_state) : shared_state_(new SharedState(*shared_state))
    {
    }
    Flyweight(const Flyweight &other) : shared_state_(new SharedState(*other.shared_state_))
    {
    }
    ~Flyweight()
    {
        delete shared_state_;
    }
    SharedState *shared_state() const
    {
        return shared_state_;
    }
    void Operation(const UniqueState &unique_state) const
    {
        std::cout << "Flyweight: Displaying shared (" << *shared_state_ << ") and unique (" << unique_state << ") state.\n";
    }
};
/**
 *The Flyweight Factory creates and manages the Flyweight objects. It
 * ensures that flyweights are shared correctly. When the client requests a
 * flyweight, the factory either returns an existing instance or creates a new
 * one, if it doesn't exist yet.
 */
class FlyweightFactory
{
    /**
     * @var Flyweight[]
     */
private:
    std::unordered_map<std::string, Flyweight> flyweights_;
    /**
     *Returns a Flyweight's string hash for a given state.
     */
    std::string GetKey(const SharedState &ss) const
    {
        return ss.brand_ + "_" + ss.model_ + "_" + ss.color_;
    }

public:
    FlyweightFactory(std::initializer_list<SharedState> share_states)
    {
        for (const SharedState &ss : share_states)
        {
            this->flyweights_.insert(std::make_pair<std::string, Flyweight>(this->GetKey(ss), Flyweight(&ss)));
        }
    }

    /**
     *Returns an existing Flyweight with a given state or creates a new
     * one.
     */
    Flyweight GetFlyweight(const SharedState &shared_state)
    {
        std::string key = this->GetKey(shared_state);
        if (this->flyweights_.find(key) == this->flyweights_.end())
        {
            std::cout << "FlyweightFactory: Can't find a flyweight, creating new one.\n";
            this->flyweights_.insert(std::make_pair(key, Flyweight(&shared_state)));
        }
        else
        {
            std::cout << "FlyweightFactory: Reusing existing flyweight.\n";
        }
        return this->flyweights_.at(key);
    }
    void ListFlyweights() const
    {
        size_t count = this->flyweights_.size();
        std::cout << "\nFlyweightFactory: I have " << count << " flyweights:\n";
        for (std::pair<std::string, Flyweight> pair : this->flyweights_)
        {
            std::cout << pair.first << "\n";
        }
    }
};

// ...
void AddCarToPoliceDatabase(
    FlyweightFactory &ff, const std::string &plates, const std::string &owner,
    const std::string &brand, const std::string &model, const std::string &color)
{
    std::cout << "\nClient: Adding a car to database.\n";
    const Flyweight &flyweight = ff.GetFlyweight({brand, model, color});
    //The client code either stores or calculates extrinsic state and
    // passes it to the flyweight's methods.

/**
 *The client code usually creates a bunch of pre-populated flyweights in
 * the initialization stage of the application.
 */

int main()
{
    FlyweightFactory *factory = new FlyweightFactory({{"Chevrolet", "Camaro2018", "pink"}, {"Mercedes Benz", "C300", "black"}, {"Mercedes Benz", "C500", "red"}, {"BMW", "M5", "red"}, {"BMW", "X6", "white"}});
    factory->ListFlyweights();

    AddCarToPoliceDatabase(*factory,
                            "CL234IR",
                            "James Doe",
                            "BMW",
                            "M5",
                            "red");

    AddCarToPoliceDatabase(*factory,
                            "CL234IR",
                            "James Doe",
                            "BMW",
                            "X1",
                            "red");
    factory->ListFlyweights();
    delete factory;

    return 0;
}

//text output
//FlyweightFactory: I have 5 flyweights:
//BMW_X6_white
//Mercedes Benz_C500_red
//Mercedes Benz_C300_black
//BMW_M5_red
//Chevrolet_Camaro2018_pink
//Client: Adding a car to database.
//FlyweightFactory: Reusing existing flyweight.
//Flyweight: Displaying shared ([ BMW , M5 , red ]) and unique ([ CL234IR , James Doe ]) state.
//Client: Adding a car to database.
//FlyweightFactory: Can't find a flyweight, creating new one.
//Flyweight: Displaying shared ([ BMW , X1 , red ]) and unique ([ CL234IR , James Doe ]) state.
//FlyweightFactory: I have 6 flyweights:
//BMW_X1_red
//Mercedes Benz_C300_black
//BMW_X6_white
//Mercedes Benz_C500_red
//BMW_M5_red
//Chevrolet_Camaro2018_pink
```
---

## When to Use

- Implementation of the Flyweight design pattern
- When you need the specific functionality provided by this pattern

---

## References

- [Refactoring Guru: Flyweight Pattern](https://refactoring.guru/design-patterns/flyweight)
- [Wikipedia: Flyweight Pattern](https://en.wikipedia.org/wiki/Flyweight_pattern)
- [GitHub: Design Patterns C++](https://github.com/RefactoringGuru/design-patterns-cpp.git)
- [GitHub: Design Patterns Python](https://github.com/RefactoringGuru/design-patterns-python.git)
---

> This work is licensed under a [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](https://creativecommons.org/licenses/by-nc-nd/4.0/).
