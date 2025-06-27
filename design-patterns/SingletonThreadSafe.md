# Singleton Design Pattern-ThreadSafe   

**Intent:**\
Lets you ensure that a class has only one instance, while providing a
global access point to this instance. One instance per each subclass (if any).
This implementation is thread-safe and used in multi-threaded applications.
---

## Python
```python

from threading import Lock, Thread


class SingletonMeta(type):
    """
    This is a thread-safe implementation of Singleton.
    """
    _instances = {}
    _lock: Lock = Lock()
    """
    We now have a lock object that will be used to synchronize
    threads during first access to the Singleton.
    """

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not
        affect the returned instance.
        """
        # Now, imagine that the program has just been launched.
        # Since there's no Singleton instance yet, multiple threads can
        # simultaneously pass the previous conditional and reach this
        # point almost at the same time. The first of them will acquire
        # lock and will proceed further, while the rest will wait here.
        #
        with cls._lock:
            # The first thread to acquire the lock, reaches this
            # conditional, goes inside and creates the Singleton
            # instance. Once it leaves the lock block, a thread that
            # might have been waiting for the lock release may then
            # enter this section. But since the Singleton field is
            # already initialized, the thread won't create a new
            # object.
            #
            # First thread to acquire the lock, reaches this
            # conditional, goes inside and creates the Singleton
            # instance. Once it leaves the lock block, a thread that
            # might have been waiting for the lock release may then
            # enter this section. But since the Singleton field is
            # already initialized, the thread won't create a new
            # object.
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    value: str = None
    """
    We'll use this property to prove that our Singleton really works.
    """

    def __init__(self, value: str) -> None:
        self.value = value

    def some_business_logic(self):
        """
        Finally, any singleton should define some business logic, which can
        be executed on its instance.
        """


def test_singleton(value: str) -> None:
    singleton = Singleton(value)
    print(singleton.value)


if __name__ == "__main__":
    # The client code.
    print("If you see the same value, then singleton was reused (yay!)\n"
          "If you see different values, "
          "then 2 singletons were created (booo!!)\n\n"
          "RESULT:\n")

    process1 = Thread(target=test_singleton, args=("FOO",))
    process2 = Thread(target=test_singleton, args=("BAR",))
    process1.start()
    process2.start()


# text output
# If you see the same value, then singleton was reused (yay!)
# If you see different values, then 2 singletons were created (booo!!)
# RESULT:
# FOO
# FOO
```
---

## C++
The Singleton class defines the `GetInstance` method that serves as an
alternative to constructor and lets clients access the same instance of this
class over and over

```cpp

#include <iostream>
#include <mutex>
#include <thread>

class Singleton
{

    /**
     * The Singleton's constructor/destructor should always be private to prevent
     * direct construction/desctruction calls with the `new`/`delete` operator.
     */
private:
    static Singleton * pinstance_;
    static std::mutex mutex_;

protected:
    Singleton(const std::string value): value_(value)
    {
    }
    ~Singleton() {}
    std::string value_;

public:
    /**
     * Singletons should not be cloneable.
     */
    Singleton(Singleton &other) = delete;
    /**
     * Singletons should not be assignable.
     */
    void operator=(const Singleton &) = delete;
    /**
     * This is the static method that controls the access to the singleton
     * instance. On the first run, it creates a singleton object and places it
     * into the static field. On subsequent runs, it returns the client existing
     * object stored in the static field.
     */

    static Singleton *GetInstance(const std::string& value);
    /*
     * Finally, any singleton should define some business logic, which can
     * be executed on its instance.
     */
    void SomeBusinessLogic()
    {
        // ...
    }
    
    std::string value() const{
        return value_;
    } 
};

    /*
     * Static methods should be defined outside the class.
     */

Singleton* Singleton::pinstance_{nullptr};
std::mutex Singleton::mutex_;

    /* The first time we call GetInstance we will lock the storage location
     * and then we make sure again that the variable is null and then we 
     * set the value.
     */
Singleton *Singleton::GetInstance(const std::string& value)
{
    std::lock_guard<std::mutex> lock(mutex_);
    if (pinstance_ == nullptr)
    {
        pinstance_ = new Singleton(value);
    }
    return pinstance_;
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
- Use in multi-threaded applications.
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

