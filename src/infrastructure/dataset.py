from pathlib import Path

import pandas as pd
from pandas import DataFrame


COLUNAS_DATASET = {
    "horasEstudo",
    "questoesRealizadas",
    "percentualAcertos",
    "perfil",
}
PERFIS_VALIDOS = {"apoio", "autonomia"}


def carregarDataset(caminhoDataset: str | Path) -> DataFrame:
    dataset = pd.read_csv(caminhoDataset)
    validarEsquemaDataset(dataset)
    return dataset


def validarEsquemaDataset(dataset: DataFrame) -> None:
    if set(dataset.columns) != COLUNAS_DATASET:
        raise ValueError("O dataset possui colunas diferentes das esperadas.")

    if dataset.empty or dataset.isnull().values.any():
        raise ValueError("O dataset não pode estar vazio ou conter valores ausentes.")

    validarColunasNumericas(dataset)

    if not dataset["perfil"].isin(PERFIS_VALIDOS).all():
        raise ValueError("O dataset possui perfil inválido.")


def validarColunasNumericas(dataset: DataFrame) -> None:
    colunasNumericas = [
        "horasEstudo",
        "questoesRealizadas",
        "percentualAcertos",
    ]

    for coluna in colunasNumericas:
        if not pd.api.types.is_numeric_dtype(dataset[coluna]):
            raise ValueError(f"A coluna {coluna} deve ser numérica.")

    if not dataset["horasEstudo"].between(0, 168).all():
        raise ValueError("As horas de estudo devem estar entre 0 e 168.")

    if (
        not (dataset["questoesRealizadas"] > 0).all()
        or not (dataset["questoesRealizadas"] % 1 == 0).all()
    ):
        raise ValueError("As questões realizadas devem ser inteiras e maiores que zero.")

    if not dataset["percentualAcertos"].between(0, 100).all():
        raise ValueError("O percentual de acertos deve estar entre 0 e 100.")
