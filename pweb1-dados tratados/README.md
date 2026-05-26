# CensoEscolarDataApp

Projeto desenvolvido em Python utilizando Pandas para extração, tratamento e organização de dados do Censo Escolar 2025.

O objetivo da aplicação é identificar as 30 Instituições de Ensino com maior quantidade de matrículas no estado da Paraíba e disponibilizar os dados em formato JSON.

---

# Tecnologias Utilizadas

- Python
- Pandas
- JSON
- VS Code

---

# Objetivo do Projeto

A aplicação realiza:

- leitura de arquivos CSV do Censo Escolar 2025;
- seleção das colunas relevantes;
- cruzamento de dados entre tabelas;
- filtragem das instituições do estado da Paraíba;
- ordenação pela quantidade de matrículas;
- geração de um arquivo JSON estruturado.

---

# Estrutura do Projeto

```bash
CensoEscolarDataApp/
│
├── app.py
├── db.json
├── Tabela_Escola_2025.csv
├── Tabela_Matricula_2025.csv
└── README.md
```

---

# Base de Dados

O projeto utiliza duas tabelas do Censo Escolar 2025:

## 1. Tabela_Escola_2025.csv

Contém dados cadastrais das instituições:

- nome da escola;
- município;
- UF;
- região;
- mesorregião;
- microrregião;
- código da entidade.

## 2. Tabela_Matricula_2025.csv

Contém os indicadores de matrículas:

- educação básica;
- ensino infantil;
- ensino fundamental;
- ensino médio;
- EJA;
- educação profissional;
- educação especial.

---

# Relacionamento dos Dados

O cruzamento das tabelas foi realizado utilizando a coluna:

```python
CO_ENTIDADE
```

Essa coluna representa o identificador único de cada instituição de ensino.

---

# Funcionamento da Aplicação

## 1. Leitura dos CSVs

Os arquivos CSV são carregados utilizando Pandas:

```python
pd.read_csv()
```

---

## 2. Seleção das Colunas

Foram selecionadas apenas as colunas necessárias para reduzir o volume de dados e melhorar a performance.

---

## 3. Merge dos Dados

Os dados das escolas e matrículas são unidos utilizando:

```python
pd.merge()
```

---

## 4. Filtragem da Paraíba

A aplicação filtra apenas instituições com:

```python
SG_UF == "PB"
```

---

## 5. Ordenação das Matrículas

As instituições são ordenadas pela coluna:

```python
QT_MAT_BAS
```

em ordem decrescente.

---

## 6. Seleção do Top 30

São selecionadas as 30 instituições com maior quantidade de matrículas:

```python
.head(30)
```

---

## 7. Exportação do JSON

O resultado final é exportado para:

```bash
db.json
```

---

# Exemplo do JSON Gerado

```json
{
  "NO_ENTIDADE": "IFPB - CAMPUS JOAO PESSOA",
  "CO_ENTIDADE": 25096850,
  "NO_UF": "Paraíba",
  "SG_UF": "PB",
  "QT_MAT_BAS": 1971
}
```

---

# Executando o Projeto

## Instalar dependências

```bash
pip install pandas
```

---

# Executar a aplicação

```bash
python app.py
```

---

# Resultado

A aplicação gera:

- um JSON estruturado;
- os 30 maiores registros de matrículas da Paraíba;
- dados organizados e prontos para integração com aplicações externas.

---

# Autor

Luiz Eduardo Souza
