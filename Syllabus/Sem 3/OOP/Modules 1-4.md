
```cpp
#include <iostream>

using namespace std;

  

// 1. Necessity for OOP

// OOP allows for better organization and reusability of code through objects and classes.

class Car

{

public:

    int speed;

    void accelerate() { speed += 10; }

};

  

// 2. Data Hiding

// Data hiding restricts access to the inner workings of an object to prevent unintended interference and misuse.

class SecureCar

{

private:

    int speed; // Hidden from outside access

  

public:

    void setSpeed(int s) { speed = s; }

    int getSpeed() { return speed; }

};

  

// 3. Data Abstraction

// Data abstraction provides only essential information to the outside world while hiding the background details.

class AbstractCar

{

public:

    void startEngine() { cout << "Engine started" << endl; }

    void stopEngine() { cout << "Engine stopped" << endl; }

};

  

// 4. Encapsulation

// Encapsulation wraps data (variables) and methods (functions) into a single unit called a class.

class EncapsulatedCar

{

private:

    int speed;

    int fuel;

  

public:

    void setSpeed(int s) { speed = s; }

    int getSpeed() { return speed; }

    void refuel(int f) { fuel = f; }

};

  

// 5. Procedural Abstraction

// Procedural abstraction manages complexity by breaking down a task into sub-tasks, which are implemented as functions or procedures.

void startEngine() { cout << "Engine started" << endl; }

void accelerate() { cout << "Car accelerated" << endl; }

void stopEngine() { cout << "Engine stopped" << endl; }

  

void drive()

{

    startEngine();

    accelerate();

    stopEngine();

}

  

// 6. Polymorphism

// Polymorphism is the ability of different classes to be treated as instances of the same class through inheritance.

class Animal

{

public:

    virtual void makeSound() { cout << "Some sound" << endl; }

};

  

class Dog : public Animal

{

public:

    void makeSound() override { cout << "Bark" << endl; }

};

  

class Cat : public Animal

{

public:

    void makeSound() override { cout << "Meow" << endl; }

};

  

void playSound(Animal *animal)

{

    animal->makeSound();

}

  

// 7. Inheritance

// Inheritance is the mechanism by which one class can inherit the properties and methods of another class, promoting code reusability.

class Vehicle

{

public:

    int speed;

    void setSpeed(int s) { speed = s; }

};

  

class InheritedCar : public Vehicle

{

public:

    void accelerate() { speed += 10; }

};

  

// Module 2: Difference between procedural and object-oriented programming

  

// 1. Single line comments

// Using // for single line comments in C++ as opposed to /* */ in C.

  

// 2. Local variable declaration within function scope

// In C++, variables can be declared anywhere in the function scope, enhancing readability and reducing errors.

void localVariableExample()

{

    int x = 10;

    if (x > 5)

    {

        int y = 20; // Variable declared within the block

        cout << y << endl;

    }

}

  

// 3. Function declaration and overloading

// Declaring functions before their use and the ability to define multiple functions with the same name but different parameters in C++.

void print(int i)

{

    cout << "Integer: " << i << endl;

}

  

void print(double d)

{

    cout << "Double: " << d << endl;

}

  

void print(string s)

{

    cout << "String: " << s << endl;

}

  

// 4. Stronger type checking

// C++ enforces stricter type checking than C.

int add(int a, int b)

{

    return a + b;

}

  

// 5. Reference variable

// Allows creating an alias for another variable, which helps in efficient parameter passing.

void referenceVariableExample()

{

    int x = 10;

    int &ref = x; // ref is a reference to x

    ref = 20;     // x is now 20

    cout << "Reference variable: " << x << endl;

}

  

// 6. Parameter passing – value vs reference

// Passing parameters by value copies the actual value, whereas passing by reference allows modification of the original variable.

void passByValue(int x)

{

    x = 20;

}

  

void passByReference(int &x)

{

    x = 20;

}

  

// 7. Passing a pointer by value or reference

// Determines whether the function can modify the pointer itself or just the value it points to.

void modifyPointer(int *p)

{

    *p = 20; // Modifies the value pointed to

}

  

void modifyPointerReference(int *&p)

{

    int y = 30;

    p = &y; // Modifies the pointer itself

}

  

// 8. #define constant vs const

// Using #define for preprocessor constants and const for typed constants in C++.

#define PI 3.14 // Preprocessor constant

  

const double pi = 3.14; // Typed constant

  

// 9. Operator new and delete

// Dynamic memory allocation and deallocation operators in C++.

void dynamicMemoryExample()

{

    int *p = new int; // Allocate memory

    *p = 10;

    cout << "Dynamic memory value: " << *p << endl;

    delete p; // Deallocate memory

}

  

// 10. Type casting operator

// Safe and explicit conversion between different data types using casting operators.

void typeCastingExample()

{

    int x = 10;

    double y = static_cast<double>(x); // Explicit type casting

    cout << "Type casted value: " << y << endl;

}

  

// 11. Inline Functions

// Functions defined with inline keyword to suggest the compiler to insert the complete body wherever the function is called to reduce overhead.

inline int addInline(int a, int b)

{

    return a + b;

}

  

// 12. Default arguments

// Specifying default values for parameters in function declarations.

void greet(string name = "Guest")

{

    cout << "Hello, " << name << endl;

}

  

// Module 3: Class & Object Properties

  

// 1. Class and Object

// A class defines a type and an object is an instance of that class.

class Person

{

public:

    string name;

    int age;

  

    void display()

    {

        cout << "Name: " << name << ", Age: " << age << endl;

    }

};

  

// 2. Scope of Class and Scope Resolution Operator

// The scope determines the visibility of class members, and the :: operator is used to define the scope.

class ScopeExample

{

public:

    void display();

};

  

void ScopeExample::display()

{

    cout << "Scope resolution operator example" << endl;

}

  

// 3. Member Function of a Class

// Functions defined inside a class that can operate on the class's data members.

class MemberFunctionExample

{

public:

    int value;

  

    void setValue(int v)

    {

        value = v;

    }

  

    int getValue()

    {

        return value;

    }

};

  

// 4. Access Specifiers

// Keywords like private, protected, and public that control the accessibility of class members.

class AccessSpecifierExample

{

private:

    int privateValue;

  

protected:

    int protectedValue;

  

public:

    int publicValue;

  

    void setPrivateValue(int v)

    {

        privateValue = v;

    }

  

    int getPrivateValue()

    {

        return privateValue;

    }

};

  

// 5. this Keyword

// A pointer to the object invoking the member function.

class ThisKeywordExample

{

public:

    int value;

  

    void setValue(int value)

    {

        this->value = value; // this->value refers to the class member

    }

  

    int getValue()

    {

        return value;

    }

};

  

// 6. Constructors and Destructors

// Special member functions that are automatically called when an object is created or destroyed.

class ConstructorDestructorExample

{

public:

    ConstructorDestructorExample()

    {

        cout << "Constructor called" << endl;

    }

  

    ~ConstructorDestructorExample()

    {

        cout << "Destructor called" << endl;

    }

};

  

// 7. Error handling (exception)

// Mechanisms to handle runtime errors using try, catch, and throw keywords.

void errorHandlingExample()

{

    try

    {

        throw runtime_error("An error occurred");

    }

    catch (const runtime_error &e)

    {

        cout << "Caught an exception: " << e.what() << endl;

    }

}

  

// Module 4: Essentials of Object-Oriented Programming

  

// 1. Operator overloading

// Providing custom implementations for operators in classes.

class Complex

{

public:

    int real, imag;

  

    Complex(int r = 0, int i = 0) : real(r), imag(i) {}

  

    // Overloading the + operator

    Complex operator+(const Complex &c)

    {

        return Complex(real + c.real, imag + c.imag);

    }

  

    void display()

    {

        cout << real << " + " << imag << "i" << endl;

    }

};

  

// 2. Function Overloading

// Defining multiple functions with the same name but different parameter lists.

void display(int i)

{

    cout << "Integer: " << i << endl;

}

  

void display(double d)

{

    cout << "Double: " << d << endl;

}

  

void display(string s)

{

    cout << "String: " << s << endl;

}

  

// 3. Friend function

// A function that is not a member of a class but has access to its private and protected members.

class FriendFunctionExample

{

private:

    int value;

  

public:

    FriendFunctionExample(int v) : value(v) {}

  

    // Friend function declaration

    friend void showValue(const FriendFunctionExample &);

};

  

void showValue(const FriendFunctionExample &f)

{

    cout << "Friend function value: " << f.value << endl;

}

  

// 4. Friend class

// A class that can access private and protected members of another class.

class FriendClassExample

{

private:

    int value;

  

public:

    FriendClassExample(int v) : value(v) {}

  

    // Friend class declaration

    friend class Accessor;

};

  

class Accessor

{

public:

    void showValue(const FriendClassExample &f)

    {

        cout << "Friend class value: " << f.value << endl;

    }

};

  

int main()

{

    // 1. Necessity for OOP

    Car myCar;

    myCar.speed = 0;

    myCar.accelerate();

    cout << "Car speed: " << myCar.speed << endl;

  

    // 2. Data Hiding

    SecureCar secureCar;

    secureCar.setSpeed(50);

    cout << "SecureCar speed: " << secureCar.getSpeed() << endl;

  

    // 3. Data Abstraction

    AbstractCar abstractCar;

    abstractCar.startEngine();

    abstractCar.stopEngine();

  

    // 4. Encapsulation

    EncapsulatedCar encapsulatedCar;

    encapsulatedCar.setSpeed(60);

    encapsulatedCar.refuel(100);

    cout << "EncapsulatedCar speed: " << encapsulatedCar.getSpeed() << endl;

  

    // 5. Procedural Abstraction

    drive();

  

    // 6. Polymorphism

    Dog dog;

    Cat cat;

    playSound(&dog);

    playSound(&cat);

  

    // 7. Inheritance

    InheritedCar inheritedCar;

    inheritedCar.setSpeed(70);

    inheritedCar.accelerate();

    cout << "InheritedCar speed: " << inheritedCar.speed << endl;

  

    // Module 2 examples

    // 2. Local variable declaration within function scope

    localVariableExample();

  

    // 3. Function declaration and overloading

    print(5);

    print(3.14);

    print("Hello");

  

    // 4. Stronger type checking

    // add(1.5, 2.5); // This will cause a compile-time error in C++

  

    // 5. Reference variable

    referenceVariableExample();

  

    // 6. Parameter passing – value vs reference

    int a = 10;

    passByValue(a);

    cout << "Pass by value: " << a << endl; // a is still 10

  

    passByReference(a);

    cout << "Pass by reference: " << a << endl; // a is now 20

  

    // 7. Passing a pointer by value or reference

    int x = 10;

    int *ptr = &x;

  

    modifyPointer(ptr);

    cout << "Value pointed to: " << *ptr << endl; // 20

  

    modifyPointerReference(ptr);

    cout << "Pointer value: " << *ptr << endl; // 30

  

    // 8. #define constant vs const

    cout << "PI: " << PI << endl;

    cout << "pi: " << pi << endl;

  

    // 9. Operator new and delete

    dynamicMemoryExample();

  

    // 10. Type casting operator

    typeCastingExample();

  

    // 11. Inline Functions

    cout << "Inline add: " << addInline(3, 4) << endl;

  

    // 12. Default arguments

    greet();        // Uses default argument

    greet("Alice"); // Uses provided argument

  

    // Module 3 examples

    // 1. Class and Object

    Person person;

    person.name = "John";

    person.age = 30;

    person.display();

  

    // 2. Scope of Class and Scope Resolution Operator

    ScopeExample scopeExample;

    scopeExample.display();

  

    // 3. Member Function of a Class

    MemberFunctionExample memberFunctionExample;

    memberFunctionExample.setValue(100);

    cout << "Member function value: " << memberFunctionExample.getValue() << endl;

  

    // 4. Access Specifiers

    AccessSpecifierExample accessSpecifierExample;

    accessSpecifierExample.publicValue = 10;

    accessSpecifierExample.setPrivateValue(20);

    cout << "Public value: " << accessSpecifierExample.publicValue << endl;

    cout << "Private value: " << accessSpecifierExample.getPrivateValue() << endl;

  

    // 5. this Keyword

    ThisKeywordExample thisKeywordExample;

    thisKeywordExample.setValue(50);

    cout << "this keyword value: " << thisKeywordExample.getValue() << endl;

  

    // 6. Constructors and Destructors

    ConstructorDestructorExample constructorDestructorExample;

  

    // 7. Error handling (exception)

    errorHandlingExample();

  

    // Module 4 examples

    // 1. Operator overloading

    Complex c1(3, 4), c2(1, 2);

    Complex c3 = c1 + c2; // Using overloaded + operator

    c3.display();

  

    // 2. Function Overloading

    display(5);

    display(3.14);

    display("Hello");

  

    // 3. Friend function

    FriendFunctionExample friendFunctionExample(100);

    showValue(friendFunctionExample);

  

    // 4. Friend class

    FriendClassExample friendClassExample(200);

    Accessor accessor;

    accessor.showValue(friendClassExample);

  

    return 0;

}
```