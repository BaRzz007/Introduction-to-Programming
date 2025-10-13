## FOUNDATIONS
### [What is programming?](https://www.freecodecamp.org/news/what-is-programming-tutorial-for-beginners)
In very concise terms, **Programming** is the task of writing code or instruction, that tell a computer what to do in order to solve a problem.  
Example instruction to add two numbers:
```python
def add(num1, num2):
  return num1 + num2

result = add(2, 3)
print(result) # This prints out the result 5
```
### Syntax, Errors, Logic and Flow
**<ins>Syntax<ins/**: Syntax is a set of rules that define the structure of how a language is written.

**<ins>Errors<ins/>**: Errors are problems that prevent a program from running. These errors can arise from many reasons - syntax error, wrong logic, missing files, invalid inputs and so on. There are 3 main types of errors:
 * [Syntax error](https://en.wikipedia.org/wiki/Syntax_error)
 * [Runtime error](https://www.techslang.com/definition/what-is-a-runtime-error/)
 * [Logical error](https://en.wikipedia.org/wiki/Logic_error)  

**<ins>Logic<ins/>**: Logic (Algorithm) refers to the sequential - step-by-step - instruction a computer follows to complete a specific task or solve a problem.

**<ins>Flow<ins/>**: A program flow is the order in which instructions, statements or operations are executed during the program's runtime.  
Some example syntax:

Python syntax
```python
print("Hello World!") # Prints a Hello World! string to the console
print "Hello World!" # Syntax error!
```
Java syntax
```java
public class Greetings{
  public static void main(String args[]){
    System.out.println("Hello World!"); // prints a Hello World! string to the console
    print("Hello World!") // Syntax error!
  }
}
```
Some languages like `Java` and `C`, make use of curly braces to structure code into different blocks, while languages like `Python` make use of indentation.
