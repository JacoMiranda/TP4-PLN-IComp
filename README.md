Análise Quantitativa do Trade-off entre Especialização e Generalização em LLMs
Este repositório contém o código e os recursos para o quarto trabalho prático de ICC220/PPGINF528, da Universidade Federal do Amazonas (UFAM), entregue em 23 de Junho de 2025.

Visão Geral do Projeto
O projeto realiza uma avaliação empírica e sistemática do processo de fine-tuning em Modelos de Linguagem de Grande Porte (LLMs). Focamos na tarefa de Text-to-SQL, utilizando o modelo mistralai/Mistral-7B-Instruct-v0.2 e o dataset Spider. A análise quantifica o ganho de desempenho na tarefa-alvo (medido pela Acurácia de Execução) e a degradação de performance em tarefas de conhecimento geral (medida pelo benchmark MMLU), explorando o trade-off inerente à especialização de modelos.

Observações iniciais:
 -  Versões das principais:
    PyTorch: 2.6.0+cu124
    Transformers: 4.52.4
    PEFT: 0.15.2
    TRL: 0.19.0
    BitsAndBytes: 0.46.0
    Datasets: 3.6.0
    Accelerate: 1.8.1
    DeepEval: 3.1.8
    Pandas: 2.2.2
    NumPy: 2.0.2
    KaggleHub: 0.3.12
    
 - Sobre o Ambiente de Execução
Este projeto foi desenvolvido para ser executado no ambiente Google Colab. Devido às limitações de armazenamento e memória da versão gratuita do Colab, que reinicia após períodos de inatividade, o Google Drive é utilizado como uma solução de armazenamento persistente.

Os scripts neste repositório estão configurados para salvar arquivos essenciais e pesados (como o dataset Spider e os checkpoints dos modelos treinados) diretamente no Google Drive do usuário. Isso garante que o progresso não seja perdido entre as sessões e que os dados só precisem ser baixados uma única vez.

Antes de executar o notebook, certifique-se de que você tem espaço de armazenamento suficiente no seu Google Drive (mínimo de 3 GB recomendado).

Estrutura do Repositório
O repositório está organizado conforme os requisitos do trabalho prático:

/scripts/T4.ipynb: Notebook Colab contendo todo o pipeline experimental, desde o setup dos dados e ambiente, treinamento dos modelos, e as avaliações das Fases 3 e 4.

/custom_metrics/execution_accuracy.py: Contém a implementação da métrica customizada ExecutionAccuracy, utilizada para avaliar a correção funcional das queries SQL geradas.

/Other/Results: Contém arquivos no formato CSV com as avaliações e resumos das fases 3 e 4. Também contém os dois aquivos .rar que foram gerados durante o fine-tuning e gravados no google drive. Arquivos mistral-7b-spider-run1 e mistral-7b-spider-run2. Caso queira testá-los sem a necessidade de rodar o código totalmente.

requirements.txt: Lista de todas as dependências de Python necessárias para executar o projeto.

README.md: Esta documentação detalhada.

Como Reproduzir os Resultados
Para reproduzir os resultados apresentados no relatório, siga os passos abaixo.

1. Pré-requisitos
Conta no Google e acesso ao Google Colab com um ambiente de GPU (T4 ou superior é recomendado).

Conta no Kaggle para baixar o dataset Spider através da API.

2. Configuração do Ambiente
Clone o Repositório: Clone este repositório para a sua máquina local ou diretamente para o seu Google Drive.

Chave da API do Kaggle: Talvez seja necessário uma chave de api, se sim, então:

  Crie um token de API na página da sua conta no Kaggle (kaggle.com/account). Isso fará o download de um arquivo kaggle.json.
  
  Ao executar o notebook pela primeira vez, faça o upload deste arquivo para o ambiente do Colab quando solicitado pela Célula 2.
  
  Abra o Notebook: Navegue até a pasta /scripts e abra o arquivo T4.ipynb no Google Colab.

3. Execução
Execute as células do notebook em ordem, de cima para baixo.

Célula 1 irá instalar todas as dependências necessárias.

Célula 2 irá configurar seu Google Drive e a API do Kaggle, e fará o download do dataset do Spider (aproximadamente 400 MB) para o seu Drive na primeira execução. Em execuções futuras, esta etapa será pulada.

Célula 3 contém a lógica para o fine-tuning dos dois modelos (Run 1 e Run 2). As execuções estão comentadas por padrão para evitar re-treinamentos acidentais. Descomente as linhas apropriadas se desejar re-treinar os modelos.

Células de Avaliação (Fase 3 e 4): As células subsequentes carregarão os checkpoints treinados e executarão as avaliações de Acurácia de Execução e MMLU. Os resultados detalhados serão salvos em arquivos .csv na pasta /content/drive/MyDrive/spider_data/custom_metrics/.

Célula Final: A última célula coletará os resultados dos arquivos CSV gerados e imprimirá as tabelas de resumo finais, idênticas às apresentadas no relatório técnico.
