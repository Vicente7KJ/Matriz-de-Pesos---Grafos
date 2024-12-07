# Matriz-de-Pesos---Grafos


Este projeto consiste em uma implementação em Python para a representação e manipulação de grafos utilizando a matriz de pesos 
como estrutura de dados. 
A aplicação permite carregar grafos a partir de arquivos formatados, 
exibir sua matriz de pesos e realizar outras operações úteis para a análise de grafos.

*** Funcionalidades ***

Leitura de grafos a partir de arquivos:

O comando read <arquivo> permite carregar um grafo descrito em um arquivo no formato especificado.
O arquivo contém o número de vértices e as arestas com seus respectivos pesos.

*** Exibição da Matriz de Pesos *** :

O comando show -mw exibe a matriz de pesos do grafo carregado.
Verificação de erros no arquivo de entrada:

O programa detecta problemas como linhas vazias ou formatação incorreta.
Formato do Arquivo de Entrada
O arquivo de entrada deve estar formatado da seguinte maneira:

A primeira linha indica o número de vértices (𝑛 n).
As linhas subsequentes definem as arestas no formato: x y z
onde x, y: são os vértices conectados por uma aresta.
z: é o peso (valor numérico positivo) da aresta.

*** Como Executar ***
° Certifique-se de ter o Python instalado (versão 3.6 ou superior).
° Clone este repositório:

git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

° Executando o programa: python grafo.py

utilize os seguintes comandos no terminal interativo:

read <nome-do-arquivo>: Carrega um grafo a partir do arquivo especificado. (arquivo inst-5 que está nesse repositório pode servir de exemplo)

show -mw: Exibe a matriz de pesos do grafo carregado.

Exemplo de Execução
Entrada: read inst-5
show -mw
