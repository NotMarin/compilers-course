import ply.yacc as yacc
from mini_pascal_lexxer import tokens
import mini_pascal_lexxer
import sys

VERBOSE = 1

precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('nonassoc', 'EQUAL'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'LPAREN', 'RPAREN'),
    # NOT eliminado por no estar definido
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

def p_block(p):
    'block : declarations compound_statement'
    pass

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
                   | const_declaration'''
    pass

def p_var_declaration(p):
    'var_declaration : VAR var_declaration_list'
    pass

def p_var_declaration_list(p):
    '''var_declaration_list : var_declaration_list var_decl
                | var_decl'''
    pass

def p_var_decl(p):
    'var_decl : id_list COLON ID SEMICOLON'
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

def p_compound_statement(p):
    'compound_statement : BEGIN statement_list END'
    pass

def p_statement_list(p):
    '''statement_list : statement
                      | statement_list SEMICOLON statement'''
    pass

def p_statement(p):
    '''statement : simple_statement
                 | compound_statement'''
    pass

def p_simple_statement(p):
    '''simple_statement : assignment_statement
                        | empty'''
    pass

def p_assignment_statement(p):
    'assignment_statement : ID EQUAL expression'
    pass

def p_expression(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | LPAREN expression RPAREN
                  | ID
                  | NUMBER'''
    pass

def p_constant(p):
    '''constant : NUMBER
                | STRING_LITERAL
                | CHARACTER_LITERAL
                | BOOLEAN_LITERAL'''
    pass

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    if VERBOSE:
        if p is not None:
            print("ERROR SINTACTICO EN LA LINEA", p.lexer.lineno, "NO SE ESPERABA EL Token", p.value)
        else:
            print("ERROR SINTACTICO EN LA LINEA:", p.lexer.lexer.lineno)
    else:
        raise Exception('syntax', 'error')

parser = yacc.yacc(debug=True)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fin = sys.argv[1]
    else:
        fin = 'test.pas'

    with open(fin, 'r') as f:
        data = f.read()

    print(data)
    result = parser.parse(data, tracking=True)
    if result is None:
        print("Se encontraron errores en el programa.")
    else:
        print("El programa fue analizado correctamente.")