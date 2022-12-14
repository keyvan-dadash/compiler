from grammar.JavaLexer import JavaLexer
from antlr4 import *
import sys
import ntpath
import argparse
import os 

class UncommentGivenJavaFile:

    def __init__(self, file_paths, result_base_path = './result/'):
        self._file_paths = file_paths
        self._result_base_path = result_base_path

        try:
            os.mkdir(result_base_path)
        except OSError as error:
            pass  

    def path_leaf(self, path):
        head, tail = ntpath.split(path)
        return tail or ntpath.basename(head)
    
    def start(self):

        for file_path in self._file_paths:
            self._start_uncommen(file_path, self.path_leaf(file_path))




    def _start_uncommen(self, file_path, file_name):
        
        lexer = JavaLexer(FileStream(file_path))  

        with open(self._result_base_path + file_name, 'w+') as f:

            while True:
                token = lexer.nextToken()
                token_text = token.text

                if token.type == lexer.LINE_COMMENT:
                    token_text = str(token.text).replace('//', '')
                elif token.type == lexer.COMMENT:
                    token_text = str(token.text).replace('/*', '')
                    token_text = str(token_text).replace('*/', '')
                elif token.type == Token.EOF:
                    return
                
                f.write(token_text)


if __name__=='__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('-p', 
                        '--path',
                        metavar='path',
                        action='store',
                        type=str,
                        required=False)

    parser.add_argument('-i',
                        '--input',
                        metavar='input',
                        action='store',
                        nargs='+',
                        required=True)

    args = parser.parse_args()

    if args.path:
        uncomment = UncommentGivenJavaFile(args.input, args.path)
    else :
        uncomment = UncommentGivenJavaFile(args.input)

    uncomment.start()