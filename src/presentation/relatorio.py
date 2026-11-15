from src.domain.resultado import AnaliseGeral, ResultadoAnalise


def gerarRelatorioEspecifico(resultados: tuple[ResultadoAnalise, ...]) -> str:
    linhas = ["ANÁLISE ESPECÍFICA"]

    for resultado in resultados:
        linhas.extend(
            [
                "",
                f"{resultado.conteudo.disciplina} — {resultado.conteudo.conteudo}",
                f"Acertos: {formatarPercentual(resultado.percentualAcertos)}",
                f"Erros: {formatarPercentual(resultado.percentualErros)}",
                f"Perfil previsto: {resultado.perfilPrevisto or 'indisponível'}",
                f"Regra aplicada: {resultado.regraAplicada}",
                f"Fatos: {formatarFatos(resultado.fatosUtilizados)}",
                f"Recomendação: {resultado.recomendacao}",
            ]
        )
        linhas.extend(f"Aviso: {aviso}" for aviso in resultado.avisos)

    return "\n".join(linhas)


def gerarRelatorioGeral(analiseGeral: AnaliseGeral) -> str:
    linhas = ["ANÁLISE GERAL", "", "Ranking de atenção:"]

    if not analiseGeral.ranking:
        linhas.append("Nenhum conteúdo elegível para ranking.")

    for posicao, resultado in enumerate(analiseGeral.ranking, start=1):
        linhas.append(
            f"{posicao}. {resultado.conteudo.disciplina} — "
            f"{resultado.conteudo.conteudo}: "
            f"índice {resultado.indiceAtencao:.2f} | "
            f"{resultado.regraGeralAplicada} | {resultado.orientacaoGeral}"
        )

    if analiseGeral.dadosInsuficientes:
        linhas.extend(["", "Dados insuficientes:"])
        for resultado in analiseGeral.dadosInsuficientes:
            linhas.append(
                f"- {resultado.conteudo.disciplina} — "
                f"{resultado.conteudo.conteudo}: {resultado.orientacaoGeral}"
            )

    return "\n".join(linhas)


def formatarPercentual(percentual: float | None) -> str:
    if percentual is None:
        return "indisponível"

    return f"{percentual:.2f}%"


def formatarFatos(fatos: tuple[str, ...]) -> str:
    return ", ".join(fatos) if fatos else "não aplicável"
