from src.application.validacao import validarConsistenciaAcerto


def calcularPercentualAcerto(
    questoesRealizadas: int,
    questoesCorretas: int,
) -> float:
    validarConsistenciaAcerto(questoesRealizadas, questoesCorretas)

    if questoesRealizadas == 0:
        raise ValueError("Não é possível calcular acertos sem questões realizadas.")

    return (questoesCorretas / questoesRealizadas) * 100
