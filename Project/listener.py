from gram.JavaParserLabeled import JavaParserLabeled
from gram.JavaParserLabeledListener import JavaParserLabeledListener



class QuestionListener(JavaParserLabeledListener):
    def __init__(self, file: str):
        self._file = file
        self._list_of_classes = []
        
        self._class_stack = []
        
        self._list_of_methods = {}
        
        
        
        self._list_of_private_fields = {}
        self._list_of_public_fields = {}
        
        
        self._fan_out = {}
        
        self._fan_out_dic = {}
        
        self.inside_fields = False
        
        self.is_private = False
        self.is_public = False
        
        self._last_modifier = ""
        
        self.last_method = None
        
        self.fan_out = 0

    def enterClassDeclaration(self, ctx: JavaParserLabeled.ClassDeclarationContext):
        self._class_stack.append(str(ctx.IDENTIFIER()))
        self._list_of_classes.append(str(ctx.IDENTIFIER()))
        
    def exitClassDeclaration(self, ctx: JavaParserLabeled.ClassDeclarationContext):
        if len(self._class_stack) != 0:
            self._class_stack.pop()
    

    def enterMethodDeclaration(self, ctx: JavaParserLabeled.MethodDeclarationContext):
        list_methods = self._list_of_methods.get(str(self._class_stack[-1]), None)
        self.last_method = str(ctx.IDENTIFIER())
        
        if list_methods:
            list_methods.append(str(ctx.IDENTIFIER()))
            self._list_of_methods[str(self._class_stack[-1])] = list(list_methods)
        else:
            self._list_of_methods[str(self._class_stack[-1])] = list([str(ctx.IDENTIFIER())])
            
            
    def exitMethodDeclaration(self, ctx: JavaParserLabeled.MethodDeclarationContext):
        
        
        self._fan_out[self.last_method] = self.fan_out
        
        self.last_method = None
        self.fan_out = 0

        
    def enterFieldDeclaration(self, ctx: JavaParserLabeled.FieldDeclarationContext):
        if self._last_modifier == "public":
            self.is_public = True
        elif self._last_modifier == "private":
            self.is_private = True
            
        self.inside_fields = True

    def enterVariableDeclaratorId(self, ctx: JavaParserLabeled.VariableDeclaratorIdContext):
        if self.inside_fields and self.is_public:
            list_fields_public = self._list_of_public_fields.get(str(self._class_stack[-1]))
            
            if list_fields_public:
                list_fields_public.append(str(ctx.IDENTIFIER()))
                self._list_of_public_fields[str(self._class_stack[-1])] = list(list_fields_public)
            else:
                self._list_of_public_fields[str(self._class_stack[-1])] = list([str(ctx.IDENTIFIER())])
            
            self.is_public = False
            
            
        elif self.inside_fields and self.is_private:
            list_fields_private = self._list_of_private_fields.get(str(self._class_stack[-1]))
            
            if list_fields_private:
                list_fields_private.append(str(ctx.IDENTIFIER()))
                self._list_of_private_fields[str(self._class_stack[-1])] = list(list_fields_private)
            else:
                self._list_of_private_fields[str(self._class_stack[-1])] = list([str(ctx.IDENTIFIER())])
                
            self.is_private = False
            
    
    def enterMethodCall0(self, ctx: JavaParserLabeled.MethodCall0Context):
        if self.last_method != None:
            listt = self._fan_out_dic.get(self.last_method, [])
            listt.append(str(ctx.IDENTIFIER()))
            self._fan_out_dic[self.last_method] = list(listt)
            self.fan_out += 1
    
    def enterMethodCall1(self, ctx: JavaParserLabeled.MethodCall1Context):
        if self.last_method != None:
            self.fan_out += 1
    
    def enterMethodCall2(self, ctx: JavaParserLabeled.MethodCall2Context):
        if self.last_method != None:
            self.fan_out += 1
    
    
        
    def exitFieldDeclaration(self, ctx: JavaParserLabeled.FieldDeclarationContext):
        self.inside_fields = False
        
    def enterClassOrInterfaceModifier(self, ctx:JavaParserLabeled.ClassOrInterfaceModifierContext):
        if ctx.getText() == "public":
            self._last_modifier = ctx.getText()
        elif ctx.getText() == "private":
            self._last_modifier = ctx.getText()
            
    def get_fan_in(self):
        list_fan_in = {}
        
        for key, value in self._fan_out_dic.items():
            for val in value:
                listt = list_fan_in.get(val, [])
                listt.append(key)
                list_fan_in[val] = list(listt)

        return [(method, len(value)) for method, value in list_fan_in.items()]
    

    def get_number_of_methods(self):
        sum = 0
        
        for x in self._list_of_methods.values():
            sum += len(x)
            
        return sum
        
    def get_number_of_private(self):
        sum = 0
        
        for x in self._list_of_private_fields.values():
            sum += len(x)
            
        return sum
        
    def get_number_of_public(self):
        sum = 0
        
        for x in self._list_of_public_fields.values():
            sum += len(x)
            
        return sum
        

    def print(self):
        """ for sake of prining"""
        print("Number of class: ", len(self._list_of_classes))
        print("Number of methods: ", self.get_number_of_methods())
        print("Number of private fields: ", self.get_number_of_private())
        print("Number of public fields: ", self.get_number_of_public())
        print("classes: ", self._list_of_classes)
        print("methods: ", self._list_of_methods)
        print("private fields: ", self._list_of_private_fields)
        print("public fields: ", self._list_of_public_fields)
        print("fan out: ", self._fan_out)
        print("fan in: ", self.get_fan_in())