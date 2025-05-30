program SemanticErrors;

var
  x: integer;
  y: real;
  square: integer;

function square(a: integer): integer;
begin
  square := a * a;
end;

begin
  x := 'hello';               { Error semántico: asignación de string a integer }
  y := square(3.5);           { Error semántico: paso de real a una función que espera integer }
  writeln(z);                { Error semántico: variable 'z' no declarada }
  y := x / 0;                { Error semántico: división por cero (aunque algunos compiladores lo permiten hasta tiempo de ejecución) }
  x := true;                 { Error semántico: asignación de boolean a integer }
end.
