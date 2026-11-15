from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from sklearn.tree import DecisionTreeClassifier, plot_tree

from src.domain.resultado import AnaliseGeral, ResultadoAnalise
from src.infrastructure.treinamento import ATRIBUTOS_MODELO


def gerarGraficoAcertos(resultados: tuple[ResultadoAnalise, ...]) -> Figure:
    resultadosElegiveis = tuple(
        resultado
        for resultado in resultados
        if resultado.percentualAcertos is not None
    )
    figura, eixo = plt.subplots(figsize=(10, 5))

    if not resultadosElegiveis:
        configurarGraficoSemDados(figura, eixo, "Percentual de acertos por conteúdo")
        return figura

    rotulos = [criarRotulo(resultado) for resultado in resultadosElegiveis]
    valores = [resultado.percentualAcertos for resultado in resultadosElegiveis]
    barras = eixo.bar(rotulos, valores, color="#2E86AB")

    eixo.set_title("Percentual de acertos por conteúdo")
    eixo.set_ylabel("Acertos (%)")
    eixo.set_ylim(0, 100)
    eixo.tick_params(axis="x", rotation=20)

    for barra, resultado in zip(barras, resultadosElegiveis):
        eixo.text(
            barra.get_x() + barra.get_width() / 2,
            barra.get_height() + 2,
            f"{resultado.percentualAcertos:.1f}%\n({resultado.conteudo.questoesRealizadas} questões)",
            ha="center",
        )

    figura.tight_layout()
    return figura


def gerarGraficoHorasEstudadas(resultados: tuple[ResultadoAnalise, ...]) -> Figure:
    figura, eixo = plt.subplots(figsize=(10, 5))
    rotulos = [criarRotulo(resultado) for resultado in resultados]
    valores = [resultado.conteudo.horasEstudo for resultado in resultados]
    eixo.bar(rotulos, valores, color="#6A994E")
    eixo.set_title("Horas estudadas por conteúdo")
    eixo.set_ylabel("Horas na semana")
    eixo.tick_params(axis="x", rotation=20)
    figura.tight_layout()
    return figura


def gerarGraficoAtencao(analiseGeral: AnaliseGeral) -> Figure:
    figura, eixo = plt.subplots(figsize=(10, 5))

    if not analiseGeral.ranking:
        configurarGraficoSemDados(figura, eixo, "Índice de atenção por conteúdo")
        return figura

    rotulos = [criarRotulo(resultado) for resultado in analiseGeral.ranking]
    valores = [resultado.indiceAtencao for resultado in analiseGeral.ranking]
    cores = [
        "#D1495B" if resultado.conteudo.prioridadeDeclarada == "alta" else "#EDAe49"
        for resultado in analiseGeral.ranking
    ]
    eixo.bar(rotulos, valores, color=cores)
    eixo.set_title("Índice de atenção por conteúdo")
    eixo.set_ylabel("Índice de atenção")
    eixo.set_ylim(0, 100)
    eixo.tick_params(axis="x", rotation=20)
    figura.tight_layout()
    return figura


def gerarGraficoArvore(classificador: DecisionTreeClassifier) -> Figure:
    figura, eixo = plt.subplots(figsize=(14, 8))
    plot_tree(
        classificador,
        feature_names=ATRIBUTOS_MODELO,
        class_names=list(classificador.classes_),
        filled=True,
        rounded=True,
        ax=eixo,
    )
    eixo.set_title("Árvore de decisão para perfil de estudo")
    figura.tight_layout()
    return figura


def criarRotulo(resultado: ResultadoAnalise) -> str:
    return f"{resultado.conteudo.disciplina}\n{resultado.conteudo.conteudo}"


def configurarGraficoSemDados(figura: Figure, eixo: object, titulo: str) -> None:
    eixo.set_title(titulo)
    eixo.text(0.5, 0.5, "Não há dados elegíveis para exibição.", ha="center", va="center")
    eixo.set_axis_off()
    figura.tight_layout()
