from src.application.validacao import validarConsistenciaAcerto
from src.application.validacao import validarDificuldadeDeclarada
from src.application.validacao import validarHorasEstudo
from src.application.validacao import validarIdentificacao
from src.application.validacao import validarPrioridadeDeclarada
from src.domain.conteudo import Conteudo


CAMPOS_CONTEUDO = {
    "disciplina",
    "conteudo",
    "horasEstudo",
    "questoesRealizadas",
    "questoesCorretas",
    "dificuldadeDeclarada",
    "prioridadeDeclarada",
}


def criarConteudos(registros: list[dict[str, object]]) -> list[Conteudo]:
    return [criarConteudo(registro) for registro in registros]


def criarConteudo(registro: dict[str, object]) -> Conteudo:
    if set(registro) != CAMPOS_CONTEUDO:
        raise ValueError("O registro possui campos diferentes dos esperados.")

    disciplina = registro["disciplina"]
    conteudo = registro["conteudo"]
    horasEstudo = registro["horasEstudo"]
    questoesRealizadas = registro["questoesRealizadas"]
    questoesCorretas = registro["questoesCorretas"]
    dificuldadeDeclarada = registro["dificuldadeDeclarada"]
    prioridadeDeclarada = registro["prioridadeDeclarada"]

    validarIdentificacao(disciplina, conteudo)
    validarHorasEstudo(horasEstudo)
    validarConsistenciaAcerto(questoesRealizadas, questoesCorretas)
    validarDificuldadeDeclarada(dificuldadeDeclarada)
    validarPrioridadeDeclarada(prioridadeDeclarada)

    return Conteudo(
        disciplina=disciplina,
        conteudo=conteudo,
        horasEstudo=horasEstudo,
        questoesRealizadas=questoesRealizadas,
        questoesCorretas=questoesCorretas,
        dificuldadeDeclarada=dificuldadeDeclarada,
        prioridadeDeclarada=prioridadeDeclarada,
    )
