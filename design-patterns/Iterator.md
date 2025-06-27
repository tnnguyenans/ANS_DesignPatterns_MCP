# Iterator Design Pattern

**Intent:**\
Lets you traverse elements of a collection without exposing its underlying representation (list, stack, tree, etc.).
---

## Python
```python
"""
Iterator Design Pattern

Intent: Lets you traverse elements of a collection without exposing its
underlying representation (list, stack, tree, etc.).

from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any

"""
To create an iterator in Python, there are two abstract classes from the
built-in `collections` module - Iterable,Iterator. We need to implement the
`__iter__()` method in the iterated object (collection), and the `__next__ ()`
method in theiterator.

class AlphabeticalOrderIterator(Iterator):
    """
Concrete Iterators implement various traversal algorithms. These classes
    store the current traversal position at all times.

    """
`_position` attribute stores the current traversal position. An iterator
    may have a lot of other fields for storing iteration state, especially when
    it is supposed to work with a particular kind of collection.

    """
This attribute indicates the traversal direction.

    def __init__(self, collection: WordsCollection, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._sorted_items = None  # Will be set on first __next__ call
        self._position = 0

    def __next__(self) -> Any:
        """
Optimization: sorting happens only when the first items is actually
        requested.

        """
The __next__() method must return the next item in the sequence. On
        reaching the end, and in subsequent calls, it must raise StopIteration.

class WordsCollection(Iterable):
    """
Concrete Collections provide one or several methods for retrieving fresh
    iterator instances, compatible with the collection class.

    def __init__(self, collection: list[Any] | None = None) -> None:
        self._collection = collection or []

    def __getitem__(self, index: int) -> Any:
        return self._collection[index]

    def __iter__(self) -> AlphabeticalOrderIterator:
        """
The __iter__() method returns the iterator object itself, by default
        we return the iterator in ascending order.

    def get_reverse_iterator(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self, True)

    def add_item(self, item: Any) -> None:
        self._collection.append(item)

if __name__ == "__main__":
    #The client code may or may not know about the Concrete Iterator or
    # Collection classes, depending on the level of indirection you want to keep
    # in your program.

    print("Straight traversal:")
    print("\n".join(collection))
    print("")

    print("Reverse traversal:")
    print("\n".join(collection.get_reverse_iterator()), end="")

# text output
# Straight traversal:
# A
# B
# C
# Reverse traversal:
# C
# B
# A
```
---

## C++
```cpp
/**
 *Iterator Design Pattern
 * Intent: Lets you traverse elements of a collection without exposing its
 * underlying representation (list, stack, tree, etc.).
 */

#include <iostream>
#include <string>
#include <vector>

/**
     *C++ has its own implementation of iterator that works with 
     * a different generics containers defined by the standard library.
     */

template <typename T, typename U>
class Iterator {
 public:
  typedef typename std::vector<T>::iterator iter_type;
  Iterator(U *p_data, bool reverse = false) : m_p_data_(p_data) {
    m_it_ = m_p_data_->m_data_.begin();
  }

  void First() {
    m_it_ = m_p_data_->m_data_.begin();
  }

  void Next() {
    m_it_++;
  }

  bool IsDone() {
    return (m_it_ == m_p_data_->m_data_.end());
  }

  iter_type Current() {
    return m_it_;
  }

 private:
  U *m_p_data_;
  iter_type m_it_;
};

/**
 *Generic Collections/Containers provides one or several methods for retrieving fresh
 * iterator instances, compatible with the collection class.
 */

template <class T>
class Container {
  friend class Iterator<T, Container>;

 public:
  void Add(T a) {
    m_data_.push_back(a);
  }

  Iterator<T, Container> *CreateIterator() {
    return new Iterator<T, Container>(this);
  }

 private:
  std::vector<T> m_data_;
};

class Data {
 public:
  Data(int a = 0) : m_data_(a) {}

  void set_data(int a) {
    m_data_ = a;
  }

  int data() {
    return m_data_;
  }

 private:
  int m_data_;
};

/**
     *The client code may or may not know about the Concrete Iterator or
     * Collection classes, for this implementation the container is generic so you
     * can used with an int or with a custom class.
     */
void ClientCode() {
  std::cout << "________________Iterator with int______________________________________" << std::endl;
  Container<int> cont;

  for (int i = 0; i < 10; i++) {
    cont.Add(i);
  }

  Iterator<int, Container<int>> *it = cont.CreateIterator();
  for (it->First(); !it->IsDone(); it->Next()) {
    std::cout << *it->Current() << std::endl;
  }

  Container<Data> cont2;
  Data a(100), b(1000), c(10000);
  cont2.Add(a);
  cont2.Add(b);
  cont2.Add(c);

  std::cout << "________________Iterator with custom Class______________________________" << std::endl;
  Iterator<Data, Container<Data>> *it2 = cont2.CreateIterator();
  for (it2->First(); !it2->IsDone(); it2->Next()) {
    std::cout << it2->Current()->data() << std::endl;
  }
  delete it;
  delete it2;
}

int main() {
  ClientCode();
  return 0;
}

//text output
//________________Iterator with int______________________________________
//0
//1
//2
//3
//4
//5
//6
//7
//8
//9
//________________Iterator with custom Class______________________________
//100
//1000
//10000
```
---

## When to Use

- Implementation of the Iterator design pattern
- When you need the specific functionality provided by this pattern

---

## References

- [Refactoring Guru: Iterator Pattern](https://refactoring.guru/design-patterns/iterator)
- [Wikipedia: Iterator Pattern](https://en.wikipedia.org/wiki/Iterator_pattern)
- [GitHub: Design Patterns C++](https://github.com/RefactoringGuru/design-patterns-cpp.git)
- [GitHub: Design Patterns Python](https://github.com/RefactoringGuru/design-patterns-python.git)
---

> This work is licensed under a [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](https://creativecommons.org/licenses/by-nc-nd/4.0/).
