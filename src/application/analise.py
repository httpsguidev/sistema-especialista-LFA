from dataclasses import replace

from pandas import DataFrame
from sklearn.tree import DecisionTreeClassifier

from src.application.classificacao import identificarAvisosForaTreino
from src.application.classificacao import preverPerfilConteudo
from src.application.inferencia_especifica import aplicarInferenciaEspecifica
from src.application.metricas import calcularPercentualAcerto
from src.application.metricas import calcularPercentualErro
from src.domain.conteudo import Conteudo
from src.domain.resultado import ResultadoAnalise


def analisarConteudo(
    conteudo: Conteudo,
    classificador: DecisionTreeClassifier,
    atributosTreino: DataFrame,
) -> ResultadoAnalise:
    percentualAcertos = calcularPercentualAcerto(
        conteudo.questoesRealizadas,
        conteudo.questoesCorretas,
    )
    percentualErros = calcularPercentualErro(
        conteudo.questoesRealizadas,
        conteudo.questoesCorretas,
    )

    if percentualAcertos is None:
        return aplicarInferenciaEspecifica(
            conteudo,
            None,
            percentualAcertos,
            percentualErros,
        )

    perfilPrevisto = preverPerfilConteudo(
        classificador,
        conteudo,
        percentualAcertos,
    )
    resultado = aplicarInferenciaEspecifica(
        conteudo,
        perfilPrevisto,
        percentualAcertos,
        percentualErros,
    )
    avisos = identificarAvisosForaTreino(
        conteudo,
        percentualAcertos,
        atributosTreino,
    )
    return replace(resultado, avisos=avisos)
