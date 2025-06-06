from typing import Iterable, Set, Tuple
import heapq
from itertools import count
import time

class Nodo:
    """
    Implemente a classe Nodo com os atributos descritos na funcao init
    """
    def __init__(self, estado:str, pai:'Nodo', acao:str, custo:int):
        """
        Inicializa o nodo com os atributos recebidos
        :param estado:str, representacao do estado do 8-puzzle
        :param pai:Nodo, referencia ao nodo pai, (None no caso do nó raiz)
        :param acao:str, acao a partir do pai que leva a este nodo (None no caso do nó raiz)
        :param custo:int, custo do caminho da raiz até este nó
        """
        # substitua a linha abaixo pelo seu codigo
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.custo = custo


    def __eq__(self, other):
        return isinstance(other, Nodo) and self.estado == other.estado

    def __hash__(self):
        return hash(self.estado)


def swap(s: str, i: int, j: int) -> str:
    string_list = list(s)
    string_list[i], string_list[j] = string_list[j], string_list[i]
    return ''.join(string_list)



def sucessor(estado:str)->Set[Tuple[str,str]]:
    """
    Recebe um estado (string) e retorna um conjunto de tuplas (ação,estado atingido)
    para cada ação possível no estado recebido.
    Tanto a ação quanto o estado atingido são strings também.
    :param estado:
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    position = estado.index("_")

    row = position // 3
    col = position % 3

    sucessores: Set[Tuple[str, str]] = set()

    if row != 0:
        sucessores.add(("acima", swap(estado, position, position-3)))

    if row != 2:
        sucessores.add(("abaixo", swap(estado, position, position+3)))

    if col != 0:
        sucessores.add(("esquerda", swap(estado, position, position-1)))

    if col != 2:
        sucessores.add(("direita", swap(estado, position, position+1)))


    return sucessores


def expande(nodo:Nodo)->Set[Nodo]:
    """
    Recebe um nodo (objeto da classe Nodo) e retorna um conjunto de nodos.
    Cada nodo do conjunto é contém um estado sucessor do nó recebido.
    :param nodo: objeto da classe Nodo
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    sucessores = sucessor(nodo.estado)

    vizinhos = set()
    for suc in sucessores:
        vizinhos.add(Nodo(estado=suc[1], pai=nodo, acao=suc[0], custo=nodo.custo+1))

    return vizinhos



def caminho(v:Nodo)->list[str]:
    
    acoes = []

    while v.acao:
        acoes.append(v.acao)
        v = v.pai

    return list(reversed(acoes))



def hamming(estado:str) -> int:
    objetivo = "12345678_"
    return sum(1 for i in range(9) if estado[i] != objetivo[i] and estado[i] != '_')



def astar_hamming(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    visitados = set()
    fronteira = []
    expandidos = 0
    start = time.time()

    #raiz
    contador = count()
    raiz = Nodo(estado, None, None, 0)
    heapq.heappush(fronteira, (hamming(estado), next(contador), raiz))

    while fronteira:
        _, _, v = heapq.heappop(fronteira)
        
        if v.estado == "12345678_":
            print("Tempo:", time.time() - start, "segundos")
            print("Nós expandidos:", expandidos)
            print("Custo da solução:", v.custo)
            return caminho(v)

        if v.estado not in visitados:
            visitados.add(v.estado)

            expandidos+=1
            for vizinho in expande(v):
                if vizinho.estado not in visitados:
                    heapq.heappush(fronteira, (vizinho.custo+hamming(vizinho.estado), next(contador), vizinho))

    return None



def manhattan(estado:str) -> int:
    objetivo = "12345678_"
    distance = 0

    for position, c in enumerate(estado):
        if c != '_':
            row = position // 3
            col = position % 3
            obj_row = (int(c)-1) // 3
            obj_col = (int(c)-1) % 3
            distance += abs(row-obj_row)+abs(col-obj_col)

    return distance


def astar_manhattan(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    visitados = set()
    fronteira = []
    expandidos = 0
    start = time.time()

    #raiz
    contador = count()
    raiz = Nodo(estado, None, None, 0)
    heapq.heappush(fronteira, (manhattan(estado), next(contador), raiz))

    while fronteira:
        _, _, v = heapq.heappop(fronteira)
        
        if v.estado == "12345678_":
            print("Tempo:", time.time() - start, "segundos")
            print("Nós expandidos:", expandidos)
            print("Custo da solução:", v.custo)
            return caminho(v)

        if v.estado not in visitados:
            visitados.add(v.estado)

            expandidos+=1
            for vizinho in expande(v):
                if vizinho.estado not in visitados:
                    heapq.heappush(fronteira, (vizinho.custo+manhattan(vizinho.estado), next(contador), vizinho))

    return None


#opcional,extra
def bfs(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca em LARGURA e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    visitados = set()
    fronteira = []
    expandidos = 0
    start = time.time()

    raiz = Nodo(estado, None, None, 0)
    fronteira.append(raiz)

    while fronteira:
        v = fronteira.pop(0)

        if v.estado == "12345678_":
            print("Tempo:", time.time() - start, "segundos")
            print("Nós expandidos:", expandidos)
            print("Custo da solução:", v.custo)
            return caminho(v)

        if v.estado not in visitados:
            visitados.add(v.estado)

            expandidos+=1
            for vizinho in expande(v):
                if vizinho.estado not in visitados:
                    fronteira.append(vizinho)

    return None

#opcional,extra
def dfs(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca em PROFUNDIDADE e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    visitados = set()
    fronteira = []
    expandidos = 0
    start = time.time()

    raiz = Nodo(estado, None, None, 0)
    fronteira.append(raiz)

    while fronteira:
        v = fronteira.pop()

        if v.estado == "12345678_":
            print("Tempo:", time.time() - start, "segundos")
            print("Nós expandidos:", expandidos)
            print("Custo da solução:", v.custo)
            return caminho(v)

        if v.estado not in visitados:
            visitados.add(v.estado)

            expandidos+=1
            for vizinho in expande(v):
                if vizinho.estado not in visitados:
                    fronteira.append(vizinho)

    return None


def heuristic(estado:str) -> int:
    objetivo = "12345678_"
    return sum(1 for i in range(9) if estado[i] != '_' and objetivo[i] != '_' and abs(int(estado[i])-int(objetivo[i]))>1)

#opcional,extra
def astar_new_heuristic(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = sua nova heurística e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    visitados = set()
    fronteira = []
    expandidos = 0
    start = time.time()

    #raiz
    contador = count()
    raiz = Nodo(estado, None, None, 0)
    heapq.heappush(fronteira, (heuristic(estado), next(contador), raiz))

    while fronteira:
        _, _, v = heapq.heappop(fronteira)
        
        if v.estado == "12345678_":
            print("Tempo:", time.time() - start, "segundos")
            print("Nós expandidos:", expandidos)
            print("Custo da solução:", v.custo)
            return caminho(v)

        if v.estado not in visitados:
            visitados.add(v.estado)

            expandidos+=1
            for vizinho in expande(v):
                if vizinho.estado not in visitados:
                    heapq.heappush(fronteira, (vizinho.custo+manhattan(vizinho.estado), next(contador), vizinho))

    return None
