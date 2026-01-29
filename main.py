from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from models import (
    Empresa, InstituicaoFinanceira, AnaliseCredito, ParecerCredito, PropostaCredito,
    RegistroDecisao, RelatorioCredito, calcular_rating, classificar_perfil_credito
)
from jinja2 import Environment, FileSystemLoader
import os

# ----------------------------
# Inicializa app
# ----------------------------
app = FastAPI(
    title="Plataforma de Análise Financeira e Crédito Empresarial",
    description="Sistema para análise de crédito, risco e capacidade de endividamento"
)

# ----------------------------
# Endpoint Home
# ----------------------------
@app.get("/")
def home():
    return {
        "status": "online",
        "mensagem": "Plataforma de Crédito Empresarial ativa"
    }

# ----------------------------
# Endpoint Análise Exemplo
# ----------------------------
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

# ----------------------------
# Endpoint Parecer e Proposta
# ----------------------------
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

# ----------------------------
# Endpoint Registro Decisão
# ----------------------------
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

# ----------------------------
# Endpoint Relatório JSON
# ----------------------------
@app.get("/relatorio/credito-final")
def relatorio_credito_final():
    empresa = "Empresa Exemplo Ltda"
    setor = "Indústria"
    capacidade = 750000

    rating = calcular_rating(capacidade)
    perfil = classificar_perfil_credito(rating)

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

    relatorio = RelatorioCredito(
        empresa=empresa,
        setor=setor,
        capacidade_endividamento=capacidade,
        rating={
            "nota": rating.nota,
            "justificativa": rating.justificativa
        },
        perfil_credito={
            "classificacao": perfil.classificacao,
            "justificativa": perfil.justificativa
        },
        parecer=parecer,
        proposta=proposta,
        decisao=decisao
    )

    return relatorio.__dict__

# ----------------------------
# Endpoint Relatório HTML
# ----------------------------
@app.get("/relatorio/credito-html", response_class=HTMLResponse)
def relatorio_credito_html():
    relatorio = relatorio_credito_final()

    # Ajusta caminho para Railway
    templates_path = os.path.join(os.path.dirname(__file__), 'templates')
    env = Environment(loader=FileSystemLoader(templates_path))
    template = env.get_template('relatorio.html')

    html_out = template.render(**relatorio)
    return HTMLResponse(content=html_out)
