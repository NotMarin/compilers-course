program TestPascal;

const
  PI = 3.14;
  MAX = 100;

var
  i, sum: integer;
  radius: real;
  name: string;

procedure PrintResult(value: integer);
begin
  writeln('Resultado: ', value);
end;

begin
  sum := 0;
  for i := 1 to MAX do
  begin
    sum := sum + i;
  end;

  writeln('Suma de 1 a ', MAX, ' es: ', sum);

  write('Ingresa el radio del círculo: ');
  readln(radius);
  writeln('Área del círculo: ', PI * radius);

  write('Ingresa tu nombre: ');
  readln(name);
  writeln('Hola, ', name);

  PrintResult(sum);
end.