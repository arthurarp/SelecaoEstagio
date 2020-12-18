# **Seleção Estágio PF/GIFOR**

Candidato: Arthur Alves Rodrigues Pinto


## **Problema 01**
Dado uma lista de dicionários (chave/valor) Python, verifique se existe a chave 'nome', e caso exista, salve o valor dessa chave em uma segunda lista, de modo que não haja repetição de valores na segunda lista.

### **Explicação**
Criei uma lista de dicionários com dados de exemplo.
Depois rodei um loop nessa lista e se o elemento em questão, que é um dicionário, tiver uma chave 'nome', o valor dessa chave é adicionado a uma 'lista' auxiliar.
Essa lista auxiliar na verdade é uma estrutura de dados chamada **set** e optei por usá-la, pois ela não permite a adição de valores iguais.


## **Problema 02**

Dado um arquivo csv com delimitador ';' e com o seguinte cabeçalho: id;nome;telefone;idade. 
Retorne uma lista com os registro ordenados por nome.
Exemplo de arquivo:
Id;nome;telefone;idade
1;João;43383832;28
2;Maria;43839322;32
.
.
.
N;Zzzz;99999999;12

### **Explicação**

Optei por utilizar a biblioteca pandas, muito usada em análise de dados, pois já tenho um certo conhecimento e para facilitar a resolução do problema. Criei uma função chamada sort_by_name() que retorna uma lista de dicionários em ordem alfabética. Essa biblioteca é bastante rica, pois ela possui os métodos para leitura de arquivo .csv, para ordenar os valores e transformar de pandas DataFrame, que é o tipo utilizado na biblioteca, para uma lista tradicional no python.
