# Singleton Pattern

**Intent:**\
Ensure a class has only one instance and provide a global point of access to it.

---

## Python

```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# Usage example:
s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # Output: True
```

---

## C++

```cpp
class Singleton {
private:
    static Singleton* instance;
    Singleton() {} // private constructor to prevent instancing
public:
    static Singleton* getInstance() {
        if (!instance)
            instance = new Singleton();
        return instance;
    }
};

// Definition of static member
Singleton* Singleton::instance = nullptr;

// Usage example:
// Singleton* s1 = Singleton::getInstance();
// Singleton* s2 = Singleton::getInstance();
// std::cout << (s1 == s2); // Output: 1 (true)
```

---

## When to Use

- When you need to ensure only one instance of a class exists across your application.
- When you want a single point of access or coordination, such as for configuration, logging, device management, etc.

---

## References

- [Refactoring Guru: Singleton Pattern](https://refactoring.guru/design-patterns/singleton)
- [Wikipedia: Singleton Pattern](https://en.wikipedia.org/wiki/Singleton_pattern)

---

> This work is licensed under a [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](https://creativecommons.org/licenses/by-nc-nd/4.0/).

