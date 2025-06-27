# Composite Design Pattern

**Intent:**\
Lets you compose objects into tree structures and then work with these structures as if they were individual objects.
---

## Python
```python
"""
Composite Design Pattern

Intent: Lets you compose objects into tree structures and then work with these
structures as if they were individual objects.

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Component(ABC):
    """
The base Component class declares common operations for both simple and
    complex objects of a composition.

    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, parent: Component):
        """
Optionally, the base Component can declare an interface for setting
        and accessing a parent of the component in a tree structure. It can also
        provide some default implementation for these methods.

        self._parent = parent

    """
In some cases, it would be beneficial to define the child-management
    operations right in the base Component class. This way, you won't need to
    expose any concrete component classes to the client code, even during the
    object tree assembly. The downside is that these methods will be empty for
    the leaf-level components.

    def add(self, component: Component) -> None:
        pass

    def remove(self, component: Component) -> None:
        pass

    def is_composite(self) -> bool:
        """
You can provide a method that lets the client code figure out
        whether a component can bear children.

        return False

    @abstractmethod
    def operation(self) -> str:
        """
The base Component may implement some default behavior or leave it
        to concrete classes (by declaring the method containing the behavior as
        "abstract").

        pass

class Leaf(Component):
    """
The Leaf class represents the end objects of a composition. A leaf can't
    have any children.

    Usually, it's the Leaf objects that do the actual work, whereas Composite
    objects only delegate to their sub-components.

    """

    def operation(self) -> str:
        return "Leaf"

class Composite(Component):
    """
The Composite class represents the complex components that may have
    children. Usually, the Composite objects delegate the actual work to their
    children and then "sum-up" the result.

    def __init__(self) -> None:
        self._children: List[Component] = []

    """
A composite object can add or remove other components (both simple or
    complex) to or from its child list.

    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def operation(self) -> str:
        """
The Composite executes its primary logic in a particular way. It
        traverses recursively through all its children, collecting and summing
        their results. Since the composite's children pass these calls to their
        children and so forth, the whole object tree is traversed as a result.

        results = []
        for child in self._children:
            results.append(child.operation())
        return f"Branch({'+'.join(results)})"

def client_code(component: Component) -> None:
    """
The client code works with all of the components via the base interface.

    print(f"RESULT: {component.operation()}", end="")

def client_code2(component1: Component, component2: Component) -> None:
    """
Thanks to the fact that the child-management operations are declared in
    the base Component class, the client code can work with any component,
    simple or complex, without depending on their concrete classes.

    if component1.is_composite():
        component1.add(component2)

    print(f"RESULT: {component1.operation()}", end="")

if __name__ == "__main__":
    #This way the client code can support the simple leaf components...

    #...as well as the complex composites.

    branch1 = Composite()
    branch1.add(Leaf())
    branch1.add(Leaf())

    branch2 = Composite()
    branch2.add(Leaf())

    tree.add(branch1)
    tree.add(branch2)

    print("Client: Now I've got a composite tree:")
    client_code(tree)
    print("\n")

    print("Client: I don't need to check the components classes even when managing the tree:")
    client_code2(tree, simple)

# text output
# Client: I've got a simple component:
# RESULT: Leaf
# Client: Now I've got a composite tree:
# RESULT: Branch(Branch(Leaf+Leaf)+Branch(Leaf))
# Client: I don't need to check the components classes even when managing the tree:
# RESULT: Branch(Branch(Leaf+Leaf)+Branch(Leaf)+Leaf)
```
---

## C++
```cpp
#include <algorithm>
#include <iostream>
#include <list>
#include <string>
/**
 *Composite Design Pattern
 * Intent: Lets you compose objects into tree structures and then work with
 * these structures as if they were individual objects.
 */
/**
 *The base Component class declares common operations for both simple and
 * complex objects of a composition.
 */
class Component {
  /**
     * @var Component
     */
 protected:
  Component *parent_;
  /**
     *Optionally, the base Component can declare an interface for setting
     * and accessing a parent of the component in a tree structure. It can also
     * provide some default implementation for these methods.
     */
 public:
  virtual ~Component() {}
  void SetParent(Component *parent) {
    this->parent_ = parent;
  }
  Component *GetParent() const {
    return this->parent_;
  }
  /**
     *In some cases, it would be beneficial to define the child-management
     * operations right in the base Component class. This way, you won't need to
     * expose any concrete component classes to the client code, even during the
     * object tree assembly. The downside is that these methods will be empty
     * for the leaf-level components.
     */
  virtual void Add(Component *component) {}
  virtual void Remove(Component *component) {}
  /**
     *You can provide a method that lets the client code figure out whether
     * a component can bear children.
     */
  virtual bool IsComposite() const {
    return false;
  }
  /**
     *The base Component may implement some default behavior or leave it to
     * concrete classes (by declaring the method containing the behavior as
     * "abstract").
     */
  virtual std::string Operation() const = 0;
};
/**
 *The Leaf class represents the end objects of a composition. A leaf can't
 * have any children.
 * Usually, it's the Leaf objects that do the actual work, whereas Composite
 * objects only delegate to their sub-components.
 */
class Leaf : public Component {
 public:
  std::string Operation() const override {
    return "Leaf";
  }
};
/**
 *The Composite class represents the complex components that may have
 * children. Usually, the Composite objects delegate the actual work to their
 * children and then "sum-up" the result.
 */
class Composite : public Component {
  /**
     * @var \SplObjectStorage
     */
 protected:
  std::list<Component *> children_;

 public:
  /**
     *A composite object can add or remove other components (both simple or
     * complex) to or from its child list.
     */
  void Add(Component *component) override {
    this->children_.push_back(component);
    component->SetParent(this);
  }
  /**
     *Have in mind that this method removes the pointer to the list but doesn't frees the 
     *     memory, you should do it manually or better use smart pointers.
     */
  void Remove(Component *component) override {
    children_.remove(component);
    component->SetParent(nullptr);
  }
  bool IsComposite() const override {
    return true;
  }
  /**
     *The Composite executes its primary logic in a particular way. It
     * traverses recursively through all its children, collecting and summing
     * their results. Since the composite's children pass these calls to their
     * children and so forth, the whole object tree is traversed as a result.
     */
  std::string Operation() const override {
    std::string result;
    for (const Component *c : children_) {
      if (c == children_.back()) {
        result += c->Operation();
      } else {
        result += c->Operation() + "+";
      }
    }
    return "Branch(" + result + ")";
  }
};
/**
 *The client code works with all of the components via the base interface.
 */
void ClientCode(Component *component) {
  // ...
  std::cout << "RESULT: " << component->Operation();
  // ...
}

/**
 *Thanks to the fact that the child-management operations are declared in
 * the base Component class, the client code can work with any component, simple
 * or complex, without depending on their concrete classes.
 */
void ClientCode2(Component *component1, Component *component2) {
  // ...
  if (component1->IsComposite()) {
    component1->Add(component2);
  }
  std::cout << "RESULT: " << component1->Operation();
  // ...
}

/**
 *This way the client code can support the simple leaf components...
 */

int main() {
  Component *simple = new Leaf;
  std::cout << "Client: I've got a simple component:\n";
  ClientCode(simple);
  std::cout << "\n\n";
  /**
     *...as well as the complex composites.
     */

  Component *tree = new Composite;
  Component *branch1 = new Composite;

  Component *leaf_1 = new Leaf;
  Component *leaf_2 = new Leaf;
  Component *leaf_3 = new Leaf;
  branch1->Add(leaf_1);
  branch1->Add(leaf_2);
  Component *branch2 = new Composite;
  branch2->Add(leaf_3);
  tree->Add(branch1);
  tree->Add(branch2);
  std::cout << "Client: Now I've got a composite tree:\n";
  ClientCode(tree);
  std::cout << "\n\n";

  std::cout << "Client: I don't need to check the components classes even when managing the tree:\n";
  ClientCode2(tree, simple);
  std::cout << "\n";

  delete simple;
  delete tree;
  delete branch1;
  delete branch2;
  delete leaf_1;
  delete leaf_2;
  delete leaf_3;

  return 0;
}

//text output
//Client: I've got a simple component:
//RESULT: Leaf
//Client: Now I've got a composite tree:
//RESULT: Branch(Branch(Leaf+Leaf)+Branch(Leaf))
//Client: I don't need to check the components classes even when managing the tree:
//RESULT: Branch(Branch(Leaf+Leaf)+Branch(Leaf)+Leaf)
```
---

## When to Use

- Implementation of the Composite design pattern
- When you need the specific functionality provided by this pattern

---

## References

- [Refactoring Guru: Composite Pattern](https://refactoring.guru/design-patterns/composite)
- [Wikipedia: Composite Pattern](https://en.wikipedia.org/wiki/Composite_pattern)
- [GitHub: Design Patterns C++](https://github.com/RefactoringGuru/design-patterns-cpp.git)
- [GitHub: Design Patterns Python](https://github.com/RefactoringGuru/design-patterns-python.git)
---

> This work is licensed under a [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](https://creativecommons.org/licenses/by-nc-nd/4.0/).
