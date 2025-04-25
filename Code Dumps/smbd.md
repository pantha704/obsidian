
Since you have a lab exam tomorrow on SQL and PL/SQL, I’ll explain everything you need in a simple, step-by-step way. We’ll cover creating tables with constraints, writing different types of SQL queries, and then move into PL/SQL topics like simple programs, exceptions, functions, procedures, cursors, and triggers. I’ll use examples with tables like emp (employees), dept (departments), and project, and give you practice questions to prepare. Let’s get started!

---

Part 1: SQL - Creating Tables with Constraints

You need to create tables with these constraints: Primary Key, Foreign Key, Check, Not Null, Default, and a Sequence for auto-incrementing IDs. Let’s build three tables: dept, emp, and project.

1. Create the dept Table

- Columns:
    
    - dept_id: A unique number for each department (Primary Key).
        
    - dept_name: The department’s name (must not be empty, so Not Null).
        

sql

```sql
CREATE TABLE dept (
    dept_id NUMBER PRIMARY KEY,
    dept_name VARCHAR2(50) NOT NULL
);
```

- Primary Key: dept_id ensures every department has a unique ID.
    
- Not Null: dept_name can’t be left blank.
    

2. Create a Sequence for emp_id

- A Sequence generates unique numbers automatically (like auto-increment).
    
- We’ll use it for the emp_id in the emp table.
    

sql

```sql
CREATE SEQUENCE emp_seq START WITH 1 INCREMENT BY 1;
```

- This starts at 1 and increases by 1 each time (1, 2, 3, etc.).
    

3. Create the emp Table

- Columns:
    
    - emp_id: Unique ID for each employee (Primary Key, auto-incremented).
        
    - emp_name: Employee’s name (Not Null).
        
    - dept_id: Links to the dept table (Foreign Key).
        
    - salary: Employee’s salary (Check: must be greater than 0).
        
    - hire_date: Date they joined (Default: today’s date).
        

sql

```sql
CREATE TABLE emp (
    emp_id NUMBER PRIMARY KEY,
    emp_name VARCHAR2(100) NOT NULL,
    dept_id NUMBER,
    salary NUMBER CHECK (salary > 0),
    hire_date DATE DEFAULT SYSDATE,
    CONSTRAINT fk_dept FOREIGN KEY (dept_id) REFERENCES dept(dept_id)
);
```

- Primary Key: emp_id is unique for each employee.
    
- Not Null: emp_name must be filled in.
    
- Foreign Key: dept_id connects to dept(dept_id)—an employee belongs to a department.
    
- Check: salary > 0 ensures no negative or zero salaries.
    
- Default: hire_date defaults to the current date (SYSDATE) if not specified.
    

4. Create the project Table

- Columns:
    
    - project_id: Unique ID for each project (Primary Key).
        
    - project_name: Project’s name (Not Null).
        
    - dept_id: Links to the dept table (Foreign Key).
        

sql

```sql
CREATE TABLE project (
    project_id NUMBER PRIMARY KEY,
    project_name VARCHAR2(100) NOT NULL,
    dept_id NUMBER,
    CONSTRAINT fk_project_dept FOREIGN KEY (dept_id) REFERENCES dept(dept_id)
);
```

- Primary Key: project_id is unique.
    
- Not Null: project_name must be provided.
    
- Foreign Key: dept_id links projects to departments.
    

5. Inserting Data with the Sequence

- Use the sequence (emp_seq) to auto-generate emp_id.
    

sql

```sql
INSERT INTO dept (dept_id, dept_name) VALUES (1, 'HR');
INSERT INTO emp (emp_id, emp_name, dept_id, salary)
VALUES (emp_seq.NEXTVAL, 'John Doe', 1, 5000);
```

- emp_seq.NEXTVAL gives the next number (e.g., 1, then 2, etc.).
    
- Insert more employees, and each gets a unique ID automatically.
    

---

Part 2: SQL Queries - Different Types

Let’s practice some common SQL queries: SELECT, UPDATE, and DELETE.

1. SELECT with JOIN

- Question: List employee names and their department names.
    

sql

```sql
SELECT e.emp_name, d.dept_name
FROM emp e
JOIN dept d ON e.dept_id = d.dept_id;
```

- Explanation: Joins emp and dept tables using dept_id to match employees to departments.
    

2. SELECT with WHERE and ORDER BY

- Question: Find employees with a salary over 3000, sorted by salary (highest first).
    

sql

```sql
SELECT emp_name, salary
FROM emp
WHERE salary > 3000
ORDER BY salary DESC;
```

- Explanation: Filters for high earners and sorts them.
    

3. UPDATE Query

- Question: Give a 10% raise to employees in department 1.
    

sql

```sql
UPDATE emp
SET salary = salary * 1.10
WHERE dept_id = 1;
```

- Explanation: Increases salary by 10% for department 1 employees.
    

4. DELETE Query

- Question: Remove employees hired before 2020.
    

sql

```sql
DELETE FROM emp
WHERE hire_date < TO_DATE('2020-01-01', 'YYYY-MM-DD');
```

- Explanation: Deletes old employees based on hire_date.
    

---

Part 3: PL/SQL - Key Concepts with Examples

Now, let’s tackle PL/SQL. I’ll explain each topic simply and give you examples.

1. Simple PL/SQL Program

- A basic block to print a message.
    

sql

```sql
BEGIN
    DBMS_OUTPUT.PUT_LINE('Hello, World!');
END;
```

- Explanation: Prints “Hello, World!”. Use SET SERVEROUTPUT ON in your tool to see output.
    

2. Exception Handling

- Catch errors, like dividing by zero.
    

sql

```sql
DECLARE
    a NUMBER := 10;
    b NUMBER := 0;
    c NUMBER;
BEGIN
    c := a / b;
EXCEPTION
    WHEN ZERO_DIVIDE THEN
        DBMS_OUTPUT.PUT_LINE('Error: Division by zero');
END;
```

- Explanation: If b = 0, it catches the error and prints a message instead of crashing.
    

3. Function

- A function to calculate a 10% bonus based on salary.
    

sql

```sql
CREATE OR REPLACE FUNCTION calculate_bonus (p_emp_id NUMBER)
RETURN NUMBER
IS
    v_salary NUMBER;
BEGIN
    SELECT salary INTO v_salary FROM emp WHERE emp_id = p_emp_id;
    RETURN v_salary * 0.10;
EXCEPTION
    WHEN NO_DATA_FOUND THEN
        RETURN 0;
END;
```

- Usage:
    

sql

```sql
SELECT calculate_bonus(1) FROM DUAL;
```

- Explanation: Takes an emp_id, finds the salary, and returns 10% of it. Returns 0 if the employee isn’t found.
    

4. Procedure

- A procedure to add a new employee.
    

sql

```sql
CREATE OR REPLACE PROCEDURE add_employee (
    p_emp_name VARCHAR2,
    p_dept_id NUMBER,
    p_salary NUMBER
)
IS
BEGIN
    INSERT INTO emp (emp_id, emp_name, dept_id, salary)
    VALUES (emp_seq.NEXTVAL, p_emp_name, p_dept_id, p_salary);
    COMMIT;
END;
```

- Usage:
    

sql

```sql
EXEC add_employee('Jane Doe', 1, 6000);
```

- Explanation: Inserts a new employee with an auto-incremented ID.
    

5. Cursor

- Fetch and display employees in a department.
    

sql

```sql
DECLARE
    CURSOR emp_cursor (p_dept_id NUMBER) IS
        SELECT emp_name, salary FROM emp WHERE dept_id = p_dept_id;
    v_emp_name emp.emp_name%TYPE;
    v_salary emp.salary%TYPE;
BEGIN
    OPEN emp_cursor(1);
    LOOP
        FETCH emp_cursor INTO v_emp_name, v_salary;
        EXIT WHEN emp_cursor%NOTFOUND;
        DBMS_OUTPUT.PUT_LINE(v_emp_name || ' earns ' || v_salary);
    END LOOP;
    CLOSE emp_cursor;
END;
```

- Explanation: Loops through employees in department 1 and prints their names and salaries.
    

6. Trigger

- Automatically set hire_date when adding an employee.
    

sql

```sql
CREATE OR REPLACE TRIGGER set_hire_date
BEFORE INSERT ON emp
FOR EACH ROW
BEGIN
    :NEW.hire_date := SYSDATE;
END;
```

- Explanation: Before inserting, sets hire_date to today’s date automatically.
    

---

Part 4: Practice Questions

Here are some questions to practice for your exam.

SQL Queries

1. Count employees per department:
    
    sql
    
    ```sql
    SELECT d.dept_name, COUNT(e.emp_id)
    FROM dept d
    LEFT JOIN emp e ON d.dept_id = e.dept_id
    GROUP BY d.dept_name;
    ```
    
2. Find the highest-paid employee:
    
    sql
    
    ```sql
    SELECT emp_name, salary FROM emp WHERE salary = (SELECT MAX(salary) FROM emp);
    ```
    
3. Update department name:
    
    sql
    
    ```sql
    UPDATE dept SET dept_name = 'Sales' WHERE dept_id = 1;
    ```
    
4. Delete unassigned projects:
    
    sql
    
    ```sql
    DELETE FROM project WHERE dept_id IS NULL;
    ```
    

PL/SQL Questions

1. Exception: Handle missing employee.
    
    sql
    
    ```sql
    DECLARE
        v_name emp.emp_name%TYPE;
    BEGIN
        SELECT emp_name INTO v_name FROM emp WHERE emp_id = 999;
    EXCEPTION
        WHEN NO_DATA_FOUND THEN
            DBMS_OUTPUT.PUT_LINE('No employee found!');
    END;
    ```
    
2. Function: Total salary in a department.
    
    sql
    
    ```sql
    CREATE OR REPLACE FUNCTION total_salary (p_dept_id NUMBER)
    RETURN NUMBER
    IS
        v_total NUMBER;
    BEGIN
        SELECT SUM(salary) INTO v_total FROM emp WHERE dept_id = p_dept_id;
        RETURN NVL(v_total, 0);
    END;
    ```
    
3. Procedure: Transfer employee to a new department.
    
    sql
    
    ```sql
    CREATE OR REPLACE PROCEDURE transfer_employee (p_emp_id NUMBER, p_new_dept_id NUMBER)
    IS
    BEGIN
        UPDATE emp SET dept_id = p_new_dept_id WHERE emp_id = p_emp_id;
        COMMIT;
    END;
    ```
    
4. Cursor: Increase salaries by 5% in a department.
    
    sql
    
    ```sql
    DECLARE
        CURSOR salary_cursor IS SELECT emp_id, salary FROM emp WHERE dept_id = 1 FOR UPDATE;
        v_emp_id emp.emp_id%TYPE;
        v_salary emp.salary%TYPE;
    BEGIN
        OPEN salary_cursor;
        LOOP
            FETCH salary_cursor INTO v_emp_id, v_salary;
            EXIT WHEN salary_cursor%NOTFOUND;
            UPDATE emp SET salary = v_salary * 1.05 WHERE emp_id = v_emp_id;
        END LOOP;
        CLOSE salary_cursor;
        COMMIT;
    END;
    ```
    
5. Trigger: Prevent deleting departments with employees.
    
    sql
    
    ```sql
    CREATE OR REPLACE TRIGGER prevent_dept_delete
    BEFORE DELETE ON dept
    FOR EACH ROW
    DECLARE
        v_count NUMBER;
    BEGIN
        SELECT COUNT(*) INTO v_count FROM emp WHERE dept_id = :OLD.dept_id;
        IF v_count > 0 THEN
            RAISE_APPLICATION_ERROR(-20001, 'Cannot delete department with employees!');
        END IF;
    END;
    ```
    

---

Final Tips for Your Exam

- Practice: Write out the code yourself—don’t just read it.
    
- Understand Constraints: Know how each one (Primary Key, Foreign Key, etc.) works.
    
- Test: If you can, run your code in a database to catch mistakes.
    
- PL/SQL Focus: Be ready for exceptions and triggers—they’re common in exams.
    
- Relax: You’ve got this! Go step by step during the exam.
    

Good luck tomorrow! If you need more help, just ask.