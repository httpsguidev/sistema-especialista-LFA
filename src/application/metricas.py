from src.application.validacao import validarConsistenciaAcerto


def calcularPercentualAcerto(
    questoesRealizadas: int,
    questoesCorretas: int,
) -> float | None:
    validarConsistenciaAcerto(questoesRealizadas, questoesCorretas)

    if questoesRealizadas == 0:
        return None

    return (questoesCorretas / questoesRealizadas) * 100


def calcularPercentualErro(
    questoesRealizadas: int,
    questoesCorretas: int,
) -> float | None:
    percentualAcerto = calcularPercentualAcerto(
        questoesRealizadas,
        questoesCorretas,
    )

    if percentualAcerto is None:
        return None

    return 100 - percentualAcerto
