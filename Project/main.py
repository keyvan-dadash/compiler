import os

from antlr4 import *
from gram.JavaLexer import JavaLexer
from gram.JavaParserLabeled import JavaParserLabeled
from listener import QuestionListener


def getListOfFiles(dirName):
    listOfFile = os.listdir(dirName)
    allFiles = list()
    for entry in listOfFile:
        fullPath = os.path.join(dirName, entry)
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles


def listFiles(path):
    # onlyfiles = [os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    onlyfiles = getListOfFiles(path)

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