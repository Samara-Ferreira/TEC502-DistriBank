<div align="center">
  <img src="/images/logo.png" width="100" height="100">

<h1> TEC502-DistriBank </h1>

</div>

<div align="justify">

> Este projeto foi desenvolvido como parte da disciplina MI - Concorrência e Conectividade, do curso de
Engenharia de Computação da Universidade Estadual de Feira de Santana (UEFS). O nome "DistriBank" foi escolhido
para representar um sistema de transações bancárias distribuído.

</div>  

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

<div align="justify">
  <h1>Descrição do projeto</h1>

O projeto DistriBank é um sistema de transações bancárias distribuído, que permite a realização de transações entre
contas de diferentes bancos sem a necessidade de um intermediário, como o Banco Central. O sistema é composto por 
vários servidores, cada um representando um banco, que se comunicam entre si para a realização das transações. 
Nos testes apresentados, são criadas quatro instâncias de servidores, que representam os bancos do consórcio, 
e cada servidor possui uma porta específica para a comunicação entre eles. É importante ressaltar que o sistema 
pode utilizar mais do que esse número de servidores, desde que seja feita a configuração adequada, 
para haver a comunicação entre eles.

Para o desenvolvimento do projeto, foi utilizado a linguagem de programação Python, com o ‘framework’ Flask.
Esse ‘framework’ permite a criação de ‘Interfaces’ de Programação de Aplicativos (Application Programming ‘Interface’ - APIs) 
de forma simples e eficiente. Também foi utilizado no projeto a biblioteca requests, que permite a comunicação entre
os servidores, por meio do Protocolo de Transferência de Hipertexto (Hypertext Transfer Protocol - HTTP). 
O ambiente de desenvolvimento utilizado para a criação do projeto foi o PyCharm, mas o projeto pode ser executado
em qualquer IDE de preferência do utilizador ou até mesmo no terminal. 

### Requisitos e funcionalidades do sistema

O sistema DistriBank foi desenvolvido para atender as seguintes funcionalidades:
- Criação de contas bancárias de pessoa física e jurídica;
- Realização de transações bancárias entre contas de diferentes bancos;
- Realização de transações bancárias internas entre contas do mesmo banco;
- Realização de transações bancárias sequenciais;
- Realização de transações bancárias concorrentes;
- Verificação de conexão entre os servidores;
- Tratamento de erros e retorno de conexão;
- Execução do sistema em containers Docker.

### Componentes principais do sistema

Como componentes principais do sistema, tem-se a aplicação e os servidores, que representam os bancos do consórcio.
A aplicação é responsável por realizar a comunicação entre os servidores, por meio de um protocolo de comunicação,
que permite a transferência de informações entre os servidores, para a realização das transações bancárias.
Os servidores, por sua vez, são responsáveis por armazenar as informações das contas bancárias, e realizar as operações
bancárias, como a criação de contas e a realização de transações. É importante ressaltar que além da aplicação, o
sistema pode usar ‘scripts’ para a realização de transações bancárias concorrentes, que são transações realizadas 
de forma paralela, para simular um cenário real, onde várias transações são realizadas simultaneamente,

#### Aplicação 

PRINTS DO TERMINAL? EXPLICAÇÃO DOS DIRETÓRIOS?

A aplicação é responsável por realizar a comunicação entre os servidores.
No diretório, segue a seguinte estrutura:

    ├── __init__.py
    ├── __main__.py
    ├── AccountCreation.py
    ├── AccountManagement.py
    ├── Application.py
    ├── Transactions.py
    ├── Dockerfile 

- __main__.py: é o arquivo principal da aplicação, que é responsável por iniciar a 
aplicação e realizar a comunicação entre os servidores.
- AccountCreation.py: é o arquivo responsável por realizar a criação de contas bancárias.
- AccountManagement.py: é o arquivo responsável por realizar a gestão de contas bancárias.
- Application.py: é o arquivo responsável por realizar a comunicação entre os servidores.
- Transactions.py: é o arquivo responsável por realizar as transações bancárias.
- Dockerfile: é o arquivo responsável por criar a imagem do Docker.

#### Bancos

Os bancos são os servidores que compõem o sistema.


    ├── api
    │   ├── __init__.py
    │   ├── API.py
    │   ├── FloatConverter.py
    ├── clients 
    │   ├── __init__.py
    │   ├── JointClient.py
    │   ├── JuridicClient.py
    │   ├── PhysicalClient.py
    ├── exceptions
    │   ├── __init__.py
    │   ├── Exceptions.py
    ├── utils
    │   ├── __init__.py
    │   ├── Utils.py
    ├── __init__.py
    ├── __main__.py
    ├── Bank.py
    ├── Dockerfile
    ├── Queue.py
    ├── UniqueTwoDigitID.py
    ├── VectorialClock.py

- __main__.py: é o arquivo principal do servidor, que é responsável por iniciar o 
servidor e realizar as operações bancárias.
- Bank.py: é o arquivo responsável por armazenar as informações das contas bancárias, 
e realizar as operações bancárias.
- Queue.py: é o arquivo responsável por criar a fila de execução, que é responsável por 
garantir que as transações sejam realizadas de forma correta, sem que haja erros ou 
inconsistências nos saldos das contas.
- UniqueTwoDigitID.py: é o arquivo responsável por gerar um id único de 2 dígitos, que é
crucial para a confirmação entre os bancos.
- VectorialClock.py: é o arquivo responsável por criar o relógio vetorial, que é utilizado
para definir a posição das transações na fila de execução, de acordo com o seu tempo vetorial.
- Dockerfile: é o arquivo responsável por criar a imagem do Docker.
- api/API.py: é o arquivo responsável por realizar a comunicação entre os servidores.
- api/FloatConverter.py: é o arquivo responsável por converter os valores das transações
- clients/JointClient.py: é o arquivo responsável por realizar as operações de conta conjunta.
- clients/JuridicClient.py: é o arquivo responsável por realizar as operações de conta jurídica.
- clients/PhysicalClient.py: é o arquivo responsável por realizar as operações de conta física.
- exceptions/Exceptions.py: é o arquivo responsável por tratar as exceções.
- utils/Utils.py: é o arquivo responsável por realizar as operações de utilidade.

</div>

<div align="justify">
  <h1>Comunicação entre servidoress</h1>

A comunicação entre os servidores do sistem é feita por meio de um protocolo de comunicação, que permite a 
transferência de informações entre os servidores, para a realização das transações bancárias. Essas 
operações são feitas por meio de uma API, que permite essa comunicação entre os diferentes servidores, que estão 
alocados em diferentes máquinas.

O protocolo utilizado para a comunicação entre a aplicação e os servidores é o HTTP, que é um protocolo de 
comunicação que permite a transferência de informações na web, e é amplamente utilizado para a comunicação entre 
servidores. O HTTP é um protocolo de comunicação cliente-servidor, onde o cliente envia uma requisição para o 
servidor, e o servidor responde com uma resposta, sendo uma boa escolha para o projeto em questão, pois permite a 
comunicação entre os servidores de forma eficiente e segura.

Essa comunicação é feita por meio de rotas, que são URLs que permitem a comunicação entre os bancos, para a 
realização das operações disponíveis no sistema. As rotas são definidas por meio de métodos HTTP, como GET, POST,
PUT e DELETE, que permitem a realização de operações de leitura, criação, atualização e exclusão de informações, 
respectivamente. 

### Rotas de comunicação

Cada função retorna um JSON com os dados solicitados. A seguir, são apresentados exemplos de requisições para 
cada uma das rotas da API REST do projeto apresentadas:

- Requisição para fazer login:
  - Método: POST
  - Rota: /<string:type>/<string:user>/<string:password>/login
  - Resposta:
  - Exemplo de requisição:
  ```json
  {
    "user": "maria11",
    "type_account": "physical"
  }
  ```
  - Exemplo de resposta:
  ```json
  {
    "message": "Login feito com sucesso!",
    "status": 200
  }
  ```
  - Exemplo de resposta:
  ```json
  {
    "message": "Cliente não encontrado!",
    "status": 404
  }
  ```
  - Exemplo de resposta:
  ```json
  {
    "message": "Senha incorreta!",
    "status": 401
  }
  ```


- Requisição para fazer logout:
  - Método: POST
  - Rota: /<string:type>/<string:user>/logout
  - Resposta:
  - Exemplo de requisição:
  ```json
  {
    "user": "maria11"
  }
  ```
  - Exemplo de resposta:
  ```json
  {
    "message": "Deslogado com sucesso da conta de Maria!",
    "status": 200
  }
  ```
  - Exemplo de resposta:
  ```json
  {
    "message": "Cliente não encontrado!",
    "status": 404
  }
  ```


- Requisição para criar conta física particular:
  - Método: POST
  - Rota: /<string:name>/<string:cpf>/<string:user>/<string:password>/<float:balance>/create_physical_particular
  - Resposta:
  - Exemplo de requisição:
  ```json
  {
    "name": "Maria",
    "cpf": "12345678910",
    "user": "maria11",
    "password": "123456",
    "balance": 100.0
  }
  ```
  - Exemplo de resposta:
  ```json
  {
    "message": "Conta particular para Maria criada com sucesso!",
    "status": 200
  }
  ```
  - Exemplo de resposta:
  ```json
  {
    "message": "Cliente já existe!",
    "status": 409
  }
  ```
  

- Requisição para criar conta física conjunta:
  - Método: POST
  - Rota: /<string:name>/<string:cpf>/<string:user>/<string:password>/<float:balance>/create_physical_joint
  - Resposta:
  - Exemplo de requisição:
  ```json
  {
    "name": "José",
    "cpf": "12345678919",
    "user": "jose11",
    "password": "123456",
    "balance": 200.0
  }
  ```
  - Exemplo de resposta:
  ```json
  {
    "message": "Conta conjunta para José criada com sucesso!",
    "status": 200
  }
  ```
  - Exemplo de resposta:
  ```json
  {
    "message": "Cliente já existe!",
    "status": 409
  }
  ```


- Requisição para criar conta jurídica:
  - Método: POST
  - Rota: /<string:company>/<string:cnpj>/<string:name>/<string:cpf>/<string:user>/<string:password>/<float:balance>/create_juridic_account
  - Resposta:
  - Exemplo de requisição:
  ```json
  {
    "company": "Empresa",
    "cnpj": "12345678910111",
    "name": "Maria",
    "cpf": "12345678910",
    "user": "maria11",
    "password": "123456",
    "balance": 300.0
    }
    ```
    - Exemplo de resposta:
    ```json
    {
        "message": "Conta jurídica (admin) para Empresa criada com sucesso!",
        "status": 200
    }
    ```
    - Exemplo de resposta:
    ```json
    {
        "message": "Cliente já existe!",
        "status": 409
    }
    ```
  
- Requisição para adicionar usuário à conta jurídica:
  - Método: POST
  - Rota: /<string:cnpj>/<string:cpf>/<string:name>/<string:user>/<string:password>/create_juridic_employee
  - Resposta:
  - Exemplo de requisição:
  ```json
  {
    "cnpj": "12345678910111",
    "cpf": "12345678911",
    "name": "José",
    "user": "jose11",
    "password": "123456"
    }
    ```
    - Exemplo de resposta:
    ```json
    {
        "message": "Usuário José adicionado à conta jurídica com sucesso!",
        "status": 200
    }
    ```
    - Exemplo de resposta:
    ```json
    {
        "message": "Cliente já existe!",
        "status": 409
    }
    ```
  
- Requisição para criar uma chave pix:
  - Método: POST
  - Rota: /<string:cpf>/<string:type>/<string:type_key>/<string:pix>/create_pix_key
  - Resposta:
  - Exemplo de requisição:
  ```json
  {
    "cpf": "12345678910",
    "type": "physical",
    "type_key": "cpf",
    "pix": "12345678910"
    }
    ```
    - Exemplo de resposta:
    ```json
    {
        "message": "Chave PIX criada com sucesso!",
        "status": 200
    }
    ```
    - Exemplo de resposta:
    ```json
    {
        "message": "Chave PIX já existe!",
        "status": 409
    }
    ```
  - Exemplo de resposta:
  ```json
  {
      "message": "Cliente não encontrado!",
      "status": 404
  }
  ```
  - Exemplo de resposta:
  ```json
  {
      "message": "Chave inválida!!",
      "status": 400
  }
  ```
  

- Requisição para obter as chaves pix:
  - Método: GET
  - Rota: /<string:cpf>/<string:type>/get_keys
  - Resposta:
  - Exemplo de requisição:
  ```json
  {
    "cpf": "12345678910",
    "type": "physical"
    }
    ```
    - Exemplo de resposta:
    ```json
    {
        "keys": [
            {
                "type_key": "cpf",
                "pix": "12345678910"
            }
        ]
    }
    ```
    - Exemplo de resposta:
    ```json
    {
        "message": "Cliente não encontrado!",
        "status": 404
    }
    ```
  

- Requisição para obter os clientes:
  - Método: GET
  - Rota: /get_clients
  - Resposta:
  - Exemplo de resposta:
  ```json
  {
    "clients": [
        {
            "cpf_cnpj": "12345678910",
            "email": "maria@uefs",
            "phone": "7599999999",
            "random": None
        }
    ]
  }
  ```
  - Exemplo de resposta:
  ```json
  {
      "message": "Cliente não encontrado!",
      "status": 404
  }
  ```
  
- Requisição para obter o saldo atual do cliente:
  - Método: GET
  - Rota: /<string:cpf>/<string:type>/get_balance
  - Resposta:
  - Exemplo de requisição:
  ```json
  {
    "cpf": "12345678910",
    "type": "physical"
    }
    ```
    - Exemplo de resposta:
    ```json
    {
        "balance": 100.0
    }
    ```
    - Exemplo de resposta:
    ```json
    {
        "message": "Cliente não encontrado!",
        "status": 404
    }
    ```

- Requisição para obter o extrato de operações do banco:
- Método: GET
- Rota: /get_bank_statement
- Resposta:
- Exemplo de resposta:
  ```json
  {
    "operations": [
        {
            "id": "5500",
            "operation": "transfer",
            "cpf_cnpj": "12345678910",
            "value": 50.0
        }
    ]
  }
  ```
  - Exemplo de resposta:
  ```json
  {
      "message": "Fila vazia!",
      "status": 404
  }
  ```
  
- Requisição para criar um depósito:
  - Método: POST
  - Rota: /<string:host>/<string:port>/<string:type>/<float:value>/create_deposit
  - Resposta:
  - Exemplo de requisição:
  ```json
  {
    "host": "172.16.103.1",
    "port": "5551",
    "type": "physical",
    "value": 100.0
   }
  ```
  - Exemplo de resposta:
  ```json
  {
    "message": "Depósito de 100.0 criado com sucesso!",
    "status": 200
  }
  ```
  
- Requisição para criar uma transferência:
  - Método: POST
  - Rota: /<string:list_operations>/create_transfer
  - Resposta:
  - Exemplo de requisição:
  ```json
  {
    "list_operations": 
    [
        {
          "host_send": "172.16.103.1",
          "port_send": "5551",
          "cpf_send": "12345678910",
          "type_send": "physical",
          "value": "value",
            
          "host_recp": "172.16.103.2",
          "port_recp": "5552",
          "cpf_recp": "12345678919",
          "type_recp": "physical",
          "key_recp": "cpf"
        }
    ]
  }
  ```
  - Exemplo de resposta:
  ```json
  {
      "message": "Transferência de 50.0 criada com sucesso!",
      "status": 200
  }
  ```  

- Requisição para fazer um saque:
  - Método: POST
  - Rota: /<string:host>/<string:port>/<string:type>/<float:value>/create_withdraw
  - Resposta:
  - Exemplo de requisição:
  ```json
  {
    "host": "172.16.103.1",
    "port": "5551",
    "type": "physical",
    "value": 50.0
  }
  ```
  - Exemplo de resposta:
  ```json
   {
     "message": "Saque de 50.0 criado com sucesso!",
     "status": 200
   }
  ```

- Requisição para fazer um depósito:
  - Método: POST
  - Rota: /<string:cpf>/<string:type>/<string:key>/<float:value>/deposit
  - Resposta:
  - Exemplo de requisição:
  ```json
  {
    "cpf": "12345678910",
    "type": "physical",
    "key": "cpf",
    "value": 100.0
  }
  ```
  - Exemplo de resposta:
  ```json
  {
    "message": "Depósito de 100.0 feito com sucesso!",
    "status": 200
  }
  ```
  - Exemplo de resposta:
  ```json
  {
    "message": "Cliente não encontrado!",
    "status": 404
  }
  ```
  - Exemplo de resposta:
  ```json
  {
    "message": "Chave não encontrada!",
    "status": 404
  }
  ```
  
- Requisição para fazer um saque:
  - Método: POST
  - Rota: /<string:cpf>/<string:type>/<string:key>/<float:value>/withdraw
  - Resposta:
  - Exemplo de requisição:
  ```json
  {
    "cpf": "12345678910",
    "type": "physical",
    "key": "cpf",
    "value": 50.0
  }
  ```
  - Exemplo de resposta:
  ```json
  {
    "message": "Saque de 50.0 feito com sucesso!",
    "status": 200
  }
  ```
  - Exemplo de resposta:
  ```json
  {
    "message": "Cliente não encontrado!",
    "status": 404
  }
  ```
  - Exemplo de resposta:
  ```json
  {
    "message": "Chave não encontrada!",
    "status": 404
  }
  ```
  
- Requisição para verificar se um cliente existe:
  - Método: GET
  - Rota: /<string:cpf>/<string:type>/check_client
  - Resposta:
  - Exemplo de requisição:
  ```json
  {
    "cpf": "12345678910",
    "type": "physical"
  }
  ```
  - Exemplo de resposta:
  ```json
  {
    "message": "Cliente encontrado!",
    "status": 200
  }
  ```
  - Exemplo de resposta:
  ```json
  {
    "message": "Cliente não encontrado!",
    "status": 404
  }
  ```

</div>

<div align="justify">
  <h1>Relógio Vetorial</h1>

  <img src="/images/relogio_vetorial.png" >

</div>

## Algoritmo da concorrência distribuída

Para o tratamento da concorrência distribuída, o sistema usa o relógio vetorial com o algoritmo mulicast totalmente 
ordenado. O algoritmo de multicast de ordenação com o uso do relógio vetorial é um algoritmo de concorrência distribuída 
que é responsável por garantir que as transações sejam realizadas de forma correta, sem que haja erros ou inconsistências 
nos saldos das contas. 

### Relógio Vetorial

O relógio vetorial é utilizado para definir a posição das transações na fila de execução, conforme o seu 
tempo vetorial. A cada nova transação, o relógio vetorial é incrementado numa unidade e, ao mandar a transação 
para os demais bancos, para que eles possam inserir na suas filas internas, o tempo dos seus relógios é atualizado 
para o relógio do banco que enviou a transação. Assim, é garantido que todos eles tenham o mesmo tempo e, dessa 
forma, estejam sincronizados. O relógio vetorial é um vetor de tamanho n, onde n é o número de bancos do consórcio, que 
é responsável por armazenar o tempo de cada banco. Assim, é possível saber a ordem correta das transações, de acordo 
com o tempo vetorial de cada banco.

IMAGEM DO RELÓGIO VETORIAL


### Algoritmo de ordenação em multicast

Com o tempo vetorial e a nova transação, é feita uma busca binária na fila de execução, para que a transação seja
inserida na posição correta, de acordo com o seu tempo vetorial. O uso da busca binária é importante para garantir
que todos os bancos ordene da mesma forma as transações que estão na fila de execução, além de ser um algoritmo
eficiente para a ordenação de elementos em uma lista, que torna o processo mais rápido e eficiente.

Para cada nova transação, é colocado um id único de 2 dígitos, que é crucial para a confirmação entre os bancos, 
que será abordada mais adiante. O ID da transação é formado pelos 2 últimos dígitos da porta daquele banco, e por 
2 dígitos que são gerados com essa classe. Assim, é garantido que o ID seja único e que não haja conflitos. 

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

As transações desse sistema são ditas como transações atomicas, pois são realizadas de forma indivisivel, ou seja,
ou todas as operações são realizadas com sucesso, ou nenhuma operação é realizada. Isso é feito para garantir que as
transações sejam realizadas de forma correta.

IMAGEM DA ATOMICIDADE

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
https://edisciplinas.usp.br/pluginfile.php/3609782/mod_resource/content/1/aula-12.pdf



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

