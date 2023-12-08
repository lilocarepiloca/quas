class Produto:
    def __init__(self):
        self.nome = input("Digite o nome do produto: ")
        self.preco = float(input("Digite o preço do produto: "))
        self.quantidade_estoque = int(input("Digite a quantidade em estoque do produto: "))

    def atualizar_estoque(self, quantidade):
        if quantidade >= 0:
            self.quantidade_estoque += quantidade
            print(f"Estoque atualizado: {self.quantidade_estoque}")
        else:
            print("A quantidade de estoque a ser atualizada deve ser maior ou igual a zero.")

# Criando uma instância da classe Produto
produto = Produto()

# Exibindo informações do produto
print(f"Nome do Produto: {produto.nome}")
print(f"Preço do Produto: R${produto.preco:.2f}")
print(f"Quantidade em Estoque: {produto.quantidade_estoque}")

# Solicitando a quantidade para atualizar o estoque
quantidade_atualizacao = int(input("Digite a quantidade para atualizar o estoque: "))
produto.atualizar_estoque(quantidade_atualizacao)

