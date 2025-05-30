class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def define(self, name, symbol_type):
        if name in self.symbols:
            raise Exception(f"Error semantico: Identificador '{name}' ya definido.")
        self.symbols[name] = symbol_type

    def lookup(self, name):
        if name not in self.symbols:
            raise Exception(f"Error semantico: Identificador '{name}' no definido.")
        return self.symbols[name]
