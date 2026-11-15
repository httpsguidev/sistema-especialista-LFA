import unittest

from src.domain.conteudo import Conteudo
from src.domain.resultado import ResultadoAnalise


class ResultadoAnaliseTest(unittest.TestCase):
    def testCriaResultadoComDadosDaAnalise(self) -> None:
        conteudo = Conteudo(
            disciplina="Português",
            conteudo="Interpretação de texto",
            horasEstudo=3.0,
            questoesRealizadas=20,
            questoesCorretas=8,
            dificuldadeDeclarada="sim",
            prioridadeDeclarada="alta",
        )
        resultado = ResultadoAnalise(
            conteudo=conteudo,
            statusAnalise="avaliado",
            percentualAcertos=40.0,
            percentualErros=60.0,
            perfilPrevisto="apoio",
            regraAplicada="RE1",
            recomendacao="Realize revisão guiada e exercícios básicos.",
            fatosUtilizados=("perfil=apoio", "dificuldade=sim"),
        )

        self.assertEqual(resultado.conteudo, conteudo)
        self.assertEqual(resultado.statusAnalise, "avaliado")
        self.assertEqual(resultado.percentualAcertos, 40.0)
        self.assertEqual(resultado.percentualErros, 60.0)
        self.assertEqual(resultado.perfilPrevisto, "apoio")
        self.assertEqual(resultado.regraAplicada, "RE1")
        self.assertEqual(
            resultado.recomendacao,
            "Realize revisão guiada e exercícios básicos.",
        )
        self.assertEqual(
            resultado.fatosUtilizados,
            ("perfil=apoio", "dificuldade=sim"),
        )
