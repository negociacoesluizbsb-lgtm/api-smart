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


@app.get("/analise/exemplo")
def analise_exemplo():
    empresa = Empresa(
        nome="Empresa Exemplo Ltda",
        cnpj="00.000.000/0001-00",
        setor="Indústria"
    )

    analise = AnaliseCredito(
        empresa=empresa.nome,
        rating="B",
        capacidade_endividamento=750000
    )

    return {
        "empresa": empresa.nome,
        "setor": empresa.setor,
        "rating_credito": analise.rating,
        "capacidade_endividamento": analise.capacidade_endividamento
    }
