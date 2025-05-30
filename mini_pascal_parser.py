import ply.yacc as yacc
from mini_pascal_lexxer import tokens
import mini_pascal_lexxer
import sys
from symbol_table import SymbolTable

symbol_table = SymbolTable()
VERBOSE = 1 # 1 para imprimir errores, 0 para no imprimir errores

# Santiago Marin Henao
# Cristian David Lopez Hurtado
# Rosendo Maximiliano Rodriguez Alvarado

class Program:
    def __init__(self, name, uses, block):
        self.name = name
        self.uses = uses
        self.block = block

class Block:
    def __init__(self, declarations, compound_statement):
        self.declarations = declarations
        self.compound_statement = compound_statement

class VarDecl:
    def __init__(self, names, var_type):
        self.names = names
        self.var_type = var_type

class Assignment:
    def __init__(self, variable, expression):
        self.variable = variable
        self.expression = expression

class BinaryOp:
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

class Num:
    def __init__(self, value):
        self.value = value

class Variable:
    def __init__(self, name):
        self.name = name

class Compound:
    def __init__(self, statements):
        self.statements = statements
        
class UnaryOp:
    def __init__(self, op, expr):
        self.op = op
        self.expr = expr

# Reglas de precedencia
precedence = (
    ('right', 'ASSIGN'),
    ('left', 'OR', 'XOR'),
    ('left', 'AND'),
    ('left', 'SHL', 'SHR'),
    ('nonassoc', 'EQUAL', 'NEQUAL', 'LT', 'LE', 'GT', 'GE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'DIVIDE_INT', 'MODULO'),
    ('left', 'LPAREN', 'RPAREN'),
    ('right', 'NOT'),
)

# Reglas para el programa principal
def p_program(p):
    'program : PROGRAM ID SEMICOLON uses_clause_opt block DOT'
    p[0] = Program(p[2], p[4], p[5])

def p_uses_clause_opt(p):
    '''uses_clause_opt : uses_clause
                       | empty'''
    p[0] = p[1] if p[1] is not None else []


def p_unit_list(p):
    '''unit_list : unit_list COMMA ID
                 | ID'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_uses_clause(p):
    'uses_clause : USES unit_list SEMICOLON'
    p[0] = ('uses_clause', p[2])

# Reglas para el bloque
def p_block(p):
    'block : declarations compound_statement'
    p[0] = Block(p[1], p[2])

# Reglas para las declaraciones
def p_declarations(p):
    '''declarations : declaration_list
                    | empty'''
    p[0] = p[1] if p[1] is not None else []

def p_declaration_list(p):
    '''declaration_list : declaration_list declaration
                        | declaration'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_declaration(p):
    '''declaration : var_declaration
                   | const_declaration
                   | type_declaration
                   | procedure_declaration
                   | function_declaration'''
    p[0] = p[1]

def p_var_declaration(p):
    'var_declaration : VAR var_declaration_list'
    p[0] = ('var_declaration', p[2])

def p_var_declaration_list(p):
    '''var_declaration_list : var_declaration_list var_decl
                            | var_decl'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_var_decl(p):
    'var_decl : id_list COLON type SEMICOLON'
    for var in p[1]:
        symbol_table.define(var, p[3])
    p[0] = VarDecl(p[1], p[3])


def p_id_list(p):
    '''id_list : id_list COMMA ID
               | ID'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_const_declaration(p):
    'const_declaration : CONST const_list'
    p[0] = ('const_declaration', p[2])

def p_const_list(p):
    '''const_list : const_list const_definition SEMICOLON
                  | const_definition SEMICOLON'''
    if len(p) == 3:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_const_definition(p):
    'const_definition : ID EQUAL constant'
    symbol_table.define(p[1], p[3])
    p[0] = ('const_def', p[1], p[3])


def p_formal_parameter_list_opt(p):
    '''formal_parameter_list_opt : LPAREN formal_parameter_list RPAREN
                                 | empty'''
    p[0] = p[2] if len(p) > 2 else []

def p_formal_parameter_list(p):
    '''formal_parameter_list : formal_parameter_list SEMICOLON formal_parameter
                             | formal_parameter'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_formal_parameter(p):
    'formal_parameter : id_list COLON type'
    p[0] = ('param', p[1], p[3])

# Reglas para las declaraciones de tipo
def p_type_declaration(p):
    'type_declaration : TYPE type_list'
    p[0] = ('type_declaration', p[2])

def p_type_list(p):
    '''type_list : type_list type_definition SEMICOLON
                 | type_definition SEMICOLON'''
    if len(p) == 3:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_type_definition(p):
    'type_definition : ID EQUAL type'
    p[0] = ('type_def', p[1], p[3])


def p_type(p):
    '''type : simple_type
            | array_type
            | record_type
            | class_type'''
    p[0] = p[1]

def p_class_type(p):
    'class_type : CLASS class_body END'
    p[0] = ('class_type', p[2])

def p_class_body(p):
    '''class_body : class_member_list'''
    p[0] = p[1]

def p_class_member_list(p):
    '''class_member_list : class_member_list class_member
                         | class_member'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_class_member(p):
    '''class_member : class_variable_declaration
                    | constructor_declaration
                    | class_function_declaration
                    | class_procedure_declaration'''
    p[0] = p[1]

def p_class_variable_declaration(p):
    'class_variable_declaration : ID COLON type SEMICOLON'
    p[0] = ('class_var_decl', p[1], p[3])

def p_constructor_declaration(p):
    'constructor_declaration : CONSTRUCTOR ID formal_parameter_list_opt SEMICOLON'
    p[0] = ('constructor_decl', p[2], p[3])

def p_class_function_declaration(p):
    'class_function_declaration : FUNCTION ID formal_parameter_list_opt COLON type SEMICOLON'
    p[0] = ('class_func_decl', p[2], p[3], p[5])

def p_function_declaration(p):
    'function_declaration : FUNCTION ID formal_parameter_list_opt COLON type SEMICOLON block SEMICOLON'
    p[0] = ('function_decl', p[2], p[3], p[5], p[7])

def p_procedure_declaration(p):
    'procedure_declaration : PROCEDURE ID formal_parameter_list_opt SEMICOLON block SEMICOLON'
    p[0] = ('procedure_decl', p[2], p[3], p[5])


def p_class_procedure_declaration(p):
    'class_procedure_declaration : PROCEDURE ID formal_parameter_list_opt SEMICOLON'
    p[0] = ('class_proc_decl', p[2], p[3])


def p_simple_type(p):
    '''simple_type : subrange_type
                   | type_identifier'''
    p[0] = p[1]

def p_subrange_type(p):
    'subrange_type : constant DOTDOT constant'
    p[0] = ('subrange', p[1], p[3])

def p_array_type(p):
    'array_type : ARRAY LBRACKET index_type RBRACKET OF type'
    p[0] = ('array', p[3], p[6])

def p_index_type(p):
    '''index_type : simple_type'''
    p[0] = p[1]

def p_record_type(p):
    'record_type : RECORD record_fields END'
    p[0] = ('record', p[2])

def p_record_fields(p):
    '''record_fields : field_list'''
    p[0] = p[1]

def p_field_list(p):
    '''field_list : field_list field_declaration SEMICOLON
                  | field_declaration SEMICOLON'''
    if len(p) == 3:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]
     
def p_field_declaration(p):
    'field_declaration : id_list COLON type'
    p[0] = ('field_decl', p[1], p[3])

def p_type_identifier(p):
    '''type_identifier : ID
                       | predefined_type'''
    p[0] = p[1]

def p_predefined_type(p):
    '''predefined_type : INTEGER
                       | REAL
                       | BOOLEAN
                       | STRING'''
    p[0] = p[1]

# Reglas para las sentencias
def p_compound_statement(p):
    'compound_statement : BEGIN statement_list END'
    p[0] = Compound(p[2])

def p_statement_list(p):
    '''statement_list : statement
                      | statement_list SEMICOLON statement'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_statement(p):
    '''statement : simple_statement
                 | structured_statement'''
    p[0] = p[1]

def p_simple_statement(p):
    '''simple_statement : assignment_statement
                        | procedure_call_statement
                        | empty'''
    p[0] = p[1]

def p_assignment_statement(p):
    'assignment_statement : variable ASSIGN expression'
    p[0] = Assignment(p[1], p[3])

def p_variable(p):
    'variable : ID'
    try:
        symbol_table.lookup(p[1])
    except Exception as e:
        print(str(e))
        raise
    p[0] = Variable(p[1])

def p_expression_list(p):
    '''expression_list : expression
                       | expression_list COMMA expression'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_procedure_call_statement(p):
    'procedure_call_statement : procedure_call'
    p[0] = p[1]

def p_procedure_call(p):
    '''procedure_call : ID LPAREN args_optional RPAREN'''
    p[0] = ('proc_call', p[1], p[3])

def p_args(p):
    '''args : args COMMA expression
            | expression'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_structured_statement(p):
    '''structured_statement : compound_statement
                            | if_statement
                            | while_statement
                            | repeat_statement
                            | for_statement
                            | case_statement
                            | record_assignment'''
    p[0] = p[1]

def p_if_statement(p):
    'if_statement : IF expression THEN statement else_part'
    p[0] = ('if', p[2], p[4], p[5])

def p_else_part(p):
    '''else_part : ELSE statement
                 | empty'''
    if len(p) == 3:
        p[0] = ('else', p[2])
    else:
        p[0] = None

def p_while_statement(p):
    'while_statement : WHILE expression DO statement'
    p[0] = ('while', p[2], p[4])

def p_repeat_statement(p):
    'repeat_statement : REPEAT statement_list UNTIL expression'
    p[0] = ('repeat', p[2], p[4])

def p_for_statement(p):
    '''for_statement : FOR ID ASSIGN expression TO expression DO statement
                     | FOR ID ASSIGN expression DOWNTO expression DO statement'''
    direction = 'to' if p[5] == 'TO' else 'downto'
    p[0] = ('for', p[2], p[4], p[6], direction, p[8])

def p_case_statement(p):
    'case_statement : CASE expression OF case_element_list else_clause_optional END'
    p[0] = ('case', p[2], p[4], p[5])

def p_case_element_list(p):
    '''case_element_list : case_element_list semicolon_optional case_element
                         | case_element'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_case_element(p):
    'case_element : case_label_list COLON statement'
    p[0] = ('case_element', p[1], p[3])

def p_case_label_list(p):
    '''case_label_list : case_label_list COMMA case_label
                       | case_label'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_case_label(p):
    'case_label : constant'
    p[0] = p[1]

def p_else_clause_optional(p):
    '''else_clause_optional : semicolon_optional ELSE statement semicolon_optional
                            | empty'''
    if len(p) > 2:
        p[0] = ('else', p[3])
    else:
        p[0] = None

def p_semicolon_optional(p):
    '''semicolon_optional : SEMICOLON
                          | empty'''
    pass

def p_record_assignment(p):
    'record_assignment : ID DOT ID ASSIGN expression'
    p[0] = ('record_assign', p[1], p[3], p[5])

# Reglas para las expresiones
# En el operador unario NOT, se utiliza %prec para asignar la precedencia correcta
def p_expression(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression DIVIDE_INT expression
                  | expression MODULO expression
                  | expression SHL expression
                  | expression SHR expression
                  | expression EQUAL expression
                  | expression NEQUAL expression
                  | expression LT expression
                  | expression GT expression
                  | expression LE expression
                  | expression GE expression
                  | expression AND expression
                  | expression OR expression
                  | expression XOR expression'''
    p[0] = BinaryOp(p[2], p[1], p[3])
    
def p_expression_not(p):
    'expression : NOT expression %prec NOT'
    p[0] = UnaryOp('NOT', p[2])

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_function_call(p):
    'expression : function_call'
    p[0] = p[1]

def p_expression_variable(p):
    'expression : variable'
    p[0] = p[1]

def p_expression_integer(p):
    'expression : INTEGER_CONST'
    p[0] = Num(p[1])

def p_expression_real(p):
    'expression : REAL_CONST'
    p[0] = Num(p[1])

def p_expression_string(p):
    'expression : STRING_LITERAL'
    p[0] = Num(p[1])  # O crea una clase StringLiteral si quieres manejarlo distinto

def p_function_call(p):
    'function_call : ID LPAREN args_optional RPAREN'
    p[0] = ('func_call', p[1], p[3])


def p_args_optional(p):
    '''args_optional : args
                     | empty'''
    p[0] = p[1] if p[1] is not None else []

# Reglas para las declaraciones de constantes
def p_constant(p):
    '''constant : UNSIGNED_NUMBER
                | sign UNSIGNED_NUMBER
                | STRING_LITERAL
                | constant_identifier'''
    pass

def p_unsigned_number(p):
    '''UNSIGNED_NUMBER : INTEGER_CONST
                       | REAL_CONST'''
    pass

def p_sign(p):
    '''sign : PLUS
            | MINUS'''
    pass

def p_constant_identifier(p):
    'constant_identifier : ID'
    pass

# Regla para vacío
def p_empty(p):
    'empty :'
    pass

def p_error(p):
	if VERBOSE:
		if p is not None:
			print ("ERROR SINTACTICO EN LA LINEA " + str(p.lexer.lineno) + " NO SE ESPERABA EL Token  " + str(p.value))
		else:
			print ("ERROR SINTACTICO EN LA LINEA: " + str(mini_pascal_lexxer.lexer.lineno))
	else:
		raise Exception('syntax', 'error')
		
parser = yacc.yacc(debug=True)

if __name__ == '__main__':
	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'test.pas'
	f = open(fin, 'r')
	data = f.read()
ast = parser.parse(data, tracking=True)
if ast is not None:
    print("No se encontraron errores.")
else:
    print("Se encontraron errores de sintaxis.")

print("Símbolos en la tabla de símbolos:")
for name, symbol in symbol_table.symbols.items():
    # Try to get 'value', if not present, get 'var_type' or just print the symbol itself
    value = getattr(symbol, 'value', None)
    if value is None:
        value = getattr(symbol, 'var_type', None)
    print(f"{name}: {symbol}, valor: {value}")
