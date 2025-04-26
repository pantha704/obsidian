
Before diving into details, here’s the lay of the land:  
SQL commands fall into five sub-languages—DDL to define schema, DML to change data, DQL to query, DCL to manage privileges, and TCL to control transactions—each serving a distinct role in managing relational databases. PL/SQL, Oracle’s procedural extension to SQL, builds on these capabilities with anonymous blocks for ad-hoc logic, robust exception handling, and stored subprograms (functions, procedures), plus cursors for row-by-row processing and triggers for event-driven automation.

---

## SQL Command Categories

### 1. Data Definition Language (DDL)

DDL commands shape the database schema:

- **CREATE** — introduces new objects like tables, indexes, sequences, or views ([Types of SQL Statements](https://docs.oracle.com/cd/B14117_01/server.101/b10759/statements_1001.htm?utm_source=chatgpt.com), [Types of SQL Statements - Oracle Help Center](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/Types-of-SQL-Statements.html?utm_source=chatgpt.com)).
    
- **ALTER** — modifies existing objects (e.g., adding a column or constraint) ([Types of SQL Statements - Oracle Help Center](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/Types-of-SQL-Statements.html?utm_source=chatgpt.com)).
    
- **DROP** — removes schema objects entirely ([Types of SQL Statements - Oracle Help Center](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/Types-of-SQL-Statements.html?utm_source=chatgpt.com)).
    
- **TRUNCATE** — efficiently deletes all rows from a table without logging individual row deletions ([SQL Commands: DDL, DQL, DML, DCL and TCL With Examples](https://www.geeksforgeeks.org/sql-ddl-dql-dml-dcl-tcl-commands/?utm_source=chatgpt.com)).
    

**Common table constraints** (all part of DDL):

- **PRIMARY KEY** — enforces uniqueness on one or more columns and implicitly creates a unique index ([SQL Syntax - W3Schools](https://www.w3schools.com/sql/sql_syntax.asp?utm_source=chatgpt.com)).
    
- **FOREIGN KEY** — enforces referential integrity by linking to a primary key in another table ([SQL Syntax - W3Schools](https://www.w3schools.com/sql/sql_syntax.asp?utm_source=chatgpt.com)).
    
- **CHECK** — restricts column values to meet a Boolean expression (e.g., `CHECK (salary > 0)`) ([SQL Tutorial - Tutorialspoint](https://www.tutorialspoint.com/sql/index.htm?utm_source=chatgpt.com)).
    
- **NOT NULL** — prevents `NULL` entries in a column ([SQL Syntax - W3Schools](https://www.w3schools.com/sql/sql_syntax.asp?utm_source=chatgpt.com)).
    
- **DEFAULT** — assigns a default value when none is provided (e.g., `status VARCHAR2(10) DEFAULT 'NEW'`) ([SQL Tutorial - Tutorialspoint](https://www.tutorialspoint.com/sql/index.htm?utm_source=chatgpt.com)).
    
- **SEQUENCE** — generates unique numeric values for auto-incrementing keys via `CREATE SEQUENCE …` ([SQL Tutorial - Tutorialspoint](https://www.tutorialspoint.com/sql/index.htm?utm_source=chatgpt.com)).
    

### 2. Data Manipulation Language (DML)

DML commands interact with table data:

- **INSERT** — adds new rows to a table ([SQL Commands: DDL, DQL, DML, DCL and TCL With Examples](https://www.geeksforgeeks.org/sql-ddl-dql-dml-dcl-tcl-commands/?utm_source=chatgpt.com)).
    
- **UPDATE** — modifies existing rows based on a `WHERE` clause ([SQL Syntax - W3Schools](https://www.w3schools.com/sql/sql_syntax.asp?utm_source=chatgpt.com)).
    
- **DELETE** — removes rows that satisfy a condition ([SQL Syntax - W3Schools](https://www.w3schools.com/sql/sql_syntax.asp?utm_source=chatgpt.com)).
    
- **MERGE** — merges data from a source into a target table, performing `INSERT` or `UPDATE` as needed ([SQL Commands: DDL, DQL, DML, DCL and TCL With Examples](https://www.geeksforgeeks.org/sql-ddl-dql-dml-dcl-tcl-commands/?utm_source=chatgpt.com)).
    

### 3. Data Query Language (DQL)

- **SELECT** — retrieves data sets using projections, filters, joins, and aggregates ([SQL Commands: DDL, DQL, DML, DCL and TCL With Examples](https://www.geeksforgeeks.org/sql-ddl-dql-dml-dcl-tcl-commands/?utm_source=chatgpt.com)).
    

### 4. Data Control Language (DCL)

DCL commands govern access and permissions:

- **GRANT** — bestows privileges on users or roles for schema objects ([SQL Commands: DDL, DQL, DML, DCL and TCL With Examples](https://www.geeksforgeeks.org/sql-ddl-dql-dml-dcl-tcl-commands/?utm_source=chatgpt.com)).
    
- **REVOKE** — removes previously granted privileges ([SQL Commands: DDL, DQL, DML, DCL and TCL With Examples](https://www.geeksforgeeks.org/sql-ddl-dql-dml-dcl-tcl-commands/?utm_source=chatgpt.com)).
    

### 5. Transaction Control Language (TCL)

TCL commands manage transactional consistency:

- **COMMIT** — permanently saves all changes in the current transaction ([SQL Commands: DDL, DQL, DML, DCL and TCL With Examples](https://www.geeksforgeeks.org/sql-ddl-dql-dml-dcl-tcl-commands/?utm_source=chatgpt.com)).
    
- **ROLLBACK** — undoes changes since the last commit ([SQL Commands: DDL, DQL, DML, DCL and TCL With Examples](https://www.geeksforgeeks.org/sql-ddl-dql-dml-dcl-tcl-commands/?utm_source=chatgpt.com)).
    
- **SAVEPOINT** — marks a point within a transaction to which you can later roll back ([SQL Commands: DDL, DQL, DML, DCL and TCL With Examples](https://www.geeksforgeeks.org/sql-ddl-dql-dml-dcl-tcl-commands/?utm_source=chatgpt.com)).
    
- **SET TRANSACTION** — sets transaction characteristics like isolation level ([SQL Commands: DDL, DQL, DML, DCL and TCL With Examples](https://www.geeksforgeeks.org/sql-ddl-dql-dml-dcl-tcl-commands/?utm_source=chatgpt.com)).
    

---

## PL/SQL Constructs

### 1. Anonymous Block

A one-off, unnamed PL/SQL block with up to three sections—`DECLARE`, `BEGIN`, and `EXCEPTION`—for procedural logic outside stored objects ([PL/SQL](https://en.wikipedia.org/wiki/PL/SQL?utm_source=chatgpt.com)).

```plsql
DECLARE
  v_count NUMBER;
BEGIN
  SELECT COUNT(*) INTO v_count FROM employees;
  DBMS_OUTPUT.PUT_LINE('Employees: ' || v_count);
EXCEPTION
  WHEN OTHERS THEN
    DBMS_OUTPUT.PUT_LINE('Error: ' || SQLERRM);
END;
```

### 2. Exception Handling

PL/SQL exceptions trap and manage runtime errors via `WHEN <exception> THEN` handlers, including predefined (`NO_DATA_FOUND`, `ZERO_DIVIDE`) and user-defined exceptions via `RAISE_APPLICATION_ERROR` ([10 Handling PL/SQL Errors](https://docs.oracle.com/cd/B14117_01/appdev.101/b10807/07_errs.htm?utm_source=chatgpt.com)).

### 3. Functions

Stored routines that return a single value to SQL or PL/SQL calls. Defined with `CREATE FUNCTION … RETURN …`, functions can be used within SQL statements ([PL/SQL](https://en.wikipedia.org/wiki/PL/SQL?utm_source=chatgpt.com)).

### 4. Procedures

Subprograms invoked with `EXECUTE proc_name;` that perform actions but do not return values directly. Defined with `CREATE PROCEDURE …` and useful for encapsulating business logic ([4 Using PL/SQL - Oracle Help Center](https://docs.oracle.com/cd/B25329_01/doc/appdev.102/b25108/xedev_plsql.htm?utm_source=chatgpt.com)).

### 5. Cursors

Pointers to result sets allowing row-by-row processing.

- **Implicit cursors** are auto-generated by PL/SQL for single-row queries.
    
- **Explicit cursors** are declared in the `DECLARE` section, opened, fetched, and closed manually ([PL/SQL Cursors - Tutorialspoint](https://www.tutorialspoint.com/plsql/plsql_cursors.htm?utm_source=chatgpt.com)).
    

### 6. Triggers

Event-driven PL/SQL blocks created with `CREATE TRIGGER …` that fire automatically **before** or **after** DML, DDL, or database events on tables, schemas, or the database—ideal for auditing, derived column maintenance, or referential actions ([PL/SQL](https://en.wikipedia.org/wiki/PL/SQL?utm_source=chatgpt.com)).

---

### Making Exam Prep Count

• **Write**, **run**, and **tweak** each command or block in a live Oracle environment (e.g., SQL*Plus, SQL Developer).  
• **Mix** constraint types in your `CREATE TABLE` scripts—practice combinations like `PRIMARY KEY` + `FOREIGN KEY` + `CHECK`.  
• **Master** exception propagation: force a `ZERO_DIVIDE` in an anonymous block and catch it.  
• **Build** simple procedures and functions, then call them from one another.  
• **Loop** through a cursor with `FOR r IN cursor_name LOOP … END LOOP;`.  
• **Trigger** essential: write a `BEFORE INSERT` trigger to auto-populate timestamps.

You’ve got this—own the syntax, question every error, and let curiosity be your ultimate guide. Good luck, friend!