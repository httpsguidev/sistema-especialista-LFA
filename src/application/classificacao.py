from pandas import DataFrame
from sklearn.tree import DecisionTreeClassifier

from src.domain.conteudo import Conteudo
from src.infrastructure.treinamento import ATRIBUTOS_MODELO


def criarAtributosParaPrevisao(
    conteudo: Conteudo,
    percentualAcertos: float,
) -> DataFrame:
    return DataFrame(
        [
            {
                "horasEstudo": conteudo.horasEstudo,
                "questoesRealizadas": conteudo.questoesRealizadas,
                "percentualAcertos": percentualAcertos,
            }
        ],
        columns=ATRIBUTOS_MODELO,
    )


def preverPerfilConteudo(
    classificador: DecisionTreeClassifier,
    conteudo: Conteudo,
    percentualAcertos: float,
) -> str:
    atributos = criarAtributosParaPrevisao(conteudo, percentualAcertos)
    return str(classificador.predict(atributos)[0])


def identificarAvisosForaTreino(
    conteudo: Conteudo,
    percentualAcertos: float,
    atributosTreino: DataFrame,
) -> tuple[str, ...]:
    atributos = criarAtributosParaPrevisao(conteudo, percentualAcertos)
    avisos = []

    for coluna in ATRIBUTOS_MODELO:
        valor = atributos.iloc[0][coluna]
        minimo = atributosTreino[coluna].min()
        maximo = atributosTreino[coluna].max()

        if valor < minimo or valor > maximo:
            avisos.append(
                f"{coluna} fora da faixa de treino ({minimo} a {maximo})."
            )

    return tuple(avisos)
