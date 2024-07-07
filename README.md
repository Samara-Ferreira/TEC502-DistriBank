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
  - <A href = "#tecnologias">Tecnologias Utilizadas</A><br>
  - <A href = "#requisitos-funcionalidades">Requisitos e Funcionalidades do Sistema</A><br>
- <A href = "#componentes">Componentes Principais do Sistema</A><br>
  - <A href = "#aplicacao">Aplicação</A><br>
  - <A href = "#servidores">Servidores</A><br>
- <A href = "#comunicacao-servidores">Comunicação entre os Servidores</A><br>
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
- <A href = "#testes">Testes de Concorrência</A><br>
- <A href = "execucao">Execução do Projeto</A><br>
- <A href = "#conclusao">Conclusão</A><br>
- <A href = "#referencias">Referências</A><br>


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

O projeto _DistriBank_ foi desenvolvido para atender a essa demanda, 
sendo um sistema de transações bancárias distribuído que possibilita 
a execução rápida e segura de transações entre contas de diferentes 
bancos.

</div>


<div align="center">
  <img src="/images/divisor.jpg" width="1280" height="5">
</div>


<A name= "descricao-projeto"></A>
<div align="justify">
  <h2>Descrição do Projeto</h2>


O sistema _DistriBank_ é uma solução de transações bancárias distribuídas que 
facilita transações entre contas de diferentes bancos sem a necessidade de um
intermediário central, como o Banco Central. O sistema é composto por múltiplos
servidores, cada um representando um banco do consórcio, que se comunicam entre
si para realizar as transações de forma eficiente e segura.

Nos testes realizados, foram criadas quatro instâncias de servidores, cada uma
configurada com uma porta específica para facilitar a comunicação entre eles.
A arquitetura do sistema permite a expansão para incluir mais servidores, desde
que a configuração adequada para a comunicação entre eles seja implementada 
corretamente.

A seguir, é apresentada a arquitetura geral do sistema, exemplificando a
configuração para quatro bancos e quatro aplicações, juntamente com as 
possíveis conexões entre eles:

<div align="center">
  <img src="/images/arquitetura.png">
</div>
<p align="center"><strong>Figura 1: Arquitetura do sistema DistriBank </strong></p>

Cada servidor (banco) é configurado para se comunicar com as aplicações 
mediante portas específicas, permitindo uma interação direta e sem 
intermediários centralizados.


  <A name= "tecnologias"></A>
  <h3>Tecnologias Utilizadas</h3>

Para o desenvolvimento do projeto _DistriBank_, foi utilizada a linguagem de 
programação Python em conjunto com o _framework_ _Flask_. O _Flask_ facilitou a 
criação de Interfaces de Programação de Aplicações (APIs) simples e eficientes 
para o sistema de transações bancárias distribuídas. Além disso, foram
empregadas várias bibliotecas para aprimorar a comunicação e garantir a
eficiência do sistema.

As principais tecnologias utilizadas no projeto foram:

- _**Flask:**_ _Framework_ utilizado para criar APIs de maneira simples e 
eficiente;
- _**Requests:**_ Biblioteca empregada para facilitar a comunicação entre os 
servidores através do Protocolo de Transferência de Hipertexto (HTTP);
- _**Asyncio:**_ Biblioteca que fornece suporte para operações assíncronas, 
permitindo uma melhor gestão de tarefas simultâneas;
- _**Aiohttp:**_ Biblioteca utilizada para realizar requisições HTTP de forma 
assíncrona, aumentando a eficiência e a capacidade de lidar com múltiplas
conexões simultaneamente;
- _**Docker:**_ Ferramenta utilizada para criar contêineres que facilitam a 
implementação, execução e escalabilidade do sistema.

O ambiente de desenvolvimento principal foi o PyCharm, que oferece uma 
_‘interface’_ robusta e ferramentas integradas para codificação, depuração e testes
do projeto. No entanto, o DistriBank é compatível com qualquer Ambiente de
Desenvolvimento Integrado (IDE) de preferência do usuário e pode também ser
executado diretamente no terminal, sem a necessidade de uma IDE específica.

  <A name= "requisitos-funcionalidades"></A>
  <h3>Requisitos e Funcionalidades</h3>

O sistema _DistriBank_ foi desenvolvido com um conjunto abrangente de requisitos
e funcionalidades para atender às necessidades de transações bancárias 
distribuídas. As principais características incluem:

1. **Criação de Contas Bancárias:** Suporte para a criação de contas de pessoa 
física e jurídica, permitindo uma ampla gama de clientes;
2. **Transações Bancárias Entre Bancos:** Capacidade de realizar transações 
entre contas de diferentes bancos, eliminando a necessidade de intermediários
centrais como o Banco Central;
3. **Transações Sequenciais:** Execução de transações de forma sequencial
para garantir a ordem e a consistência das operações, essencial para a
integridade dos dados financeiros;
4. **Transações Concorrentes:** Suporte para a execução de transações 
concorrentes, simulando cenários de alta demanda e testando a resiliência do
sistema;
5. **Verificação de Conexão:** Implementação de verificações regulares entre 
os servidores para garantir a disponibilidade e a comunicação adequada;
6. **Tratamento de Erros:** Mecanismos robustos para lidar com erros e retornar
conexões de forma adequada, garantindo a estabilidade do sistema em situações
inesperadas;
7. **Execução em Contêineres Docker:** Utilização de contêineres _Docker_ para
facilitar a implantação e manutenção do ambiente de desenvolvimento, 
assegurando consistência e portabilidade.

Esses requisitos e funcionalidades tornam o DistriBank um sistema completo 
para a realização de transações bancárias distribuídas, proporcionando
segurança para os bancos e seus clientes.

</div>


<div align="center">
  <img src="/images/divisor.jpg" width="1280" height="5">
</div>


<A name= "componentes"></A>
<div id="componentes" align="justify">
  <h2>Componentes Principais do Sistema</h2>

No sistema _DistriBank_, os principais componentes são a aplicação e os 
servidores, que atuam como representantes dos bancos consorciados. A aplicação
é responsável pela comunicação entre os servidores, utilizando um protocolo
que permite a transferência de informações para a realização de transações 
bancárias. Já os servidores têm a função de armazenar informações das contas
bancárias e realizar operações como a criação de contas e transações.
Adicionalmente, o sistema pode utilizar _scripts_ para simular transações 
bancárias concorrentes, representando um cenário real onde múltiplas transações
ocorrem simultaneamente.

A seguir, são detalhados os principais componentes do sistema DistriBank e
suas funções dentro da arquitetura distribuída de transações bancárias.

  <A name= "aplicacao"></A>
  <h3>Aplicação</h3>

A aplicação _DistriBank_ desempenha um papel essencial na facilitação da 
comunicação entre os servidores, utilizando um protocolo específico que permite
a transferência de informações críticas para a realização de transações 
bancárias entre contas de diferentes instituições financeiras.

A estrutura da aplicação _DistriBank_ é composta por diversos componentes, 
organizados da seguinte forma:

    ├── __init__.py
    ├── __main__.py
    ├── AccountCreation.py
    ├── AccountManagement.py
    ├── Application.py
    ├── Transactions.py
    ├── Dockerfile 

Para cada um desses arquivos, as funções desempenham papéis específicos no 
sistema DistriBank:


- **init.py:** Este arquivo inicializa o pacote da aplicação, preparando o
ambiente para a execução dos módulos subsequentes;

- **main.py:** Como o arquivo principal da aplicação, é responsável por 
iniciar o sistema e coordenar a comunicação entre os servidores bancários 
distribuídos;

- **AccountCreation.py:** Definição das classes e funções que facilitam a 
criação de novas contas bancárias dentro do sistema. Ele suporta tanto contas 
de pessoas físicas quanto jurídicas;

- **AccountManagement.py:** Responsável pela gestão e administração das 
contas bancárias dentro do sistema;

- **Application.py:** Encarregado de facilitar a comunicação entre os 
diferentes servidores bancários distribuídos;

- **Transactions.py:** Responsável pela implementação das operações de 
transações bancárias dentro do sistema _DistriBank_;

- **Dockerfile:** Este arquivo é utilizado para definir e construir a 
imagem do Docker que encapsula todo o ambiente de execução do sistema
DistriBank. Ele facilita a implantação e execução do sistema em diferentes 
ambientes de maneira consistente e confiável.

O DistriBank foi projetado com uma interface de linha de comando (CLI) 
intuitiva, permitindo aos usuários interagir facilmente com o sistema para 
realizar operações bancárias distribuídas entre diferentes bancos consorciados.
Abaixo, são apresentadas as principais telas e funcionalidades da CLI:

1. **Tela de Escolha de Banco**:
    - Na tela inicial, o usuário pode selecionar com qual banco deseja 
   interagir. As opções disponíveis incluem os bancos 1, 2, 3 e 4, cada um
   representando uma instância do servidor DistriBank.

<div align="center">
  <img src="/images/cli1.jpg">
</div>
<p align="center"><strong>Figura 2: Tela de escolha de banco </strong></p>

2. **Tela de Operações Bancárias**:
    - Após escolher o banco, o usuário é apresentado à tela de operações 
   bancárias. Aqui, ele tem acesso a funcionalidades essenciais para gerenciar
   sua conta bancária.

<div align="center">
  <img src="/images/cli2.jpg">
</div>
<p align="center"><strong>Figura 3: Tela de operações bancárias </strong></p>

3. **Tela de Operações da Conta**:
    - Ao acessar a conta bancária, o usuário é direcionado para a tela de 
   operações específicas da conta. Aqui, ele pode realizar uma série de
   operações.

<div align="center">
    <img src="/images/cli3.jpg">
</div>
<p align="center"><strong>Figura 4: Tela de operações da conta </strong></p>


Além da aplicação principal, o sistema _DistriBank_ utiliza _scripts_ 
especializados para implementar transações bancárias concorrentes. Essa 
abordagem permite simular situações reais onde múltiplas transações são 
processadas simultaneamente, testando a capacidade do sistema em lidar com uma
alta carga de operações de forma resiliente e eficaz. Esses _scripts_, 
disponíveis no diretório ``tests``, são fundamentais para garantir a robustez do
sistema sob condições de alta demanda. Detalhes sobre esses _scripts_ serão 
abordados na seção de testes.


  <A name= "servidores"></A>
  <h3>Servidores</h3>

Os servidores no sistema _DistriBank_ desempenham um papel crucial, 
armazenando dados detalhados das contas bancárias dos usuários e executando
operações fundamentais, como a criação de novas contas e a realização de 
transações financeiras. Essa arquitetura garante que o _DistriBank_ opere de
maneira eficiente e segura, assegurando a integridade e precisão das operações
bancárias realizadas pelos usuários.

Os bancos, que funcionam como servidores no sistema, são a espinha dorsal do
_DistriBank_. Abaixo, são apresentados os diretórios e arquivos que compõem essa
estrutura:

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


Os principais arquivos e suas funções dentro da arquitetura do _DistriBank_
são detalhados a seguir:

- **main.py:** Este é o arquivo central do servidor, responsável por 
iniciar e coordenar todas as operações bancárias críticas. Ele garante que
o servidor esteja preparado para receber e processar requisições, mantendo a
integridade e a fluidez das transações bancárias;

- **Bank.py:** Serve como o repositório central de todas as informações das
contas bancárias. Este arquivo implementa as operações bancárias essenciais,
assegurando que os dados sejam consistentes e seguros durante todas as 
transações realizadas no sistema;

- **Queue.py:** Gerencia a fila de execução das transações, garantindo que 
sejam realizadas de forma ordenada e correta. Esta estrutura é fundamental 
para minimizar erros e inconsistências nos saldos das contas, coordenando a
execução das operações bancárias de maneira sequencial e organizada;

- **UniqueTwoDigitID.py:** Responsável pela geração de IDs únicos de dois 
dígitos, este arquivo é crucial para a identificação e confirmação das 
transações entre os bancos participantes. Ele garante que cada transação
seja identificada de forma única e possa ser rastreada com precisão dentro
do sistema distribuído;

- **VectorialClock.py:** Implementa o relógio vetorial, usado para ordenar
as transações na fila de execução com base no tempo vetorial associado a cada
operação. Esse mecanismo é crucial para garantir a precisão temporal e a 
correta execução das transações distribuídas;

- **Dockerfile:** Define os passos necessários para a criação da imagem Docker,
encapsulando todo o ambiente de desenvolvimento e produção do _DistriBank_. 
Este arquivo simplifica o processo de implantação e escalabilidade do sistema
em diferentes ambientes de execução;

- **api/API.py:** Gerencia a comunicação entre os servidores, facilitando a 
troca de informações para a realização das transações bancárias
distribuídas. Este componente assegura uma integração eficiente e segura
entre os diferentes nós do sistema _DistriBank_;

- **api/FloatConverter.py:** Converte os valores das transações, garantindo 
a consistência e precisão dos dados financeiros manipulados pelo **DistriBank**.
Este arquivo é essencial para assegurar que todas as transações sejam
realizadas com exatidão matemática, evitando imprecisões nos cálculos
financeiros;

- **clients/JointClient.py**, **clients/JuridicClient.py**, 
**clients/PhysicalClient.py:** Implementam operações específicas para 
diferentes tipos de clientes bancários, como contas conjuntas, jurídicas e
físicas. Cada arquivo oferece funcionalidades adaptadas às necessidades e
exigências de cada categoria de conta dentro do ecossistema do _DistriBank_;

- **exceptions/Exceptions.py:**  Este módulo é responsável por gerenciar e 
tratar as exceções que podem ocorrer durante a execução das operações 
bancárias. Através do tratamento adequado de situações inesperadas, ele
assegura a estabilidade e confiabilidade do sistema, mesmo em cenários 
adversos;

- **utils/Utils.py:** Este módulo oferece uma variedade de funções utilitárias 
usadas no sistema.

</div>


<div align="center">
  <img src="/images/divisor.jpg" width="1280" height="5">
</div>


<A name= "comunicacao-servidores"></A>
<div align="justify">
  <h2>Comunicação entre os Servidores</h2>

No sistema DistriBank, a comunicação entre os bancos é realizada por meio 
de rotas definidas como URLs. Essas rotas facilitam a troca de informações
necessárias para a execução das operações bancárias distribuídas. Para 
configurar essas rotas, são utilizados métodos HTTP padrão, como GET, POST,
PUT e DELETE, que correspondem às operações de leitura, criação, atualização
e exclusão de dados, respectivamente.

A comunicação entre os servidores no sistema DistriBank é facilitada por um
protocolo de comunicação, essencial para a transferência eficiente de
informações entre os nós do sistema. Já a interoperabilidade, que é a 
capacidade de diferentes sistemas e organizações trabalharem juntos, é
viabilizada por meio de uma API, projetada para facilitar a comunicação entre
os diferentes nós distribuídos do _DistriBank_. Cada servidor, localizado em 
máquinas distintas, utiliza essa API para trocar dados de forma 
independentemente da localização física dos servidores.

O protocolo escolhido para a comunicação entre a aplicação e os servidores 
no sistema _DistriBank_ é o HTTP. Amplamente utilizado na web, o HTTP facilita 
a transferência de informações de maneira eficiente e segura entre os 
diferentes componentes distribuídos do sistema.

O HTTP opera em um modelo cliente-servidor, onde o cliente envia uma
requisição para o servidor e aguarda uma resposta. Essa arquitetura é ideal
para o _DistriBank_, pois permite uma comunicação confiável e orientada a 
mensagens entre os servidores distribuídos. 


  <A name="rotas-comunicacao"></A>
  <h3>Rotas de Comunicação</h3>

Cada função da API REST do projeto DistriBank é projetada para retornar um
JSON estruturado com os dados solicitados. Essa abordagem garante que a 
comunicação entre os componentes do sistema seja clara, eficiente e segura.
A seguir, são apresentados exemplos detalhados de requisições para as 
principais rotas da API, destacando como as operações bancárias são realizadas
de forma distribuída e segura.

- Requisição para fazer _login_:
  - Método: POST
  - Rota: /<<string:type>>/<<string:user>>/<<string:password>>/login
  - Exemplo de requisição:
  ```json
  {
    "user": "thiago03",
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

- Requisição para fazer _logout_:
  - Método: POST
  - Rota: /<<string:type>>/<<string:user>>/logout
  - Exemplo de requisição:
  ```json
  {
    "user": "silvio11"
  }
  ```
  - Exemplo de resposta:
  ```json
  {
    "message": "Deslogado com sucesso da conta de Silvio!",
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
  - Rota: /<<string:name>>/<<string:cpf>>/<<string:user>>/<<string:password>>
  /<<float:balance>>/create_physical_particular
  - Exemplo de requisição:
  ```json
  {
    "name": "João",
    "cpf": "08500000000",
    "user": "joao25",
    "password": "joao123",
    "balance": 100.0
  }
  ```
  - Exemplo de resposta:
  ```json
  {
    "message": "Conta particular para João criada com sucesso!",
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
  - Rota: /<<string:name>>/<<string:cpf>>/<<string:user>>/<<string:password>>
  /<<float:balance>>/create_physical_joint
  - Exemplo de requisição:
  ```json
  {
    "name": "Thiago",
    "cpf": "08300000000",
    "user": "thiago03",
    "password": "thiago123",
    "balance": 200.0
  }
  ```
  - Exemplo de resposta:
  ```json
  {
    "message": "Conta conjunta para Thiago criada com sucesso!",
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
  - Rota: /<<string:company>>/<<string:cnpj>>/<<string:name>>/<<string:cpf>>
  /<<string:user>>/<<string:password>>/<<float:balance>>/create_juridic_account
  - Exemplo de requisição:
  ```json
  {
  "company": "Empresa",
  "cnpj": "01400000000000",
  "name": "Silvio",
  "cpf": "08100000000",
  "user": "silvio11",
  "password": "silvio123",
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

- Requisição para adicionar um usuário à conta física conjunta:
  - Método: POST
  - Rota: /<<string:cpf_holder>>/<<string:name>>/<<string:cpf>>/<<string:user>>
  /<<string:password>>/create_joint_complementary
  - Exemplo de requisição:
  ```json
  {
    "cpf_holder": "08300000000",
    "name": "Silvio",
    "cpf": "08100000000",
    "user": "silvio11",
    "password": "silvio123"
  }
  ```
  - Exemplo de resposta:
  ```json
  {
    "message": "Usuário Silvio adicionado à conta conjunta com sucesso!",
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
  - Exemplo de resposta:
  ```json
  {
    "message": "Cliente titular não encontrado!",
    "status": 404
  }
  ```

- Requisição para adicionar um usuário à conta jurídica:
  - Método: POST
  - Rota: /<<string:cnpj>>/<<string:cpf>>/<<string:name>>/<<string:user>>
  /<<string:password>>/create_juridic_employee
  - Exemplo de requisição:
  ```json
  {
    "cnpj": "01400000000000",
    "cpf": "08300000000",
    "name": "Thiago",
    "user": "thiago03",
    "password": "thiago123"
  }
  ```
  - Exemplo de resposta:
  ```json
  {
    "message": "Usuário Thiago adicionado à conta jurídica com sucesso!",
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
  - Exemplo de resposta:
  ```json
  {
    "message": "Cliente titular não encontrado!",
    "status": 404
  }
  ```

- Requisição para criar uma chave pix:
  - Método: POST
  - Rota: /<<string:cpf>>/<<string:type>>/<<string:type_key>>/<<string:pix>>
  /create_pix_key
  - Exemplo de requisição:
  ```json
  {
    "cpf": "08500000000",
    "type": "physical",
    "type_key": "cpf",
    "pix": "08500000000"
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
  - Rota: /<<string:host>>/<<string:port>>/<<string:cpf>>/<<string:type>>
  /<<float:value>>/create_deposit
  - Exemplo de requisição:
  ```json
  {
    "host": "172.16.103.1",
    "port": "5551",
    "cpf": "08300000000",
    "type": "physical_joint",
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
  - Exemplo de requisição:
  ```json
  {
    "list_operations": 
    [
      {
        "host_send": "172.16.103.1",
        "port_send": "5551",
        "cpf_send": "08100000000",
        "type_send": "juridic",
        "value": "value",
          
        "host_recp": "172.16.103.2",
        "port_recp": "5552",
        "cpf_recp": "08300000000",
        "type_recp": "physical_joint",
        "key_recp": "thiago@uefs"
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
  - Rota: /<<string:host>>/<<string:port>>/<<string:cpf>>/<<string:type>>
  /<<float:value>>/create_withdraw
  - Exemplo de requisição:
  ```json
  {
    "host": "172.16.103.1",
    "port": "5551",
    "cpf": "08300000000",
    "type": "physical_joint",
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
  - Rota: /<<string:cpf>>/<<string:type>>/<<string:key>>/<<float:value>>
  /deposit
  - >Observação: Essa rota de depósito não é utilizada diretamente pela aplicação,
  > pois antes de realizar um depósito é necessário criar uma operação desse tipo
  > e adicionar na fila. 
  - Exemplo de requisição:
  ```json
  {
    "cpf": "08300000000",
    "type": "physical_joint",
    "key": "thiago@uefs",
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
  - Rota: /<<string:cpf>>/<<string:type>>/<<string:key>>/<<float:value>>
  /withdraw
  - >Observação: Essa rota de saque não é utilizada diretamente pela aplicação,
  > pois antes de realizar um saque é necessário criar uma operação desse tipo
  > e adicionar na fila.
  - Exemplo de requisição:
  ```json
  {
    "cpf": "08100000000",
    "type": "juridic",
    "key": "silvio@uefs",
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
do _DistriBank_ emprega uma combinação estratégica entre o relógio vetorial e 
o algoritmo de multicast totalmente ordenado. Esses mecanismos são essenciais
para garantir a precisão e a consistência das transações bancárias, evitando 
erros e inconsistências nos saldos das contas.

  <A name= "relogio-vetorial"></A>
  <h3>Relógio Vetorial</h3>

O relógio vetorial é um algoritmo fundamental no sistema _DistriBank_, 
projetado para coordenar o tempo das operações em um ambiente distribuído.
Ele desempenha um papel crucial na determinação da ordem das transações na 
fila de execução com base em marcas de tempo lógicas associadas a cada 
evento. Esse processo é essencial para garantir a consistência e a 
integridade das operações bancárias distribuídas.

O funcionamento do relógio vetorial no sistema _DistriBank_ é baseado em
três princípios fundamentais:

1. **Incremento do Relógio:** A cada nova transação, o relógio vetorial é 
incrementado em uma unidade. Isso reflete o progresso do tempo no servidor
que originou a transação;

2. **Atualização de Marcas de Tempo:** Quando uma transação é enviada entre
os bancos, o tempo nos relógios de cada banco é atualizado para refletir o
tempo do banco que originou a transação. Isso garante que todos os servidores
mantenham uma visão consistente da ordem dos eventos;

3. **Sincronização de Tempo:** Esse processo de atualização contínua assegura
que todos os bancos mantenham um tempo sincronizado. Essa sincronização é 
essencial para a consistência e integridade das operações bancárias 
distribuídas, prevenindo conflitos e garantindo que as transações sejam
processadas na ordem correta.

A implementação do relógio vetorial no _DistriBank_ é feita com a criação de
um vetor de tamanho n, onde n representa o número de bancos no consórcio.
Por exemplo, com quatro instâncias de servidores no ambiente de teste,
o vetor tem tamanho quatro. Cada posição no vetor armazena o tempo associado a
cada banco, permitindo que todos os nós do sistema estejam alinhados 
temporalmente.

Como um exemplo de aplicação do relógio vetorial, considera-se um relógio 
aplicado a quatro processos: P1, P2, P3 e P4. Cada processo possui um relógio
vetorial de tamanho 4, que armazena o tempo associado a cada um deles.

1. **Início da Transação:** Quando o processo P3 inicia uma transação, seu
relógio vetorial é incrementado em uma unidade para refletir essa operação;

2. **Envio e Atualização da Transação:** A transação é então enviada ao
processo P2, que atualiza seu próprio relógio vetorial para refletir o tempo 
do processo P3. Esse processo se repete para cada novo processo que recebe a 
transação, garantindo que todos os processos mantenham uma sincronia temporal.

<div align="center">
  <img src="/images/relogio.png">
</div>
<p align="center"><strong>Figura 5: Exemplo de uma aplicação do relógio vetorial </strong></p>

Algumas vantagens do uso do relógio vetorial são:

1. **Precisão na Ordem das Transações:** Ao utilizar marcas de tempo lógicas,
o relógio vetorial assegura que todas as transações sejam ordenadas 
corretamente, mesmo quando ocorrem simultaneamente em diferentes servidores;

2. **Consistência dos Dados:** A atualização contínua dos relógios entre os
bancos garante que todos os servidores tenham uma visão consistente dos 
saldos das contas, evitando discrepâncias e erros;

3. **Coordenação Eficiente:** O relógio vetorial facilita a coordenação das
operações distribuídas, garantindo que as transações sejam processadas de 
maneira eficiente e confiável.


  <A name= "multicast"></A>
  <h3>Multicast Totalmente Ordenado</h3>

O uso do algoritmo de _multicast_ totalmente ordenado é essencial para
garantir a consistência das transações no sistema distribuído do _DistriBank_.
Este algoritmo assegura que todas as mensagens enviadas sejam entregues a 
todos os destinatários na mesma ordem em que foram enviadas, evitando 
inconsistências nos saldos das contas bancárias durante as transações.

O funcionamento do algoritmo de _multicast_ totalmente ordenado é baseado em
três princípios fundamentais:

1. **Registro de Tempo pelo Relógio Vetorial:** Quando uma transação é 
iniciada, seu tempo é registrado pelo relógio vetorial. Esse registro garante
que a ordem das operações seja mantida;

2. **Entrega Ordenada das Mensagens:** O algoritmo de _multicast_ totalmente
ordenado garante que todas as operações relacionadas a uma transação sejam 
processadas na ordem correta em todos os servidores envolvidos. Isso significa
que cada servidor recebe e processa as mensagens de transação na mesma 
sequência, independentemente da ordem em que as mensagens são recebidas;

3. **Sincronização entre Servidores:** Esse processo assegura que todas as
mensagens são entregues e processadas de forma sincronizada, mantendo a 
integridade e consistência dos dados em todo o sistema distribuído.

Quando uma transação é iniciada e seu tempo é registrado pelo relógio
vetorial, o algoritmo de multicast totalmente ordenado entra em ação para 
garantir que todas as operações relacionadas a essa transação sejam processadas
na ordem correta em todos os servidores envolvidos. Isso significa que cada
servidor recebe e processa as mensagens de transação na mesma sequência,
independentemente da ordem em que as mensagens são recebidas.

  <A name= "busca-binaria"></A>
  <h4>Busca Binária e Ordenação</h4>

No sistema _DistriBank_, para determinar a posição correta de uma nova
transação na fila de execução com base em seu tempo vetorial, utiliza-se um
método de busca binária. Esse algoritmo de divisão e conquista divide a lista
de transações em duas metades e verifica se o elemento a ser inserido deve 
ser colocado antes ou depois do elemento do meio. Esse processo é repetido 
até que a posição correta do novo elemento seja encontrada, garantindo que 
a lista permaneça ordenada de acordo com o tempo vetorial associado a cada 
transação.

A busca binária no sistema funciona da seguinte maneira:

1. **Divisão da Lista:** Inicialmente, a lista de transações está ordenada de
acordo com o tempo vetorial de cada transação;

2. **Verificação da Posição:** O algoritmo compara o tempo vetorial da nova
transação com o tempo vetorial do elemento no meio da lista. Com base nessa
comparação, decide se a nova transação deve ser inserida antes ou depois do
elemento do meio;

3. **Iteração e Conquista:** O processo é repetido para a metade relevante
da lista até que a posição correta da nova transação seja determinada. Isso
garante uma inserção eficiente e ordenada na lista de transações.

A busca binária foi escolhida devido à sua eficiência e capacidade de manter
a ordem em listas. Por tratar-se de um algoritmo logarítmico, o tempo de busca
é reduzido proporcionalmente ao logaritmo do número de elementos da lista. 
Isso acelera significativamente o processo de inserção.

Outra vantagem da busca binária é a sua capacidade de manter a ordenação. Com
esse algoritmo, as transações que são inseridas na fila de execução permanecem
ordenadas de acordo com o tempo vetorial associado a cada operação. Dessa forma
é possível garantir a precisão temporal e a correta execução das transações.

[//]: # (Abaixo, tem-se um exemplo simplificado de como a busca binária é aplicada)

[//]: # (para ordenar as transações na fila de execução do DistriBank. Neste exemplo,)

[//]: # (tem-se quatro transações, cada uma com um tempo vetorial associado. A busca)

[//]: # (binária é utilizada para determinar a posição correta de uma nova transação)

[//]: # (com base em seu tempo vetorial, garantindo que a lista permaneça ordenada)

[//]: # (de acordo com a sequência temporal das operações.)

  <A name="id"></A>
  <h4>ID Único de Transação</h4>

A cada nova transação no sistema _DistriBank_, o tempo do relógio vetorial é
incrementado e um ID de transação de 4 dígitos é gerado de forma única. 
Esse ID é composto pelos 2 últimos dígitos da porta do banco e mais 2 dígitos
gerados por uma classe específica, garantindo sua unicidade e evitando 
conflitos.

O processo de geração do ID de transação assegura que cada transação seja
devidamente identificada e rastreada dentro do sistema distribuído do 
_DistriBank_. Isso é essencial para verificar se todos os bancos receberam
a transação e confirmaram sua execução, garantindo a integridade e a
precisão das operações bancárias distribuídas.

Para exemplificar, suponha que um banco com a porta 5551 inicie uma nova
transação. O relógio vetorial é incrementado e um ID de transação único é
gerado, composto pelos 2 últimos dígitos da porta (51) e mais 2 dígitos, que
são incrementados a cada nova transação. Portanto, esse ID seria algo como
5100. Caso ocorresse uma nova transação nesse mesmo banco, o ID gerado seria
5101, e assim por diante.


  <A name="ACKs"></A>
  <h4>ACKs e Confirmação de Transações></h4>

No sistema _DistriBank_, após o pacote de transação ser completo e enviado
aos demais bancos do consórcio, cada banco realiza operações de organização
e criação de identificadores, conforme descrito anteriormente. Após essas 
operações, os bancos enviam confirmações de recebimento, conhecidas como ACKs,
para todos os outros bancos do consórcio.

Os ACKs são armazenados em um dicionário interno em cada banco, onde a chave
é o ID de cada operação e os valores são listas contendo todos os ACKs 
recebidos para essa operação. A verificação de recebimento é feita da 
seguinte maneira:

- **No Banco que Enviou a Transação:** O número de ACKs recebidos para uma 
determinada transação é igual ao número total de bancos no consórcio menos 1;

- **Nos Outros Bancos do Consórcio:** O número de ACKs recebidos para a mesma
transação deve ser igual ao número total de bancos no consórcio menos 2.

Essa estratégia assegura que todos os bancos tenham recebido a transação e
confirmado seu recebimento. Ao calcular o número esperado de ACKs com base no
número total de bancos no consórcio, o sistema garante que todas as partes 
envolvidas estejam cientes e tenham confirmado a transação de forma 
consistente.


  <A name="fila-execucao"></A>
  <h4>Fila de Execução</h4>

No sistema _DistriBank_, para garantir que todos os bancos estejam 
sincronizados antes de executar uma transação, após a confirmação 
de recebimento dos ACKs, é feita uma verificação da fila de execução
para determinar se a operação recebida é a próxima a ser executada. Caso a
transação seja a primeira, significa que não há transações pendentes que
devem ser processadas. 

Dessa forma, caso o número de ACKs recebidos seja igual ao número esperado,
e a operação seja a primeira da fila, o banco pode executar a transação
com segurança. Caso contrário, a operação é mantida na fila de execução
até que todas as transações anteriores sejam processadas. Dessa forma
esse banco que dispara as operações é considerado o líder de execução
desse conjunto de operações. Caso as operações sejam de forma sequenciais, 
é feita a eleição de vários líderes, pois cada um deles pode liberar a 
execução daquela operação que está na primeira posição da fila.

Essa abordagem assegura que todas as partes do sistema estejam em acordo 
antes de executar qualquer transação, evitando conflitos e garantindo a 
consistência das operações no sistema distribuído do DistriBank. Se alguma
das condições não for atendida, significa que ainda há transações pendentes
na fila, e a operação atual deve aguardar até que as condições sejam todas 
satisfeitas.


  <A name="lock"></A>
  <h4>Locks e Exclusão Mútua</h4>

No sistema DistriBank, para garantir a consistência dos dados e evitar
condições de corrida em operações críticas, são utilizados _locks_ (travas).
Esses locks são mecanismos essenciais para controlar o acesso a recursos 
compartilhados entre os bancos e garantir a integridade das transações em um
ambiente distribuído.

O funcionamento dessas travas dá-se da seguinte forma:

1. **Acionamento do Lock:** Quando um banco recebe uma transação, um _lock_
é acionado para travar a operação associada à transação. Isso significa que
o recurso necessário para processar a transação é bloqueado para outros 
bancos ou processos durante o tempo necessário para completar a operação;

2. **Garantia de Execução Segura:** Ao travar a operação, o banco assegura
que ela seja processada de forma segura e completa. Isso impede que outras
transações interfiram na operação em andamento, mantendo a consistência dos
dados.


  <A name="exemplo-comunicacao"></A>
  <h3>Exemplo de Comunicação entre Bancos</h3>


No exemplo apresentado do sistema _DistriBank_, a comunicação entre os 
bancos é facilitada pelo algoritmo de multicast totalmente ordenado com o
suporte do relógio vetorial. Nessa integração entre os bancos B1 e B2,
é feito o gerenciamento descrito abaixo.

Cada banco (B1, B2, B3, B4) possui um relógio vetorial de tamanho 4 para 
manter o registro do tempo associado a cada um deles. O relógio vetorial 
é crucial para determinar a ordem das transações e garantir que todas as 
operações sejam executadas de forma consistente em todos os bancos.

Os bancos B1 e B2 recebem transações simultâneas com o mesmo tempo vetorial,
o que indica que ambas as transações são vistas como ocorrendo simultaneamente
de acordo com o relógio vetorial. Para lidar com transações concorrentes que
acessam e modificam os mesmos recursos, como atualizações de saldo em uma
conta bancária, são utilizados _locks_. Esses locks são acionados e, assim, 
cada banco processa uma transação por vez.

Na Figura abaixo, tem-se um exemplo simplificado simplificado dessa primeira
etapa de comunicação entre os bancos B1 e B2. 

<div align="center">
  <img src="/images/multicast1.png">
</div>
<p align="center"><strong>Figura 6: Recebimento de novas transações </strong></p>

Nesse caso, o _lock_ travará a segunda operação, enquanto a primeira é
processada. Após a conclusão da primeira operação, o _lock_ é liberado e a
segunda operação é processada. Assim, a primeira operação é inserida na fila
de execução do banco 1 e enviada para os demais bancos, para que todos
possam processar a transação de forma consistente, como mostrado na Figura
abaixo.

<div align="center">
  <img src="/images/multicast2.png">
</div>
<p align="center"><strong>Figura 7: Envio da primeira operação para os demais bancos </strong></p

Após enviar uma operação para os demais bancos do consórcio, cada banco
aguarda os ACKs de confirmação de recebimento. A quantidade de ACKs recebidos
por cada banco segue uma regra específica para garantir que todas as 
operações sejam processadas de forma consistente e que todos os bancos 
estejam cientes das transações realizadas. Na Figura 8, é possível 
visualizar que o banco 1 recebeu os ACKs dos bancos 2, 3 e 4, indicando que
a transação foi recebida por todos os bancos. Já os bancos 2, 3, e 4 receberam
os ACKs dos demais bancos, conforme esperado.

<div align="center">
  <img src="/images/multicast3.png">
</div>
<p align="center"><strong>Figura 8: Verificação do número de ACKs </strong></p>

Recebido o número de ACKs, deve-se verificar em seguida se a operação é a 
primeira na fila dos demais bancos. Com a liberação da trava, já que a operação
foi processada com sucesso, a operação 2 é inserida na fila de execução do
banco 2 e enviada para os demais bancos. Dessa forma, é notável que os bancos
não tem a mesma fila de operações e, por isso, o banco 1 não pode executar a
operação 1, pois mais operações estão sendo inseridas na fila. Essa representação
pode ser vista na imagem abaixo.

<div align="center">
  <img src="/images/multicast4.png">
</div>
<p align="center"><strong>Figura 9: Envio da operação 2 para os demais bancos </strong></p>

Após o banco 2 receber a operação 2 e verificar que é necessário enviar para
os demais bancos do consórcio, ele segue os passos descritos anteriormente.

<div align="center">
  <img src="/images/multicast5.png">
</div>
<p align="center"><strong>Figura 10: Envio da operação 2 para os demais bancos </strong></p>

Após receber o número correto de ACKs e verificar que a operação 2 é a
primeira na fila de todos os bancos, o banco 2 pode ser eleito como líder
para iniciar a execução das operações.

<div align="center">
  <img src="/images/multicast6.png">
</div>
<p align="center"><strong>Figura 11: Verificação da fila de execução </strong></p>

Para as operações sequenciais, o sistema segue o mesmo passo a passo. Entretanto,
nesse caso, o lider será aquele banco que estiver enviando a operação.
Ou seja, pode ser feita a eleição de um lider para cada operação e, dessa
forma, garante que as operações sejam realizadas na ordem.

</div>


<div align="center">
  <img src="/images/divisor.jpg">
</div>


<A name= "transacoes"></A>
<div align="justify">
  <h2>Transações Bancárias</h2>

No sistema _DistriBank_, as transações são executadas de forma atômica, o
que significa que são indivisíveis: ou todas as operações dentro de uma 
transação são concluídas com sucesso, ou nenhuma operação é realizada. Esse
princípio fundamental assegura que todas as transações sejam realizadas 
corretamente, mantendo a consistência e a integridade dos dados bancários
distribuídos.

O funcionamento das transações atômicas é baseado nos seguintes tópicos:

1. **Preparação da Transação:** Antes da execução efetiva das operações, o
sistema realiza uma fase de preparação. Nesta fase, as operações são
semiexecutadas para verificar a ocorrência de erros ou inconsistências 
que poderiam comprometer a transação;

2. **Verificação de Consistência:** Durante a fase de preparação, o sistema
verifica se todas as operações podem ser concluídas com sucesso. Isso inclui
a validação de fundos suficientes nas contas de origem, verificação de
conexão entre os bancos e outros critérios essenciais para a execução da
transação.

Na imagem abaixo, tem-se se o exemplo de 3 operações em uma única transação,
em que o cliente tem contas em três bancos diferentes:
- Transferência do banco 1 para o banco 4;
- Transferência do banco 2 para o banco 4;
- Transferência do banco 3 para o banco 4.

Nesse caso, todas as operações antes de serem executadas de fato, elas são 
semiexecutadas e verifica se houve a ocorrencia de algum erro durante esse
processo.

<div align="center">
  <img src="/images/atomicidade1.png">
</div>
<p align="center"><strong>Figura 12: Semiexecução das operações </strong></p>

No caso registrado abaixo, tem-se o exemplo de que a operação de transferencia do banco 1
para o banco 4 não foi bem sucedida, por motivos que podem ser: saldo insuficiente, conta
inexistente, entre outros. Nesse caso, a toda operação é cancelada e retirada da fila de 
execução, como pode ser visto, que mesmo as outras que não houve inconsistencias, foram 
canceladas de serem executadas.

No exemplo registrado abaixo, é possível observar que a operação de
transferência do Banco 1 para o Banco 4 não foi concluída com sucesso.
Isso ocorreu devido a possíveis razões, como saldo insuficiente ou conta
inexistente. Como resultado, todas as operações foram canceladas e removidas 
da fila de execução, mesmo aquelas que não apresentavam inconsistências.

<div align="center">
  <img src="/images/atomicidade2.png">
</div>
<p align="center"><strong>Figura 13: Cancelamento das operações </strong></p>

No caso a seguir, todas as operações foram concluídas com sucesso e,
após isso, foram removidas da fila de execução, como demonstrado.

<div align="center">
  <img src="/images/atomicidade3.png">
</div>
<p align="center"><strong>Figura 14: Execução das operações </strong></p>


  <A name="transacoes-internas"></A>
  <h3>Transações Bancárias Internas</h3>

O sistema permite a realização de transações bancárias internas, incluindo
transferências entre contas do mesmo banco, além das operações de depósito
e saque, que são realizadas na conta do usuário que está utilizando o 
sistema.


  <A name="transacoes-externas"></A>  
  <h3>Transações Bancárias Externas</h3>

O sistema permite a realização de transações bancárias externas, facilitando
transferências para contas em diferentes bancos. Para iniciar uma transação 
bancária externa, o usuário deve fornecer os seguintes dados:

- Dados do remetente: O usuário deve fornecer informações detalhadas para garantir que 
a transação seja iniciada corretamente, incluindo:
  - Banco de origem: Escolha do banco no qual o remetente está registrado.
  Pode ser o banco atual que está sendo utilizado ou outro banco onde o usuário possua 
  conta;
  - Tipo de conta: Especificar se a conta do remetente é de pessoa física particular, 
  pessoa física conjunta ou pessoa jurídica. Isso ajuda a verificar se o usuário,
  através do seu CPF, está cadastrado no banco, considerando que ele pode ter mais de
  um tipo de conta;
  - Valor da transferência: O montante exato que o usuário deseja transferir. 

- Dados do destinatário: O usuário deve fornecer as seguintes informações 
para garantir a execução correta da transação:
  - Chave Pix: Identificador único (como CPF, e-mail, número de telefone ou 
  chave aleatória) associado à conta do destinatário. Com a chave pix, as
  demais informações necessárias para a transferencia, como o CPF, tipo
  de conta e o banco são obtidas de forma automática;

Ao fornecer esses dados, o sistema processa a transação bancária externa
de forma precisa e eficiente, assegurando que os fundos sejam transferidos
para o destinatário correto e que a operação seja concluída com sucesso.

Após inserir os dados necessários, o usuário pode optar por adicionar uma 
nova operação ou finalizar a transação. As operações adicionadas são 
acumuladas em uma lista e, quando completa, são enviadas para a fila de
execução.

Antes de serem colocadas na fila de execução, as operações passam por uma
fase de pré-execução. Durante esta fase, todas as operações na lista são 
executadas com um valor nulo para garantir a verificação de possíveis erros.
Caso algum erro seja identificado, a lista específica de transações é
cancelada e removida da fila de operações.

Se não houver erros durante a pré-execução, as operações são executadas 
normalmente. Após a conclusão, são removidas da lista, garantindo que a fila
de operações seja processada de forma eficiente e segura.


  <A name="transacoes-sequenciais"></A>
  <h3>Transações Bancárias Sequenciais</h3>

No sistema, as transações são executadas de forma sequencial. Isso significa
que cada transação é processada uma após a outra, garantindo a ausência de 
erros ou inconsistências nos saldos das contas. Esse método sequencial 
assegura a execução correta de cada operação, preservando a integridade e a
consistência dos dados financeiros no sistema.

  <A name="transacoes-concorrentes"></A>
  <h3>Transações Bancárias Concorrentes</h3>

O sistema possibilita a execução de transações bancárias concorrentes por 
meio de _scripts_. Para isso, foi implementada a seguinte função:

```
  async def create_request(url):
      async with aiohttp.ClientSession() as session:
          async with session.get(url) as response:
              return await response.text()
  
  async def main():
      url = 'http://localhost:5000/aluno@uefs/100.0/create_transfer'
      tasks = [create_request(url) for url in urls]
      resultados = await asyncio.gather(*tasks)
      for response in responses:
          print(response)
  
  asyncio.run(main())
```

Assim, as transações podem ser enviadas de forma simultânea para o sistema
bancário, desde que as URLs corretas sejam adicionadas. Esse método de 
execução paralela simula um ambiente real onde múltiplas transações ocorrem
simultaneamente. O sistema é projetado para gerenciar essas transações de 
maneira precisa, assegurando a integridade e consistência dos saldos das 
contas sem erros ou inconsistências.

</div>


<div align="center">
  <img src="/images/divisor.jpg">
</div>


<A name= "confiabilidade"></A>
<div align="justify">
  <h2>Tratamento de Erros e Confiabilidade</h2>

Com relação ao tratamento de confiabilidade, é importante ressaltar que o 
algoritmo de _multicast_ ordenado não é projetado para garantir a 
confiabilidade no sentido de tolerância a falhas ou recuperação automática 
caso um dos bancos falhe durante uma operação.

Dessa forma, a solução proposta para garantir a confiabilidade é a 
implementação de um mecanismo de verificação de conexão. Nesse caso, foi 
criada uma _thread_ que verifica continuamente, a cada 5 segundos, se os
servidores do consórcio estão ativos ou não. Essa verificação é feita por
meio de uma conexão via _socket_ com cada servidor. 

Caso haja um erro na conexão, a _thread_ muda o status do servidor no 
dicionário de servidores para inativo. Dessa forma, caso um banco esteja
inativo, o sistema não poderá realizar transações até que o banco volte a
ficar _online_. Esse sistema simula uma trava de segurança para garantir
que todas as operações sejam realizadas de forma correta e segura, e
tratando-se de um consórcio de bancos, para que não haja erros ou 
inconsistências nas filas de operações, é necessário que todos os bancos 
estejam ativos.

Após o retorno da conexão, o sistema poderá continuar a realizar transações 
normalmente. 

Esse mecanismo pode ser visto na imagem abaixo:

<div align="center">
  <img src="/images/conexao.png">
</div>
<p align="center"><strong>Figura 12: Verificação de Conexão </strong></p>

Nessa imagem, o Banco 1 inicia criando uma operação. Em seguida, ele empacota
a transação e realiza uma verificação para garantir que o Banco 2, Banco 3 e 
Banco 4 estejam todos ativos. Se qualquer um deles estiver inativo, a 
operação é imediatamente cancelada e não é adicionada à fila de execução.
Nesse caso, uma mensagem é emitida informando que a transação não pode ser
realizada devido à inatividade de um dos bancos.

Por outro lado, se todos os bancos estiverem ativos, a operação é colocada
na fila de execução e processada posteriormente.

Além disso, o sistema utiliza exceções para lidar com erros durante a 
execução das operações. Caso ocorra algum problema, as exceções são 
lançadas e capturadas para que o sistema possa tratá-las adequadamente.

</div>


<div align="center">
  <img src="/images/divisor.jpg">
</div>


<A name= "testes"></A>
<div align="justify">
  <h2>Testes de Concorrência</h2>

Para assegurar a qualidade e eficiência do sistema, foram realizados testes 
unitários e de integração. Os testes unitários validam o funcionamento 
correto de cada função e módulo isoladamente, enquanto os testes de 
integração verificam a interação entre os diferentes componentes do sistema.

Os testes estão organizados nos seguintes arquivos:

- ``tests\Account.py``: Contém testes unitários para a classe Account,
focados em funcionalidades relacionadas à gestão de contas de usuários,
como criação de contas e chaves Pix;
- ``tests\Transaction.py``: Contém testes unitários para a classe 
Transaction, que cobrem funcionalidades relacionadas às transações bancárias.

Para executar os testes, utilize-se os seguintes comandos:

```
python tests\Account.py
python tests\Transaction.py
```

Esses testes são essenciais para garantir que todas as partes do sistema 
funcionem conforme esperado e que as interações entre os módulos ocorram 
sem problemas, contribuindo para a robustez e confiabilidade do sistema 
como um todo.


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

```
    git clone https://github.com/Samara-Ferreira/TEC502-DistriBank.git
```

  <A name= "execucao-sem-docker"></A>
  <h3>Execução sem Docker</h3>

Para executar o projeto sem o Docker, é necessário atender aos seguintes 
pré-requisitos:

- Python 3.8 ou superior;
- Pip, para instalação das dependências do projeto;
- Bibliotecas do Python, como o Flask e a requests.

Para instalar as dependências do projeto, execute o seguinte comando nos
diretórios da aplicação e do consórcio:

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

Para executar o projeto com o Docker, siga os passos abaixo:

1. Primeiro, obtenha o diretório de cada um dos componentes executando os 
seguintes comandos:

```
  docker pull samarasf/app
```

```
  docker pull samarasf/bank
```

2. Após a obtenção dos diretórios, o projeto pode ser executado
utilizando o comando abaixo, nos diretórios da aplicação e do consórcio:

```
  docker run --network=host -it samarasf/app
```

```
  docker run --network=host -it -e PORT=555x samarasf/bank
```

Estes comandos configuram e iniciam os containers Docker necessários para 
executar o projeto, garantindo que os componentes estejam corretamente 
interconectados e operacionais.

</div>


<div align="center">
  <img src="/images/divisor.jpg">
</div>


<A name= "conclusao"></A>
<div align="justify">
  <h2>Conclusão</h2>
  
O sistema _DistriBank_ representa uma solução inovadora e eficiente para 
realizar transações bancárias em um ambiente distribuído. Utilizando 
algoritmos avançados como relógio vetorial e _multicast_ totalmente ordenado,
o sistema garante a precisão e consistência das operações bancárias, 
mitigando erros e inconsistências nos saldos das contas.

</div>


<div align="center">
  <img src="/images/divisor.jpg">
</div>


<A name= "referencias"></A>
<div align="justify">
  <h2>Referências</h2>

https://edisciplinas.usp.br/pluginfile.php/3609782/mod_resource/content/1/aula-12.pdf

</div> 
