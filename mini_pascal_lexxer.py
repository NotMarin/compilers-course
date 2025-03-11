import ply.lex as lex
import sys

# Definir los tokens que se usarán
tokens = (
    # Palabras reservadas
    'ABSOLUTE',
    'AND',
    'ARRAY',
    'BEGIN',
    'CONST',
    'DESTRUCTOR',
    'DIV',
    'DOWNTO',
    'DO',
    'END',
    'FOR',
    'FUNCTION',
    'IF',
    'IN',
    'INTERFACE',
    'LABEL',
    'NIL',
    'OBJECT',
    'OR',
    'PRIVATE',
    'PROGRAM',
    'REPEAT',
    'SHL',
    'STRING',
    'TO',
    'THEN',
    'UNIT',
    'UNTIL',
    'USES',
    'VAR',
    'VIRTUAL',
    'WRITE',
    'WHILE',
    'INTEGER',
    'READLN',
    'READ',
    'WRITELN',
    'XOR',
    'OUTPUT',
    'INPUT',
    'PROCEDURE',


    #Simbolos
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LESS',
    'LESSEQUAL',
    'GREATER',
    'GREATEREQUAL',
    'EQUAL',
    'DISTINT',
    'SEMICOLON',
    'COMMA',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'LBLOCK',
    'RBLOCK',
    'DOT',
    'ASSIGNMENT',
    'DOUBLEQUOTE',
    'QUOTE',
    'COLON',
    
    'ID',
    'NUMBER',
    'FLOAT',
    'STRING_LITERAL',
    'CHARACTER_LITERAL',
    'BOOLEAN_LITERAL'
    
)

# Definir las expresiones regulares para los tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LESS = r'<'
t_LESSEQUAL = r'<='
t_GREATER = r'>'
t_GREATEREQUAL = r'>='
t_EQUAL = r'='
t_DISTINT = r'<>'
t_SEMICOLON = r';'
t_COMMA = r','
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBLOCK = r'\{'
t_RBLOCK = r'\}'
t_DOT = r'\.'
t_ASSIGNMENT = r'\:='
t_COLON = r'\:'
t_DOUBLEQUOTE = r'\"'
t_QUOTE = r'\''


# Definir las palabras reservadas
def t_ABSOLUTE(t):
    r'\babsolute\b'
    return t
  
def t_AND(t):
    r'\band\b'
    return t

def t_ARRAY(t):
    r'\barray\b'
    return t
  
def t_BEGIN(t):
    r'\bbegin\b'
    return t

def t_CONST(t):
    r'\bconst\b'
    return t
  
def t_DESTRUCTOR(t):
    r'\bdestructor\b'
    return t
  
def t_DIV(t):
    r'\bdiv\b'
    return t

def t_DOWNTO(t):
    r'\bdownto\b'
    return t
  
def t_DO(t):
    r'\bdo\b'
    return t
  
def t_END(t):
    r'\bend\b'
    return t
  
def t_FOR(t):
    r'\bfor\b'
    return t
  
def t_FUNCTION(t):
    r'\bfunction\b'
    return t

def t_IF(t):
    r'\bif\b'
    return t
  
def t_INTERFACE(t):
    r'\binterface\b'
    return t
  
def t_LABEL(t):
    r'\blabel\b'
    return t
  
def t_NIL(t):
    r'\bnil\b'
    return t
  
def t_OBJECT(t):
    r'\bobject\b'
    return t

def t_OR(t):
    r'\bor\b'
    return t
  
def t_PRIVATE(t):
    r'\bprivate\b'
    return t
  
def t_PROCEDURE(t):
    r'\bprocedure\b'
    return t

def t_PROGRAM(t):
    r'\bprogram\b'
    return t

def t_REPEAT(t):
    r'\brepeat\b'
    return t
  
def t_SHL(t):
    r'\bshl\b'
    return t
  
def t_STRING(t):
    r'\bstring\b'
    return t
  
def t_TO(t):
    r'\bto\b'
    return t

def t_THEN(t):
    r'\bthen\b'
    return t

def t_UNIT(t):
    r'\bunit\b'
    return t
  
def t_UNTIL(t):
    r'\buntil\b'
    return t

def t_USES(t):
    r'\buses\b'
    return t
  
def t_VAR(t):
    r'\bvar\b'
    return t
  
def t_VIRTUAL(t):
    r'\bvirtual\b'
    return t
  
def t_WRITELN(t):
    r'\bwriteln\b'
    return t
  
def t_WRITE(t):
    r'\bwrite\b'
    return t
  
def t_WHILE(t):
    r'\bwhile\b'
    return t
  
def t_INTEGER(t):
    r'\binteger\b'
    return t
  
def t_READLN(t):
    r'\breadln\b'
    return t

def t_READ(t):
    r'\bread\b'
    return t
  
def t_XOR(t):
    r'\bxor\b'
    return t

def t_FLOAT(t):
    r'\d+\.\d*([eE][-+]?\d+)?|\.\d+([eE][-+]?\d+)?|\d+[eE][-+]?\d+'
    t.value = float(t.value)
    return t

  
def t_NUMBER(t):
    r'\b\d+\b'
    t.value = int(t.value)
    return t

def t_STRING_LITERAL(t):
    r'\"([^\\\n]|(\\.))*?\"|\'([^\\\n]|(\\.))*?\''
    t.value = t.value[1:-1]
    return t
  
def t_CHARACTER_LITERAL(t):
    r'\'[^\']\''
    t.value = t.value[1:-1]
    return t
  
def t_BOOLEAN_LITERAL(t):
    r'\btrue\b|\bfalse\b'
    return t

def t_OUTPUT(t):
    r'\boutput\b'
    return t
  
def t_INPUT(t):
    r'\binput\b'
    return t

def t_IN(t):
    r'\bin\b'
    return t
  
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

# Ignorar espacios en blanco
t_ignore = ' \t'

# Definir un contador de líneas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    
# Definir comentarios
def t_COMMENT(t):
    r'\{[^}]*\}|\(\*[^*]*\*\)'
    pass
  
def t_comment_multiline(t):
    r'\(\*[^*]*\*\)'
    pass
  
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1) 
    
# Construir el lexer
def test(data, lexer):
	lexer.input(data)
	while True:
		tok = lexer.token()
		if not tok:
			break
		print (tok)

lexer = lex.lex()


if __name__ == '__main__':
	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'test.pas'
	f = open(fin, 'r')
	data = f.read()
	print (data)
	lexer.input(data)
	test(data, lexer)