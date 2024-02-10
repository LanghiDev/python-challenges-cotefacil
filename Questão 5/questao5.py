#   Passo a passo para a contrução da Estrutura de dados ÁRVORE
#       CONCEITO de Árvore:
#           - Mantém os dados organizados de forma hierárquica, de maneira flexível e poderosa
#           - Essa estrutura pode ser aplicada em vários cenários, como:
#               • Organização Hierárquica de uma Empresa
#               • Sistema de Arquivos
#               • Árvores de Decisão em Machine Learning
#               • ...entre outros.
#
#   Esta aplicação toma como exemplo uma organização hierárquica de uma empresa.
#       Ex.: (CEO, CTO, Diretores, etc...)

# Definindo a classe TreeNode, que representa um nó da árvore.
#       - Um nó é uma unidade básica que compõe uma estrutura complexa.
#       - Este nó contém dados e pode ter referências ou ligações para outros nós, formando assim uma estrutura mais ampla (como uma árvore com raízes e vários galhos).
class TreeNode:
    # Este método construtor cria o nó com dados e uma lista de filhos vazia
    def __init__(self, data):
        self.data = data    # No exemplo deste script, este atributo receberia o cargo da pessoa na empresa.
        self.children = []  # Lista de filhos vazia. Sua alimentação é explicado a seguir:

    # Este método adiciona um nó filho à lista de filhos. Neste exemplo, receberia os cargos que estão debaixo, sob o comando do nó atual.
    def add_child(self, child_node):
        self.children.append(child_node)

# Definindo a classe Tree, que representa a árvore como um todo.
class Tree:
    # Este método construtor cria a árvore com um nó raiz (que está acima de todos na hierarquia)
    def __init__(self, root):
        self.root = root

    # Método para exibir a árvore
    def __str__(self):
        return self.display_tree(self.root, 0)

    # Método que organiza a exibição da árvore de forma hierarquica e sua estrutura.
    def display_tree(self, node, level):
        # Constrói a representação do nó atual com base no nível da árvore
        result = f'{"   -- " * level}{node.data}\n'
        # Percorre os filhos do nó atual.
        for child in node.children:
            result += self.display_tree(child, level + 1)
        return result

# TESTES UNITÁRIOS
# Criando instâncias dos nós (representando os cargos na empresa)
ceo = TreeNode("CEO") # (Chief Executive Officer)
cto = TreeNode("CTO") # (Chief Technology Officer)
cfo = TreeNode("CFO") # (Chief Financial Officer)
coo = TreeNode("COO") # (Chief Operating Officer)
dev_director = TreeNode("Diretor de Desenvolvimento")
research_director = TreeNode("Diretor de Pesquisa")
intl_operations_director = TreeNode("Diretor de Operações Internacionais")
natl_operations_director = TreeNode("Diretor de Operações Nacionais")

# Adicionando certos nós como filhos de outros nós (construindo a hierarquia da empresa)
ceo.add_child(cto)
ceo.add_child(cfo)
ceo.add_child(coo)

cto.add_child(dev_director)
cto.add_child(research_director)

coo.add_child(intl_operations_director)
coo.add_child(natl_operations_director)

# Construindo a árvore toda utilizando como raíz o nó "CEO"
company_tree = Tree(ceo)

print(company_tree)
