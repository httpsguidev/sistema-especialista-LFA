def validarIdentificacao(disciplina: str, conteudo: str) -> None:
    validarTextoObrigatorio(disciplina, "disciplina")
    validarTextoObrigatorio(conteudo, "conteúdo")


def validarTextoObrigatorio(valor: str, nomeCampo: str) -> None:
    if not isinstance(valor, str) or not valor.strip():
        raise ValueError(f"O campo {nomeCampo} é obrigatório.")
