#implementação de algumas funções da árvore AVL

# Classe que representa um nó da árvore
class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
        self.altura = 1
# Classe que representa a árvore AVL
class AVL:
    def __init__(self):
        self.raiz = None
   #Função para calcular a altura de um nó
    def altura(self, no):
        if no is None:
            return 0
        return no.altura
    # Função para calcular o fator de balanceamento de um nó
    def fator_balanceamento(self, no):
        if no is None:
            return 0
        return self.altura(no.esquerda) - self.altura(no.direita)
    # Função para realizar uma rotação à esquerda
    def rotacao_esquerda(self, no):
        no_direita = no.direita
        no_direita_esquerda = no_direita.esquerda

        no_direita.esquerda = no
        no.direita = no_direita_esquerda 

        no.altura = 1 + max(self.altura(no.esquerda), self.altura(no.direita))
        no_direita.altura = 1 + max(self.altura(no_direita.esquerda), self.altura(no_direita.direita))

        return no_direita
    # Função para realizar uma rotação à direita
    def rotacao_direita(self, no):
        no_esquerda = no.esquerda
        no_esquerda_direita = no_esquerda.direita

        no_esquerda.direita = no
        no.esquerda = no_esquerda_direita

        no.altura = 1 + max(self.altura(no.esquerda), self.altura(no.direita))
        no_esquerda.altura = 1 + max(self.altura(no_esquerda.esquerda), self.altura(no_esquerda.direita))# atualiza a altura do nó

        return no_esquerda
    # Função para inserir um nó na árvore
    def inserir(self, raiz, valor):
        if raiz is None:
            return No(valor)
        elif valor < raiz.valor:# se o valor for menor que o valor do nó
            raiz.esquerda = self.inserir(raiz.esquerda, valor)
        else:
            raiz.direita = self.inserir(raiz.direita, valor)

        raiz.altura = 1 + max(self.altura(raiz.esquerda), self.altura(raiz.direita))

        fator_balanceamento = self.fator_balanceamento(raiz)

        if fator_balanceamento > 1 and valor < raiz.esquerda.valor:# se o fator de balanceamento for maior que 1 e o valor for menor que o valor do nó
            return self.rotacao_direita(raiz)

        if fator_balanceamento < -1 and valor > raiz.direita.valor:# se o fator de balanceamento for menor que -1 e o valor for maior que o valor do nó
            return self.rotacao_esquerda(raiz)

        if fator_balanceamento > 1 and valor > raiz.esquerda.valor:# se o fator de balanceamento for maior que 1 e o valor for maior que o valor do nó
            raiz.esquerda = self.rotacao_esquerda(raiz.esquerda)
            return self.rotacao_direita(raiz)
        
        if fator_balanceamento < -1 and valor < raiz.direita.valor:# se o fator de balanceamento for menor que -1 e o valor for menor que o valor do nó
            raiz.direita = self.rotacao_direita(raiz.direita)
            return self.rotacao_esquerda(raiz)

        return raiz

    # Função para remover um nó da árvore
    def remover(self, raiz, valor):
        if raiz is None:# se a raiz for vazia
            return raiz

        elif valor < raiz.valor:# se o valor for menor que o valor do nó
            raiz.esquerda = self.remover(raiz.esquerda, valor)

        elif valor > raiz.valor:
            raiz.direita = self.remover(raiz.direita, valor)

        else:# se o valor for igual ao valor do nó
            if raiz.esquerda is None:
                no_direita = raiz.direita
                raiz = None
                return no_direita

            elif raiz.direita is None:# se o nó não tiver filho a direita
                no_esquerda = raiz.esquerda
                raiz = None
                return no_esquerda

            no_menor = self.menor_valor(raiz.direita)# se o nó tiver dois filhos
            raiz.valor = no_menor.valor
            raiz.direita = self.remover(raiz.direita, no_menor.valor)

        if raiz is None:# se a raiz for vazia
            return raiz

        raiz.altura = 1 + max(self.altura(raiz.esquerda), self.altura(raiz.direita))

        fator_balanceamento = self.fator_balanceamento(raiz)

        if fator_balanceamento > 1 and self.fator_balanceamento(raiz.esquerda) >= 0:# se o fator de balanceamento for maior que 1 e o fator de balanceamento do filho a esquerda for maior ou igual a 0
            return self.rotacao_direita(raiz)

        if fator_balanceamento < -1 and self.fator_balanceamento(raiz.direita) <= 0:# se o fator de balanceamento for menor que -1 e o fator de balanceamento do filho a direita for menor ou igual a 0
            return self.rotacao_esquerda(raiz)

        if fator_balanceamento > 1 and self.fator_balanceamento(raiz.esquerda) < 0:# se o fator de balanceamento for maior que 1 e o fator de balanceamento do filho a esquerda for menor que 0
            raiz.esquerda = self.rotacao_esquerda(raiz.esquerda)
            return self.rotacao_direita(raiz)

        if fator_balanceamento < -1 and self.fator_balanceamento(raiz.direita) > 0:# se o fator de balanceamento for menor que -1 e o fator de balanceamento do filho a direita for maior que 0
            raiz.direita = self.rotacao_direita(raiz.direita)
            return self.rotacao_esquerda(raiz)

        return raiz 
