from src.domain.conteudo import Conteudo
from src.domain.regras import REGRA_DADO_AUSENTE, REGRAS_ESPECIFICAS
from src.domain.resultado import ResultadoAnalise


PERFIS_VALIDOS = {"apoio", "autonomia"}
DIFICULDADES_VALIDAS = {"sim", "nao"}


def aplicarInferenciaEspecifica(
    conteudo: Conteudo,
    perfilPrevisto: str | None,
    percentualAcertos: float | None,
    percentualErros: float | None,
) -> ResultadoAnalise:
    if conteudo.questoesRealizadas == 0:
        return ResultadoAnalise(
            conteudo=conteudo,
            statusAnalise="dados_insuficientes",
            regraAplicada=REGRA_DADO_AUSENTE.idRegra,
            recomendacao=REGRA_DADO_AUSENTE.recomendacao,
            fatosUtilizados=("questoesRealizadas=0",),
        )

    validarFatosDaInferencia(
        conteudo.dificuldadeDeclarada,
        perfilPrevisto,
        percentualAcertos,
        percentualErros,
    )
    regra = REGRAS_ESPECIFICAS[(perfilPrevisto, conteudo.dificuldadeDeclarada)]
    fatosUtilizados = (
        f"perfilPrevisto={perfilPrevisto}",
        f"dificuldadeDeclarada={conteudo.dificuldadeDeclarada}",
        f"questoesRealizadas={conteudo.questoesRealizadas}",
    )
    return ResultadoAnalise(
        conteudo=conteudo,
        statusAnalise="avaliado",
        percentualAcertos=percentualAcertos,
        percentualErros=percentualErros,
        perfilPrevisto=perfilPrevisto,
        regraAplicada=regra.idRegra,
        recomendacao=regra.recomendacao,
        fatosUtilizados=fatosUtilizados,
    )


def validarFatosDaInferencia(
    dificuldadeDeclarada: str,
    perfilPrevisto: str | None,
    percentualAcertos: float | None,
    percentualErros: float | None,
) -> None:
    if perfilPrevisto not in PERFIS_VALIDOS:
        raise ValueError("O perfil previsto deve ser apoio ou autonomia.")

    if dificuldadeDeclarada not in DIFICULDADES_VALIDAS:
        raise ValueError("A dificuldade declarada deve ser sim ou nao.")

    if percentualAcertos is None or percentualErros is None:
        raise ValueError("Percentuais são obrigatórios quando há questões realizadas.")
