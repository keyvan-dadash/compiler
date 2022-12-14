
from antlr4 import *


import sys

#### A ####
from A.ALexer import ALexer
from A.AListener import AListener
from A.AParser import AParser

#### B ####
from B.BLexer import BLexer
from B.BListener import BListener
from B.BParser import BParser

#### C ####
from C.CLexer import CLexer
from C.CListener import CListener
from C.CParser import CParser





def validateInput(input_test, lexer_class, parser_class):
    
    lexer = lexer_class(InputStream(input_test))

    stream = CommonTokenStream(lexer)

    parser = parser_class(stream)

    parser.begin()

def isValid(input_test, lexer_class, parser_class):
    try:
        validateInput(input_test, lexer_class, parser_class)
    except Exception as ex:
        print(str(ex))
        print("provided text not valid with given grammar")

if __name__=='__main__':
    grammer = str(sys.argv[1])
    if len(sys.argv) < 3:
        text = ""
    else:
        text = str(sys.argv[2])

    if (grammer == "A"):
        isValid(text, ALexer, AParser)
    elif (grammer == "B"):
        isValid(text, BLexer, BParser)
    elif (grammer == "C"):
        isValid(text, CLexer, CParser)
    else:
        print("provided grammar is invalid")


