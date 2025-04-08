
# Projeto de Análise e Integração de Dados Energéticos

## Visão Geral

Este projeto tem como objetivo a coleta, transformação, integração e análise de dados relacionados à geração de energia no Brasil, utilizando fontes como o ONS (Operador Nacional do Sistema) e dados de radiação solar da NASA. A solução foi desenvolvida com foco em automação de pipelines de dados, análise espacial e preparação de dados para visualizações e modelagens futuras.

## Estrutura do Projeto

```
.
├── data/                      # Diretório para armazenamento de dados brutos
├── datasets_ons/             # Conjunto de dados extraídos do ONS
├── notebooks/                # Notebooks para exploração e validação
├── output_brazil_grid/       # Resultados processados com grade espacial do Brasil
├── reports/                  # Relatórios e outputs visuais
├── src/                      # Código-fonte principal do projeto
│   ├── data/                 # Pipelines de ETL
│   │   ├── main_etl.py       # Arquivo principal de execução do pipeline - em desenvolvimento
│   │   ├── ons_extract.py    # Extração de dados do ONS
│   │   ├── ons_transform.py  # Transformações nos dados do ONS
│   │   ├── ons_loading.py    # Carga dos dados do ONS
│   │   ├── nasa_extract.py   # Extração de dados da NASA
│   │   ├── nasa_transform.py # Transformações nos dados da NASA
│   │   ├── nasa_loading.py   # Carga dos dados da NASA
│   └── utils/                # Utilitários auxiliares
│       └── utils.py
├── tests/                    # Testes automatizados
├── localizacao_usinas.csv   # Base com coordenadas das usinas brasileiras
├── nasa_grid_data.parquet   # Dados da NASA com interpolação espacial
├── pipeline_dados.ipynb     # Notebook de testes de integração dos dados
```

## Principais Funcionalidades

- Extração de dados do ONS e da NASA.
- Transformações padronizadas e limpeza dos dados energéticos e ambientais.
- Integração espacial de dados por meio de interpolação em grade (grid) nacional.
- Armazenamento em formatos otimizados (e.g., Parquet).
- Pipeline modular e automatizável, com arquivos separados para cada etapa (ETL).

## Requisitos

- Python 3.8+
- Pandas, Numpy, Geopandas, Pyproj, Matplotlib, etc.

Para instalar os pacotes:

```bash
pip install -r requirements.txt
```

## Como Executar

1. Clone este repositório:

```bash
git clone <url-do-repositorio>
cd <nome-da-pasta>
```

2. Execute o pipeline principal:

```bash
python src/data/main_etl.py
```

3. Os dados processados estarão disponíveis na pasta `output_brazil_grid/`.

## Organização do Código

O código segue a estrutura de uma pipeline de dados dividida em três etapas principais para cada fonte:

- Extract (extração)
- Transform (transformação)
- Load (carga)

Cada fonte (ONS e NASA) possui seus próprios módulos para cada etapa, permitindo independência e facilidade de manutenção.

## Contato

Para dúvidas ou sugestões, entre em contato com o autor do projeto.
