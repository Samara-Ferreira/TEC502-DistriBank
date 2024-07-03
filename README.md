<div align="center">
  <img src="/images/logo.png" width="100" height="100">

<h1> TEC502-DistriBank </h1>

</div>

<div align="justify">

> Este projeto foi desenvolvido como parte da disciplina MI - Concorrência e Conectividade, do curso de
Engenharia de Computação da Universidade Estadual de Feira de Santana (UEFS). O nome "DistriBank" foi escolhido
para representar um sistema de transações bancárias distribuído.

</div>  

<div align="center">
  <img src="/images/divisor.jpg" width="1280" height="5">
</div>

<h2>Sumário</h2>

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

<div align="center">
  <img src="/images/divisor.jpg" width="1280" height="5">
</div>

<div align="justify">
  <h2>Descrição do projeto</h2>

O projeto DistriBank é um sistema de transações bancárias distribuído, que permite a realização de transações entre
contas de diferentes bancos sem a necessidade de um intermediário, como o Banco Central. O sistema é composto por 
vários servidores, cada um representando um banco, que se comunicam entre si para a realização das transações. 
Nos testes apresentados, são criadas quatro instâncias de servidores, que representam os bancos do consórcio, 
e cada servidor possui uma porta específica para a comunicação entre eles. É importante ressaltar que o sistema 
pode utilizar mais do que esse número de servidores, desde que seja feita a configuração adequada, 
para haver a comunicação entre eles.

Para o desenvolvimento do projeto, foi utilizado a linguagem de programação Python, com o ‘framework’ Flask.
Esse ‘framework’ permite a criação de ‘Interfaces’ de Programação de Aplicativos (Application Programming ‘Interface’ 
- APIs) 
de forma simples e eficiente. Também foi utilizado no projeto a biblioteca requests, que permite a comunicação entre
os servidores, por meio do Protocolo de Transferência de Hipertexto (Hypertext Transfer Protocol - HTTP). 
O ambiente de desenvolvimento utilizado para a criação do projeto foi o PyCharm, mas o projeto pode ser executado
em qualquer IDE de preferência do utilizador ou até mesmo no terminal. 


<h3>Requisitos e Funcionalidades do Sistema</h3>

O sistema DistriBank foi desenvolvido para atender as seguintes funcionalidades:
- Criação de contas bancárias de pessoa física e jurídica;
- Realização de transações bancárias entre contas de diferentes bancos;
- Realização de transações bancárias internas entre contas do mesmo banco;
- Realização de transações bancárias sequenciais;
- Realização de transações bancárias concorrentes;
- Verificação de conexão entre os servidores;
- Tratamento de erros e retorno de conexão;
- Execução do sistema em containers Docker.


<h3>Componentes Principais do Sistema</h3>

Como componentes principais do sistema, tem-se a aplicação e os servidores, que representam os bancos do consórcio.
A aplicação é responsável por realizar a comunicação entre os servidores, por meio de um protocolo de comunicação,
que permite a transferência de informações entre os servidores, para a realização das transações bancárias.
Os servidores, por sua vez, são responsáveis por armazenar as informações das contas bancárias, e realizar as operações
bancárias, como a criação de contas e a realização de transações. É importante ressaltar que além da aplicação, o
sistema pode usar ‘scripts’ para a realização de transações bancárias concorrentes, que são transações realizadas 
de forma paralela, para simular um cenário real, onde várias transações são realizadas simultaneamente,


<h4>Aplicação</h4>

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

<h4>Bancos</h4>

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

</div>

<div align="center">
  <img src="/images/divisor.jpg" width="1280" height="5">
</div>

<div align="justify">
  <h2>Comunicação entre os Servidores<h2>


<h3>Rotas de Comunicação</h3>

Cada função retorna um JSON com os dados solicitados. A seguir, são apresentados exemplos 
de requisições para cada uma das rotas da API REST do projeto apresentadas:

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

<div align="center">
  <img src="/images/divisor.jpg" width="1280" height="5">
</div>

<div align="justify">
  <h1>Relógio Vetorial</h1>

  <img src="/images/relogio_vetorial.png" >

</div>

<div align="justify">
  <h2>Algoritmos da Concorrência Distribuída</h2>

Para o tratamento da concorrência distribuída, o sistema faz uso do relógio vetorial com o algoritmo de multicast
totalmente ordenado. A junção desses algoritmos é responsável por garantir que as transações sejam realizadas de forma 
correta, sem que haja erros ou inconsistências nos saldos das contas.

  <h3>Relógio Vetorial</h3>

O relógio vetorial é um algoritmo usado para definir o tempo das operações de um sistema distribuído. Ele é utilizado 
no sistema para definir a posição das transações na fila de execução, de acordo com o seu tempo vetorial. A cada nova
transação, o relógio vetorial é incrementado em uma unidade, e ao enviar a transação para os demais bancos, o tempo dos
seus relógios é atualizado para o relógio do banco que enviou a transação. Assim, é garantido que todos os bancos tenham
o mesmo tempo e, dessa forma, estejam sincronizados. O relógio vetorial é um vetor de tamanho n, onde n é o número de
bancos do consórcio, que é responsável por armazenar o tempo de cada banco. No exemplo abordado para testes, como são
criadas quatro instâncias de servidores, o vetor terá tamanho 4, e cada posição do vetor será responsável por armazenar
o tempo de cada banco.

Na imagem abaixo, é apresentado um exemplo de relógio vetorial, onde tem-se quatro processos (P1, P2, P3 e P4), e cada
processo possui um relógio vetorial de tamanho 4, que é responsável por armazenar o tempo de cada processo. O processo
3 inicia a transação, e o seu relógio vetorial é incrementado em uma unidade. Após isso, é enviado para o processo 2,
que atualiza o seu relógio vetorial para o relógio do processo 3. A cada processo que recebe a transação, o seu relógio
vetorial é atualizado para o relógio do processo que enviou a transação. Assim, é garantido que todos os processos 
estejam sincronizados.

<div align="center">
  <img src="/images/relogio.png" width="1920" height="1080">
</div>

<h3>Algoritmo de Multicast Totalmente Ordenado</h3>

Com o tempo vetorial, é necessário um algoritmo de ordenação para garantir que as transações sejam realizadas de forma
correta, sem que haja erros ou inconsistências nos saldos das contas. Para isso, o sistema faz uso do algoritmo de 
multicast totalmente ordenado. Esse algoritmo refere-se a um método de comunicação em sistemas distribuídos que 
garante que todas as mensagens enviadas sejam entregues a todos os destinatários, na mesma ordem. Essa ordenação é
crucial para manter a consistência entre os estados dos processos.

A cada nova transação, o tempo do relógio vetorial é incrementado e é criado um ID de 2 dígitos para aquela 
determinada transação. Esse identificador é formado pelos 2 últimos dígitos da porta daquele banco, e por 2 dígitos
que são gerados com uma classe específica. Assim, é garantido que o ID seja único e que não haja conflitos. Esse ID
é utilizado para a confirmação entre os bancos do recebimento dos pacotes, e é armazenado em uma lista juntamente com 
tempo do relógio vetorial, a transação e o ID. 

Após isso, é feita uma busca binária para saber a posição na qual o novo elemento na fila de execução, de acordo 
com o seu tempo vetorial. A busca binária foi escolhida por ser um algoritmo eficiente para a ordenação de elementos 
em uma lista, que torna o processo mais rápido e eficiente. 

Após isso, essa operação é enviada para os demais bancos do consóricio onde, respectivamente, são feitas as etapas
descritas anteriormente. Após os bancos receberem essas transações, eles enviam a confirmação de recebimento para
todos os outros bancos do consórcio, que são conhecidos como ACKs. Esses ACKs são armazenados em um dicionário interno
em cada banco, que tem como chave o ID de cada operação e os valores são listas com todos os ACKs recebidos daquela 
operação. Para saber se o número de ACKs está correto, é feito o seguinte cálculo: o número de ACKs recebidos no banco
que enviou a determinada transação é igual ao número total de bancos do consórcio menos 1. Já nos demais bancos, aquele
mesmo ACKs deve ter sido recebido o número total de bancos menos 2. Caso esse cálculo não seja verdadeiro, significa
que nem todos os bancos receberam o pacote.

Para garantir que todos os bancos estejam sincronizados, ou seja, todos eles com a mesma fila de transação, antes
de executar é feita uma verificação se o pacote é o primeiro da fila em todos os bancos. Caso seja, essse banco 
que enviou a verificação é considerado como líder e assume o papel de disparar todas as transações disponíveis 
na fila de execução.

Abaixo, é apresentado um exemplo de como é feita a comunicação entre os bancos, por meio do algoritmo de multicast 
totalmente ordenado com o relógio vetorial. Nesse exemplo, tem-se quatro bancos (B1, B2, B3 e B4), e cada banco 
possui um relógio vetorial de tamanho 4, que é responsável por armazenar o tempo de cada banco. O banco 1 e o banco 2
recebem transações de forma paralela, com o mesmo tempo vetorial. Para o tratamento desse tipo de operação é feito 
o uso dos Locks (travas), que são mecanismos utilizados para garantir a consistência de dados em sistemas distribuídos,
especialmente em ambientes onde múltiplas transações podem acessar e modificar os mesmos recursos simultaneamente. 
O uso dessas travas assegura que apenas uma transação por vez possa acessar um recurso crítico, evitando condições
de corrida e garantindo a integridade dos dados.

<div align="center">
  <img src="/images/multicast1.png" width="1920" height="1080">
</div>

Nesse caso, o Lock vai travar uma das operações recebidas, e a outra poderá ser manipulada. Supoe-se que a operação
1 seja escolhida para manipulação e a operação 2 seja travada. Dessa forma, a operação 1 é inserida na fila do banco 
1 e é enviada para ser inserida na fila dos demais bancos, como pode ser visto na imagem abaixo.

<div align="center">
  <img src="/images/multicast2.png" width="1920" height="1080">
</div>

Após isso, é feita a verificação do número de ACKs, que são a confirmação de recebimento dos pacotes. Como pode ser
visualizado na imagem abaixo, o banco 1 recebeu o ACK do banco 2, 3 e 4, mas não fez envio. Já o banco 2 recebeu
ACKs do banco 3 e do banco 4, enquanto o banco 3 recebeu ACKs do banco 4 e 2, e o banco 4 recebeu ACKs do banco 2 e 3.
Assim, é possível visualizar a fórmula de cálculo do número de ACKs, que foi descrita anteriormente, pois o banco 
que enviou a operação deve receber o número total de bancos menos 1, e os demais bancos devem receber o número total
de bancos menos 2.

<div align="center">
  <img src="/images/multicast3.png" width="1920" height="1080">
</div>

Recebido o número de ACKs, tem-se que verificar a se a operação que é a primeira da lista no banco 1 é a mesma 
dos demais bancos. Com a liberação do Lock, a operação 2 é liberada e inserida na fila do banco 2, e, dessa forma, 
a OP1 não é a primeira da fila em todos os bancos, retornando falso para essa verificação. Logo, o banco 1 não 
poderá executar a operação 1, pois mais operações estão sendo inseridas na fila. Essa representação pode ser
vista na imagem abaixo.

<div align="center">
  <img src="/images/multicast4.png" width="1920" height="1080">
</div>

Agora com a operação 2, repete-se o mesmo processo anterior: essa nova transação deve ser enviada para os demais
bancos, assim mostrado na imagem abaixo, como na operação 1.

<div align="center">
  <img src="/images/multicast5.png" width="1920" height="1080">
</div>

E, por fim, é feita a verificação do número de ACKs e da posição da operação na fila de execução. Como todos os 
bancos tem a mesma operação como a primeira da fila, então o banco 2 pode ser eleito um lider e disparar a 
execução das operações da lista. Assim, a operação 2 é executada e, após isso, a operação 1 é executada, pois
a operação 2 foi a primeira da fila. Essa última parte da verificação pode ser vista na imagem abaixo.

<div align="center">
  <img src="/images/multicast6.png" width="1920" height="1080">
</div>

Para as operações sequenciais, o sistema segue o mesmo passo a passo so que, nesse caso, o lider será aquele
banco que estiver enviando a operação. Ou seja, pode ser feita a eleição de um lider para cada operação, e,
dessa forma, garantir que as operações sejam realizadas na ordem.

</div>

<div align="center">
  <img src="/images/divisor.jpg" width="1280" height="5">
</div>


<div align="justify">
  <h2>Transações Bancárias</h2>

As transações neste sistema são chamadas de transações atômicas porque são executadas
de forma indivisível. Isso significa que ou todas as operações dentro de uma transação
são concluídas com sucesso, ou nenhuma operação é realizada. Esse mecanismo assegura que
as transações sejam realizadas corretamente, mantendo a consistência e a integridade dos
dados.

Na imagem abaixo, tem-se se o exemplo de 3 operações em uma única transação, caso o cliente
tenha contas em tres bancos diferentes:
- Transferência do banco 1 para o banco 4;
- Transferência do banco 2 para o banco 4;
- Transferência do banco 3 para o banco 4.

Nesse caso, todas as operações antes de serem executadas de fato, elas são semiexecutadas
e verifica se houve a ocorrencia de algum erro durante esse processo.

<div align="center">
  <img src="/images/atomicidade1.png.png" width="1920" height="1080
</div>

No caso registrado abaixo, tem-se o exemplo de que a operação de transferencia do banco 1
para o banco 4 não foi bem sucedida, por motivos que podem ser: saldo insuficiente, conta
inexistente, entre outros. Nesse caso, a toda operação é cancelada e retirada da fila de 
execução, como pode ser visto, que mesmo as outras que não houve inconsistencias, foram 
canceladas de serem executadas.

<div align="center">
  <img src="/images/atomicidade2.png.png" width="1920" height
</div>

Já em outro caso, como o abaixo, todas as operações foram bem sucedidas e, dessa forma,
foram retiradas da fila de execução, como pode ser visto.

<div align="center">
  <img src="/images/atomicidade3.png.png" width="1920" height
</div>


**<h3>Transações Bancárias Internas</h3>

O sistema permite a execução de transações bancárias internas, possibilitando 
transferências entre contas do mesmo banco, além das opções de depósito e saque, que se 
referem à conta do próprio usuário que está utilizando o sistema no momento.

<h3>Transações Bancárias Externas</h3>

O sistema permite a execução de transações bancárias externas, facilitando transferências
para contas em diferentes bancos. Para realizar uma transação bancária externa, o 
usuário deve fornecer os seguintes dados:

- Dados do remetente: O usuário deve fornecer informações detalhadas para garantir que 
a transação seja iniciada corretamente. Os dados exigidos incluem:
  - Banco de origem: Nome ou código do banco onde a conta do remetente está registrada. 
  Pode ser o banco atual que está sendo utilizado ou outro banco onde o usuário possua 
  conta.
  - Tipo de conta: Especificar se a conta do remetente é de pessoa física particular, 
  pessoa física conjunta ou pessoa jurídica. Isso ajuda a verificar se o usuário,
  através do seu CPF, está cadastrado no banco, considerando que ele pode ter mais de
  um tipo de conta.
  - CPF do remetente: O número do CPF do titular da conta de origem, necessário para
  identificar e autenticar o usuário.
  - Valor da transferência: O montante exato que o usuário deseja transferir. 
  Esse valor deve ser especificado claramente para garantir a precisão da transação.**

- Dados do destinatário: O usuário deve fornecer informações detalhadas para 
garantir que a transação seja realizada corretamente. Os dados exigidos incluem:
  - Banco de destino: Nome ou código do banco onde a conta do destinatário está registrada.
  - Tipo de conta: Especificar se a conta do destinatário é de pessoa física particular,
  pessoa física conjunta ou pessoa jurídica. Isso ajuda a garantir que a transferência
  seja direcionada corretamente.
  - CPF do destinatário: O número do CPF do titular da conta de destino, que é 
  utilizado para confirmar a identidade do destinatário e evitar erros de transferência.
  - Chave Pix: A chave Pix associada à conta do destinatário, que pode ser um CPF, 
  e-mail, número de telefone ou chave aleatória. O Pix é um sistema de pagamento 
  instantâneo, e a chave ajuda a direcionar a transferência de forma rápida e segura.
  - Valor da transferência: O montante exato que o usuário deseja transferir para a 
  conta do destinatário. Esse valor deve ser especificado claramente para evitar 
  qualquer erro na transação.

Ao fornecer todos esses dados, o sistema pode processar a transação bancária externa
de forma precisa e eficiente, garantindo que os fundos sejam transferidos para o 
destinatário correto e que a operação seja concluída com sucesso.

Após inserir todos esses dados, o usuário tem a opção de adicionar uma nova operação ou 
finalizar a transação. Se o usuário optar por adicionar uma nova operação, essas 
operações serão acumuladas em uma lista. Quando a lista estiver completa, ela é enviada
para a fila de execução.

Antes de serem enviadas para a fila de execução, é realizada uma semiexecução. Durante 
a semiexecução, todas as operações na lista são executadas com um valor nulo, 
garantindo que não haja alterações no saldo das contas. Essa etapa é crucial para 
detectar possíveis erros. Se um erro for encontrado, a lista específica de transações 
é cancelada e removida da fila de operações. Em seguida, o processo é repetido para a 
próxima lista, se houver.

Se não houver erros durante a semiexecução, as operações são então executadas 
normalmente. Após a conclusão das operações, elas são removidas da lista, garantindo
que a fila de operações seja processada de forma eficiente e segura.


<h3>Transações Bancárias Sequenciais</h3>

Na aplicação, as transações são realizadas de forma sequencial. Isso significa que cada 
transação é executada uma após a outra, garantindo que não ocorram erros ou inconsistências
nos saldos das contas. Esse método sequencial assegura a correta execução de cada 
transação, mantendo a integridade e a consistência dos dados financeiros no sistema.


<h3>Transações Bancárias Concorrentes</h3>

O sistema possibilita a execução de transações bancárias concorrentes por meio de 
scripts. Para isso, foi implementada a seguinte função:

```
  async def create_request(url):
      async with aiohttp.ClientSession() as session:
          async with session.get(url) as response:
              return await response.text()
  
  async def main():
      url = 'http://localhost:5000/transfer/1/2/100'
      tasks = [create_request(url) for url in urls]
      resultados = await asyncio.gather(*tasks)
      for response in responses:
          print(response)
  
  asyncio.run(main())
```

Dessa forma, as transações podem ser enviadas de forma paralela para o sistema bancário, 
contanto que as URLs corretas sejam adicionadas. Esse método de execução paralela é 
empregado para simular um ambiente real onde múltiplas transações ocorrem 
simultaneamente. O sistema é projetado para gerenciar essas transações de maneira 
precisa, garantindo a integridade e consistência dos saldos das contas, sem erros ou
inconsistências.

</div>


<div align="justify">
  <h2>Tratamento da Confiabilidade</h2>

Com relação ao tratamento de confiabilidade, é importante ressaltar que o algoritmo de 
multicast ordenado não é projetado para garantir a confiabilidade no sentido de tolerância
a falhas ou recuperação automática caso um dos bancos falhe durante uma operação.

Dessa forma, a solução proposta para garantir a confiabilidade é a implementação de um
macanismo de verificação de conexão. Nesse caso, foi criada uma thread que verifica 
continuamente, a cada 5 segundos, se os servidores do consórcio estão ativos ou não.
Essa verificação é feita por meio de uma conexão via socket com cada servidor. Caso haja
um erro na conexão, a thread muda o status do servidor no dicionário de servidores para
offline. Dessa forma, caso um banco esteja inativo, o sistema não poderá realizar 
transações até que o banco volte a ficar online. Tratando-se de um consórcio de bancos,
para que não haja erros ou inconsistências nas filas de operações, é necessário que todos
os bancos estejam ativos e online.

Após o retorno da conexão, o sistema poderá continuar a realizar transações normalmente,
garantindo a confiabilidade e a integridade dos dados financeiros. 

Esse mecanismo pode ser visto na imagem abaixo:

<div align="center">
  <img src="/images/conexao.png" width="1920" height="1080">
</div>

Nessa imagem, tem-se o banco 1 criando uma operação. Após isso, o banco 1 empacota essa 
operação e faz a verificação: se o banco 2 está online, o banco 3 e o banco 4. Caso 
qualquer uma das opções seja falsa, a operação é cancelada e retirada da fila de execução.
Assim, é retornada uma mensagem informando que um dos bancos está inativo e, por tanto, 
não é possível realizar a transação. Caso todos os bancos estejam online, a operação é
enviada para a fila de execução e, posteriormente, é executada.

Além disso, o sistema também faz uso de exceções para tratar erros e garantir que as
transações sejam realizadas de forma correta. As exceções são lançadas quando ocorre um
erro, e são capturadas para que o sistema possa lidar com o erro de forma correta.

</div>

<div align="center">
  <img src="/images/divisor.jpg" width="1280" height="5">
</div>

<div align="justify">
  <h2>Docker</h2>

Para facilitar a execução do sistema, foi criado um arquivo Dockerfile que contém as 
instruções necessárias para a criação de uma imagem Docker. Esse arquivo é responsável
por definir o ambiente de execução do sistema, incluindo as dependências e configurações
necessárias para a execução do sistema.

O Dockerfile contém as seguintes instruções:

```
  FROM python:3.8
  WORKDIR /app
  COPY . /app
  RUN pip install -r requirements.txt
  CMD ["python", "app.py"]
```

</div>


## Testes

Para garantir a qualidade e a eficiência do sistema, foram realizados testes unitários e
de integração. Os testes unitários foram feitos para verificar o funcionamento correto de
cada função e módulo do sistema, enquanto os testes de integração foram realizados para
verificar a interação entre os diferentes módulos e componentes do sistema.

Esses testes estão disponíveis no arquivos


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

