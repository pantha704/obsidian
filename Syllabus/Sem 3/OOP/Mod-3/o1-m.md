
# Module 3: Class & Object Properties (6L)

This comprehensive guide covers the essential topics of **Module 3: Class & Object Properties** in Object-Oriented Programming (OOP). It provides clear and detailed explanations of each concept to help you prepare effectively for your exam.

---

## 1. Class and Object

### **What are Classes and Objects?**

- **Class:**
  - A **class** is a blueprint or template for creating objects.
  - It defines a data type by bundling data (attributes) and methods (functions) that operate on the data.
  
- **Object:**
  - An **object** is an instance of a class.
  - It represents a specific entity with state (attribute values) and behavior (methods).

### **Example in C++**

```cpp:path/to/file/Car.h
// Class definition for Car
class Car {
public:
    // Attributes
    std::string color;
    int year;

    // Methods
    void startEngine();
    void stopEngine();
};
```

```cpp:path/to/file/main.cpp
#include <iostream>
#include "Car.h"

// Method definitions
void Car::startEngine() {
    std::cout << "Engine started." << std::endl;
}

void Car::stopEngine() {
    std::cout << "Engine stopped." << std::endl;
}

int main() {
    // Creating an object of class Car
    Car myCar;
    myCar.color = "Red";
    myCar.year = 2022;

    // Using object methods
    myCar.startEngine();
    myCar.stopEngine();

    return 0;
}
```

**Output:**
```
Engine started.
Engine stopped.
```

---

## 2. Scope of Class and Scope Resolution Operator

### **Scope of Class Members**

- **Scope:**
  - Determines the visibility and accessibility of class members (attributes and methods).
  - Controlled using **access specifiers** (`public`, `protected`, `private`).

### **Scope Resolution Operator (`::`)**

- Used to define functions outside the class and to access static members.
- Syntax: `ClassName::MemberName`

### **Example in C++**

```cpp:path/to/file/MathUtils.h
class MathUtils {
public:
    // Static method declaration
    static int add(int a, int b);
};
```

```cpp:path/to/file/MathUtils.cpp
#include "MathUtils.h"

// Defining the add method using scope resolution operator
int MathUtils::add(int a, int b) {
    return a + b;
}
```

```cpp:path/to/file/main.cpp
#include <iostream>
#include "MathUtils.h"

int main() {
    int sum = MathUtils::add(5, 3);
    std::cout << "Sum: " << sum << std::endl; // Output: Sum: 8
    return 0;
}
```

**Output:**
```
Sum: 8
```

**Reference:** [GeeksforGeeks: Classes and Objects in C++](https://www.geeksforgeeks.org/classes-objects-java/)

---

## 3. Member Function of a Class

### **What are Member Functions?**

- **Member Functions** are functions defined inside a class that operate on the class's data members.
- They can be used to manipulate object data and provide functionality.

### **Example in C++**

```cpp:path/to/file/Rectangle.h
class Rectangle {
private:
    double length;
    double breadth;

public:
    // Constructor
    Rectangle(double l, double b);

    // Member functions
    double area();
    double perimeter();
};
```

```cpp:path/to/file/Rectangle.cpp
#include "Rectangle.h"

// Constructor definition
Rectangle::Rectangle(double l, double b) {
    length = l;
    breadth = b;
}

// Member function to calculate area
double Rectangle::area() {
    return length * breadth;
}

// Member function to calculate perimeter
double Rectangle::perimeter() {
    return 2 * (length + breadth);
}
```

```cpp:path/to/file/main.cpp
#include <iostream>
#include "Rectangle.h"

int main() {
    // Creating an object of Rectangle
    Rectangle rect(5.0, 3.0);

    // Calling member functions
    std::cout << "Area: " << rect.area() << std::endl;         // Output: Area: 15
    std::cout << "Perimeter: " << rect.perimeter() << std::endl; // Output: Perimeter: 16

    return 0;
}
```

**Output:**
```
Area: 15
Perimeter: 16
```

---

## 4. Access Specifiers

### **What are Access Specifiers?**

- **Access Specifiers** control the accessibility of class members.
- **Types:**
  - **Public:** Accessible from anywhere.
  - **Protected:** Accessible within the class and its subclasses.
  - **Private:** Accessible only within the class.

### **Example in C++**

```cpp:path/to/file/Person.h
class Person {
private:
    std::string name; // Private member

protected:
    int age; // Protected member

public:
    // Public member
    void setName(std::string n) {
        name = n;
    }

    std::string getName() {
        return name;
    }
};
```

```cpp:path/to/file/Student.h
#include "Person.h"

class Student : public Person {
public:
    void setAge(int a) {
        age = a; // Accessible because age is protected
    }

    int getAge() {
        return age;
    }
};
```

```cpp:path/to/file/main.cpp
#include <iostream>
#include "Student.h"

int main() {
    Student student;
    student.setName("Alice");
    student.setAge(20);

    std::cout << "Name: " << student.getName() << std::endl; // Output: Name: Alice
    std::cout << "Age: " << student.getAge() << std::endl;   // Output: Age: 20

    // std::cout << student.name; // Error: 'name' is private
    // std::cout << student.age;  // Error: 'age' is protected

    return 0;
}
```

**Output:**
```
Name: Alice
Age: 20
```

**Reference:** [GeeksforGeeks: Classes and Objects in C++](https://www.geeksforgeeks.org/classes-objects-java/)

---

## 5. `this` Keyword

### **What is the `this` Keyword?**

- **`this`** is a pointer referring to the calling object within a class.
- It is used to differentiate between class members and parameters with the same name.

### **Example in C++**

```cpp:path/to/file/Point.h
class Point {
private:
    int x;
    int y;

public:
    // Constructor with parameters having the same name as class members
    Point(int x, int y);

    // Method to display coordinates
    void display();
};
```

```cpp:path/to/file/Point.cpp
#include <iostream>
#include "Point.h"

// Constructor definition using 'this' keyword
Point::Point(int x, int y) {
    this->x = x; // 'this->x' refers to class member, 'x' is parameter
    this->y = y;
}

// Method to display coordinates
void Point::display() {
    std::cout << "Point(" << this->x << ", " << this->y << ")" << std::endl;
}
```

```cpp:path/to/file/main.cpp
#include "Point.h"

int main() {
    Point p(10, 20);
    p.display(); // Output: Point(10, 20)
    return 0;
}
```

**Output:**
```
Point(10, 20)
```

**Reference:** [GeeksforGeeks: This Pointer in C++](https://www.geeksforgeeks.org/this-pointer-cpp/)

---

## 6. Constructors and Destructors

### **What are Constructors and Destructors?**

- **Constructor:**
  - A special member function called **automatically** when an object is created.
  - Initializes object attributes.
  - Has the same name as the class and no return type.

- **Destructor:**
  - A special member function called **automatically** when an object is destroyed.
  - Cleans up resources before the object is removed from memory.
  - Has the same name as the class prefixed with a tilde (`~`) and no return type.

### **Example in C++**

```cpp:path/to/file/Book.h
#include <iostream>

class Book {
private:
    std::string title;
    std::string author;

public:
    // Constructor
    Book(std::string t, std::string a);

    // Destructor
    ~Book();

    // Method to display book details
    void display();
};
```

```cpp:path/to/file/Book.cpp
#include "Book.h"

// Constructor definition
Book::Book(std::string t, std::string a) {
    title = t;
    author = a;
    std::cout << "Book Created: " << title << " by " << author << std::endl;
}

// Destructor definition
Book::~Book() {
    std::cout << "Book Destroyed: " << title << std::endl;
}

// Method to display book details
void Book::display() {
    std::cout << "Title: " << title << ", Author: " << author << std::endl;
}
```

```cpp:path/to/file/main.cpp
#include "Book.h"

int main() {
    {
        Book myBook("1984", "George Orwell");
        myBook.display(); // Output: Title: 1984, Author: George Orwell
    } // Destructor called here

    return 0;
}
```

**Output:**
```
Book Created: 1984 by George Orwell
Title: 1984, Author: George Orwell
Book Destroyed: 1984
```

**Reference:** [GeeksforGeeks: Constructors and Destructors in C++](https://www.geeksforgeeks.org/constructors-destructors-c/)
  
---

## 7. Error Handling (Exception)

### **What is Exception Handling?**

- **Exception Handling** is a mechanism to handle runtime errors, ensuring the normal flow of the program is maintained.
- Uses `try`, `catch`, and `throw` blocks to manage exceptions.

### **Example in C++**

```cpp:path/to/file/Calculator.h
class Calculator {
public:
    int divide(int numerator, int denominator);
};
```

```cpp:path/to/file/Calculator.cpp
#include <iostream>
#include "Calculator.h"

// Method to perform division with exception handling
int Calculator::divide(int numerator, int denominator) {
    if (denominator == 0) {
        throw "Division by zero error!";
    }
    return numerator / denominator;
}
```

```cpp:path/to/file/main.cpp
#include <iostream>
#include "Calculator.h"

int main() {
    Calculator calc;
    int a = 10;
    int b = 0;

    try {
        int result = calc.divide(a, b);
        std::cout << "Result: " << result << std::endl;
    }
    catch (const char* msg) {
        std::cerr << "Exception: " << msg << std::endl;
    }

    return 0;
}
```

**Output:**
```
Exception: Division by zero error!
```

**Explanation:**

- The `divide` method throws an exception if the denominator is zero.
- The `try` block attempts to execute the division.
- If an exception is thrown, the `catch` block catches it and handles the error gracefully.

**Reference:** [GeeksforGeeks: Exception Handling in C++](https://www.geeksforgeeks.org/exception-handling-cpp/)

---

## Summary

**Module 3: Class & Object Properties** delves into the fundamental aspects of Class and Object-oriented programming in C++. Understanding these concepts is crucial for designing robust, scalable, and maintainable software systems. The key topics covered include:

1. **Class and Object:** Fundamental constructs defining types and their instances.
2. **Scope of Class and Scope Resolution Operator:** Managing visibility and accessing class members.
3. **Member Function of a Class:** Functions that operate on class data.
4. **Access Specifiers:** Controlling accessibility of class members.
5. **`this` Keyword:** Referencing the calling object within class methods.
6. **Constructors and Destructors:** Managing object lifecycle and resource allocation.
7. **Error Handling (Exception):** Managing runtime errors to maintain program flow.

Mastering these concepts is essential for effective software development and will significantly aid you in your programming career.

---

## Resources

To further enhance your understanding of **Class & Object Properties**, consider exploring the following resources:

- **GeeksforGeeks: Classes and Objects in Java**
  [Read more](https://www.geeksforgeeks.org/classes-objects-java/)

- **GeeksforGeeks: Exception Handling in C++**
  [Read more](https://www.geeksforgeeks.org/exception-handling-cpp/)

- **YouTube Tutorials:**
  - [**C++ Object-Oriented Programming** by The Cherno](https://www.youtube.com/watch?v=__Z3X3SfGvU)
  - [**OOP Concepts in C++** by ProgrammingKnowledge](https://www.youtube.com/watch?v=Q4kH2Pjz7k8)

- **Books:**
  - *"C++ Primer"* by Stanley B. Lippman, Josée Lajoie, and Barbara E. Moo
  - *"Effective C++"* by Scott Meyers

- **Online Courses:**
  - **Udemy:** [Beginning C++ Programming - From Beginner to Beyond](https://www.udemy.com/course/beginning-c-plus-plus-programming/)
  - **Coursera:** [C++ For C Programmers](https://www.coursera.org/learn/c-plus-plus-a)

- **Documentation:**
  - **C++ Reference:** [cppreference.com](https://en.cppreference.com/w/)
  - **GeeksforGeeks: C++ Programming Language](https://www.geeksforgeeks.org/c-plus-plus/)

These resources provide comprehensive tutorials, examples, and lectures to enhance your understanding of Class & Object properties and Object-Oriented Programming in C++.

---

Good luck with your exam! Mastering these foundational concepts will significantly enhance your programming skills and prepare you for more advanced topics in software development.
