import math


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
