import unittest

from src.application.metricas import calcularPercentualAcerto
from src.application.metricas import calcularPercentualErro


class MetricasTest(unittest.TestCase):
    def testCalculaPercentuaisComQuestoesRealizadas(self) -> None:
        percentualAcerto = calcularPercentualAcerto(20, 8)
        percentualErro = calcularPercentualErro(20, 8)

        self.assertEqual(percentualAcerto, 40.0)
        self.assertEqual(percentualErro, 60.0)

    def testRetornaMetricasIndisponiveisSemQuestoes(self) -> None:
        percentualAcerto = calcularPercentualAcerto(0, 0)
        percentualErro = calcularPercentualErro(0, 0)

        self.assertIsNone(percentualAcerto)
        self.assertIsNone(percentualErro)
