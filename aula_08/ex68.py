# Implemente uma classe chamada "SafeDict" que estende a 
# funcionalidade de um dicionário comum. A classe deve
# aceitar um valor padrão a ser retornado caso a chave não
# exista no dicionário, em vez de lançar uma exceção
# KeyError.

def main():
    safedict = SafeDict(default_value=0)
    safedict['a'] = int(input("Escolha um número: "))
    safedict['b'] = int(input("Escolha um número: "))

    print(safedict['a']) 
    print(safedict['b'])  
    

class SafeDict(dict):
    def __init__(self, default_value, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.default_value = default_value

    def __getitem__(self, key):
        try:
            return super().__getitem__(key)
        except KeyError:
            return self.default_value      

if __name__ == "__main__":
    main()
    

    