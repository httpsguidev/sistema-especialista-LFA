import unittest

from src.domain.conteudo import Conteudo


class ConteudoTest(unittest.TestCase):
    def testCriaConteudoComTodosOsCampos(self) -> None:
        conteudo = Conteudo(
            disciplina="Matemática",
            conteudo="Porcentagem",
            horasEstudo=5.0,
            questoesRealizadas=30,
            questoesCorretas=24,
            dificuldadeDeclarada="nao",
            prioridadeDeclarada="media",
        )

        self.assertEqual(conteudo.disciplina, "Matemática")
        self.assertEqual(conteudo.conteudo, "Porcentagem")
        self.assertEqual(conteudo.horasEstudo, 5.0)
        self.assertEqual(conteudo.questoesRealizadas, 30)
        self.assertEqual(conteudo.questoesCorretas, 24)
        self.assertEqual(conteudo.dificuldadeDeclarada, "nao")
        self.assertEqual(conteudo.prioridadeDeclarada, "media")
