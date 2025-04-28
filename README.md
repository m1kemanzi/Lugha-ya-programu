# Ururimi rw'Iprograma (LUP)

Ururimi is a simple stack-based interpreted programming language inspired by [Ultimate](https://github.com/dgriff24/ultimate/blob/main/README.md), implemented in Python.

| Instruction | Description |
| ------ | ------ |
| `SHYIRAMO n` | Push integer n onto the stack. |
| `KURAMO` | Pop the top value from the stack. |
| `DUPRIKASIYO` | Duplicate the top value on the stack. |
| `HINDURA` | Swap the top two values on the stack. |
| `TERANYA` | Pops A and then B from the stack and pushes B + A to the stack |
| `GABANYA` | Pops A and then B from the stack and pushes B - A to the stack |
| `KUBA` | Pops A and then B from the stack and pushes B * A to the stack |
| `SOMA` | Read one character from stdin, push its ASCII value. Pushes 0 if EOF is reached. |
| `ANDIKA_INYUGUTI` | Pop a value, print its corresponding ASCII character to stdout. |
| `ANDIKA_UMUBARÉ` | Pop a value, print it as an integer to stdout. |
| `SIMBUKA n` | Jump to nth line. |
| `SIMBUKA_UBUSA n` | If the value popped is zero, jump to nth line. |
| `HAGARARA` | Terminate program execution. |

*Note: Comments are not supported. Empty lines are ignored.*

### Examples of Code Inputs and Outputs


`python3 interpreter.py helloworld.txt`

Hello, World!


`python3 interpreter.py cat.txt`
Hello  
Hello  
123    
123    


`python3 interpreter.py multiply.txt`
76

42


`python3 interpreter.py repeater.txt`
*5

*****


`python3 interpreter.py reversestring.txt`
Ururimi


imiruR 
