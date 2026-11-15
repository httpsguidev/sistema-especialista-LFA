from pandas import DataFrame
from sklearn.tree import DecisionTreeClassifier

from src.application.analise import analisarConteudo
from src.application.inferencia_geral import analisarPrioridades
from src.domain.conteudo import Conteudo
from src.domain.resultado import RelatorioAnalise


def processarAnaliseEmLote(
    conteudos: list[Conteudo],
    classificador: DecisionTreeClassifier,
    atributosTreino: DataFrame,
) -> RelatorioAnalise:
    resultadosEspecificos = tuple(
        analisarConteudo(conteudo, classificador, atributosTreino)
        for conteudo in conteudos
    )
    analiseGeral = analisarPrioridades(list(resultadosEspecificos))
    return RelatorioAnalise(
        resultadosEspecificos=resultadosEspecificos,
        analiseGeral=analiseGeral,
    )
