[![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.3-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![scikit--learn](https://img.shields.io/badge/scikit--learn-1.7-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.11-11557C?style=for-the-badge&logo=python&logoColor=white)](https://matplotlib.org/)

# SEOE — Sistema Especialista de Orientação de Estudos

O SEOE é uma aplicação didática desenvolvida para orientar o estudo por disciplina e conteúdo. O projeto integra aprendizado supervisionado e regras explícitas de sistema especialista: uma árvore de decisão prevê um perfil de estudo e o motor de inferência transforma essa previsão, as métricas e as informações declaradas em recomendações justificadas.

O sistema trabalha exclusivamente com dados fictícios e tem finalidade acadêmica. Ele não realiza diagnósticos pedagógicos ou psicológicos e não pretende validar a eficácia das recomendações em estudantes reais.

## Tecnologias utilizadas

- Python 3.13
- Pandas 2.3 — manipulação do dataset simulado
- scikit-learn 1.7 — árvore de decisão e avaliação do modelo
- Matplotlib 3.11 — visualização das métricas e do modelo
- Git — versionamento incremental

## Funcionalidades previstas

- Cadastro de múltiplos conteúdos, inclusive de disciplinas diferentes.
- Validação de horas de estudo, questões realizadas, acertos, dificuldade e prioridade.
- Cálculo de percentual de acertos e erros sem divisão por zero.
- Classificação do perfil como `apoio` ou `autonomia`.
- Recomendação específica com regra, fatos utilizados e explicação.
- Ranking geral de atenção, considerando desempenho e prioridade declarada.
- Gráficos de desempenho, horas estudadas, índice de atenção e avaliação técnica do classificador.

## Estrutura atual

```text
.
├── main.py             # Ponto de entrada; será implementado na etapa adequada
├── README.md           # Apresentação e instruções da aplicação
├── requirements.txt    # Dependências Python reproduzíveis
└── .gitignore          # Arquivos locais e temporários excluídos do Git
```

Os módulos de domínio, validação, métricas, treinamento, inferência e testes serão criados de forma incremental, somente quando suas etapas forem iniciadas.

## Diferenciais do projeto

- Arquitetura híbrida: previsão supervisionada integrada a regras `SE... ENTÃO...`.
- Recomendações explicáveis, com identificação da regra aplicada e dos fatos avaliados.
- Separação entre análise individual e comparação geral dos conteúdos.
- Tratamento explícito de dados ausentes e de pouca evidência.
- Dataset simulado e critérios de rotulagem documentados antes do treinamento.

## Pré-requisitos

- Python 3.13 ou compatível.
- `pip` disponível no terminal.

## Instalação

```bash
python -m venv .venv
.venv\\Scripts\\activate
python -m pip install -r requirements.txt
```

## Estado de desenvolvimento

O projeto está na fase inicial de preparação. A implementação seguirá uma sequência incremental com testes e commits pequenos por unidade funcional. A documentação de requisitos e de planejamento é mantida fora desta pasta de aplicação.
