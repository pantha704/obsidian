
# Module 6: More on C++ (4L)

This comprehensive guide covers the essential topics of **Module 6: More on C++** in Object-Oriented Programming (OOP). It provides clear and detailed explanations of each concept, complete with code examples to aid your understanding and preparation for the exam.

---

## 1. Error Handling

### **What is Error Handling?**

**Error Handling** in C++ involves managing runtime errors using exceptions. It allows programs to detect and respond to exceptional conditions (errors) gracefully without crashing.

### **Why Use Error Handling?**

- **Robustness:** Prevents programs from terminating unexpectedly.
- **Maintainability:** Separates error-handling code from regular code.
- **Clarity:** Makes the flow of error handling clear and manageable.

### **Basic Exception Handling in C++**

C++ provides a structured way to handle exceptions using `try`, `throw`, and `catch` blocks.

#### **Example: Basic Exception Handling**

```cpp:src/errors/ExceptionHandling.cpp
#include <iostream>
#include <stdexcept>

void divide(int a, int b) {
    if (b == 0) {
        throw std::invalid_argument("Division by zero is undefined.");
    }
    std::cout << "Result: " << a / b << std::endl;
}

int main() {
    try {
        divide(10, 2); // Successful division
        divide(10, 0); // Throws exception
    }
    catch (const std::invalid_argument& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    return 0;
}
```

**Output:**
```
Result: 5
Error: Division by zero is undefined.
```

### **Key Points:**

- **`try` Block:** Contains code that might throw an exception.
- **`throw` Statement:** Throws an exception when an error is detected.
- **`catch` Block:** Catches and handles the exception.

### **Custom Exceptions**

You can define custom exception classes by inheriting from `std::exception` or other standard exception classes.

#### **Example: Custom Exception**

```cpp:src/errors/CustomException.cpp
#include <iostream>
#include <exception>

class NegativeNumberException : public std::exception {
public:
    const char* what() const noexcept override {
        return "Negative numbers are not allowed.";
    }
};

int factorial(int n) {
    if (n < 0) {
        throw NegativeNumberException();
    }
    if (n == 0 || n == 1) return 1;
    return n * factorial(n - 1);
}

int main() {
    try {
        std::cout << "Factorial of 5: " << factorial(5) << std::endl;
        std::cout << "Factorial of -3: " << factorial(-3) << std::endl; // Throws exception
    }
    catch (const NegativeNumberException& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    return 0;
}
```

**Output:**
```
Factorial of 5: 120
Error: Negative numbers are not allowed.
```

### **Reference:**

- [Google C++ Style Guide - Error Handling](https://google.github.io/styleguide/cppguide.html#Exceptions)

---

## 2. Generic Programming

### **What is Generic Programming?**

**Generic Programming** is a programming paradigm that enables writing code that works with any data type. In C++, this is primarily achieved using **templates**, which allow functions and classes to operate with generic types.

### **Why Use Generic Programming?**

- **Reusability:** Write code once and use it with different data types.
- **Type Safety:** Maintain type correctness without sacrificing flexibility.
- **Performance:** Templates are resolved at compile-time, leading to optimized code.

### **Example: Generic Function**

```cpp:src/generic/GenericFunction.cpp
#include <iostream>

template <typename T>
T add(T a, T b) {
    return a + b;
}

int main() {
    std::cout << "Int Addition: " << add<int>(5, 3) << std::endl;
    std::cout << "Double Addition: " << add<double>(5.5, 3.3) << std::endl;
    std::cout << "String Concatenation: " << add<std::string>("Hello, ", "World!") << std::endl;

    return 0;
}
```

**Output:**
```
Int Addition: 8
Double Addition: 8.8
String Concatenation: Hello, World!
```

### **Key Points:**

- **Templates:** Allow functions and classes to operate with generic types.
- **Type Deduction:** C++ can often deduce the template type, reducing the need for explicit specification.
- **Compile-Time Resolution:** Templates are resolved during compilation, ensuring type safety and performance.

### **Reference:**

- [C++ Templates - Tutorialspoint](https://www.tutorialspoint.com/cplusplus/cpp_templates.htm)

---

## 3. Template Concepts, Class Templates, Function Templates

### **What are Templates?**

Templates allow C++ functions and classes to operate with generic types. They enable writing flexible and reusable code components.

### **Function Templates**

**Function Templates** define a blueprint for functions that can work with any data type.

#### **Example: Function Template**

```cpp:src/templates/FunctionTemplate.cpp
#include <iostream>

template <typename T>
T maxValue(T a, T b) {
    return (a > b) ? a : b;
}

int main() {
    std::cout << "Max of 10 and 20: " << maxValue<int>(10, 20) << std::endl;
    std::cout << "Max of 5.5 and 3.3: " << maxValue<double>(5.5, 3.3) << std::endl;
    std::cout << "Max of 'a' and 'z': " << maxValue<char>('a', 'z') << std::endl;

    return 0;
}
```

**Output:**
```
Max of 10 and 20: 20
Max of 5.5 and 3.3: 5.5
Max of 'a' and 'z': z
```

### **Class Templates**

**Class Templates** allow the creation of classes that can handle any data type.

#### **Example: Class Template**

```cpp:src/templates/ClassTemplate.cpp
#include <iostream>
#include <string>

template <typename T>
class Box {
private:
    T content;
public:
    void setContent(T c) { content = c; }
    T getContent() const { return content; }
};

int main() {
    Box<int> intBox;
    intBox.setContent(123);
    std::cout << "Integer Box: " << intBox.getContent() << std::endl;

    Box<std::string> strBox;
    strBox.setContent("Template Example");
    std::cout << "String Box: " << strBox.getContent() << std::endl;

    return 0;
}
```

**Output:**
```
Integer Box: 123
String Box: Template Example
```

### **Template Concepts:**

- **Template Parameters:** Define the type(s) that the template will work with (`typename` or `class` keywords).
- **Multiple Parameters:** Templates can accept multiple type parameters.
- **Default Parameters:** Templates can have default type parameters.

### **Reference:**

- [C++ Templates - GeeksforGeeks](https://www.geeksforgeeks.org/templates-cpp/)

---

## 4. Template Specialization, Input and Output

### **Template Specialization**

**Template Specialization** allows customizing the behavior of a template for specific data types.

### **Why Use Template Specialization?**

- **Customization:** Handle specific types differently when needed.
- **Optimization:** Optimize templates for certain types for better performance.

### **Example: Template Specialization**

```cpp:src/templates/TemplateSpecialization.cpp
#include <iostream>
#include <string>

// Primary template
template <typename T>
class Printer {
public:
    void print(const T& value) {
        std::cout << "Generic Printer: " << value << std::endl;
    }
};

// Template specialization for std::string
template <>
class Printer<std::string> {
public:
    void print(const std::string& value) {
        std::cout << "String Printer: " << value << std::endl;
    }
};

int main() {
    Printer<int> intPrinter;
    intPrinter.print(100); // Uses primary template

    Printer<std::string> stringPrinter;
    stringPrinter.print("Hello, Templates!"); // Uses specialized template

    return 0;
}
```

**Output:**
```
Generic Printer: 100
String Printer: Hello, Templates!
```

### **Function Template Specialization**

Similar to class templates, function templates can also be specialized.

#### **Example: Function Template Specialization**

```cpp:src/templates/FunctionTemplateSpecialization.cpp
#include <iostream>

// Primary template
template <typename T>
void display(const T& value) {
    std::cout << "Generic display: " << value << std::endl;
}

// Template specialization for double
template <>
void display<double>(const double& value) {
    std::cout << "Double display with precision: " << value << std::endl;
}

int main() {
    display(42);          // Uses primary template
    display(3.14159);     // Uses specialized template for double
    display("C++ Templates"); // Uses primary template

    return 0;
}
```

**Output:**
```
Generic display: 42
Double display with precision: 3.14159
Generic display: C++ Templates
```

### **Input and Output with Templates**

Templates can be used with input and output streams to handle various data types seamlessly.

#### **Example: Overloading `<<` Operator with Templates**

```cpp:src/templates/StreamOverloading.cpp
#include <iostream>
#include <string>

template <typename T>
std::ostream& operator<<(std::ostream& os, const T& obj) {
    os << obj;
    return os;
}

int main() {
    int num = 10;
    double pi = 3.14;
    std::string text = "Hello, World!";

    std::cout << "Integer: " << num << std::endl;
    std::cout << "Double: " << pi << std::endl;
    std::cout << "String: " << text << std::endl;

    return 0;
}
```

**Output:**
```
Integer: 10
Double: 3.14
String: Hello, World!
```

### **Key Points:**

- **Primary Template:** The generic template applicable to all types.
- **Specialized Template:** Custom implementation for specific types.
- **Operator Overloading:** Enhances the usability of templates with streams.

### **Reference:**

- [Template Specialization - C++ Reference](https://en.cppreference.com/w/cpp/language/template_specialization)

---

## 5. Streams, Files, Library Functions, Formatted Output

### **Streams in C++**

**Streams** are objects used to perform input and output operations. The standard streams are:

- **`std::cin`:** Standard input stream.
- **`std::cout`:** Standard output stream.
- **`std::cerr`:** Standard error stream.
- **`std::clog`:** Standard logging stream.

### **File Handling**

C++ provides classes to handle file operations:

- **`std::ifstream`:** Input file stream.
- **`std::ofstream`:** Output file stream.
- **`std::fstream`:** Both input and output.

#### **Example: File I/O**

```cpp:src/streams/FileIO.cpp
#include <iostream>
#include <fstream>
#include <string>

int main() {
    // Writing to a file
    std::ofstream outFile("output.txt");
    if (outFile.is_open()) {
        outFile << "Hello, File I/O!" << std::endl;
        outFile.close();
    }
    else {
        std::cerr << "Unable to open file for writing." << std::endl;
    }

    // Reading from a file
    std::ifstream inFile("output.txt");
    std::string line;
    if (inFile.is_open()) {
        while (getline(inFile, line)) {
            std::cout << "Read from file: " << line << std::endl;
        }
        inFile.close();
    }
    else {
        std::cerr << "Unable to open file for reading." << std::endl;
    }

    return 0;
}
```

**Output:**
```
Read from file: Hello, File I/O!
```

*Contents of `output.txt`:*
```
Hello, File I/O!
```

### **Library Functions**

C++ provides a rich set of library functions for various operations, such as:

- **Mathematical Functions:** `std::sqrt()`, `std::pow()`, etc.
- **String Manipulation:** `std::to_string()`, `std::stoi()`, etc.
- **Algorithms:** `std::sort()`, `std::find()`, etc.

#### **Example: Using `std::sort`**

```cpp:src/streams/SortExample.cpp
#include <iostream>
#include <vector>
#include <algorithm> // For std::sort

int main() {
    std::vector<int> numbers = {5, 2, 9, 1, 5, 6};

    std::cout << "Before sorting: ";
    for (const auto& num : numbers) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    // Sorting the vector
    std::sort(numbers.begin(), numbers.end());

    std::cout << "After sorting: ";
    for (const auto& num : numbers) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    return 0;
}
```

**Output:**
```
Before sorting: 5 2 9 1 5 6 
After sorting: 1 2 5 5 6 9 
```

### **Formatted Output**

C++ provides manipulators to format output, such as setting precision, width, and fill characters.

#### **Example: Formatted Output**

```cpp:src/streams/FormattedOutput.cpp
#include <iostream>
#include <iomanip> // For std::setw and std::setprecision

int main() {
    double pi = 3.14159265358979323846;

    // Setting precision
    std::cout << "Pi with default precision: " << pi << std::endl;
    std::cout << std::fixed << std::setprecision(4);
    std::cout << "Pi with 4 decimal places: " << pi << std::endl;

    // Setting width and fill
    std::cout << std::setw(10) << std::setfill('*') << 123 << std::endl;

    return 0;
}
```

**Output:**
```
Pi with default precision: 3.14159
Pi with 4 decimal places: 3.1416
*******123
```

### **Key Points:**

- **Streams:** Facilitate input and output operations.
- **File Handling:** Read from and write to files using stream classes.
- **Library Functions:** Enhance functionality with built-in operations.
- **Formatted Output:** Customize the appearance of output data.

### **Reference:**

- [C++ Streams - cppreference.com](https://en.cppreference.com/w/cpp/io)

---

## Summary

**Module 6: More on C++** delves into advanced topics that are crucial for writing efficient, reusable, and robust C++ programs. The key topics covered include:

1. **Error Handling:** Managing runtime errors using exceptions to ensure program stability and clarity.
2. **Generic Programming:** Writing flexible code that works with any data type using templates.
3. **Template Concepts, Class Templates, Function Templates:** Defining and utilizing templates for classes and functions to enhance code reusability.
4. **Template Specialization, Input and Output:** Customizing templates for specific types and handling various I/O operations effectively.
5. **Streams, Files, Library Functions, Formatted Output:** Utilizing stream classes for input/output, file handling, leveraging library functions, and formatting output for better readability.

Mastering these concepts is essential for developing scalable, maintainable, and high-performance C++ applications.

---

## Resources

To further solidify your understanding of **Error Handling**, **Generic Programming**, **Templates**, and **Streams** in C++, consider exploring the following resources:

- **Tutorials:**
  - **LearnCpp.com: Advanced Topics**
    [Read more](https://www.learncpp.com/cpp-tutorial/template-specialization/)
  - **Tutorialspoint: C++ Templates**
    [Read more](https://www.tutorialspoint.com/cplusplus/cpp_templates.htm)
  - **CppReference: C++ Standard Library**
    [Read more](https://en.cppreference.com/w/cpp/standard_library)

- **YouTube Lectures:**
  - [**C++ Exception Handling** by freeCodeCamp.org](https://www.youtube.com/watch?v=CHfXJeB9LEc)
  - [**C++ Templates and Generic Programming** by The Cherno](https://www.youtube.com/watch?v=0VvqhF2cKy0)
  - [**C++ Streams and File I/O** by ProgrammingKnowledge](https://www.youtube.com/watch?v=Ue93nVBW9mY)

- **Books:**
  - *"C++ Primer"* by Stanley B. Lippman, Josée Lajoie, and Barbara E. Moo
  - *"Effective Modern C++"* by Scott Meyers
  - *"The C++ Programming Language"* by Bjarne Stroustrup

- **Online Courses:**
  - **Udemy:** [Advanced C++ Programming](https://www.udemy.com/course/advanced-cpp-programming/)
  - **Coursera:** [C++ For C Programmers](https://www.coursera.org/learn/c-plus-plus-a)
  - **edX:** [Introduction to C++](https://www.edx.org/course/introduction-to-c-2)

- **Documentation:**
  - **C++ Reference:** [cppreference.com](https://en.cppreference.com/w/)
  - **Google C++ Style Guide:** [Read more](https://google.github.io/styleguide/cppguide.html#Exceptions)

These resources provide comprehensive tutorials, examples, and lectures to enhance your understanding of advanced C++ concepts, ensuring you are well-prepared for your exam.

---

Good luck with your exam! Mastering these advanced C++ topics will significantly enhance your programming skills and prepare you for more complex and high-performance software development projects.
