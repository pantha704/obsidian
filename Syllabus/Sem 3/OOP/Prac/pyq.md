
### Group A

1. **What is used to write/display to the console in C++?**
   - **Answer**: (b) `cout`

2. **A derived class is also called a __________.**
   - **Answer**: (b) `Subclass`

3. **Which header file is required in C++ to use OOP?**
   - **Answer**: (c) `iostream.h`

4. **Which among the following doesn’t come under OOP concept?**
   - **Answer**: (c) `Platform independent`

5. **How many types of access specifiers are provided in OOP (C++)?**
   - **Answer**: (a) `3` (public, private, protected)

6. **Which of the following is not true about polymorphism?**
   - **Answer**: (b) `Increases overhead of function definition always`

7. **The copy constructors can be used to __________.**
   - **Answer**: (c) `Copy an object so that it can be passed to a function`

8. **Which feature of OOP reduces the use of nested classes?**
   - **Answer**: (a) `Inheritance`

9. **Which keyword is used to declare virtual functions?**
   - **Answer**: (a) `virtual`

10. **Encapsulation and abstraction differ as __________.**
   -  **Answer**: (a) `Hiding and hiding respectively`


---

### Group B

1. **What is scope resolution operator? Which operators are not used for operator overloading?**

   - **Scope Resolution Operator (`::`)**: It is used to define the context in which a name is defined. It helps access global variables or functions when there is a local variable with the same name.
   - **Operators Not Used for Overloading**: The following operators cannot be overloaded in C++:
     - `::` (Scope resolution)
     - `.` (Member access)
     - `.*` (Pointer-to-member access)
     - `?:` (Ternary conditional)
     - `sizeof` (Size of operator)
     - `typeid` (Type identification)

2. **Write down the difference between procedural languages and object-oriented language.**

   - **Procedural Languages**:
     - Focus on functions and procedures.
     - Data and functions are separate.
     - Example: C.
   - **Object-Oriented Languages**:
     - Focus on objects and classes.
     - Encapsulate data and functions together.
     - Support inheritance, polymorphism, and encapsulation.
     - Example: C++.

3. **Explain the features of constructors. How many types of constructors are used in C++? Write a C++ program to explain parameterized constructor.**

   - **Features of Constructors**:
     - Special member functions called automatically when an object is created.
     - Used to initialize objects.
     - Can be overloaded.
   - **Types of Constructors**:
     - Default Constructor
     - Parameterized Constructor
     - Copy Constructor

   ```cpp
   #include <iostream>
   using namespace std;

   class Example {
   public:
       int value;
       // Parameterized Constructor
       Example(int v) : value(v) {
           cout << "Parameterized Constructor called with value: " << value << endl;
       }
   };

   int main() {
       Example obj(10); // Calls parameterized constructor
       return 0;
   }
   ```

4. **Advantages and disadvantages of inline functions in C++. Why we use the inline function?**

   - **Advantages**:
     - Reduces function call overhead.
     - Can improve performance for small, frequently called functions.
   - **Disadvantages**:
     - Increases binary size if overused.
     - Not suitable for large functions.
   - **Usage**: Inline functions are used to optimize performance by reducing the overhead of function calls, especially for small functions.

5. **Difference between abstraction and encapsulation? Write a C++ program to explain encapsulation property.**

   - **Abstraction**:
     - Focuses on hiding complex implementation details and showing only essential features.
   - **Encapsulation**:
     - Bundles data and methods that operate on the data within a single unit (class).
     - Protects data from outside interference and misuse.

   ```cpp
   #include <iostream>
   using namespace std;

   class Encapsulated {
   private:
       int data;

   public:
       void setData(int d) {
           data = d;
       }

       int getData() {
           return data;
       }
   };

   int main() {
       Encapsulated obj;
       obj.setData(5);
       cout << "Encapsulated Data: " << obj.getData() << endl;
       return 0;
   }
   ```

These answers should help clarify the concepts and provide a solid foundation for understanding the topics. Let me know if you need further assistance!


---

### Group C

1. **What is encapsulation? What are the advantages of encapsulation? Explain three types of C++ class access modifiers.**

   - **Encapsulation**: Encapsulation is the bundling of data and methods that operate on the data within a single unit or class. It restricts direct access to some of an object's components and can prevent the accidental modification of data.
   - **Advantages**:
     - Protects data integrity.
     - Enhances code maintainability.
     - Facilitates modularity.
   - **Access Modifiers**:
     - **Public**: Members are accessible from outside the class.
     - **Private**: Members are accessible only within the class.
     - **Protected**: Members are accessible within the class and by derived class instances.

2. **Write down the features of Constructors. How many types of constructors are used in C++? Write a C++ program to explain parameterized constructor.**

   - **Features of Constructors**:
     - Automatically called when an object is created.
     - Used to initialize objects.
     - Can be overloaded.
   - **Types of Constructors**:
     - Default Constructor
     - Parameterized Constructor
     - Copy Constructor

   ```cpp
   #include <iostream>
   using namespace std;

   class Example {
   public:
       int value;
       // Parameterized Constructor
       Example(int v) : value(v) {
           cout << "Parameterized Constructor called with value: " << value << endl;
       }
   };

   int main() {
       Example obj(10); // Calls parameterized constructor
       return 0;
   }
   ```

3. **Advantages and disadvantages of inline functions in C++. Why we use the inline function?**

   - **Advantages**:
     - Reduces function call overhead.
     - Can improve performance for small, frequently called functions.
   - **Disadvantages**:
     - Increases binary size if overused.
     - Not suitable for large functions.
   - **Usage**: Inline functions are used to optimize performance by reducing the overhead of function calls, especially for small functions.

4. **Difference between abstraction and encapsulation? Write a C++ program to explain encapsulation property.**

   - **Abstraction**:
     - Focuses on hiding complex implementation details and showing only essential features.
   - **Encapsulation**:
     - Bundles data and methods that operate on the data within a single unit (class).
     - Protects data from outside interference and misuse.

   ```cpp
   #include <iostream>
   using namespace std;

   class Encapsulated {
   private:
       int data;

   public:
       void setData(int d) {
           data = d;
       }

       int getData() {
           return data;
       }
   };

   int main() {
       Encapsulated obj;
       obj.setData(5);
       cout << "Encapsulated Data: " << obj.getData() << endl;
       return 0;
   }
   ```

These answers should help you understand the key concepts and prepare effectively. Let me know if you need further assistance!
