from dataclasses import dataclass


@dataclass(frozen=True)
class Conteudo:
    disciplina: str
    conteudo: str
    horasEstudo: float
    questoesRealizadas: int
    questoesCorretas: int
    dificuldadeDeclarada: str
    prioridadeDeclarada: str
