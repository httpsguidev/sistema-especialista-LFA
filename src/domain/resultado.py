from dataclasses import dataclass

from src.domain.conteudo import Conteudo


@dataclass(frozen=True)
class ResultadoAnalise:
    conteudo: Conteudo
    statusAnalise: str
    percentualAcertos: float | None = None
    percentualErros: float | None = None
    perfilPrevisto: str | None = None
    regraAplicada: str | None = None
    recomendacao: str | None = None
    fatosUtilizados: tuple[str, ...] = ()
    avisos: tuple[str, ...] = ()
    indiceAtencao: float | None = None
    regraGeralAplicada: str | None = None
    orientacaoGeral: str | None = None


@dataclass(frozen=True)
class AnaliseGeral:
    ranking: tuple[ResultadoAnalise, ...]
    dadosInsuficientes: tuple[ResultadoAnalise, ...]
