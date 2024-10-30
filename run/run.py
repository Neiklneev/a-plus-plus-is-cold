from ..interpreter.interpret import *
from ..lexer.lexer import *
from ..parser.parse import *
import time

if __name__ == "__main__":
    code = input("> ")
    tokenized = tokenize(code)
    parsed = parse(tokenized)
    print(f"\n\nCode Successfully Lexed: {tokenized}")
    print(f"Code Successfully Parsed: {parsed}\n\n\n")
    time.sleep(0.5)
    print("Code being Run in 3..\n")
    time.sleep(1)
    print("Code being Run in 2..\n")
    time.sleep(1)
    print("Code being Run in 1..\n")
    time.sleep(1)
    interpret(parsed)

