# TEC502-DistriBank
> Este projeto foi desenvolvido como parte da disciplina MI - Concorrência e Conectividade, do curso de
Engenharia de Computação da Universidade Estadual de Feira de Santana (UEFS). O nome "DistriBank" foi escolhido
> para representar um sistema de transações bancárias distribuído, que permite a realização de transações entre
> contas de diferentes bancos, sem a necessidade de um intermediário. 

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
contas de diferentes bancos, sem a necessidade de um intermediário, que no cenário real seria o Banco Central. 
O sistema é composto por vários servidores, cada um representando um banco, que se comunicam entre si para a 
realização das transações bancárias. Nos testes apresentados, são criadas 4 instâncias de servidores, que 
representam os bancos do consórcio, e cada servidor possui uma porta específica para a comunicação entre eles.
É importante ressaltar que o sistema pode utilizar mais de 4 servidores, desde que seja feita a configuração 
adequada para a comunicação entre eles.

Para o desenvolvimento do projeto, foi utilizado a linguagem de programação Python, com o framework Flask para a 
criação de APIs, e a biblioteca requests para a comunicação entre os servidores, que foi via HTTP. Por fim, 
o ambiente de desenvolvimento utilizado para criação do projeto foi o PyCharm, podendo ser executado em qualquer 
IDE de preferência do usuário.


## Requisitos e funcionalidades do sistema

O sistema DistriBank foi desenvolvido para atender as seguintes funcionalidades:
- Criação de contas bancárias de pessoa física e jurídica;
- Realização de transações bancárias entre contas de diferentes bancos;
- Realização de transações bancárias internas entre contas do mesmo banco;
- Realização de transações bancárias sequenciais;
- Realização de transações bancárias concorrentes;
- Verificação de conexão entre os servidores;
- Tratamento de erros e retorno de conexão;
- Execução do sistema em containers Docker.


## Gerenciamento de contas

### Criação de contas

O sistema DistriBank permite a criação de contas bancárias de pessoa física e jurídica. Para a criação de uma conta, o
usuário deve informar os seguintes dados: nome, CPF, usuário, senha e o valor inicial daquela conta. No caso de uma 
conta física particular, o valor mínimo exigido para a criação de conta no sistema é de R$ 100,00. 

Já para a criação de conta física conjunta, há duas opções: quando a pessoa vai abrir a conta, que cria a conta do 
titular (opção 2), ou quando a conta já existe e deseja-se adicionar um novo membro, que é a opção 3 (complementar).
No primeiro caso, segue a mesma lógica da conta de pessoa física particular, mas o limite mínimo exigido é de R$ 200,00.
No segundo caso, o usuário deve informar o CPF do titular da conta, e só depois entrar com seus dados pessoais, que 
são os mesmos da pessoa física particular, exceto pelo saldo, que nesse caso, não é informado.

Por fim, para a criação de conta jurídica, o usuário deve informar os seguintes dados: nome da empresa, CNPJ, e os
dados pessoais do usuário, como nome, CPF, usuário, senha e o valor inicial da conta. O valor mínimo exigido para a
criação de conta jurídica é de R$ 300,00. Nesse caso segue a mesma lógica da conta conjunta: o primeiro usuário que cria
a conta é dito como o "administrador", enquanto ou outros podem ser adicionados, utilizando o cnpj da empre para a busca
da conta e suas informações pessoais, com exceção, novamente, do saldo inicial.

As rotas para as criações das contas e suas respectivas respostas podem ser visualizadas abaixo.

### Tipos de contas

O sistema DistriBank permite a criação de três tipos de contas bancárias: pessoa física particular, pessoa física conjunta
e pessoa jurídica. Cada tipo de conta possui suas particularidades, como o valor mínimo exigido para a criação da conta,
e os dados necessários para a criação da conta. Abaixo, segue a descrição de cada tipo de conta:

- Pessoa física particular: é uma conta de pessoa física, onde o usuário entra com os seguintes dados: nome, CPF, usuário,
- senha e o valor inicial da conta. O valor mínimo exigido para a criação de conta de pessoa física particular é de R$ 100,00.
- Pessoa física conjunta: é uma conta de pessoa física, onde o usuário entra com os seguintes dados: nome, CPF, usuário,
- senha e o valor inicial da conta. O valor mínimo exigido para a criação de conta de pessoa física conjunta é de R$ 200,00.
- Pessoa jurídica: é uma conta de pessoa jurídica, onde o usuário entra com os seguintes dados: nome da empresa, CNPJ,
- e os dados pessoais do usuário, como nome, CPF, usuário, senha e o valor inicial da conta. O valor mínimo exigido para a
- criação de conta jurídica é de R$ 300,00.
- O sistema permite a criação de mais de uma conta jurídica, sendo diferenciadas por seus CNPJs, que não podem ser iguais.
- O primeiro usuário que cria a conta é considerado como o "administrador" da conta, e pode adicionar outros usuários à
- conta, utilizando o CNPJ da empresa para a busca da conta e suas informações pessoais, com exceção do saldo inicial.


## Algoritmo da concorrência distribuída

Para o tratamento da concorrência distribuída, o sistema faz uso do relógio vetorial junto com o algoritmo mulicast
totalmente ordenado. O algoritmo de multicast de ordenação com o uso do relógio vetorial é um algoritmo de 
concorrência distribuída que é responsável por garantir que as transações sejam realizadas de forma correta, 
sem que haja erros ou inconsistências nos saldos das contas. 

O relógio vetorial é utilizado para definir a posição das transações na fila de execução, de acordo com o seu 
tempo vetorial. A cada nova transação, o relógio vetorial é incrementado em uma unidade e, ao mandar a transação 
para os demais bancos, para que eles possam inserir em suas filas internas, o tempo de seus relógios é atualizado 
para o relógio do banco que enviou a transação. Assim, é garantido que todos eles tenham o mesmo tempo e, dessa 
forma, estejam sincronizados. 

Com o tempo vetorial e a nova transação, é feita uma busca binária na fila de execução, para que a transação seja
inserida na posição correta, de acordo com o seu tempo vetorial. O uso da busca binária é importante para garantir
que todos os bancos ordene da mesma forma as transações que estão na fila de execução, além de ser um algoritmo
eficiente para a ordenação de elementos em uma lista, que torna o processo mais rápido e eficiente.

Para cada nova transação, é colocado um id único de 2 dígitos, que é crucial para a confirmação entre os bancos, 
que será abordada mais adiante.

Com relação ao algoritmo de ordenação de multicast, ele funciona da seguinte forma: ao receber uma transação e 
passar pelas etapas anteriores, essa nova transação é enviada para todos os bancos do consórcio. Após todos os 
bancos receberem, eles enviam a confirmação de recebimento, chamados de ACKs, para os demais bancos. Esses ACKs
são armazenados em um dicionário interno em cada banco, que tem como chave o ID de cada operação e os valores é 
a transação e o ACKs, que é um "OK". Para saber se o número de ACKs está correto, é feito o seguinte cálculo: 
o número de ACKs recebidos no banco que enviou a determinada transação é igual ao número total de bancos do 
consórcio menos 1. Já nos demais bancos, aquele mesmo ACKs deve ter sido recebido o número total de bancos menos 2.
Caso esse cálculo não seja verdadeiro, significa que nem todos os bancos receberam aquela determinada transação, 
então ela ainda não pode ser executada.

ESQUEMA DE ENVIO DOS ACKS

Além disso, antes de executar uma determinada operação é verificado se ela também é a primeira da fila. Essa 
verificação é feita para todos os bancos.

Para executar uma determinada operação, é feita uma eleição de um líder, ou de vários liders. Esse lider será o 
banco que tem essas duas verificações verdadeiras: o número de ACKs correto e a operação é a primeira da fila. 
No caso de uma trnsação paralela, o líder sempre será o último banco que enviar a transação, de acordo com a
fila interna do Lock, pois ele será o único que ambas as verificações serão verdadeiras. No caso das transações
sequenciais, são eleitos vários líderes, que são os bancos que estão inserindo as operações de forma sequencial.

Assim, vai se para a próxima etapa, que é a execução da operação. Antes de executar de fato uma operação, é feita
uma semiexecução para saber se a operação pode ser realizada ou não. Isso é feito pois caos haja mais de uma 
operação em uma única transação, ou seja, tratando-se de uma fila de operações, se houver algum erro, todas 
as operações são canceladas e a lista é retirada da fila do banco. Assim, garante-se a atomicidade das operações.

Quando todas as operações são semiexecutadas com sucesso, então é retornado verdadeiro para a função de execução 
de fato e elas são realizadas.

Quando finalizadas, aquela operação é retirada da fila e é feita a verificação se tem mais operações para serem
executadas. Caso tenha, segue os mesmos passos anteriores, até o final.

## Transações bancárias

### Transações bancárias internas

O sistema permite a realização de transações bancárias internas, para contas de um mesmo banco, ou as opções de depósito
e saque, que são referentes a conta do próprio usuário que está utilizando no mmomento. 

### Transações bancárias externas

O sistema permite a realização de transações bancárias externas, para contas de diferentes bancos. Para a realização de
uma transação bancária externa, o usuário deve informar os seguintes dados: para os dados do remetente, deve se
informar o banco de origem, pois pode ser o banco atual que está sendo utilizado ou algum outro banco em que tenha conta.
Nesse caso, ele deve informar também o tipo de conta, que pode ser pessoa física particular, pessoa física conjunta ou
pessoa jurídica. O tipo de conta é necessário pois para verificar se aquele usuário, por meio do seu cpf, está cadastrado
no banco, ele pode ter mais de um tipo de conta, então deve-se ter o tipo também.

Para os dados do destinatário, deve-se informar o banco de destino, o tipo de conta, o cpf do destino, a chave pix
e o valor da transferencia. 

Após inserir todos esses dados, há a possibilidade de inserir uma nova operação ou finalizar a transação. Caso insira 
uma nova, essas novas operações vão sendo adicionadas em uma lista, que ao estar completa, é enviada para a fila de
execução. Antes de mandar propriamente para a fila, é feita uma semiexecução. Nessa semiexecução da fila de operações, 
são feitas todas as operações na lista com um valor nulo, para não haver alteração no saldo das contas. Caso haja algum
erro, essa lista de transações específica é cancelada e retirada da fila de operações e a próxima, se houver, é feita a 
mesma operação. Caso não haja erros, as operações são executadas normalmente e, quando finalizadas, são retiradas da 
lista.

### Transações sequenciais

Na aplicação, as transações são feitas de forma sequenciais. Isso significa que, ao realizar uma transação, ela é 
executada de forma sequencial, ou seja, uma após a outra. Isso é feito para garantir que as transações sejam realizadas
de forma correta, sem que haja erros ou inconsistências nos saldos das contas.

### Transações concorrentes

O sistema permite, por meio de scripts, a realização de transações bancárias concorrentes. Para isso, foi utilizado a
seguinte função:

Nela, as transações são enviadas de forma paralela para o sistema bancário. Isso é feito para simular um cenário
real, onde várias transações são realizadas ao mesmo tempo, e o sistema deve ser capaz de lidar com essas transações de
forma correta, sem que haja erros ou inconsistências nos saldos das contas. 

Nessa caso, o sistema faz o uso do algoritmo de concorrência distribuída, que é responsável por garantir que as transações
sejam realizadas de forma correta, sem que haja erros ou inconsistências nos saldos das contas, e o uso do Lock para
a criação de filas internas de execução, que são responsáveis por garantir que as transações sejam realizadas de forma
sequencial, uma após a outra.

## Comunicação entre servidores

### Protocolo utilizado

O sistema DistriBank utiliza o protocolo HTTP para a comunicação entre os servidores. O protocolo HTTP é um protocolo
de comunicação que permite a transferência de informações na web, e é amplamente utilizado para a comunicação entre
servidores. 

### Rotas de comunicação

O sistema DistriBank possui as seguintes rotas de comunicação:


## Tratamento da concorrência

### Algoritmo da concorrência distribuída

O sistema DistriBank utiliza o algoritmo de multicast de ordenação com o uso do relógio vetorial, para garantir que as
transações sejam realizadas de forma correta, sem que haja erros ou inconsistências nos saldos das contas. O algoritmo
de multicast de ordenação com o uso do relógio vetorial é um algoritmo de concorrência distribuída que é responsável por4
garantir que as transações sejam realizadas de forma correta, sem que haja erros ou inconsistências nos saldos das contas.

### Operações atômicas

O sistema DistriBank utiliza operações atômicas para garantir que as transações sejam realizadas de forma correta, sem
que haja erros ou inconsistências nos saldos das contas. As operações atômicas são operações que são realizadas de forma
indivisível, ou seja, ou todas as operações são realizadas com sucesso, ou nenhuma operação é realizada.

### Operações simultâneas em um único servidor

O sistema DistriBank permite a realização de operações simultâneas em um único servidor, para garantir que as transações
sejam realizadas de forma correta, sem que haja erros ou inconsistências nos saldos das contas. As operações simultâneas
são operações que são realizadas ao mesmo tempo, e o sistema deve ser capaz de lidar com essas operações de forma correta,
sem que haja erros ou inconsistências nos saldos das contas.

## Tratamento da confiabilidade

### Verificação de conexão

O sistema verifica a conexão se os servidores do consórcio estão ativos ou não por meio de uma thread, que fica 
tantando fazer a conexão via socket com o servidor. Caso haja erro, a thread muda o status do servidor no dicionário
de servidores, que é um dicionário que contém os servidores do consórcio e seus status, para offline.

Antes de adicionar uma oeração na fila, é verificado todos os bancos do consórcio. caso algum esteja offline, aquela
operação é descartada e é retornado que existe um banco offline e por isso, não é possível fazer a operação. Quando 
o servidor volta, aquele status no dicionaário é atualizado e, então pode se ralizar novas operalçoes.

### Retorno de conexão


### Tratamento de erros

O sistema DistriBank trata os erros de forma correta, para garantir que as transações sejam realizadas de forma 
correta, sem que haja erros ou inconsistências nos saldos das contas. Os erros são tratados por meio de exceções,
que são lançadas quando ocorre um erro, e são capturadas para que o sistema possa lidar com o erro de forma correta.


## Docker


## Testes

## Execução do projeto

## Referências


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

