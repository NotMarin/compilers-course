program TestParser;

var
  x, y: integer;
  z: boolean;

begin
  x := 5;
  y := 10;
  z := true;

  if x < y then
    x := x + 1
  else
    x := x - 1;

  while x < 20 do
  begin
    x := x + 2;
  end;

end.
