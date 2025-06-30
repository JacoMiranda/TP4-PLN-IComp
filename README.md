# 📊 Análise Quantitativa do Trade-off entre Especialização e Generalização em LLMs via Fine-Tuning - By Jacó Miranda

Este projeto implementa uma avaliação empírica e sistemática do processo de fine-tuning em Modelos de Linguagem de Grande Porte (LLMs), focando na quantificação do ganho de desempenho na tarefa-alvo (Text-to-SQL) e na medição da degradação de performance em tarefas de conhecimento geral (MMLU).

## 📋 Objetivo

Avaliar quantitativamente o trade-off entre especialização e generalização em LLMs através do fine-tuning com LoRA, medindo:

- **Ganho de especialização**: Melhoria na tarefa Text-to-SQL usando o dataset Spider  
- **Perda de generalização**: Regressão de capacidade no benchmark MMLU (esquecimento catastrófico)

## 🏗️ Estrutura do Projeto

```
.
├── custom_metrics/
│   └── execution_accuracy.py         # Métrica ExecutionAccuracy
├── others/
│   └── Results/
│       ├── avaliacao_Baseline_Model.csv
│       ├── avaliacao_Fine-Tuned_Run_1.csv
│       ├── avaliacao_Fine-Tuned_Run_2.csv
│       ├── avaliacao_mmlu_resultados.csv
│       ├── summary_fase3_accuracy.csv
│    ├── mistral-7b-spider-run1.rar
│    ├── mistral-7b-spider-run2.rar
|    └── Relatório técnico-TP4.pdf
├── scripts/
│   └── T4.ipynb                      # Notebook principal
├── requirements.txt                 # Dependências
└── README.md                        # Documentação
```

## ⚙️ Ambiente de Execução

Este projeto foi desenvolvido para ser executado no ambiente Google Colab.  
Devido às limitações de armazenamento e memória da versão gratuita do Colab, o Google Drive é utilizado como solução de armazenamento persistente.  
Antes de executar o notebook, certifique-se de ter no mínimo 3 GB de espaço livre no seu Drive.

## 📦 Requisitos

Versões das principais dependências:

- PyTorch: 2.6.0+cu124  
- Transformers: 4.52.4  
- PEFT: 0.15.2  
- TRL: 0.19.0  
- BitsAndBytes: 0.46.0  
- Datasets: 3.6.0  
- Accelerate: 1.8.1  
- DeepEval: 3.1.8  
- Pandas: 2.2.2  
- NumPy: 2.0.2  
- KaggleHub: 0.3.12

Instalação:

```bash
pip install -r requirements.txt
```

## 🚀 Como Executar

### 1. Clonar o Repositório

```bash
git clone <url-do-repositorio>
cd <nome-do-projeto>
```

### 2. Executar o Notebook

Abra o arquivo `scripts/T4.ipynb` no Google Colab.

### 3. Executar as Células

- Célula 1: Instala as dependências
- Célula 2: Conecta ao Google Drive e configura a API do Kaggle
- Célula 3: Fine-tuning dos modelos 
- Células seguintes: Avaliação com ExecutionAccuracy e MMLU
- Célula final: Consolida os resultados em tabelas `.csv`

Os dados serão armazenados automaticamente no Google Drive, e reutilizados nas próximas execuções.

## 📊 Resultados

Os resultados ficam salvos na pasta `others/Results/`:

- `avaliacao_Baseline_Model.csv`
- `avaliacao_Fine-Tuned_Run_1.csv`
- `avaliacao_Fine-Tuned_Run_2.csv`
- `avaliacao_mmlu_resultados.csv`
- `summary_fase3_accuracy.csv`
- `mistral-7b-spider-run1.rar`
- `mistral-7b-spider-run2.rar`

Esses arquivos contêm os resultados das fases 3 e 4 e os modelos treinados, que podem ser utilizados diretamente para inferência.

## 🧪 Métrica ExecutionAccuracy

Local: `custom_metrics/execution_accuracy.py`

Essa métrica avalia a acurácia funcional de consultas SQL:

- Executa a query esperada e a query gerada nos bancos SQLite
- Compara os resultados (sem considerar a ordem)
- Retorna `1.0` se iguais, `0.0` se diferentes

## ✅ Checklist de Execução

- [x] Conta Google com Colab + GPU T4
- [x] API do Kaggle configurada
- [x] Dataset Spider baixado
- [x] Fine-tuning executado ou restaurado
- [x] Avaliação ExecutionAccuracy
- [x] Avaliação MMLU
- [x] Resultados exportados (.csv)
- [x] Relatório Técnico (.pdf)

## 📄 Licença

Este projeto foi desenvolvido exclusivamente para fins acadêmicos na disciplina ICC220/PPGINF528 da Universidade Federal do Amazonas (UFAM).

**Autor(es)**: JACÓ MIRANDA  
**Instituição**: Instituto de Computação - UFAM  
**Disciplina**: ICC220 - Tópicos Especiais em Bancos de Dados  
**Ano**: 2025
