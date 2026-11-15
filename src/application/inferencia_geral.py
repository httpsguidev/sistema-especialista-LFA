from dataclasses import replace

from src.domain.regras import REGRA_GERAL_DADO_AUSENTE, REGRAS_GERAIS
from src.domain.resultado import AnaliseGeral, ResultadoAnalise


PESOS_PRIORIDADE = {"alta": 100, "media": 50, "baixa": 0}
LIMITE_AMOSTRA_PEQUENA = 10


def calcularIndiceAtencao(
    percentualAcertos: float,
    prioridadeDeclarada: str,
) -> float:
    pesoPrioridade = mapearPesoPrioridade(prioridadeDeclarada)
    return round(0.70 * (100 - percentualAcertos) + 0.30 * pesoPrioridade, 2)


def mapearPesoPrioridade(prioridadeDeclarada: str) -> int:
    if prioridadeDeclarada not in PESOS_PRIORIDADE:
        raise ValueError("A prioridade deve ser alta, media ou baixa.")

    return PESOS_PRIORIDADE[prioridadeDeclarada]


def analisarPrioridades(resultados: list[ResultadoAnalise]) -> AnaliseGeral:
    resultadosComRegra = tuple(aplicarRegraGeral(resultado) for resultado in resultados)
    ranking = tuple(
        sorted(
            (
                resultado
                for resultado in resultadosComRegra
                if resultado.indiceAtencao is not None
            ),
            key=criarChaveOrdenacao,
        )
    )
    dadosInsuficientes = tuple(
        resultado
        for resultado in resultadosComRegra
        if resultado.indiceAtencao is None
    )
    return AnaliseGeral(
        ranking=ranking,
        dadosInsuficientes=dadosInsuficientes,
    )


def aplicarRegraGeral(resultado: ResultadoAnalise) -> ResultadoAnalise:
    if resultado.percentualAcertos is None:
        return replace(
            resultado,
            regraGeralAplicada=REGRA_GERAL_DADO_AUSENTE.idRegra,
            orientacaoGeral=REGRA_GERAL_DADO_AUSENTE.orientacao,
        )

    prioridadeDeclarada = resultado.conteudo.prioridadeDeclarada
    categoriaPrioridade = "alta" if prioridadeDeclarada == "alta" else "comum"
    regra = REGRAS_GERAIS[(resultado.perfilPrevisto, categoriaPrioridade)]
    avisos = resultado.avisos

    if resultado.conteudo.questoesRealizadas < LIMITE_AMOSTRA_PEQUENA:
        avisos += (
            "Amostra pequena: resultado baseado em menos de 10 questões.",
        )

    return replace(
        resultado,
        avisos=avisos,
        indiceAtencao=calcularIndiceAtencao(
            resultado.percentualAcertos,
            prioridadeDeclarada,
        ),
        regraGeralAplicada=regra.idRegra,
        orientacaoGeral=regra.orientacao,
    )


def criarChaveOrdenacao(resultado: ResultadoAnalise) -> tuple[float, float, int, str, str]:
    return (
        -resultado.indiceAtencao,
        resultado.percentualAcertos,
        -mapearPesoPrioridade(resultado.conteudo.prioridadeDeclarada),
        resultado.conteudo.disciplina.casefold(),
        resultado.conteudo.conteudo.casefold(),
    )
