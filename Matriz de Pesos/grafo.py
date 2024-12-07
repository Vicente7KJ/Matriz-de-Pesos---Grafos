# Representação de Grafo com Matriz de Pesos
class Grafo:
    def __init__(self):
        self.n = 0  # Número de vértices
        self.matriz_pesos = []  # Matriz de pesos

    def read(self, arquivo):
        """Lê um arquivo de grafo no formato especificado."""
        try:
            with open(arquivo, "r") as file:
                linhas = file.readlines()
                self.n = int(linhas[0].strip())  # Número de vértices
                
                # Inicializa a matriz de pesos com zeros (grafo sem arestas inicialmente)
                self.matriz_pesos = [[0 for _ in range(self.n)] for _ in range(self.n)]
                
                # Preenche a matriz com os pesos das arestas
                for linha in linhas[1:]:
                    # Divide os valores independentemente de tabulação ou espaço
                    x, y, z = map(float, linha.strip().split())
                    x, y = int(x), int(y)  # Convertendo para inteiros
                    self.matriz_pesos[x - 1][y - 1] = z
                    self.matriz_pesos[y - 1][x - 1] = z  # Grafo não direcionado
                
                print("Arquivo lido com sucesso!")
        except FileNotFoundError:
            print(f"Erro: O arquivo '{arquivo}' não foi encontrado.")
        except Exception as e:
            print(f"Erro ao ler o arquivo: {e}")

    def show(self):
        """Exibe a matriz de pesos do grafo."""
        print("\nMatriz de Pesos:")
        for linha in self.matriz_pesos:
            print(" ".join(f"{peso:.2f}" for peso in linha))

if __name__ == "__main__":
    import sys
    
    # Instância do grafo
    grafo = Grafo()
    
    # Entrada e comandos interativos
    print("Digite os comandos (exemplo: read arquivo.g ou show):")
    while True:
        comando = input("> ").strip().split()
        if len(comando) == 0:
            continue
        
        if comando[0] == "read" and len(comando) == 2:
            grafo.read(comando[1])
        elif comando[0] == "show":
            grafo.show()
        elif comando[0] == "exit":
            print("Saindo...")
            break
        else:
            print("Comando inválido! Use: read <arquivo.g>, show ou exit.")
