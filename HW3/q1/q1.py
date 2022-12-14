
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from grammar.ipLexer import ipLexer
from grammar.ipParser import ipParser
from grammar.ipListener import ipListener
import sys

class GrammarException(ErrorListener):

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception()

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        raise Exception()

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        raise Exception()

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        raise Exception()

def isIpValid(text):

    lexer = ipLexer(InputStream(text))
    stream = CommonTokenStream(lexer=lexer)
    parser = ipParser(stream)
    parser.addErrorListener(GrammarException())
    parser.begin()
    return ipLexer(InputStream(text))

def isIpPivate(text):

    try:
        lexer = isIpValid(text)
        token = lexer.nextToken()
        if (token.type == lexer.V24 or token.type == lexer.V20 or token.type == lexer.V16):
            print("ip is private(drop it)")
        else:
            print("ip is public")
    except Exception as e:
        print(str(e))
        print("ip is invalid")

if __name__=='__main__':
    text = sys.argv[1]

    isIpPivate(str(text))
