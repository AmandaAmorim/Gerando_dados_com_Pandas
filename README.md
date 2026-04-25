Aqui está a versão completa e formatada do seu arquivo `README.md`, consolidando todos os pontos técnicos e a estrutura que desenvolvemos. Este documento foi desenhado para destacar suas habilidades em **POO**, **Engenharia de Dados** e **Desenvolvimento Web** no seu portfólio.

---

# Gerando Dados com Pandas 📊

Este projeto é uma ferramenta robusta desenvolvida para a geração de bases de dados financeiros fictícios, mas convincentes, projetada especificamente para apoiar estudos de análise e ciência de dados.

## 📝 Descrição

O objetivo principal deste sistema é fornecer uma alternativa realista a dados sintéticos aleatórios. Ao implementar lógicas de correlação — como a relação direta entre a renda mensal e o score de crédito do cliente — o gerador produz um conjunto de dados que reflete comportamentos reais do setor financeiro.

O projeto utiliza uma arquitetura modular que separa a interface de usuário da lógica de processamento, demonstrando boas práticas de organização de código e escalabilidade.

---

## 🚀 Funcionalidades

* **Geração de Identidade**: Criação de nomes, CPFs e datas de nascimento brasileiros realistas através da biblioteca `Faker`.
* **Lógica de E-mail Coerente**: Os e-mails são gerados a partir do nome do cliente, passando por um processo de limpeza que remove acentos e espaços internos para garantir a validade do formato.
* **Cálculo de Score Financeiro**: Implementação de algoritmo que utiliza a renda mensal como peso para o cálculo do Score de Crédito, incluindo fatores de ruído aleatório para simular a variabilidade real.
* **Interface Gráfica Interativa**: Front-end desenvolvido com `Streamlit`, permitindo que o usuário escolha a volumetria de dados e visualize o status da geração em tempo real.
* **Exportação de Dados**: Pipeline automatizado que converte a lista de objetos em um DataFrame Pandas e disponibiliza o download imediato em formato `.csv`.

---

## 🏗️ Arquitetura

A estrutura de pastas foi organizada para facilitar a manutenção e a reutilização de código:

```text
Gerando_dados_com_Pandas/
├── app.py                      # Interface Streamlit e gestão de estado
├── requirements.txt            # Lista de dependências do sistema
├── gerador_de_dados/
│   ├── modules/
│   │   ├── client_gen.py       # Classe ClientGenerator (Lógica de Negócio)
│   │   └── utils.py            # Utilitários de tratamento de texto
│   └── services/
│       └── pipeline.py         # Orquestração e conversão para Pandas
└── README.md                   # Documentação do projeto
```

---

## 🛠️ Instalação e Uso

### Pré-requisitos
* Python 3.8 ou superior
* Zorin OS ou qualquer distribuição baseada em Linux/Debian (recomendado)

### 1. Configuração do Ambiente
```bash
# Clonar o repositório
git clone https://github.com/seu-usuario/Gerando_dados_com_Pandas.git
cd Gerando_dados_com_Pandas

# Criar ambiente virtual
python3 -m venv .venv
source .venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
```

### 2. Executando a Aplicação
```bash
streamlit run app.py
```

Após executar o comando, a interface abrirá automaticamente no seu navegador padrão. Informe a quantidade de registros e clique em **Gerar Dados** para liberar o botão de download.

---

## 🧪 Tecnologias Utilizadas

* **Pandas**: Manipulação e estruturação de dados tabulares.
* **Streamlit**: Criação da interface web interativa.
* **Faker**: Geração de dados sintéticos realistas.
* **NumPy**: Operações matemáticas e distribuições aleatórias para lógica de crédito.

---

> **Nota**: Este projeto foi desenvolvido como parte de um portfólio técnico para demonstrar competências em Python aplicado à Ciência de Dados.