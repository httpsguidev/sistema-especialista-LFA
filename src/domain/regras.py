from dataclasses import dataclass


@dataclass(frozen=True)
class RegraEspecifica:
    idRegra: str
    recomendacao: str


@dataclass(frozen=True)
class RegraGeral:
    idRegra: str
    orientacao: str


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

REGRA_GERAL_DADO_AUSENTE = RegraGeral(
    idRegra="RG0",
    orientacao="Colete questões resolvidas antes de comparar este conteúdo no ranking.",
)

REGRAS_GERAIS = {
    ("apoio", "alta"): RegraGeral(
        idRegra="RG1",
        orientacao="Atenção elevada: priorize reforço neste conteúdo.",
    ),
    ("apoio", "comum"): RegraGeral(
        idRegra="RG2",
        orientacao="Há necessidade de reforço, respeitando a ordem do ranking.",
    ),
    ("autonomia", "alta"): RegraGeral(
        idRegra="RG3",
        orientacao="Mantenha a continuidade deste conteúdo de alta prioridade.",
    ),
    ("autonomia", "comum"): RegraGeral(
        idRegra="RG4",
        orientacao="Mantenha o acompanhamento regular deste conteúdo.",
    ),
}
