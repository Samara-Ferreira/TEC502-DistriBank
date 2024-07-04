<div align="center">
  <img src="/images/logo.png" width="120" height="120">
<h1> TEC502-DistriBank </h1>
</div>


<div align="justify">

>Este projeto, intitulado "DistriBank", foi desenvolvido como parte 
da disciplina MI - Concorrência e Conectividade do curso de Engenharia
de Computação da Universidade Estadual de Feira de Santana (UEFS).
Ele representa um sistema de transações bancárias distribuído, criado
para explorar conceitos de concorrência e conectividade em ambientes
computacionais distribuídos.

</div>  

<div align="center">
  <img src="/images/divisor.jpg" width="1280" height="5">
</div>


<h2>Sumário</h2>
<div id="sumario">

- <A href = "#Introducao">Introdução</A><br>
- <A href = "#descricao-projeto">Descrição do Projeto</A><br>
  - <A href = "#requisitos-funcionalidades">Requisitos e Funcionalidades do Sistema</A><br>
- <A href = "#componentes">Componentes Principais do Sistema</A><br>
  - <A href = "#aplicacao">Aplicação</A><br>
  - <A href = "#servidores">Servidores</A><br>
- <A href = "#comunicacao-servidores">Comunicação entre Servidores</A><br>
  - <A href = "#rotas-comunicacao">Rotas de Comunicação</A><br>
- <A href = "#algoritmos">Algoritmos da Concorrência Distribuída</A><br>
  - <A href = "#relogio-vetorial">Relógio Vetorial</A><br>
  - <A href = "#multicast">Multicast Totalmente Ordenado</A><br>
    - <A href = "#busca-binaria">Busca Binária e Ordenação</A><br>
    - <A href = "#id">ID Único de Transação</A><br>
    - <A href = "#ACKs">ACKs e Confirmação de Transações</A><br>
    - <A href = "#fila-execucao">Fila de Execução</A><br>
    - <A href = "#lock">Locks e Exclusão Mútua</A><br>
  - <A href = "#exemplo-comunicacao">Exemplo de Comunicação</A><br>
- <A href = "#transacoes">Transações Bancárias</A><br>
  - <A href = "#transacoes-internas">Transações Bancárias Internas</A><br>
  - <A href = "#transacoes-externas">Transações Bancárias Externas</A><br>
  - <A href = "#transacoes-sequenciais">Transações Bancárias Sequenciais</A><br>
  - <A href = "#transacoes-concorrentes">Transações Bancárias Concorrentes</A><br>
- <A href = "#confiabilidade">Tratamento de Erros e Confiabilidade</A><br>
  - <A href = "#tratamento-erros">Tratamento de Erros</A><br>
  - <A href = "#confiabilidade">Confiabilidade</A><br>
- <A href = "docker">Docker</A><br>
- <A href = "#testes">Testes de Concorrência</A><br>
- <A href = "execucao">Execução do Projeto</A><br>
- <A href = "#conclusao">Conclusão</A><br>
- <A href = "#referencias">Referências</A><br>
  
<\div>


<div align="center">
  <img src="/images/divisor.jpg" width="1280" height="5">
</div>


<A name= "Introducao"></A>
<div align="justify">
  <h2>Introdução</h2>

No cenário atual, a tecnologia desempenha um papel fundamental
na vida das pessoas, e o setor financeiro não é exceção. Com os 
avanços tecnológicos, os bancos têm procurado inovações para melhor 
atender às necessidades de seus clientes. Uma das soluções encontradas 
foi a criação de sistemas de transações bancárias distribuídos. Esses 
sistemas permitem que transações sejam realizadas entre contas de 
diferentes bancos sem a necessidade de um intermediário central, como 
o Banco Central.

O projeto DistriBank foi desenvolvido para atender a essa demanda, 
sendo um sistema de transações bancárias distribuído que possibilita 
a execução rápida e segura de transações entre contas de diferentes 
bancos.

</div>


<div align="center">
  <img src="/images/divisor.jpg" width="1280" height="5">
</div>


<A name= "descricao-projeto"></A>
<div align="justify">
  <h2>Descrição do projeto</h2>

O sistema DistriBank é um sistema de transações bancárias distribuído
que facilita transações entre contas de diferentes bancos sem a 
necessidade de um intermediário central, como o Banco Central. O 
sistema consiste em múltiplos servidores, cada um representando um 
banco do consórcio, que se comunicam entre si para realizar as transações. 
Nos testes apresentados, foram criadas quatro instâncias de servidores, cada 
uma com uma porta específica para facilitar a comunicação entre eles. 
É possível expandir o sistema para utilizar mais servidores, contanto 
que a configuração adequada para a comunicação entre eles seja feita.

Abaixo, tem-se a arquitetura geral do sistema para tres bancos e tres 
aplicações, e as possíveis conexões entre si.

<div align="center">
  <img src="/images/arquitetura.png">
</div>
<p align="center"><strong>Figura 1: Arquitetura do sistema DistriBank </strong></p>

Para o desenvolvimento do projeto DistriBank, foi utilizada a linguagem
de programação Python em conjunto com o framework Flask. O Flask 
permitiu criar APIs de forma simples e eficiente para o sistema de 
transações bancárias distribuídas. Além disso, utilizei a biblioteca 
requests para facilitar a comunicação entre os servidores, utilizando 
o protocolo HTTP.

O ambiente de desenvolvimento principal foi o PyCharm, porém o projeto
é compatível com qualquer IDE de preferência do usuário ou pode ser
executado diretamente no terminal.


  <A name= "requisitos-funcionalidades"></A>
  <h3>Requisitos e Funcionalidades do Sistema</h3>

O sistema DistriBank foi desenvolvido com os seguintes requisitos e funcionalidades:

1. **Criação de contas bancárias** para pessoa física e jurídica.
2. **Realização de transações bancárias** entre contas de diferentes 
bancos.
3. **Realização de transações bancárias internas** entre contas do 
mesmo banco.
4. **Execução de transações bancárias sequenciais** para garantir a 
ordem e consistência das operações.
5. **Execução de transações bancárias concorrentes** para simular 
cenários de alta demanda.
6. **Verificação de conexão entre os servidores** para garantir a 
disponibilidade e comunicação adequada.
7. **Tratamento de erros** e retorno de conexão para lidar com situações
inesperadas de forma adequada.
8. **Execução do sistema em containers Docker** para facilitar a 
implantação e manutenção do ambiente de desenvolvimento.

Esses requisitos e funcionalidades garantem que o DistriBank seja um 
sistema robusto e eficiente para transações bancárias distribuídas.

</div>


<div align="center">
  <img src="/images/divisor.jpg" width="1280" height="5">
</div>


<A name= "componentes"></A>
<div id="componentes" align="justify">
  <h2>Componentes Principais do Sistema</h2>

No sistema DistriBank, os principais componentes são a aplicação e os
servidores, que atuam como representantes dos bancos consorciados. 


  <A name= "aplicacao"></A>
  <h3>Aplicação</h3>

A aplicação desempenha um papel crucial ao facilitar a comunicação entre os 
servidores por meio de um protocolo específico. Esse protocolo viabiliza a 
transferência de informações essenciais para a realização de transações 
bancárias entre contas de diferentes instituições financeiras.

A estrutura da aplicação DistriBank é composta por diversos componentes 
essenciais, cada um desempenhando um papel crucial na operação do sistema 
distribuído de transações bancárias. Os arquivos que compõem essa estrutura
são organizados da seguinte forma:

    ├── __init__.py
    ├── __main__.py
    ├── AccountCreation.py
    ├── AccountManagement.py
    ├── Application.py
    ├── Transactions.py
    ├── Dockerfile 

Para cada um desses arquivos, tem-se as seguintes funções:

- init.py: Este arquivo inicializa o pacote da aplicação, preparando o
ambiente para a execução dos módulos subsequentes;

- main.py: Como o arquivo principal da aplicação, é responsável por iniciar o
sistema e coordenar a comunicação entre os servidores bancários distribuídos;

- AccountCreation.py: Aqui são definidas as classes e funções dedicadas à
criação de novas contas bancárias, atendendo tanto a pessoas físicas quanto
jurídicas;

- AccountManagement.py: é o arquivo responsável por realizar a gestão de
contas bancárias;

- Application.py: é o arquivo responsável por realizar a comunicação entre
os servidores;

- Transactions.py: é o arquivo responsável por realizar as transações bancárias;

- Dockerfile: é o arquivo responsável por criar a imagem do Docker.

A aplicação foi feita utilizando uma interface de linha de comando (CLI),
que permite ao usuário interagir com o sistema de forma intuitiva e eficiente.

Abaixo, estão as 3 principais telas do sistema:

1. **Tela de escolha de qual banco irá se conectar**:
    - Nesta tela, o usuário escolhe com qual banco deseja se conectar,
    escolhendo entre os bancos 1, 2, 3 e 4.

<div align="center">
  <img src="/images/cli1.jpg">
</div>
<p align="center"><strong> Tela de escolha de banco </strong></p>

2. **Tela de operações bancárias**:
    - Nesta tela, o usuário pode escolher entre as operações para fazer
   login, criar uma conta, ver todos os clientes cadastrados no banco
   e também, ver todo o extrato bancário.

<div align="center">
  <img src="/images/cli2.jpg">
</div>
<p align="center"><strong> Tela de operações bancárias </strong></p>

3. **Tela de operações da conta**:
    - Nesta tela, o usuário poderá criar uma nova chave pix, listar
   todas as chaves que tem cadastradas, fazer um depósito, fazer um
    saque, fazer uma transferência e deslogar da conta.

<div align="center">
    <img src="/images/cli3.jpg">
</div>
<p align="center"><strong> Tela de operações da conta </strong></p>

Além da aplicação principal, o sistema utiliza scripts especializados para 
implementar transações bancárias concorrentes. Essa abordagem permite 
simular situações reais onde múltiplas transações são processadas 
simultaneamente, testando a capacidade do sistema em lidar com uma alta 
carga de operações de forma resiliente e eficaz. Alguns scripts prontos
estão dizponíveis no diretório `tests`, como será abordado na seção 
de testes.


  <A name= "servidores"></A>
  <h3>Servidores</h3>

Por sua vez, os servidores são responsáveis por armazenar dados detalhados 
das contas bancárias dos usuários e executar operações fundamentais, como a
criação de novas contas e a condução de transações financeiras. Essa 
estrutura permite que o DistriBank opere de maneira eficiente e segura, 
garantindo a integridade e a precisão das operações bancárias realizadas 
pelos usuários.

Os bancos são os servidores que compõem o sistema.

Os bancos, que funcionam como servidores no sistema, são a espinha dorsal 
do DistriBank. Abaixo, são apresentados os diretórios e arquivos 
que compõem essa estrutura:

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

Os principais arquivos e suas funções dentro da arquitetura do DistriBank são:

- main.py: Como o arquivo principal do servidor, é responsável por 
inicializar e coordenar as operações bancárias essenciais. Este componente
assegura que o servidor esteja pronto para receber e processar requisições,
mantendo a integridade das transações;

- Bank.py: Armazena de forma centralizada todas as informações das contas
bancárias e implementa as operações bancárias fundamentais. Este arquivo
garante a consistência e segurança dos dados durante todas as operações 
realizadas pelo DistriBank;

- Queue.py: Cria e gerencia a fila de execução, essencial para garantir 
a ordem e correção das transações. Esta estrutura é projetada para minimizar
erros e inconsistências nos saldos das contas ao coordenar a execução das 
operações bancárias de forma sequencial e organizada;

- UniqueTwoDigitID.py: Gera IDs únicos de dois dígitos, fundamentais 
para a identificação e confirmação das transações entre os bancos 
participantes. Este componente assegura que cada transação seja devidamente
identificada e rastreada dentro do sistema distribuído;

- VectorialClock.py: Implementa o relógio vetorial, utilizado para ordenar
as transações na fila de execução com base no tempo vetorial associado
a cada operação. Este arquivo é crucial para garantir a precisão temporal
e a correta execução das transações distribuídas pelo DistriBank;

- Dockerfile: Define os passos necessários para a criação da imagem Docker
que encapsula todo o ambiente de desenvolvimento e produção do DistriBank.
Este arquivo simplifica o processo de implantação e escalabilidade do 
sistema em diferentes ambientes de execução;

- api/API.py: Gerencia a comunicação entre os servidores, facilitando a 
troca de informações críticas para a realização das transações bancárias
distribuídas. Este componente assegura uma integração eficiente e segura
entre os diferentes nós do sistema DistriBank;

- api/FloatConverter.py: Converte os valores das transações, garantindo 
a consistência e precisão dos dados financeiros manipulados pelo DistriBank.
Este arquivo é essencial para assegurar que todas as transações sejam
realizadas com exatidão matemática, evitando erros de arredondamento ou
imprecisões nos cálculos financeiros;

- clients/JointClient.py, clients/JuridicClient.py, clients/PhysicalClient.py: 
Implementam operações específicas para diferentes tipos de clientes bancários,
como contas conjuntas, jurídicas e físicas. Cada arquivo oferece funcionalidades
adaptadas às necessidades e exigências de cada categoria de conta dentro do
ecossistema do DistriBank;

- exceptions/Exceptions.py: Gerencia e trata exceções que podem ocorrer 
durante a execução das operações bancárias, garantindo um tratamento 
adequado de situações inesperadas e mantendo a robustez do sistema. Este 
arquivo é crucial para a estabilidade e confiabilidade do DistriBank em 
face de cenários adversos;

- utils/Utils.py: Oferece funções utilitárias diversas do sistema.

</div>


<div align="center">
  <img src="/images/divisor.jpg" width="1280" height="5">
</div>


<A name= "comunicacao-servidores"></A>
<div align="justify">
  <h2>Comunicação entre os Servidores</h2>

No sistema DistriBank, a comunicação entre os bancos é realizada por meio 
de rotas definidas como URLs, que facilitam a troca de informações necessárias
para a execução das operações bancárias distribuídas. Essas rotas são
configuradas utilizando métodos HTTP padrão, como GET, POST, PUT e DELETE,
que correspondem a operações de leitura, criação, atualização e exclusão de 
dados, respectivamente.

A comunicação entre os servidores no sistema DistriBank é facilitada por um
protocolo de comunicação, que é essencial para a transferência eficiente de
informações entre os nós do sistema. Esse protocolo desempenha um papel 
crucial na coordenação das transações bancárias distribuídas, garantindo a 
integridade das operações realizadas.

A interoperabilidade entre os servidores é viabilizada por meio de uma API,
projetada para facilitar a comunicação entre os diferentes nós distribuídos
do DistriBank. Cada servidor, localizado em máquinas distintas, utiliza essa
API para trocar dados de forma, independentemente da localização física dos
servidores.

O protocolo escolhido para a comunicação entre a aplicação e os servidores 
no sistema DistriBank é o HTTP (Hypertext Transfer Protocol). Amplamente 
utilizado na web, o HTTP facilita a transferência de informações de maneira
eficiente e segura entre os diferentes componentes distribuídos do sistema.

O HTTP opera em um modelo cliente-servidor, onde o cliente envia uma
requisição para o servidor e aguarda uma resposta. Essa arquitetura é ideal
para o DistriBank, pois permite uma comunicação confiável e orientada a
mensagens entre os servidores distribuídos. Cada requisição HTTP contém
métodos padrão como GET, POST, PUT e DELETE, que são utilizados para diferentes
tipos de interações entre os componentes do sistema.


  <A name="rotas-comunicacao"></A>
  <h3>Rotas de Comunicação</h3>

Cada função da API REST do projeto DistriBank é projetada para retornar
um JSON estruturado com os dados solicitados. A seguir, são apresentados
exemplos detalhados de requisições para as principais rotas da API, destacando
como operações bancárias são realizadas de forma distribuída e segura:

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
  - Rota: /<string:company>/<string:cnpj>/<string:name>/<string:cpf>/<string:user>/<string:password>/<float:balance>
  /create_juridic_account
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
  
</div>


<div align="center">
  <img src="/images/divisor.jpg" width="1280" height="5">
</div>


<A name= "algoritmos"></A>
<div align="justify">
  <h2>Algoritmos da Concorrência Distribuída</h2>

Para assegurar o tratamento eficiente da concorrência distribuída, o sistema
do DistriBank emprega uma combinação estratégica entre o relógio vetorial 
e o algoritmo de multicast totalmente ordenado. Esses mecanismos são
essenciais para garantir a precisão e a consistência das transações bancárias,
evitando erros e inconsistências nos saldos das contas.


  <A name= "relogio-vetorial"></A>
  <h3>Relógio Vetorial</h3>

O relógio vetorial é um algoritmo fundamental no sistema DistriBank, 
projetado para coordenar o tempo das operações em um ambiente distribuído.
Ele desempenha um papel crucial na determinação da ordem das transações na
fila de execução com base em marcas de tempo lógicas associadas a cada evento.
A cada nova transação, o relógio vetorial é incrementado em uma unidade.
Quando uma transação é enviada entre os bancos, o tempo nos relógios de
cada banco é atualizado para refletir o tempo do banco que originou a
transação. Esse processo garante que todos os bancos mantenham um tempo 
sincronizado, essencial para a consistência e integridade das operações 
bancárias distribuídas.

No DistriBank, o relógio vetorial é implementado como um vetor de tamanho n, 
onde n representa o número de bancos no consórcio. Por exemplo, com quatro
instâncias de servidores no ambiente de teste, o vetor tem tamanho 4. Cada
posição no vetor armazena o tempo associado a cada banco, permitindo que 
todos os nós do sistema estejam alinhados temporalmente. Essa sincronização 
é fundamental para evitar conflitos de dados e assegurar que todas as transações
sejam processadas de acordo com uma ordem globalmente consistente.

Na representação abaixo, temos um exemplo de relógio vetorial aplicado a 
quatro processos: P1, P2, P3 e P4. Cada processo possui um relógio vetorial 
de tamanho 4, que armazena o tempo associado a cada um deles. Quando o 
processo 3 inicia uma transação, seu relógio vetorial é incrementado em uma
unidade para refletir essa operação. Em seguida, a transação é enviada ao 
processo 2, que atualiza seu próprio relógio vetorial para refletir o tempo 
do processo 3. Esse processo se repete para cada novo processo que recebe 
a transação, garantindo que todos os processos mantenham uma sincronia temporal.

O relógio vetorial no exemplo ilustra como cada processo mantém um registro 
do tempo de todos os outros processos no sistema distribuído.

<div align="center">
  <img src="/images/relogio.png">
</div>
<p align="center"><strong>Figura 2: Relógio Vetorial no DistriBank </strong></p>


  <A name= "multicast"></A>
  <h3>Multicast Totalmente Ordenado</h3>

O uso do algoritmo de multicast totalmente ordenado é essencial para 
garantir a consistência das transações no sistema distribuído do DistriBank.
Este algoritmo é responsável por assegurar que todas as mensagens enviadas 
sejam entregues a todos os destinatários na mesma ordem em que foram enviadas.
Isso é crucial para evitar que ocorram inconsistências nos saldos das contas 
bancárias durante as transações.

Quando uma transação é iniciada e seu tempo é registrado pelo relógio
vetorial, o algoritmo de multicast totalmente ordenado entra em ação para 
garantir que todas as operações relacionadas a essa transação sejam processadas
na ordem correta em todos os servidores envolvidos. Isso significa que cada
servidor recebe e processa as mensagens de transação na mesma sequência,
independentemente da ordem em que as mensagens são recebidas.

A cada nova transação no sistema DistriBank, o tempo do relógio vetorial é 
incrementado e um ID de transação de 2 dígitos é gerado de forma única.
Esse ID é composto pelos 2 últimos dígitos da porta do banco e por mais 2
dígitos gerados por uma classe específica, garantindo sua unicidade e evitando
conflitos. Esse identificador é crucial para a confirmação entre os bancos
sobre o recebimento dos pacotes de transação e é armazenado junto com o tempo
do relógio vetorial, detalhes da transação e o próprio ID em uma lista.

  
  <A name= "busca-binaria"></A>
  <h4>Busca Binária e Ordenação</h4>

Para determinar a posição correta dessa nova transação na fila de execução,
conforme seu tempo vetorial, utiliza-se um método de busca binária.
A busca binária é um algoritmo de divisão e conquista que divide a lista
de transações em duas metades e verifica se o elemento a ser inserido
deve ser colocado antes ou depois do elemento do meio. Esse processo é
repetido até que a posição correta do novo elemento seja encontrada,
garantindo que a lista permaneça ordenada de acordo com o tempo
vetorial associado a cada transação.

Esse algoritmo foi escolhido devido à sua eficiência na ordenação de 
elementos em uma lista. A busca binária não apenas acelera o processo
de inserção, mas também garante que as transações sejam ordenadas 
de acordo com seu tempo vetorial, mantendo a integridade temporal 
das operações no sistema distribuído.

Abaixo, tem-se um exemplo simplificado de como a busca binária é aplicada
para ordenar as transações na fila de execução do DistriBank. Neste exemplo,
tem-se quatro transações, cada uma com um tempo vetorial associado. A busca
binária é utilizada para determinar a posição correta de uma nova transação
com base em seu tempo vetorial, garantindo que a lista permaneça ordenada
de acordo com a sequência temporal das operações.


  <A name="id"></A>
  <h4>ID Único de Transação</h4>

O de geração de indentificador (ID) único de duas casas decimais é um
componente essencial para a identificação e rastreamento das transações
bancárias no sistema DistriBank. Esse ID é composto por quatro dígitos
totais, sendo os dois primeiros dígitos referentes à porta do banco e os
dois últimos dígitos gerados de forma única. Essa abordagem garante que
cada transação seja devidamente identificada e rastreada dentro do
sistema distribuído.

No esquema abaixo, é retratado exemplos de IDs únicos gerados para as
transações no DistriBank. Cada ID é composto por dois dígitos, que são
utilizados para identificar e rastrear as operações bancárias entre os


  <A name="ACKs"></A>
  <h4>ACKs e Confirmação de Transações></h4>

O pacote estando completo, ele é enviado então aos demais bancos do 
consórcio, nos quais são feitas as mesmas operações de organização
e criação de identificadores descritas anteriormente. Após o recebimento
dessas operações, os bancos enviam a confirmação de recebimento para
todos os outros bancos do consórcio, conhecidos como ACKs. Esses ACKs
são armazenados em um dicionário interno em cada banco, que tem como
chave o ID de cada operação e os valores são listas com todos os ACKs
recebidos daquela operação. Para saber se o número de ACKs está correto,
é feito o seguinte cálculo: 

- o número de ACKs recebidos no banco que enviou a determinada transação
é igual ao número total de bancos do consórcio menos 1;
- nos demais bancos, aquele mesmo ACKs deve ter sido recebido o número
total de bancos menos 2.

Assim, é garantido que todos os bancos receberam a transação e os outros
bancos do consórcio tem essa confirmação.


  <A name="fila-execucao"></A>
  <h4>Fila de Execução</h4>

Para garantir que todos os bancos estejam sincronizados, ou seja, 
todos eles com a mesma fila de transação, antes de executar é feita
uma verificação se o pacote é o primeiro da fila em todos os bancos.

Caso o número de ACKs esteja correto e a operação seja a primeira da
fila em todos os bancos, então é possível eleger um banco como líder
para disparar a execução das operações. Esse banco líder é aquele que
executa as operações. Caso uma dessas verificações não seja verdadeira,
significa que outra transação está sendo inserida na fila e, portanto,
não é possível executar a operação atual.


  <A name="lock"></A>
  <h4>Locks e Exclusão Mútua</h4>

Para garantir a consistência dos dados e evitar condições de corrida
em operações críticas, o DistriBank utiliza locks (travas) para controlar
o acesso a recursos compartilhados entre os bancos. Esses locks são
mecanismos essenciais para garantir a integridade das transações e
evitar conflitos de dados em um ambiente distribuído.

Quando uma transação é recebida por um banco, um lock é acionado para
travar a operação e garantir que ela seja processada de forma segura.
Isso evita que outras transações interfiram na operação em andamento,
garantindo que a execução seja concluída com sucesso e sem conflitos.


  <A name="exemplo-comunicacao"></A>
  <h3>Exemplo de Comunicação entre Bancos</h3>

Abaixo, é apresentado um exemplo de como é feita a comunicação 
entre os bancos, por meio do algoritmo de multicast totalmente 
ordenado com o relógio vetorial. Nesse exemplo, tem-se q uatro bancos
(B1, B2, B3 e B4), e cada banco possui um relógio vetorial de tamanho 4,
que é responsável por armazenar o tempo de cada banco. O banco 1 e o banco
2 recebem transações de forma paralela, com o mesmo tempo vetorial. Para
o tratamento desse tipo de operação é feito o uso dos Locks (travas),
que são mecanismos utilizados para garantir a consistência de dados em
sistemas distribuídos, especialmente em ambientes onde múltiplas 
transações podem acessar e modificar os mesmos recursos simultaneamente. 
O uso dessas travas assegura que apenas uma transação por vez possa
acessar um recurso crítico, evitando condições
de corrida e garantindo a integridade dos dados.

<div align="center">
  <img src="/images/multicast1.png">
</div>
<p align="center"><strong>Figura 3: Recebimento de novas transações </strong></p>

Nesse caso, o Lock vai travar uma das operações recebidas, e a outra poderá ser manipulada. Supoe-se que a operação
1 seja escolhida para manipulação e a operação 2 seja travada. Dessa forma, a operação 1 é inserida na fila do banco 
1 e é enviada para ser inserida na fila dos demais bancos, como pode ser visto na imagem abaixo.

<div align="center">
  <img src="/images/multicast2.png">
</div>
<p align="center"><strong>Figura 4: Envio de operações para os demais bancos </strong></p>

Após isso, é feita a verificação do número de ACKs, que são a confirmação de recebimento dos pacotes. Como pode ser
visualizado na imagem abaixo, o banco 1 recebeu o ACK do banco 2, 3 e 4, mas não fez envio. Já o banco 2 recebeu
ACKs do banco 3 e do banco 4, enquanto o banco 3 recebeu ACKs do banco 4 e 2, e o banco 4 recebeu ACKs do banco 2 e 3.
Assim, é possível visualizar a fórmula de cálculo do número de ACKs, que foi descrita anteriormente, pois o banco 
que enviou a operação deve receber o número total de bancos menos 1, e os demais bancos devem receber o número total
de bancos menos 2.

<div align="center">
  <img src="/images/multicast3.png">
</div>
<p align="center"><strong>Figura 5: Verificação do número de ACKs </strong></p>

Recebido o número de ACKs, tem-se que verificar a se a operação que é a primeira da lista no banco 1 é a mesma 
dos demais bancos. Com a liberação do Lock, a operação 2 é liberada e inserida na fila do banco 2, e, dessa forma, 
a OP1 não é a primeira da fila em todos os bancos, retornando falso para essa verificação. Logo, o banco 1 não 
poderá executar a operação 1, pois mais operações estão sendo inseridas na fila. Essa representação pode ser
vista na imagem abaixo.

<div align="center">
  <img src="/images/multicast4.png">
</div>
<p align="center"><strong>Figura 6: Verificação da fila de execução </strong></p>

Agora com a operação 2, repete-se o mesmo processo anterior: essa nova transação deve ser enviada para os demais
bancos, assim mostrado na imagem abaixo, como na operação 1.

<div align="center">
  <img src="/images/multicast5.png">
</div>
<p align="center"><strong>Figura 7: Envio de operações para os demais bancos </strong></p>

E, por fim, é feita a verificação do número de ACKs e da posição da operação na fila de execução. Como todos os 
bancos tem a mesma operação como a primeira da fila, então o banco 2 pode ser eleito um lider e disparar a 
execução das operações da lista. Assim, a operação 2 é executada e, após isso, a operação 1 é executada, pois
a operação 2 foi a primeira da fila. Essa última parte da verificação pode ser vista na imagem abaixo.

<div align="center">
  <img src="/images/multicast6.png">
</div>
<p align="center"><strong>Figura 8: Verificação da fila de execução </strong></p>

Para as operações sequenciais, o sistema segue o mesmo passo a passo so que, nesse caso, o lider será aquele
banco que estiver enviando a operação. Ou seja, pode ser feita a eleição de um lider para cada operação, e,
dessa forma, garantir que as operações sejam realizadas na ordem.

</div>


<div align="center">
  <img src="/images/divisor.jpg">
</div>


<A name= "transacoes"></A>
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
  <img src="/images/atomicidade1.png">
</div>
<p align="center"><strong>Figura 9: Semiexecução das operações </strong></p>

No caso registrado abaixo, tem-se o exemplo de que a operação de transferencia do banco 1
para o banco 4 não foi bem sucedida, por motivos que podem ser: saldo insuficiente, conta
inexistente, entre outros. Nesse caso, a toda operação é cancelada e retirada da fila de 
execução, como pode ser visto, que mesmo as outras que não houve inconsistencias, foram 
canceladas de serem executadas.

<div align="center">
  <img src="/images/atomicidade2.png">
</div>
<p align="center"><strong>Figura 10: Cancelamento das operações </strong></p>

Já em outro caso, como o abaixo, todas as operações foram bem sucedidas e, dessa forma,
foram retiradas da fila de execução, como pode ser visto.

<div align="center">
  <img src="/images/atomicidade3.png">
</div>
<p align="center"><strong>Figura 11: Execução das operações </strong></p>


  <A name="transacoes-internas"></A>
  <h3>Transações Bancárias Internas</h3>

O sistema permite a execução de transações bancárias internas, possibilitando 
transferências entre contas do mesmo banco, além das opções de depósito e saque, que se 
referem à conta do próprio usuário que está utilizando o sistema no momento.


  <A name="transacoes-externas"></A>  
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


  <A name="transacoes-sequenciais"></A>
  <h3>Transações Bancárias Sequenciais</h3>

Na aplicação, as transações são realizadas de forma sequencial. Isso significa que cada 
transação é executada uma após a outra, garantindo que não ocorram erros ou inconsistências
nos saldos das contas. Esse método sequencial assegura a correta execução de cada 
transação, mantendo a integridade e a consistência dos dados financeiros no sistema.


  <A name="transacoes-concorrentes"></A>
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


<div align="center">
  <img src="/images/divisor.jpg">
</div>


<A name= "confiabilidade"></A>
<div align="justify">
  <h2>Tratamento de Erros e Confiabilidade</h2>

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
  <img src="/images/conexao.png">
</div>
<p align="center"><strong>Figura 12: Verificação de Conexão </strong></p>

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
  <img src="/images/divisor.jpg">
</div>


<A name= "docker"></A>
<div align="justify">
  <h2>Docker</h2>

Para facilitar a execução do sistema, foi criado um arquivo Dockerfile que contém as 
instruções necessárias para a criação de uma imagem Docker. Esse arquivo é responsável
por definir o ambiente de execução do sistema, incluindo as dependências e configurações
necessárias para a execução do sistema.

</div>


<div align="center">
  <img src="/images/divisor.jpg">
</div>


<A name= "testes"></A>
<div align="justify">
  <h2>Testes de Concorrência</h2>

Para garantir a qualidade e a eficiência do sistema, foram realizados testes unitários e
de integração. Os testes unitários foram feitos para verificar o funcionamento correto de
cada função e módulo do sistema, enquanto os testes de integração foram realizados para
verificar a interação entre os diferentes módulos e componentes do sistema.

Esses testes estão disponíveis no arquivos:

- tests\AccountTest.py: testes unitários para a classe Account, que
são relacionados com as funções que envolve as contas dos usuários;
- tests\Transaction.py: testes unitários para a classe Transaction,
que são relacionados com as funções que envolvem as transações bancárias.

Para executar os testes, basta executar o comando abaixo:

```
python tests\AccountTest.py
python tests\Transaction.py
python tests\TransNew.py
```


<div align="center">
  <img src="/images/divisor.jpg">
</div>


<A name= "execucao"></A>
<div id="execucao" align="justify">
  <h2>Execução do Projeto</h2>

O projeto pode ser executado com ou sem a utilização do Docker. A
execução sem o Docker requer a instalação das dependências do projeto.

Primeiramente, é necessário obter o repositório do projeto. Ele pode ser
obtido clonando o repositório do GitHub, caso tenha o Git instalado
na máquina, ou baixando o arquivo ZIP do projeto.

  <A name= "execucao-sem-docker"></A>
  <h3>Execução sem Docker</h3>

Para a execução do projeto sem o Docker, tem-se os seguitnes pré-
requisitos:

- Python 3.8 ou superior;
- Pip, para instalação das dependências do projeto.
- Bibliotecas do Python, como o Flask e a requests.

Para instalar as dependências do projeto, basta executar o comando 
abaixo, nos diretórios da aplicação e do consórcio:

```
  pip install -r requirements.txt
```

Após a instalação das dependências, o projeto pode ser executado 
utilizando o comando abaixo, nos diretórios da aplicação e do consórcio:

```
  python __main__.py
```

  <A name= "execucao-com-docker"></A>
  <h3>Execução com o Docker</h3>

Para a execução com o Docker, primeiramente obtem o diretório
de cada um dos componentes executando o seguinte comando

```
  docker pull samarasf/app
```

```
  docker pull samarasf/bank
```

Após a obtenção dos diretórios, o projeto pode ser executado
utilizando o comando abaixo, nos diretórios da aplicação e do consórcio:

```
  docker run --network=host -it -e PORT=555x samarasf/bank
```

```
  docker run --network=host -it samarasf/app
```

</div>


<div align="center">
  <img src="/images/divisor.jpg">
</div>


<A name= "conclusao"></A>
<div align="justify">
  <h2>Conclusão</h2>
  
O sistema DistriBank é uma solução inovadora e eficiente para
a realização de transações bancárias em um ambiente distribuído.
Por meio do uso de algoritmos avançados, como o relógio vetorial
e o multicast totalmente ordenado, o sistema garante a precisão
e a consistência das operações bancárias, evitando erros e
inconsistências nos saldos das contas.

</div>


<div align="center">
  <img src="/images/divisor.jpg">
</div>


<A name= "referencias"></A>
<div align="justify">
  <h2>Referências</h2>

https://edisciplinas.usp.br/pluginfile.php/3609782/mod_resource/content/1/aula-12.pdf

</div>
