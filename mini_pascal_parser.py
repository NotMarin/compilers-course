import ply.yacc as yacc
from mini_pascal_lexxer import tokens
import mini_pascal_lexxer
import sys

VERBOSE = 1 # 1 para imprimir errores, 0 para no imprimir errores

# Santiago Marin Henao
# Cristian David Lopez Hurtado
# Rosendo Maximiliano Rodriguez Alvarado

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
    ('right', 'EXPONENT'), 
)

# Reglas para el programa principal
def p_program(p):
    'program : PROGRAM ID SEMICOLON uses_clause_opt block DOT'
    pass

def p_uses_clause_opt(p):
    '''uses_clause_opt : uses_clause
                       | empty'''
    pass


def p_unit_list(p):
    '''unit_list : unit_list COMMA ID
                 | ID'''
    pass

def p_uses_clause(p):
    'uses_clause : USES unit_list SEMICOLON'
    pass

# Reglas para el bloque
def p_block(p):
    'block : declarations compound_statement'
    pass

# Reglas para las declaraciones
def p_declarations(p):
    '''declarations : declaration_list
                    | empty'''
    pass

def p_declaration_list(p):
    '''declaration_list : declaration_list declaration
                        | declaration'''
    pass

def p_declaration(p):
    '''declaration : var_declaration
                   | const_declaration
                   | type_declaration
                   | procedure_declaration
                   | function_declaration'''
    pass

def p_var_declaration(p):
    'var_declaration : VAR var_declaration_list'
    pass

def p_var_declaration_list(p):
    '''var_declaration_list : var_declaration_list var_decl
                | var_decl'''
    pass

def p_var_decl(p):
    'var_decl : id_list COLON type SEMICOLON'
    pass

def p_id_list(p):
    '''id_list : id_list COMMA ID
               | ID'''
    pass

def p_const_declaration(p):
    'const_declaration : CONST const_list'
    pass

def p_const_list(p):
    '''const_list : const_list const_definition SEMICOLON
                  | const_definition SEMICOLON'''
    pass

def p_const_definition(p):
    'const_definition : ID EQUAL constant'
    pass

def p_procedure_declaration(p):
    'procedure_declaration : PROCEDURE ID  formal_parameter_list_opt SEMICOLON block SEMICOLON'
    pass

def p_function_declaration(p):
    'function_declaration : FUNCTION ID formal_parameter_list_opt COLON type SEMICOLON block SEMICOLON'
    pass

def p_formal_parameter_list_opt(p):
    '''formal_parameter_list_opt : LPAREN formal_parameter_list RPAREN
                             | empty'''
    pass

def p_formal_parameter_list(p):
    '''formal_parameter_list : formal_parameter_list SEMICOLON formal_parameter
                             | formal_parameter'''
    pass

def p_formal_parameter(p):
    'formal_parameter : id_list COLON type'
    pass

# Reglas para las declaraciones de tipo
def p_type_declaration(p):
    'type_declaration : TYPE type_list'
    pass

def p_type_list(p):
    '''type_list : type_list type_definition SEMICOLON
                 | type_definition SEMICOLON'''
    pass

def p_type_definition(p):
    'type_definition : ID EQUAL type'
    pass


def p_type(p):
    '''type : simple_type
            | array_type
            | record_type
            | class_type
            | enumerated_type'''
    pass

def p_class_type(p):
    'class_type : CLASS class_body END'
    pass

def p_enumerated_type(p):
    'enumerated_type : LPAREN identifier_list RPAREN'
    pass

def p_identifier_list(p):
    '''identifier_list : identifier_list COMMA ID
                       | ID'''
    pass

def p_class_body(p):
    '''class_body : class_member_list'''
    pass

def p_class_member_list(p):
    '''class_member_list : class_member_list class_member
                         | class_member'''
    pass
def p_class_member(p):
    '''class_member : class_variable_declaration
                    | constructor_declaration
                    | class_function_declaration
                    | class_procedure_declaration'''
    pass

def p_class_variable_declaration(p):
    'class_variable_declaration : ID COLON type SEMICOLON'
    pass

def p_constructor_declaration(p):
    'constructor_declaration : CONSTRUCTOR ID formal_parameter_list_opt SEMICOLON'
    pass
def p_class_function_declaration(p):
    'class_function_declaration : FUNCTION ID formal_parameter_list_opt COLON type SEMICOLON'
    pass
def p_function_declaration(p):
    'function_declaration : FUNCTION ID formal_parameter_list_opt COLON type SEMICOLON block SEMICOLON'
    pass

def p_procedure_declaration(p):
    'procedure_declaration : PROCEDURE ID formal_parameter_list_opt SEMICOLON block SEMICOLON'
    pass


def p_class_procedure_declaration(p):
    'class_procedure_declaration : PROCEDURE ID formal_parameter_list_opt SEMICOLON'
    pass


def p_simple_type(p):
    '''simple_type : subrange_type
                   | type_identifier'''
    pass

def p_subrange_type(p):
    'subrange_type : constant DOTDOT constant'
    pass

def p_array_type(p):
    'array_type : ARRAY LBRACKET index_type RBRACKET OF type'
    pass

def p_index_type(p):
    '''index_type : simple_type'''
    pass

def p_record_type(p):
    'record_type : RECORD record_fields END'
    pass

def p_record_fields(p):
    '''record_fields : field_list'''
    pass

def p_field_list(p):
    '''field_list : field_list field_declaration SEMICOLON
                  | field_declaration SEMICOLON'''
    pass
     
def p_field_declaration(p):
    'field_declaration : id_list COLON type'
    pass

def p_type_identifier(p):
    '''type_identifier : ID
                       | predefined_type'''
    pass

def p_predefined_type(p):
    '''predefined_type : INTEGER
                       | REAL
                       | BOOLEAN
                       | STRING'''
    pass

# Reglas para las sentencias
def p_compound_statement(p):
    'compound_statement : BEGIN statement_list END'
    pass

def p_statement_list(p):
    '''statement_list : statement
                      | statement_list SEMICOLON statement'''
    pass

def p_statement(p):
    '''statement : simple_statement
                 | structured_statement'''
    pass

def p_simple_statement(p):
    '''simple_statement : assignment_statement
                        | procedure_call_statement
                        | empty'''
    pass

def p_assignment_statement(p):
    'assignment_statement : variable ASSIGN expression'
    pass

def p_variable(p):
    '''variable : ID
                | variable DOT ID
                | variable LBRACKET expression_list RBRACKET'''
    pass

def p_expression_list(p):
    '''expression_list : expression
                       | expression_list COMMA expression'''
    pass

def p_procedure_call_statement(p):
    'procedure_call_statement : procedure_call'
    pass

def p_procedure_call(p):
    '''procedure_call : ID LPAREN args_optional RPAREN'''
    pass

def p_args(p):
    '''args : args COMMA expression
            | expression'''
    pass

def p_structured_statement(p):
    '''structured_statement : compound_statement
                            | if_statement
                            | while_statement
                            | repeat_statement
                            | for_statement
                            | case_statement
                            | record_assignment'''
    pass

def p_if_statement(p):
    'if_statement : IF expression THEN statement else_part'
    pass

def p_else_part(p):
    '''else_part : ELSE statement
                 | empty'''
    pass

def p_while_statement(p):
    'while_statement : WHILE expression DO statement'
    pass

def p_repeat_statement(p):
    'repeat_statement : REPEAT statement_list UNTIL expression'
    pass

def p_for_statement(p):
    '''for_statement : FOR ID ASSIGN expression TO expression DO statement
                     | FOR ID ASSIGN expression DOWNTO expression DO statement'''
    pass

def p_case_statement(p):
    'case_statement : CASE expression OF case_element_list else_clause_optional END'
    pass

def p_case_element_list(p):
    '''case_element_list : case_element_list semicolon_optional case_element
                         | case_element'''
    pass

def p_case_element(p):
    'case_element : case_label_list COLON statement'
    pass

def p_case_label_list(p):
    '''case_label_list : case_label_list COMMA case_label
                       | case_label'''
    pass

def p_case_label(p):
    'case_label : constant'
    pass

def p_else_clause_optional(p):
    '''else_clause_optional : semicolon_optional ELSE statement semicolon_optional
                            | empty'''
    pass

def p_semicolon_optional(p):
    '''semicolon_optional : SEMICOLON
                          | empty'''
    pass

def p_record_assignment(p):
    'record_assignment : ID DOT ID ASSIGN expression'
    pass

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
                  | expression XOR expression
                  | NOT expression %prec NOT
                  | expression EXPONENT expression 
                  | LPAREN expression RPAREN
                  | function_call
                  | variable
                  | INTEGER_CONST
                  | REAL_CONST
                  | STRING_LITERAL'''
    pass


def p_function_call(p):
    'function_call : ID LPAREN args_optional RPAREN'
    pass


def p_args_opt(p):
    '''args_optional : args
                     | empty'''
    pass

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
with open(fin, 'r', encoding='utf-8') as f:
    data = f.read()
if parser.parse(data, tracking=True) == None:
    print("No se encontraron errores de sintaxis.")
else:
    print("Se encontraron errores de sintaxis.")
