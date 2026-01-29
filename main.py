from fastapi import FastAPI
from models import Empresa, InstituicaoFinanceira, AnaliseCredito

app = FastAPI(
    title="Plataforma de Análise Financeira e Crédito Empresarial",
    description="Sistema para análise de crédito, risco e capacidade de endividamento"
)

@app.get("/")
def home():
    return {
        "status": "online",
        "mensagem": "Plataforma de Crédito Empresarial ativa"
    }


from models import calcular_rating, classificar_perfil_credito

@app.get("/analise/exemplo")
def analise_exemplo():
    empresa = Empresa(
        nome="Empresa Exemplo Ltda",
        cnpj="00.000.000/0001-00",
        setor="Indústria"
    )

    capacidade = 750000

    rating = calcular_rating(capacidade)
    perfil = classificar_perfil_credito(rating)

    return {
        "empresa": empresa.nome,
        "setor": empresa.setor,
        "capacidade_endividamento": capacidade,
        "rating_credito": rating.nota,
        "justificativa_rating": rating.justificativa,
        "perfil_credito": perfil.classificacao,
        "justificativa_perfil": perfil.justificativa
    }
