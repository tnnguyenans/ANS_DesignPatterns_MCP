# Singleton Design Pattern

**Intent:**\
Lets you ensure that a class has only one instance, while providing a
global access point to this instance. One instance per each subclass (if any).
---

## Python
```python

class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not
        affect the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        """
        Finally, any singleton should define some business logic, which can
        be executed on its instance.
        """

        # ...


if __name__ == "__main__":
    # The client code.
    #
    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")

# text output
# Singleton works, both variables contain the same instance.
```
---

## C++
The Singleton class defines the `GetInstance` method that serves as an
alternative to constructor and lets clients access the same instance of this
class over and over

```cpp
class Singleton
{
    /*The Singleton's constructor should always be private to prevent
    direct construction calls with the `new` operator.*/

protected:
    Singleton(const std::string value): value_(value)
    {
    }

    static Singleton* singleton_;

    std::string value_;

public:

    /*Singletons should not be cloneable.*/
    Singleton(Singleton &other) = delete;
    /*Singletons should not be assignable.*/
    void operator=(const Singleton &) = delete;
    /*This is the static method that controls the access to the singleton
    instance. On the first run, it creates a singleton object and places it
    into the static field. On subsequent runs, it returns the client existing
    object stored in the static field.*/
    static Singleton *GetInstance(const std::string& value);
    /*Finally, any singleton should define some business logic, which can
    be executed on its instance.*/
    void SomeBusinessLogic()
    {
        // ...
    }

    std::string value() const{
        return value_;
    } 
};

Singleton* Singleton::singleton_= nullptr;;

/*Static methods should be defined outside the class.*/
Singleton *Singleton::GetInstance(const std::string& value)
{
    /*This is a safer way to create an instance. instance = new Singleton is dangerous 
    in case two instance threads wants to access at the same time*/
    if(singleton_==nullptr){
        singleton_ = new Singleton(value);
    }
    return singleton_;
}

void ThreadFoo(){
    // Following code emulates slow initialization.
    std::this_thread::sleep_for(std::chrono::milliseconds(1000));
    Singleton* singleton = Singleton::GetInstance("FOO");
    std::cout << singleton->value() << "\n";
}

void ThreadBar(){
    // Following code emulates slow initialization.
    std::this_thread::sleep_for(std::chrono::milliseconds(1000));
    Singleton* singleton = Singleton::GetInstance("BAR");
    std::cout << singleton->value() << "\n";
}


int main()
{
    std::cout <<"If you see the same value, then singleton was reused (yay!\n" <<
                "If you see different values, then 2 singletons were created (booo!!)\n\n" <<
                "RESULT:\n";   
    std::thread t1(ThreadFoo);
    std::thread t2(ThreadBar);
    t1.join();
    t2.join();

    return 0;
}

//text output
//If you see the same value, then singleton was reused (yay!
//If you see different values, then 2 singletons were created (booo!!)
//RESULT:
//BAR
//FOO
```
---

## When to Use

- When you need to ensure only one instance of a class exists across your application.
- When you want a single point of access or coordination, such as for configuration, logging, device management, etc.

---

## References

- [Refactoring Guru: Singleton Pattern](https://refactoring.guru/design-patterns/singleton)
- [Wikipedia: Singleton Pattern](https://en.wikipedia.org/wiki/Singleton_pattern)
- [GitHub: Design Patterns C++](https://github.com/RefactoringGuru/design-patterns-cpp.git)
- [GitHub: Design Patterns Python](https://github.com/RefactoringGuru/design-patterns-python.git)
---

> This work is licensed under a [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](https://creativecommons.org/licenses/by-nc-nd/4.0/).

