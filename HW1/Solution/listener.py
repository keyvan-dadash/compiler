from gram.JavaParserLabeled import JavaParserLabeled
from gram.JavaParserLabeledListener import JavaParserLabeledListener



class QuestionListener(JavaParserLabeledListener):
    def __init__(self, file: str):
        self._file = file
        self._list_of_classes = []
        self._list_of_methods = []
        self._list_of_variables = []

    def enterClassDeclaration(self, ctx: JavaParserLabeled.ClassDeclarationContext):
        self._list_of_classes.append(str(ctx.IDENTIFIER()))

    def enterMethodDeclaration(self, ctx: JavaParserLabeled.MethodDeclarationContext):
        self._list_of_methods.append(str(ctx.IDENTIFIER()))

    def enterVariableDeclaratorId(self, ctx: JavaParserLabeled.VariableDeclaratorIdContext):
        self._list_of_variables.append(str(ctx.IDENTIFIER()))

    def print(self):
        """ for sake of prining"""
        print("classes: ", self._list_of_classes)
        print("methods: ", self._list_of_methods)
        print("variables: ", self._list_of_variables)