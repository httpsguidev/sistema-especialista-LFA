import math


PRIORIDADES_VALIDAS = {"alta", "media", "baixa"}


def validarIdentificacao(disciplina: str, conteudo: str) -> None:
    validarTextoObrigatorio(disciplina, "disciplina")
    validarTextoObrigatorio(conteudo, "conteúdo")


def validarTextoObrigatorio(valor: str, nomeCampo: str) -> None:
    if not isinstance(valor, str) or not valor.strip():
        raise ValueError(f"O campo {nomeCampo} é obrigatório.")


def validarHorasEstudo(horasEstudo: float) -> None:
    if (
        isinstance(horasEstudo, bool)
        or not isinstance(horasEstudo, (int, float))
        or not math.isfinite(horasEstudo)
        or not 0 <= horasEstudo <= 168
    ):
        raise ValueError("As horas de estudo devem estar entre 0 e 168.")


def validarQuantidadeQuestao(quantidade: int, nomeCampo: str) -> None:
    if isinstance(quantidade, bool) or not isinstance(quantidade, int) or quantidade < 0:
        raise ValueError(f"{nomeCampo} deve ser uma quantidade inteira não negativa.")


def validarConsistenciaAcerto(
    questoesRealizadas: int,
    questoesCorretas: int,
) -> None:
    validarQuantidadeQuestao(questoesRealizadas, "Questões realizadas")
    validarQuantidadeQuestao(questoesCorretas, "Questões corretas")

    if questoesRealizadas == 0 and questoesCorretas != 0:
        raise ValueError("Não pode haver acertos sem questões realizadas.")

    if questoesCorretas > questoesRealizadas:
        raise ValueError("Questões corretas não podem superar questões realizadas.")


def validarPrioridadeDeclarada(prioridadeDeclarada: str) -> None:
    if prioridadeDeclarada not in PRIORIDADES_VALIDAS:
        raise ValueError("A prioridade deve ser alta, media ou baixa.")
