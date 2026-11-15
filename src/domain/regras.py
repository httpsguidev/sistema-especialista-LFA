from dataclasses import dataclass


@dataclass(frozen=True)
class RegraEspecifica:
    idRegra: str
    recomendacao: str


REGRA_DADO_AUSENTE = RegraEspecifica(
    idRegra="RE0",
    recomendacao="Realize questões do conteúdo para obter evidência inicial.",
)

REGRAS_ESPECIFICAS = {
    ("apoio", "sim"): RegraEspecifica(
        idRegra="RE1",
        recomendacao="Realize revisão guiada e exercícios básicos do conteúdo.",
    ),
    ("apoio", "nao"): RegraEspecifica(
        idRegra="RE2",
        recomendacao="Revise o conteúdo e mantenha prática regular de questões.",
    ),
    ("autonomia", "sim"): RegraEspecifica(
        idRegra="RE3",
        recomendacao="Resolva exercícios específicos nos pontos de dificuldade.",
    ),
    ("autonomia", "nao"): RegraEspecifica(
        idRegra="RE4",
        recomendacao="Aprofunde o conteúdo e realize aplicações práticas.",
    ),
}
