# Estruturas principais do sistema de crédito

class Empresa:
    def __init__(self, nome, cnpj, setor):
        self.nome = nome
        self.cnpj = cnpj
        self.setor = setor


class InstituicaoFinanceira:
    def __init__(self, nome):
        self.nome = nome


class AnaliseCredito:
    def __init__(self, empresa, rating, capacidade_endividamento):
        self.empresa = empresa
        self.rating = rating
        self.capacidade_endividamento = capacidade_endividamento

class PerfilCredito:
    def __init__(self, classificacao, justificativa):
        self.classificacao = classificacao  # Positivo ou Negativo
        self.justificativa = justificativa


class RatingCredito:
    def __init__(self, nota, justificativa):
        self.nota = nota  # A, B, C, D
        self.justificativa = justificativa

def calcular_rating(capacidade_endividamento):
    if capacidade_endividamento >= 1000000:
        return RatingCredito(
            nota="A",
            justificativa="Alta capacidade de endividamento e baixo risco de crédito"
        )
    elif capacidade_endividamento >= 500000:
        return RatingCredito(
            nota="B",
            justificativa="Boa capacidade de crédito, com risco controlado"
        )
    elif capacidade_endividamento >= 200000:
        return RatingCredito(
            nota="C",
            justificativa="Capacidade restrita de crédito"
        )
    else:
        return RatingCredito(
            nota="D",
            justificativa="Capacidade insuficiente para concessão de crédito"
        )


def classificar_perfil_credito(rating):
    if rating.nota in ["A", "B"]:
        return PerfilCredito(
            classificacao="Positivo",
            justificativa="Empresa com perfil adequado para concessão de crédito"
        )
    else:
        return PerfilCredito(
            classificacao="Negativo",
            justificativa="Risco elevado para concessão de crédito"
        )
