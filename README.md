# TEC502-DistriBank
🚧 Em construção: este projeto foi desenvolvido como parte da disciplina MI - Concorrência e Conectividade, do curso de
Engenharia de Computação da Universidade Estadual de Feira de Santana (UEFS).

## Sumário 
- Descrição do projeto
- Requisitos e funcionalidades do sistema
- Gerenciamento de contas 
  - Criação de contas
  - Tipos de contas
- Transações bancárias
  - Transações bancárias internas
  - Transações bancárias externas
  - Transações sequenciais
  - Transações concorrentes
- Comunicação entre servidores
  - Protocolo utilizado 
  - Rotas de comunicação
- Tratamento da concorrência
  - Algoritmo da concorrência distribuída
  - Operações atômicas
  - Operações simultâneas em um único servidor
- Tratamento da confiabilidade
  - Verificação de conexão 
  - Tratamento de erros
  - Retorno de conexão
- Docker
- Testes
- Execução do projeto
- Referências


## Descrição do projeto 

O projeto DistriBank é um sistema de transações bancárias distribuído, que permite a realização de transações entre
contas de diferentes bancos, sem a necessidade de um intermediário, que no cenário real seria o Banco Central. O sistema
é composto por vários servidores, cada um representando um banco, que se comunicam entre si para a realização das 
transações bancárias. Para o desenvolvimento do projeto, foi utilizado a linguagem de programação Python, com o framework
Flask para a criação de APIs, e a biblioteca requests para a comunicação entre os servidores. Por fim, o ambiente de 
desenvolvimento utilizado para criação do projeto foi o PyCharm, podendo ser executado em qualquer IDE de preferência
do usuário.


## Requisitos e funcionalidades do sistema

O sistema DistriBank foi desenvolvido para atender as seguintes funcionalidades:
- Criação de contas bancárias de pessoa física e jurídica;
- Realização de transações bancárias entre contas de diferentes bancos;
- Realização de transações bancárias internas entre contas do mesmo banco;
- Realização de transações bancárias sequenciais;
- Realização de transações bancárias concorrentes;
- Verificação de conexão entre os servidores;
- Tratamento de erros e retorno de conexão;
- Execução do sistema em containers Docker;


## Gerenciamento de contas

### Criação de contas

O sistema DistriBank permite a criação de contas bancárias de pessoa física e jurídica. Para a criação de uma conta, o
usuário deve informar os seguintes dados:





! ------------------------------------------------------------------------------------------------------------------- !

## FALTA A PARTE DA CONEXÃO, SALDO AUTOMÁTICO

## Gerenciamento de contas
- realiza a gestão de contas? cria e realiza transações?

- sim, o sistema faz a gestão de contas corretamente. os possíveis tipos de contas que podem ser criados são: conta
de pessoa física particular e conjunta, e conta de pessoa jurídica.
- na conta de pessoa física particular, o usuário entra com os seguintes dados: ... . 
- na conta de pessoa física conjunta, o usuário entra com os seguintes dados: ... . nesse caso, pode-se ter mais de
usuário acessando essa conta, tendo usuários e senha diferentes. esses usuários são diferenciados por seus cpfs, que
não podem ser iguais. o primeiro usuário, que cria a conta, é considerado como o titular.
- no caso da conta jurídica, o usuário entra com os seguintes dados: ... . nesse caso, o usuário pode ter mais de uma
conta jurídica, sendo diferenciadas por seus cnpjs, que não podem ser iguais. o prim

## Seleciona e realiza transações entre diferentes contas?
- É possível transacionar entre diferentes bancos? Por exemplo, enviar do 
banco A, B e C para o banco D?

## Comunicação entre servidores
- Os bancos estão se comunicando com o protocolo adequado?

## Sincronzação em um único servidor
- Como foi o tratamento da concorrencia num único servidor, quando 
chegam mais de um pedido de transação a um único servidor?

## Algoritmo da concorrência distribuída está teoricamente bem empregado?
- Qual algoritmo foi utilizado? está correto para a solução?

## Algoritmo está tratando o problema na prática?
- A implementação do algoritmo funciona corretamente?

## Tratamento da confiabilidade
- Quando um dos bancos perde a conexão, o sistema continua a funcionar
corretamente? E quando o banco retorna à conexão?

Como resolver essa parte?
- no dicionário, tem uma booleana se está online ou não
- thread que fica mandando mensagem toda hora e se houver erro, pega e muda no dicionário
- 

## Pelo menos uma transação concorrente é realizada?
- Como foi tratado o caso em que mais de duas transações ocorrem no mesmo
banco de forma concorrente? O saldo fica correto? Os clientes conseguem 
realizar as transações?

## Docker 

## Testes

## Documentação

