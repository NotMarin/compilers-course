import ply.lex as lex
import sys

# Santiago Marin Henao
# Cristian David Lopez Hurtado
# Rosendo Maximiliano Rodriguez Alvarado

reserved = {
    'absolute': 'ABSOLUTE',
    'array': 'ARRAY',
    'begin': 'BEGIN',
    'const': 'CONST',
    'destructor': 'DESTRUCTOR',
    'downto': 'DOWNTO',
    'end': 'END',
    'for': 'FOR',
    'function': 'FUNCTION',
    'if': 'IF',
    'in': 'IN',
    'interface': 'INTERFACE',
    'label': 'LABEL',
    'nil': 'NIL',
    'object': 'OBJECT',
    'or': 'OR',
    'private': 'PRIVATE',
    'class': 'CLASS',
    'program': 'PROGRAM',
    'repeat': 'REPEAT',
    'shl': 'SHL',
    'to': 'TO',
    'unit': 'UNIT',
    'uses': 'USES',
    'virtual': 'VIRTUAL',
    'with': 'WITH',
    'and': 'AND',
    'asm': 'ASM',
    'case': 'CASE',
    'constructor': 'CONSTRUCTOR',
    'external': 'EXTERNAL',
    'do': 'DO',
    'function': 'FUNCTION',
    'procedure': 'PROCEDURE',
    'else': 'ELSE',
    'file': 'FILE',
    'forward': 'FORWARD',
    'goto': 'GOTO',
    'implementation': 'IMPLEMENTATION',
    'inline': 'INLINE',
    'interrupt': 'INTERRUPT',
    'not': 'NOT',
    'off': 'OFF',
    'packed': 'PACKED',
    'procedure': 'PROCEDURE',
    'record': 'RECORD',
    'set': 'SET',
    'shr': 'SHR',
    'then': 'THEN',
    'type': 'TYPE',
    'until': 'UNTIL',
    'var': 'VAR',
    'while': 'WHILE',
    'xor': 'XOR',
    'of': 'OF',
    'div': 'DIVIDE_INT',
    'mod': 'MODULO',
}

# Lista de tokens
tokens = (
    # Reserved words
    'ABSOLUTE', 'ARRAY', 'BEGIN', 'CONST', 'DESTRUCTOR', 'DOWNTO', 'END', 'FOR', 'FUNCTION', 'IF', 'IN', 'INTERFACE',
    'LABEL', 'NIL', 'OBJECT', 'OR', 'PRIVATE', 'PROGRAM', 'REPEAT', 'SHL', 'STRING', 'TO', 'UNIT', 'USES', 'VIRTUAL',
    'WITH', 'AND', 'ASM', 'CASE', 'CONSTRUCTOR', 'EXTERNAL', 'DO', 'ELSE', 'FILE', 'FORWARD', 'GOTO', 'IMPLEMENTATION',
    'INLINE', 'INTERRUPT', 'NOT', 'OFF', 'PACKED', 'PROCEDURE', 'RECORD', 'SET', 'SHR', 'THEN', 'TYPE', 'UNTIL', 'VAR',
    'WHILE', 'XOR', 'INTEGER', 'REAL', 'BOOLEAN', 'OF', 'CLASS', 'FUNCTION', 'PROCEDURE',

    # Operators
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'DIVIDE_INT', 'MODULO', 'EQUAL', 'NEQUAL', 'LT', 'GT', 'LE', 'GE', 'ASSIGN',

    # Delimiters
    'LPAREN', 'RPAREN', 'LBRACKET', 'RBRACKET', 'SEMICOLON', 'COMMA', 'COLON', 'DOT', 'DOTDOT',

    # Others   
    'ID', 'INTEGER_CONST', 'REAL_CONST', 'STRING_LITERAL',
)

# Reglas de expresiones regulares para tokens simples (Operadores)
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_DIVIDE_INT = r'div'  # Token para "div" (división entera)
t_MODULO = r'mod'      # Token para "mod" (operador módulo)
t_EQUAL = r'='
t_NEQUAL = r'<>'
t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='
t_ASSIGN = r':='

# Delimiters
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_SEMICOLON = r';'
t_COMMA = r','
t_COLON = r':'
t_DOTDOT = r'\.\.'
t_DOT = r'\.'

# Regular expression rules for complex tokens

def t_ABSOLUTE(t):
    r'absolute'
    return t

def t_ARRAY(t):
    r'array'
    return t

def t_BEGIN(t):
    r'begin'
    return t

def t_CONST(t):
    r'const'
    return t

def t_DESTRUCTOR(t):    
    r'destructor'
    return t

def t_DOWNTO(t):
    r'downto'
    return t

def t_END(t):
    r'end'
    return t

def t_FOR(t):
    r'for'
    return t

def t_FUNCTION(t):
    r'function'
    return t

def t_IF(t):
    r'if'
    return t

def t_INTEGER(t):  
    r'integer'
    #t.type = 'INTEGER'
    return t

def t_REAL(t):
    r'real'
    return t

def t_BOOLEAN(t):
    r'boolean'
    return t

def t_IN(t):
    r'\bin\b'
    t.type = 'IN'
    return t

def t_INTERFACE(t):
    r'interface'
    return t

def t_LABEL(t):
    r'label'
    return t

def t_NIL(t):
    r'nil'
    return t

def t_OBJECT(t):
    r'object'
    return t    

def t_OR(t):
    r'or'
    return t

def t_PRIVATE(t):
    r'private'
    return t

def t_PROGRAM(t):
    r'program'
    return t

def t_REPEAT(t):
    r'repeat'
    return t

def t_SHL(t):
    r'shl'
    return t

def t_STRING(t):
    r'string'
    return t

def t_TO(t):
    r'to'
    return t

def t_UNIT(t):
    r'unit'
    return t

def t_USES(t):
    r'uses'
    return t

def t_VIRTUAL(t):
    r'virtual'
    return t

def t_WITH(t):
    r'with'
    return t

def t_AND(t):
    r'and'
    return t

def t_ASM(t):
    r'asm'
    return t

def t_CASE(t):
    r'case'
    return t    

def t_CONSTRUCTOR(t):
    r'constructor'
    return t

def t_EXTERNAL(t):
    r'external'
    return t

def t_DO(t):
    r'do'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_FILE(t):
    r'file'
    return t

def t_FORWARD(t):
    r'forward'
    return t

def t_GOTO(t):
    r'goto'
    return t

def t_IMPLEMENTATION(t):
    r'implementation'
    return t

def t_INLINE(t):
    r'inline'
    return t

def t_CLASS(t):
    r'class'
    return t

def t_INTERRUPT(t):
    r'interrupt'
    return t

def t_NOT(t):
    r'not'
    return t

def t_OFF(t):
    r'off'
    return t

def t_PACKED(t):
    r'packed'
    return t

def t_PROCEDURE(t):
    r'procedure'
    return t

def t_RECORD(t):
    r'record'
    return t

def t_SET(t):
    r'set'
    return t

def t_SHR(t):
    r'shr'
    return t

def t_THEN(t):
    r'then'
    return t

def t_TYPE(t):
    r'type'
    return t

def t_UNTIL(t):
    r'until'
    return t

def t_VAR(t):
    r'var'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_XOR(t):
    r'xor'
    return t

# Números
def t_INVALID_ID(t):
    r'\d+[a-zA-Z_][a-zA-Z0-9_]*'
    print(f"Error léxico: Identificador inválido '{t.value}' en la línea {t.lineno}")
    t.lexer.skip(len(t.value))
    
def t_REAL_CONST(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INTEGER_CONST(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Identificadores



def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value.lower(), 'ID') # Se verifica si es una palabra reservada dentro del diccionario
    return t

# Literales de cadena
def t_STRING_LITERAL(t):
    r'\'([^\\\n]|(\\.))*?\''
    t.value = t.value[1:-1]  # Remueve las comillas
    return t

# Comentarios { ... }
def t_COMMENT(t):
    r'\{[^}]*\}'
    pass

# Comentarios (* ... *)
def t_COMMENT_MULTILINE(t):  # Cambiado de T a t (minúscula)
    r'\(\*(.|\n)*?\*\)'
    pass

# Nueva línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    
# Espacios y tabulaciones que se ignoran
t_ignore = ' \t'

# Manejo de errores léxicos
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lexer.lineno}")
    t.lexer.skip(1)
    

def test(data, lexer):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)

lexer = lex.lex()

if __name__ == '__main__':
    if (len(sys.argv) > 1):
        fin = sys.argv[1]
    else:
        

        fin = 'test.pas'
    try:
        with open(fin, 'r') as f:
            data = f.read()
            print(data)
            lexer.input(data)
            test(data, lexer)
    except FileNotFoundError:
        print(f"Error: El archivo '{fin}' no existe.")
