from dataclasses import dataclass

from pandas import DataFrame, Series
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


ATRIBUTOS_MODELO = [
    "horasEstudo",
    "questoesRealizadas",
    "percentualAcertos",
]
ROTULO_MODELO = "perfil"
TEST_SIZE = 0.25
RANDOM_STATE = 42
MAX_DEPTH = 2


@dataclass(frozen=True)
class ParticaoTreinamento:
    atributosTreino: DataFrame
    atributosTeste: DataFrame
    rotulosTreino: Series
    rotulosTeste: Series


def separarAtributosRotulo(dataset: DataFrame) -> tuple[DataFrame, Series]:
    atributos = dataset[ATRIBUTOS_MODELO].copy()
    rotulos = dataset[ROTULO_MODELO].copy()
    return atributos, rotulos


def dividirTreinoTeste(
    atributos: DataFrame,
    rotulos: Series,
) -> ParticaoTreinamento:
    atributosTreino, atributosTeste, rotulosTreino, rotulosTeste = train_test_split(
        atributos,
        rotulos,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
        stratify=rotulos,
    )
    return ParticaoTreinamento(
        atributosTreino=atributosTreino,
        atributosTeste=atributosTeste,
        rotulosTreino=rotulosTreino,
        rotulosTeste=rotulosTeste,
    )


def criarClassificador() -> DecisionTreeClassifier:
    return DecisionTreeClassifier(
        max_depth=MAX_DEPTH,
        random_state=RANDOM_STATE,
    )


def treinarModelo(
    classificador: DecisionTreeClassifier,
    atributosTreino: DataFrame,
    rotulosTreino: Series,
) -> DecisionTreeClassifier:
    return classificador.fit(atributosTreino, rotulosTreino)


def preverPerfil(
    classificador: DecisionTreeClassifier,
    atributos: DataFrame,
) -> Series:
    return Series(classificador.predict(atributos), index=atributos.index)
