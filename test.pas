program Simple;

var
  a, b, c, z: integer;
  promedio: real;

begin
  a := 7;
  b := 9;
  c := 8;
  promedio := (a + b + c) / 3 + z;
  
  if promedio > 7.0 then
    writeln('Aprobado')
  else
    writeln('Reprobado');

  while promedio > 5.0 do
  begin
    promedio := promedio - 1.0;
    writeln('Reduciendo promedio: ', promedio);
  end;
end.