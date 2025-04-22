program project1;
const
  y = 'X';

var
  i, x : byte;
 
  procedure writeln_n_times(x : char; n : byte);
  var
    i : byte;
  begin
    for i := 1 to n do
      write(x);
    writeln('hola');
  end;

begin
  write('Ievadiet veselu skaitli: ');
  readln(x);

  for i := x downto 1 do
    writeln_n_times(y, i);
end.