from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Empresa, ParecerCredito, PropostaCredito, RegistroDecisao
from fastapi.responses import HTMLResponse


app = FastAPI(
    title="Plataforma de Análise Financeira e Crédito Empresarial",
    description="Sistema para análise de crédito, risco e capacidade de endividamento"
)

# Permitir que o frontend web acesse a API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Para produção, coloque apenas seu domínio
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def home():
    return {
        "status": "online",
        "mensagem": "Plataforma de Crédito Empresarial ativa"
    }

# Endpoint de análise de exemplo
@app.get("/analise/exemplo")
def analise_exemplo():
    empresa = Empresa(
        nome="Empresa Exemplo Ltda",
        cnpj="00.000.000/0001-00",
        setor="Indústria"
    )

    capacidade = 750000

    # Exemplo simplificado
    rating = {"nota": "B", "justificativa": "Boa capacidade de crédito, com risco controlado"}
    perfil = {"classificacao": "Positivo", "justificativa": "Empresa com perfil adequado para concessão de crédito"}

    return {
        "empresa": empresa.nome,
        "setor": empresa.setor,
        "capacidade_endividamento": capacidade,
        "rating_credito": rating["nota"],
        "justificativa_rating": rating["justificativa"],
        "perfil_credito": perfil["classificacao"],
        "justificativa_perfil": perfil["justificativa"]
    }

# Endpoint parecer e proposta
@app.get("/credito/parecer-e-proposta")
def parecer_e_proposta():
    parecer = ParecerCredito(
        analista="Instituição Financeira Exemplo",
        conclusao="Aprovado com ressalvas",
        observacoes="Empresa com boa capacidade de pagamento, porém dependente de capital de giro"
    )

    proposta = PropostaCredito(
        valor=500000,
        prazo_meses=36,
        taxa_juros=1.5,
        garantias="Alienação fiduciária de recebíveis"
    )

    return {
        "parecer_tecnico": {
            "analista": parecer.analista,
            "conclusao": parecer.conclusao,
            "observacoes": parecer.observacoes
        },
        "proposta_credito": {
            "valor": proposta.valor,
            "prazo_meses": proposta.prazo_meses,
            "taxa_juros": proposta.taxa_juros,
            "garantias": proposta.garantias
        }
    }

# Endpoint registro de decisão
@app.get("/governanca/registro-decisao")
def registro_decisao_exemplo():
    registro = RegistroDecisao(
        usuario="Analista Crédito Banco X",
        acao="Aprovação com condições",
        justificativa="Rating B, perfil positivo e garantias adequadas"
    )

    return {
        "usuario": registro.usuario,
        "acao": registro.acao,
        "justificativa": registro.justificativa,
        "data_hora": registro.data_hora
    }

# 🔹 Endpoint seguro do relatório HTML
@app.get("/relatorio/credito-html", response_class=HTMLResponse)
def relatorio_credito_html():
    empresa = "Empresa Exemplo Ltda"
    setor = "Indústria"
    capacidade = 750000

    rating = {"nota": "B", "justificativa": "Boa capacidade de crédito, com risco controlado"}
    perfil_credito = {"classificacao": "Positivo", "justificativa": "Empresa com perfil adequado para concessão de crédito"}

    parecer = {
        "conclusao": "Aprovado com ressalvas",
        "observacoes": "Boa capacidade financeira, dependência moderada de capital de giro"
    }

    proposta = {
        "valor": 500000,
        "prazo_meses": 36,
        "taxa_juros": 1.5,
        "garantias": "Alienação fiduciária de recebíveis"
    }

    decisao = {
        "status": "Aprovado",
        "condicoes": "Manutenção das garantias e covenants financeiros"
    }

    html = f"""
    <h2>Relatório de Crédito - {empresa}</h2>
    <p><strong>Setor:</strong> {setor}</p>
    <p><strong>Capacidade de Endividamento:</strong> R$ {capacidade}</p>
    <p><strong>Rating:</strong> {rating['nota']} - {rating['justificativa']}</p>
    <p><strong>Perfil de Crédito:</strong> {perfil_credito['classificacao']} - {perfil_credito['justificativa']}</p>
    <p><strong>Parecer:</strong> {parecer['conclusao']} - {parecer['observacoes']}</p>
    <p><strong>Proposta:</strong> R$ {proposta['valor']} | {proposta['prazo_meses']} meses | Juros {proposta['taxa_juros']}% | Garantias: {proposta['garantias']}</p>
    <p><strong>Decisão:</strong> {decisao['status']} | {decisao['condicoes']}</p>
    """

    # Retornar HTML de forma que o navegador renderize corretamente
    return HTMLResponse(content=html)
