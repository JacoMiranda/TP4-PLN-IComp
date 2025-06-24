# /custom_metrics/execution_accuracy.py

import deepeval
from deepeval.metrics import BaseMetric
from deepeval.test_case import LLMTestCase
import sqlite3
import json
import os

class ExecutionAccuracy(BaseMetric):
    """
    Métrica customizada para avaliar a acurácia de execução de queries Text-to-SQL
    no dataset Spider, conforme especificado no TP4 de ICC220/PPGINF528.
    """
    def __init__(self, threshold: float = 1.0, data_path: str = "/content/drive/MyDrive/spider_data/spider"):
        self.threshold = threshold
        self.data_path = data_path
        
        # Carrega os dados de desenvolvimento uma vez para mapear questões aos bancos de dados
        dev_json_path = os.path.join(self.data_path, "dev.json")
        try:
            with open(dev_json_path, "r") as f:
                self.dev_data = json.load(f)
        except FileNotFoundError:
            # Lida com o caso onde o script é executado de um diretório diferente
            # e o caminho relativo precisa de ajuste.
            # No contexto do Colab, o caminho absoluto é mais seguro.
            self.dev_data = []
            print(f"AVISO: {dev_json_path} não encontrado. A métrica não poderá mapear db_id.")

    def measure(self, test_case: LLMTestCase) -> float:
        """
        Mede a acurácia comparando os resultados da execução da query gerada
        com a query gabarito.
        """
        # Encontra o ID do banco de dados para a questão atual
        db_id = next((item['db_id'] for item in self.dev_data if item['question'] == test_case.input), None)
        if not db_id:
            return 0.0

        db_path_full = os.path.join(self.data_path, "database", db_id, f"{db_id}.sqlite")

        # Conecta ao banco de dados
        try:
            conn = sqlite3.connect(db_path_full)
            cursor = conn.cursor()
        except Exception:
            return 0.0

        # Executa a query gerada pelo modelo
        try:
            cursor.execute(test_case.actual_output)
            predicted_result = cursor.fetchall()
        except Exception:
            predicted_result = []

        # Executa a query gabarito
        try:
            cursor.execute(test_case.expected_output)
            ground_truth_result = cursor.fetchall()
        except Exception:
            conn.close()
            return 0.0
        
        conn.close()

        # Compara os conjuntos de resultados de forma insensível à ordem
        if set(map(str, predicted_result)) == set(map(str, ground_truth_result)):
            self.success = True
            return 1.0
        else:
            self.success = False
            return 0.0

    def is_successful(self) -> bool:
        """
        Retorna True se a última medição foi um sucesso.
        """
        return getattr(self, "success", False)

    @property
    def __name__(self):
        return "Execution Accuracy"

    async def a_measure(self, test_case: LLMTestCase) -> float:
        """
        Wrapper assíncrono para compatibilidade com o modo padrão do DeepEval.
        """
        return self.measure(test_case)

