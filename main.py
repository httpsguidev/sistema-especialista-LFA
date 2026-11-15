from pathlib import Path

from src.application.processamento_lote import processarAnaliseEmLote
from src.infrastructure.dataset import carregarDataset
from src.infrastructure.treinamento import criarClassificador
from src.infrastructure.treinamento import dividirTreinoTeste
from src.infrastructure.treinamento import separarAtributosRotulo
from src.infrastructure.treinamento import treinarModelo
from src.presentation.entrada import criarConteudos
from src.presentation.relatorio import gerarRelatorioGeral
from src.presentation.relatorio import gerarRelatorioEspecifico


def criarRegistrosExemplo() -> list[dict[str, object]]:
    return [
        {
            "disciplina": "Português",
            "conteudo": "Interpretação de texto",
            "horasEstudo": 3.0,
            "questoesRealizadas": 20,
            "questoesCorretas": 8,
            "dificuldadeDeclarada": "sim",
            "prioridadeDeclarada": "alta",
        },
        {
            "disciplina": "Matemática",
            "conteudo": "Porcentagem",
            "horasEstudo": 5.0,
            "questoesRealizadas": 30,
            "questoesCorretas": 24,
            "dificuldadeDeclarada": "nao",
            "prioridadeDeclarada": "media",
        },
        {
            "disciplina": "História",
            "conteudo": "Brasil Colônia",
            "horasEstudo": 2.0,
            "questoesRealizadas": 0,
            "questoesCorretas": 0,
            "dificuldadeDeclarada": "sim",
            "prioridadeDeclarada": "alta",
        },
    ]


def executar() -> None:
    raizProjeto = Path(__file__).resolve().parent
    dataset = carregarDataset(raizProjeto / "data" / "dataset_estudos.csv")
    atributos, rotulos = separarAtributosRotulo(dataset)
    particao = dividirTreinoTeste(atributos, rotulos)
    classificador = treinarModelo(
        criarClassificador(),
        particao.atributosTreino,
        particao.rotulosTreino,
    )
    conteudos = criarConteudos(criarRegistrosExemplo())
    relatorio = processarAnaliseEmLote(
        conteudos,
        classificador,
        particao.atributosTreino,
    )

    print(gerarRelatorioEspecifico(relatorio.resultadosEspecificos))
    print()
    print(gerarRelatorioGeral(relatorio.analiseGeral))


if __name__ == "__main__":
    executar()
