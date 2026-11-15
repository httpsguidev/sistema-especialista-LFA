from pandas import DataFrame, Series
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.tree import DecisionTreeClassifier, export_text


def calcularAcuracia(rotulosEsperados: Series, rotulosPrevistos: Series) -> float:
    return float(accuracy_score(rotulosEsperados, rotulosPrevistos))


def calcularMatrizConfusao(
    rotulosEsperados: Series,
    rotulosPrevistos: Series,
) -> DataFrame:
    rotulos = ["apoio", "autonomia"]
    matriz = confusion_matrix(rotulosEsperados, rotulosPrevistos, labels=rotulos)
    return DataFrame(matriz, index=rotulos, columns=rotulos)


def extrairRegrasAprendidas(classificador: DecisionTreeClassifier) -> str:
    return export_text(
        classificador,
        feature_names=list(classificador.feature_names_in_),
    )
