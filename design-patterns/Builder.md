# Builder Design Pattern

**Intent:**\
Lets you construct complex objects step by step. The pattern allows you to produce different types and representations of an object using the same construction code.
---

## Python
```python
"""
Builder Design Pattern

Intent: Lets you construct complex objects step by step. The pattern allows you
to produce different types and representations of an object using the same
construction code.

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

class Builder(ABC):
    """
The Builder interface specifies methods for creating the different parts
    of the Product objects.

    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def produce_part_a(self) -> None:
        pass

    @abstractmethod
    def produce_part_b(self) -> None:
        pass

    @abstractmethod
    def produce_part_c(self) -> None:
        pass

class ConcreteBuilder1(Builder):
    """
The Concrete Builder classes follow the Builder interface and provide
    specific implementations of the building steps. Your program may have
    several variations of Builders, implemented differently.

    def __init__(self) -> None:
        """
A fresh builder instance should contain a blank product object,
        which is used in further assembly.

    def reset(self) -> None:
        self._product = Product1()

    @property
    def product(self) -> Product1:
        """
Concrete Builders are supposed to provide their own methods for
        retrieving results. That's because various types of builders may create
        entirely different products that don't follow the same interface.
        Therefore, such methods cannot be declared in the base Builder interface
        (at least in a statically typed programming language).

        Usually, after returning the end result to the client, a builder
        instance is expected to be ready to start producing another product.
        That's why it's a usual practice to call the reset method at the end of
        the `getProduct` method body. However, this behavior is not mandatory,
        and you can make your builders wait for an explicit reset call from the
        client code before disposing of the previous result.

        """
        product = self._product
        self.reset()
        return product

    def produce_part_a(self) -> None:
        self._product.add("PartA1")

    def produce_part_b(self) -> None:
        self._product.add("PartB1")

    def produce_part_c(self) -> None:
        self._product.add("PartC1")

class Product1():
    """
It makes sense to use the Builder pattern only when your products are
    quite complex and require extensive configuration.

    Unlike in other creational patterns, different concrete builders can produce
    unrelated products. In other words, results of various builders may not
    always follow the same interface.

    """

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Product parts: {', '.join(self.parts)}", end="")

class Director:
    """
The Director is only responsible for executing the building steps in a
    particular sequence. It is helpful when producing products according to a
    specific order or configuration. Strictly speaking, the Director class is
    optional, since the client can control builders directly.

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        """
The Director works with any builder instance that the client code
        passes to it. This way, the client code may alter the final type of the
        newly assembled product.

    """
The Director can construct several product variations using the same
    building steps.

    def build_minimal_viable_product(self) -> None:
        self.builder.produce_part_a()

    def build_full_featured_product(self) -> None:
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()

if __name__ == "__main__":
    """
The client code creates a builder object, passes it to the director and
    then initiates the construction process. The end result is retrieved from
    the builder object.

    director = Director()
    builder = ConcreteBuilder1()
    director.builder = builder

    print("Standard basic product: ")
    director.build_minimal_viable_product()
    builder.product.list_parts()

    print("\n")

    print("Standard full featured product: ")
    director.build_full_featured_product()
    builder.product.list_parts()

    print("\n")

    #Remember, the Builder pattern can be used without a Director class.

# text output
# Standard basic product: 
# Product parts: PartA1
# Standard full featured product: 
# Product parts: PartA1, PartB1, PartC1
# Custom product: 
# Product parts: PartA1, PartB1
```
---

## C++
```cpp
#include <iostream>
#include <string>
#include <vector>

/**
 *Builder Design Pattern
 * Intent: Lets you construct complex objects step by step. The pattern allows
 * you to produce different types and representations of an object using the
 * same construction code.
 */

/**
 *It makes sense to use the Builder pattern only when your products are
 * quite complex and require extensive configuration.
 * Unlike in other creational patterns, different concrete builders can produce
 * unrelated products. In other words, results of various builders may not
 * always follow the same interface.
 */

class Product1{
    public:
    std::vector<std::string> parts_;
    void ListParts()const{
        std::cout << "Product parts: ";
        for (size_t i=0;i<parts_.size();i++){
            if(parts_[i]== parts_.back()){
                std::cout << parts_[i];
            }else{
                std::cout << parts_[i] << ", ";
            }
        }
        std::cout << "\n\n"; 
    }
};

/**
 *The Builder interface specifies methods for creating the different parts
 * of the Product objects.
 */
class Builder{
    public:
    virtual ~Builder(){}
    virtual void ProducePartA() const =0;
    virtual void ProducePartB() const =0;
    virtual void ProducePartC() const =0;
};
/**
 *The Concrete Builder classes follow the Builder interface and provide
 * specific implementations of the building steps. Your program may have several
 * variations of Builders, implemented differently.
 */
class ConcreteBuilder1 : public Builder{
    private:

    Product1* product;

    /**
     *A fresh builder instance should contain a blank product object, which
     * is used in further assembly.
     */
    public:

    ConcreteBuilder1(){
        this->Reset();
    }

    ~ConcreteBuilder1(){
        delete product;
    }

    void Reset(){
        this->product= new Product1();
    }
    /**
     *All production steps work with the same product instance.
     */

    void ProducePartA()const override{
        this->product->parts_.push_back("PartA1");
    }

    void ProducePartB()const override{
        this->product->parts_.push_back("PartB1");
    }

    void ProducePartC()const override{
        this->product->parts_.push_back("PartC1");
    }

    /**
     *Concrete Builders are supposed to provide their own methods for
     * retrieving results. That's because various types of builders may create
     * entirely different products that don't follow the same interface.
     * Therefore, such methods cannot be declared in the base Builder interface
     * (at least in a statically typed programming language). Note that PHP is a
     * dynamically typed language and this method CAN be in the base interface.
     * However, we won't declare it there for the sake of clarity.
     * Usually, after returning the end result to the client, a builder instance
     * is expected to be ready to start producing another product. That's why
     * it's a usual practice to call the reset method at the end of the
     * `getProduct` method body. However, this behavior is not mandatory, and
     * you can make your builders wait for an explicit reset call from the
     * client code before disposing of the previous result.
     */

    /**
     *Please be careful here with the memory ownership. Once you call GetProduct
     * the user of this function is responsable to release this memory. Here could be 
     * a better option to use smart pointers to avoid memory leaks
     */

    Product1* GetProduct() {
        Product1* result= this->product;
        this->Reset();
        return result;
    }
};

/**
 *The Director is only responsible for executing the building steps in a
 * particular sequence. It is helpful when producing products according to a
 * specific order or configuration. Strictly speaking, the Director class is
 * optional, since the client can control builders directly.
 */
class Director{
    /**
     * @var Builder
     */
    private:
    Builder* builder;
    /**
     *The Director works with any builder instance that the client code
     * passes to it. This way, the client code may alter the final type of the
     * newly assembled product.
     */

    public:

    void set_builder(Builder* builder){
        this->builder=builder;
    }

    /**
     *The Director can construct several product variations using the same
     * building steps.
     */

    void BuildMinimalViableProduct(){
        this->builder->ProducePartA();
    }
    
    void BuildFullFeaturedProduct(){
        this->builder->ProducePartA();
        this->builder->ProducePartB();
        this->builder->ProducePartC();
    }
};
/**
 *The client code creates a builder object, passes it to the director and
 * then initiates the construction process. The end result is retrieved from the
 * builder object.
 */
/**
 *I used raw pointers for simplicity however you may prefer to use smart pointers here
 */
void ClientCode(Director& director)
{
    ConcreteBuilder1* builder = new ConcreteBuilder1();
    director.set_builder(builder);
    std::cout << "Standard basic product:\n"; 
    director.BuildMinimalViableProduct();
    
    Product1* p= builder->GetProduct();
    p->ListParts();
    delete p;

    std::cout << "Standard full featured product:\n"; 
    director.BuildFullFeaturedProduct();

    p= builder->GetProduct();
    p->ListParts();
    delete p;

    //Remember, the Builder pattern can be used without a Director class.

    delete builder;
}

int main(){
    Director* director= new Director();
    ClientCode(*director);
    delete director;
    return 0;    
}

//text output
//Standard basic product:
//Product parts: PartA1
//Standard full featured product:
//Product parts: PartA1, PartB1, PartC1
//Custom product:
//Product parts: PartA1, PartC1
```
---

## When to Use

- Implementation of the Builder design pattern
- When you need the specific functionality provided by this pattern

---

## References

- [Refactoring Guru: Builder Pattern](https://refactoring.guru/design-patterns/builder)
- [Wikipedia: Builder Pattern](https://en.wikipedia.org/wiki/Builder_pattern)
- [GitHub: Design Patterns C++](https://github.com/RefactoringGuru/design-patterns-cpp.git)
- [GitHub: Design Patterns Python](https://github.com/RefactoringGuru/design-patterns-python.git)
---

> This work is licensed under a [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](https://creativecommons.org/licenses/by-nc-nd/4.0/).
