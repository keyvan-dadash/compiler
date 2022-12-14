import os

from antlr4 import *
from gram.JavaLexer import JavaLexer
from gram.JavaParserLabeled import JavaParserLabeled
from listener import QuestionListener


def listFiles(path):
    onlyfiles = [os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

    onlyJavaFiles = [x for x in onlyfiles if "java" in str(x)]

    return onlyJavaFiles

def run_listener_for_given_file(full_file_path):
    lexer = JavaLexer(FileStream(fileName=full_file_path))
    stream = CommonTokenStream(lexer=lexer)
    parser = JavaParserLabeled(input=stream)
    tree = parser.compilationUnit()
    listener = QuestionListener(file=file)
    walker = ParseTreeWalker()
    walker.walk(listener=listener, t=tree)
    return listener

if __name__ == '__main__':
    path = input("Enter path... \n")
    files = listFiles(path)

    for file in files:
        print("############")
        print(file)
        run_listener_for_given_file(file).print()
        print()