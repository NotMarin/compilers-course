program OtroTest;

var
  a: integer;
  b: integer;  

begin
  a := 0;
  b := 1;

  repeat
    a := a + b;
    b := b + 1;
  until a > 10;

  if (a mod 2 = 0) then
    a := a div 2;

end.
