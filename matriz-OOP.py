import array


class Matrix:
    
    def __init__(self, n: int, m: int, valor: array):
        self.linhas = n
        self.colunas = m
        self.valor = array.array('d', valor)

    def zeros_like(self): 
        D=[0]*self.linhas*self.colunas
        return(Matrix(self.linhas, self.colunas, D))
    
    def add(self, B):
        D = self.zeros_like()
        for i in range(self.linhas * self.colunas):
            D.valor[i] = self.valor[i] + B.valor[i]
        return D

    def escal(self, alpha):
        D = self.zeros_like()
        for i in range(self.linhas * self.colunas):
            D.valor[i] = self.valor[i]*alpha
        return D

    def mostrar(self):
        for i in range(self.linhas):
            for j in range(self.colunas):
                print(self.valor[j + i*self.colunas], end=" ")
            print("\r")
        print("\r")

    def multiplicar(self, B):
        D = Matrix(self.linhas, B.colunas, [0]*self.linhas*self.colunas)
        for i in range(self.linhas):
            for j in range(B.colunas):
                for k in range(self.colunas):
                    D.valor[j+i*B.colunas] += self.valor[i*self.colunas + k] * B.valor[j + k*(B.colunas)]
        return D
    
    def tran(self):
        D = Matrix(self.colunas, self.linhas, [0]*len(self.valor))
        for i in range(self.linhas):
            for j in range(self.colunas):
                    D.valor[j*self.linhas+i] = self.valor[i*self.colunas + j]
        return D
    
    def quad(self):
        return self

class Quadrada(Matrix):
    
    def __init__(self, n: int, valor: array):
        self.linhas = n
        self.colunas = n
        self.valor = array.array('d', valor)
    
    def traco(self):  
        D = 0
        for i in range(0,self.linhas*self.linhas, self.linhas+1):
                    D += self.valor[i]
        return D

class TriangularInferior(Quadrada):

    def zeros_like(self):  
        D = TriangularInferior(self.linhas, [0]*len(self.valor))
        return D

    def tran(self):  
        D = TriangularSuperior(self.linhas, [0]*len(self.valor))
        for i in range(len(self.valor)):
                    D.valor[i] = self.valor[-i-1]
        return D
    
    def traco(self):  
        N = len(self.valor) - 1
        D = self.valor[-1]
        for n in range(2,self.linhas+1):
            N += -n
            D += self.valor[N]
        return D

    def det(self):  
        N = len(self.valor) - 1
        D = self.valor[-1]
        for n in range(2,self.linhas+1):
            N += -n
            D *= self.valor[N]
        return D
    
    def quad(self):
        counter = 0
        D = Quadrada(self.linhas, [0] * self.linhas ** 2)
        D = D.zeros_like()

        for i in range(self.linhas):
            for j in range(self.linhas):
                k = i * self.linhas + j
                
                if i >= j:
                    D.valor[k] = self.valor[counter]
                    counter += 1
                else:
                    D.valor[k] = 0
        
        return(D)
    
    def mostrar(self):
        D = self.quad()
        return(D.mostrar())
    
    def multiplicar(self, B):
        D = self.quad().multiplicar(B.quad())
        return(D.mostrar())    

class TriangularSuperior(Quadrada):

    def zeros_like(self):  
        D = TriangularSuperior(self.linhas, [0]*len(self.valor))
        return D

    def quad(self):
        counter = 0
        D = Quadrada(self.linhas, [0] * self.linhas ** 2)
        D = D.zeros_like()

        for i in range(self.linhas):
            for j in range(self.linhas):
                k = i * self.linhas + j
                
                if i <= j:
                    D.valor[k] = self.valor[counter]
                    counter += 1
                else:
                    D.valor[k] = 0
        
        return(D)
    
    def mostrar(self):
        D = self.quad()
        return(D.mostrar())
    
    def multiplicar(self, B):
        D = self.quad().multiplicar(B.quad())
        return(D.mostrar())

    def tran(self):  
        D = TriangularInferior(self.linhas, self.valor)
        return D

    def traco(self):  
        N = 0
        D = self.valor[0]
        for n in range(2,self.linhas+1):
            N += n
            D += self.valor[N]
        return D

    def det(self):  
        N = 0
        D = self.valor[0]
        for n in range(2,self.linhas+1):
            N += n
            D *= self.valor[N]
        return D
    
class Diagonal(Quadrada):
    
    def quad(self):
        D = Quadrada(self.linhas, [0] * self.linhas ** 2)
        
        for i in range(self.linhas):
            for j in range(self.linhas):
                k = i * self.linhas + j
                
                if i == j:
                    D.valor[k] = self.valor[i]
                else:
                    D.valor[k] = 0

        return(D)
    
    def mostrar(self):
        D = self.quad()
        return (D.mostrar())
    
    def traco(self):
        traco = 0
        for i in self.valor:
            traco += i 
        return (traco)
    
    def det(self):
        determinante = 1
        for i in self.valor:
            determinante *= i
        return(determinante)
    
    def tran(self):
        return(self)
    
    def multiplicar(self, B):
        D = self.quad().multiplicar(B.quad())
        return(D)
            
#-------------------------------------------------------------------------------------------------#
def T_matriz(a):
    a= a.split(",")
    try:
        for i in range(len(a)):
            a[i] = float(a[i])
    except:
        print("erro inesperado, favor checar se todos os itens são")
    return(a)

def soma(matriz_A,matriz_B):
    if matriz_B.linhas == matriz_A.linhas and matriz_B.colunas == matriz_A.colunas:
        if type(matriz_A) == type(matriz_B):
            return(matriz_A.add(matriz_B).mostrar())
        else:
            A = matriz_A.quad()
            B = matriz_B.quad()
            return(A.add(B).mostrar())
    else:
        print("essas matrizes não podem ser adicionadas, elas precisam ter o mesmo numero de linhas e colunas")

def subtrai(matriz_A,matriz_B):
    matriz_B = matriz_B.escal(-1)
    return(soma(matriz_A, matriz_B))

def multiplica(matriz_A, matriz_B):
    if matriz_B.colunas == matriz_A.linhas:
        if type(matriz_A) == type(matriz_B):
            return(matriz_A.multiplicar(matriz_B).mostrar())
        else:
            A = matriz_A.quad()
            B = matriz_B.quad()
            return(A.multiplicar(B).mostrar())
    else:
        print("essas matrizes não podem ser multiplicadas, o numero de linhas da primeira deve ser igual o numero de colunas da segunda")

def menu_1():
    print('bem-vindo à calculadora matricial, para continuar escolha uma opção:')
    print(' [0]-sair \n','[1]-Adicionar uma matriz')

def menu_2(matriz_A):
    while True:
        print('[0]-retornar \n','[1]-mostrar matriz\n','[2]-somar com outra matriz\n','[3]-subtrair por outra matriz\n',
          '[4]-multiplicar por escalar\n','[5]-multiplicar por outra matriz\n','[6]-matriz transposta\n',
          '[7]-traço(apenas quadradas)\n','[8]-determinante(apenas triangulares, incluido diagonais)\n')
        escolha = input()
        
        if escolha == '0':
            break

        elif escolha == '1':
            try:
                matriz_A.mostrar()
            except:
                print("ocorreu um erro inesperado, tente reinserir a matriz")
        
        elif escolha == '2':
            soma(matriz_A,segunda_matriz() )
        
        elif escolha == '3':
            subtrai(matriz_A, segunda_matriz())
        
        elif escolha == '4':
            try:
                escalar = float(input("insira um escalar para ser multiplicado"))
            except:
                print("favor escolher um numero válido")
            
            try:
                print(matriz_A.escal(escalar).mostrar())
            except:
                print("ocorreu um erro inesperado, tente reinserir a matriz")

        elif escolha == '5':
            multiplica(matriz_A, segunda_matriz())
        
        elif escolha == '6':
            try:
                matriz_A.transposta().mostrar()
            except:
                print("ocorreu um erro inesperado, tente reinserir a matriz")
        
        elif escolha == '7':
            try:
                print(matriz_A.traco())
            except:
                print('esta operação não está disponivel para este tipo de matriz ou ocorreu um erro inesperado')
        
        elif escolha == '8':
            try:
                print(matriz_A.det())
            except:
                print('esta operação não está disponivel para este tipo de matriz ou ocorreu um erro inesperado') 
        
        else:
            print("favor inserir uma opção válida")

def tipo_escolha():
    print("Qual tipo de matriz gostaria de inserir?")
    while True:
        
        print(' [0]-retornar \n','[1]-Quadrada\n','[2]-Triangular inferior\n','[3]-Triangular superior\n','[4]-Diagonal\n',
              '[5]-Outro')
        
        escolha_1 = input()
        
        if escolha_1 == '0':
            break

        elif escolha_1 == '1':
            tipo_quadrada()
        
        elif escolha_1 == '2':
            tipo_tri_inf()
        
        elif escolha_1 == '3':
            tipo_tri_sup()
        
        elif escolha_1 == '4':
            tipo_diagonal()
        
        elif escolha_1 == '5':
            tipo_outro()
        
        else:
            print("favor inserir uma opção válida")

def tipo_quadrada():
    try:
        tamanho =int(input("insira o tamanho da matriz quadrada como um numero inteiro\n"))
    except:
        print("favor inserir um numero inteiro como tamaho")
    
    print("insira uma matriz no formato sugerido ou escreva 'sair' para sair")
    print('|a b c|\n|d e f|\n|g h i|\n seria escrita como: a, b, c, d, e, f, g, h, i')
    lista = input()
    if lista == 'sair':
        return(None)
    
    else:
        matriz_inicial = T_matriz(lista)
    
    try:
        matriz_inicial = Quadrada(tamanho, matriz_inicial)
        menu_2(matriz_inicial)
    except:
        print("favor inserir uma matriz válida")
    
def tipo_outro():
    try:
        linhas =int(input("insira o numero de linhas da matriz quadrada como um numero inteiro\n"))
    except:
        print("favor inserir um numero inteiro como numero de linhas")
    
    try:
        colunas =int(input("insira o numero de colunas da matriz quadrada como um numero inteiro\n"))
    except:
        print("favor inserir um numero inteiro como numero de colunas")
    
    print("insira uma matriz no formato sugerido ou escreva 'sair' para sair")
    print('|a b c|\n|d e f|\n|g h i|\n seria escrita como: a, b, c, d, e, f, g, h, i')
    lista = input()
    if lista == 'sair':
        return(None)
    
    else:
        matriz_inicial = T_matriz(lista)
    
    try:
        matriz_inicial = Matrix(linhas, colunas, matriz_inicial)
        menu_2(matriz_inicial)
    except:
        print("favor inserir uma matriz válida")
    
def tipo_tri_sup():
    try:
        tamanho =int(input("insira o tamanho da matriz quadrada como um numero inteiro\n"))
    except:
        print("favor inserir um numero inteiro como tamaho")
    
    print("insira uma matriz no formato sugerido ou escreva 'sair' para sair")
    print('|a b c|\n|d e 0|\n|f 0 0|\n seria escrita como: a, b, c, d, e, f')
    lista = input()
    if lista == 'sair':
        return(None)
    
    else:
        matriz_inicial = T_matriz(lista)
    
    try:
        matriz_inicial = TriangularSuperior(tamanho, matriz_inicial)
        menu_2(matriz_inicial)
    except:
        print("favor inserir uma matriz válida")

def tipo_tri_inf():
    try:
        tamanho =int(input("insira o tamanho da matriz quadrada como um numero inteiro\n"))
    except:
        print("favor inserir um numero inteiro como tamaho")
    
    print("insira uma matriz no formato sugerido ou escreva 'sair' para sair")
    print('|a 0 0|\n|b c 0|\n|d e f|\n seria escrita como: a, b, c, d, e, f')
    lista = input()
    if lista == 'sair':
        return(None)
    
    else:
        matriz_inicial = T_matriz(lista)
    
    try:
        matriz_inicial = TriangularSuperior(tamanho, matriz_inicial)
        menu_2(matriz_inicial)
    except:
        print("favor inserir uma matriz válida")

def tipo_diagonal():
    try:
        tamanho =int(input("insira o tamanho da matriz quadrada como um numero inteiro\n"))
    except:
        print("favor inserir um numero inteiro como tamaho")
    
    print("insira uma matriz no formato sugerido ou escreva 'sair' para sair")
    print('|a 0 0|\n|0 b 0|\n|0 0 c|\n seria escrita como: a, b, c')
    lista = input()
    if lista == 'sair':
        return(None)
    
    else:
        matriz_inicial = T_matriz(lista)
    
    try:
        matriz_inicial = Diagonal(tamanho, matriz_inicial)
        menu_2(matriz_inicial)
    except:
        print("favor inserir uma matriz válida")

def init():
    while True:
        menu_1()
        escolha = input()
        if escolha == '0':
            break
        elif escolha == '1':
            print("Qual tipo de matriz gostaria de inserir?")
            tipo_escolha()
        else:
            print("favor inserir uma opção válida")

def tipo_quadrada2():
    try:
        tamanho =int(input("insira o tamanho da matriz quadrada como um numero inteiro\n"))
    except:
        print("favor inserir um numero inteiro como tamaho")
    
    print("insira uma matriz no formato sugerido ou escreva 'sair' para sair")
    print('|a b c|\n|d e f|\n|g h i|\n seria escrita como: a, b, c, d, e, f, g, h, i')
    lista = input()
    if lista == 'sair':
        return(None)
    
    else:
        matriz_inicial = T_matriz(lista)
    
    try:
        matriz_inicial = Quadrada(tamanho, matriz_inicial)
        return(matriz_inicial)
    except:
        print("favor inserir uma matriz válida")

def tipo_outro2():
    try:
        linhas =int(input("insira o numero de linhas da matriz quadrada como um numero inteiro\n"))
    except:
        print("favor inserir um numero inteiro como numero de linhas")
    
    try:
        colunas =int(input("insira o numero de colunas da matriz quadrada como um numero inteiro\n"))
    except:
        print("favor inserir um numero inteiro como numero de colunas")
    
    print("insira uma matriz no formato sugerido ou escreva 'sair' para sair")
    print('|a b c|\n|d e f|\n|g h i|\n seria escrita como: a, b, c, d, e, f, g, h, i')
    lista = input()
    if lista == 'sair':
        return(None)
    
    else:
        matriz_inicial = T_matriz(lista)
    
    try:
        matriz_inicial = Matrix(linhas, colunas, matriz_inicial)
        return(matriz_inicial)
    except:
        print("favor inserir uma matriz válida")

def tipo_tri_sup2():
    try:
        tamanho =int(input("insira o tamanho da matriz quadrada como um numero inteiro\n"))
    except:
        print("favor inserir um numero inteiro como tamaho")
    
    print("insira uma matriz no formato sugerido ou escreva 'sair' para sair")
    print('|a b c|\n|d e 0|\n|f 0 0|\n seria escrita como: a, b, c, d, e, f')
    lista = input()
    if lista == 'sair':
        return(None)
    
    else:
        matriz_inicial = T_matriz(lista)
    
    try:
        matriz_inicial = TriangularSuperior(tamanho, matriz_inicial)
        return(matriz_inicial)
    except:
        print("favor inserir uma matriz válida")

def tipo_tri_inf2():
    try:
        tamanho =int(input("insira o tamanho da matriz quadrada como um numero inteiro\n"))
    except:
        print("favor inserir um numero inteiro como tamaho")
    
    print("insira uma matriz no formato sugerido ou escreva 'sair' para sair")
    print('|a 0 0|\n|b c 0|\n|d e f|\n seria escrita como: a, b, c, d, e, f')
    lista = input()
    if lista == 'sair':
        return(None)
    
    else:
        matriz_inicial = T_matriz(lista)
    
    try:
        matriz_inicial = TriangularSuperior(tamanho, matriz_inicial)
        return(matriz_inicial)
    except:
        print("favor inserir uma matriz válida")

def tipo_diagonal2():
    try:
        tamanho =int(input("insira o tamanho da matriz quadrada como um numero inteiro\n"))
    except:
        print("favor inserir um numero inteiro como tamaho")
    
    print("insira uma matriz no formato sugerido ou escreva 'sair' para sair")
    print('|a 0 0|\n|0 b 0|\n|0 0 c|\n seria escrita como: a, b, c')
    lista = input()
    if lista == 'sair':
        return(None)
    
    else:
        matriz_inicial = T_matriz(lista)
    
    try:
        matriz_inicial = Diagonal(tamanho, matriz_inicial)
        return(matriz_inicial)
    except:
        print("favor inserir uma matriz válida")

def segunda_matriz():
    print("Qual tipo de matriz gostaria de inserir?")
    while True:
        
        print(' [0]-retornar \n','[1]-Quadrada\n','[2]-Triangular inferior\n','[3]-Triangular superior\n','[4]-Diagonal\n',
              '[5]-Outro')
        
        escolha_1 = input()
        
        if escolha_1 == '0':
            break

        elif escolha_1 == '1':
            return(tipo_quadrada2())
        
        elif escolha_1 == '2':
            return(tipo_tri_inf2())
        
        elif escolha_1 == '3':
            return(tipo_tri_sup2())
        
        elif escolha_1 == '4':
            return(tipo_diagonal2())
        
        elif escolha_1 == '5':
            return(tipo_outro2())
        
        else:
            print("favor inserir uma opção válida")

init()