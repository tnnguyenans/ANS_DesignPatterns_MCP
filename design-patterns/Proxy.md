# Proxy Design Pattern

**Intent:**\
Provide a surrogate or placeholder for another object to control access to the original object or to add other responsibilities.
---

## Python
```python
"""
Proxy Design Pattern

Intent: Provide a surrogate or placeholder for another object to control access
to the original object or to add other responsibilities.

from abc import ABC, abstractmethod

class Subject(ABC):
    """
The Subject interface declares common operations for both RealSubject
    and the Proxy. As long as the client works with RealSubject using this
    interface, you'll be able to pass it a proxy instead of a real subject.

    @abstractmethod
    def request(self) -> None:
        pass

class RealSubject(Subject):
    """
The RealSubject contains some core business logic. Usually, RealSubjects
    are capable of doing some useful work which may also be very slow or
    sensitive - e.g. correcting input data. A Proxy can solve these issues
    without any changes to the RealSubject's code.

    def request(self) -> None:
        print("RealSubject: Handling request.")

class Proxy(Subject):
    """
The Proxy has an interface identical to the RealSubject.

    def __init__(self, real_subject: RealSubject) -> None:
        self._real_subject = real_subject

    def request(self) -> None:
        """
The most common applications of the Proxy pattern are lazy loading,
        caching, controlling the access, logging, etc. A Proxy can perform one
        of these things and then, depending on the result, pass the execution to
        the same method in a linked RealSubject object.

        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self) -> bool:
        print("Proxy: Checking access prior to firing a real request.")
        return True

    def log_access(self) -> None:
        print("Proxy: Logging the time of request.", end="")

def client_code(subject: Subject) -> None:
    """
The client code is supposed to work with all objects (both subjects and
    proxies) via the Subject interface in order to support both real subjects
    and proxies. In real life, however, clients mostly work with their real
    subjects directly. In this case, to implement the pattern more easily, you
    can extend your proxy from the real subject's class.

    # ...

    subject.request()

    # ...

if __name__ == "__main__":
    print("Client: Executing the client code with a real subject:")
    real_subject = RealSubject()
    client_code(real_subject)

    print("")

    print("Client: Executing the same client code with a proxy:")
    proxy = Proxy(real_subject)
    client_code(proxy)

# text output
# Client: Executing the client code with a real subject:
# RealSubject: Handling request.
# Client: Executing the same client code with a proxy:
# Proxy: Checking access prior to firing a real request.
# RealSubject: Handling request.
# Proxy: Logging the time of request.
```
---

## C++
```cpp
#include <iostream>
/**
 *Proxy Design Pattern
 * Intent: Provide a surrogate or placeholder for another object to control
 * access to the original object or to add other responsibilities.
 */
/**
 *The Subject interface declares common operations for both RealSubject and
 * the Proxy. As long as the client works with RealSubject using this interface,
 * you'll be able to pass it a proxy instead of a real subject.
 */
class Subject {
 public:
  virtual void Request() const = 0;
};
/**
 *The RealSubject contains some core business logic. Usually, RealSubjects
 * are capable of doing some useful work which may also be very slow or
 * sensitive - e.g. correcting input data. A Proxy can solve these issues
 * without any changes to the RealSubject's code.
 */
class RealSubject : public Subject {
 public:
  void Request() const override {
    std::cout << "RealSubject: Handling request.\n";
  }
};
/**
 *The Proxy has an interface identical to the RealSubject.
 */
class Proxy : public Subject {
  /**
     * @var RealSubject
     */
 private:
  RealSubject *real_subject_;

  bool CheckAccess() const {
    //Some real checks should go here.

  /**
     *The Proxy maintains a reference to an object of the RealSubject
     * class. It can be either lazy-loaded or passed to the Proxy by the client.
     */
 public:
  Proxy(RealSubject *real_subject) : real_subject_(new RealSubject(*real_subject)) {
  }

  ~Proxy() {
    delete real_subject_;
  }
  /**
     *The most common applications of the Proxy pattern are lazy loading,
     * caching, controlling the access, logging, etc. A Proxy can perform one of
     * these things and then, depending on the result, pass the execution to the
     * same method in a linked RealSubject object.
     */
  void Request() const override {
    if (this->CheckAccess()) {
      this->real_subject_->Request();
      this->LogAccess();
    }
  }
};
/**
 *The client code is supposed to work with all objects (both subjects and
 * proxies) via the Subject interface in order to support both real subjects and
 * proxies. In real life, however, clients mostly work with their real subjects
 * directly. In this case, to implement the pattern more easily, you can extend
 * your proxy from the real subject's class.
 */
void ClientCode(const Subject &subject) {
  // ...
  subject.Request();
  // ...
}

int main() {
  std::cout << "Client: Executing the client code with a real subject:\n";
  RealSubject *real_subject = new RealSubject;
  ClientCode(*real_subject);
  std::cout << "\n";
  std::cout << "Client: Executing the same client code with a proxy:\n";
  Proxy *proxy = new Proxy(real_subject);
  ClientCode(*proxy);

  delete real_subject;
  delete proxy;
  return 0;
}

//text output
//Client: Executing the client code with a real subject:
//RealSubject: Handling request.
//Client: Executing the same client code with a proxy:
//Proxy: Checking access prior to firing a real request.
//RealSubject: Handling request.
//Proxy: Logging the time of request.
```
---

## When to Use

- Implementation of the Proxy design pattern
- When you need the specific functionality provided by this pattern

---

## References

- [Refactoring Guru: Proxy Pattern](https://refactoring.guru/design-patterns/proxy)
- [Wikipedia: Proxy Pattern](https://en.wikipedia.org/wiki/Proxy_pattern)
- [GitHub: Design Patterns C++](https://github.com/RefactoringGuru/design-patterns-cpp.git)
- [GitHub: Design Patterns Python](https://github.com/RefactoringGuru/design-patterns-python.git)
---

> This work is licensed under a [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](https://creativecommons.org/licenses/by-nc-nd/4.0/).
