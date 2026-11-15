import math
import unittest

from src.application.validacao import validarConsistenciaAcerto
from src.application.validacao import validarDificuldadeDeclarada
from src.application.validacao import validarHorasEstudo
from src.application.validacao import validarIdentificacao
from src.application.validacao import validarPrioridadeDeclarada
from src.application.validacao import validarQuantidadeQuestao


class ValidacaoTest(unittest.TestCase):
    def testRejeitaIdentificacaoAusente(self) -> None:
        with self.assertRaisesRegex(ValueError, "disciplina"):
            validarIdentificacao("", "Porcentagem")

        with self.assertRaisesRegex(ValueError, "conteúdo"):
            validarIdentificacao("Matemática", "   ")

    def testRejeitaHorasForaDaFaixa(self) -> None:
        for horasEstudo in (-1, 169, math.inf, "cinco"):
            with self.subTest(horasEstudo=horasEstudo):
                with self.assertRaises(ValueError):
                    validarHorasEstudo(horasEstudo)

    def testRejeitaQuantidadeInvalida(self) -> None:
        for quantidade in (-1, 1.5, True):
            with self.subTest(quantidade=quantidade):
                with self.assertRaises(ValueError):
                    validarQuantidadeQuestao(quantidade, "Questões realizadas")

    def testRejeitaAcertosInconsistentes(self) -> None:
        with self.assertRaises(ValueError):
            validarConsistenciaAcerto(10, 11)

        with self.assertRaises(ValueError):
            validarConsistenciaAcerto(0, 1)

    def testRejeitaDificuldadeInvalida(self) -> None:
        with self.assertRaises(ValueError):
            validarDificuldadeDeclarada("talvez")

    def testRejeitaPrioridadeInvalida(self) -> None:
        with self.assertRaises(ValueError):
            validarPrioridadeDeclarada("urgente")
