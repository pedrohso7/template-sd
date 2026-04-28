# Projeto de Sistemas Distribuídos - Socket TCP com MVC

Este projeto implementa um sistema distribuído de autenticação (Cadastro e Login) utilizando Python, Sockets TCP e uma arquitetura robusta baseada no padrão **MVC (Model-View-Controller)**.

## 🏗️ Arquitetura do Sistema

O projeto foi totalmente refatorado para seguir o padrão MVC em ambas as pontas (Cliente e Servidor), garantindo separação de responsabilidades e facilidade de manutenção.

### Cliente (PyQt6)
- **Model (`client/model/`)**: Gerencia a conexão de rede (`ClienteRede`) e a tradução de mensagens. Não conhece a interface gráfica.
- **View (`client/view/`)**: Contém as páginas (`Login`, `Registro`, `Home`) e componentes visuais reaproveitáveis. É responsável apenas por exibir dados e capturar eventos.
- **Controller (`client/controller/`)**: O orquestrador. Recebe comandos da View, solicita dados ao Model e gerencia o **Worker** (Thread separada) para evitar que a interface trave durante requisições de rede.

### Servidor (Socket TCP + SQLite)
- **Model (`server/modelo/`)**: Lida com a persistência de dados (`bd_base.py`, `usuario_modelo.py`) e scripts SQL.
- **View (`server/view/`)**: No servidor, a "Visão" é a interface de rede (`servidor_rede.py`). Ela gerencia os Sockets e o protocolo de comunicação.
- **Controller (`server/controller/`)**: Processa as regras de negócio de autenticação e decide quais dados o modelo deve salvar ou buscar.

---

## 🚀 Como Executar (Docker)

Esta é a maneira recomendada, pois garante que todas as dependências do PyQt6 e do banco de dados estejam configuradas.

### 1. Permitir acesso ao Servidor X (Apenas Linux)
Como o cliente possui interface gráfica, você precisa autorizar o Docker a abrir janelas no seu monitor:
```bash
xhost +local:docker
```

### 2. Iniciar o projeto
Para compilar e iniciar o servidor e um cliente:
```bash
docker-compose up --build
```

### 3. Executar múltiplas instâncias do Cliente
Para testar a concorrência do servidor com vários clientes simultâneos:
```bash
docker-compose up --scale client=3
```
*(Substitua `3` pelo número desejado de instâncias)*

---

## 💻 Execução Local (Desenvolvimento)

Caso prefira rodar sem Docker, siga estes passos:

### Servidor
```bash
cd server
python3 main.py
```

### Cliente
```bash
cd client
pip install -r requirements.txt
python3 main.py
```

---

## 📡 Protocolo de Comunicação

A comunicação utiliza **Sockets TCP** com um protocolo de mensagem estruturado:
1.  **Cabeçalho (4 bytes)**: Um inteiro Big-endian representando o tamanho do corpo da mensagem.
2.  **Corpo (JSON)**: Dados da requisição ou resposta codificados em UTF-8.

**Exemplo de fluxo:**
- O Cliente envia o tamanho (4 bytes) + JSON de Login.
- O Servidor lê o tamanho, recebe o JSON, processa no Controller e devolve tamanho + JSON de Resposta.

---

## 🛠️ Tecnologias Utilizadas
- **Python 3.10**
- **PyQt6** (Interface Gráfica)
- **SQLite3** (Banco de Dados)
- **Docker & Docker Compose** (Containerização)
- **Socket & Threading** (Comunicação Distribuída)
