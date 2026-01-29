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
