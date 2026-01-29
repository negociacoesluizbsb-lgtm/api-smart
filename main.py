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

    # HTML estruturado
    html = f"""
    <div style="font-family: Arial, sans-serif; max-width: 700px; margin: auto; padding: 20px; border: 1px solid #ccc; border-radius: 8px;">
        <h1 style="text-align:center; color:#2F4F4F;">Relatório de Crédito Empresarial</h1>
        <hr>
        <h2>{empresa}</h2>
        <p><strong>Setor:</strong> {setor}</p>
        <p><strong>Capacidade de Endividamento:</strong> R$ {capacidade}</p>

        <h3>Rating</h3>
        <p><strong>Nota:</strong> {rating['nota']}<br>
           <strong>Justificativa:</strong> {rating['justificativa']}</p>

        <h3>Perfil de Crédito</h3>
        <p><strong>Classificação:</strong> {perfil_credito['classificacao']}<br>
           <strong>Justificativa:</strong> {perfil_credito['justificativa']}</p>

        <h3>Parecer Técnico</h3>
        <p><strong>Conclusão:</strong> {parecer['conclusao']}<br>
           <strong>Observações:</strong> {parecer['observacoes']}</p>

        <h3>Proposta de Crédito</h3>
        <p><strong>Valor:</strong> R$ {proposta['valor']}<br>
           <strong>Prazo:</strong> {proposta['prazo_meses']} meses<br>
           <strong>Taxa de Juros:</strong> {proposta['taxa_juros']}%<br>
           <strong>Garantias:</strong> {proposta['garantias']}</p>

        <h3>Decisão</h3>
        <p><strong>Status:</strong> {decisao['status']}<br>
           <strong>Condições:</strong> {decisao['condicoes']}</p>
    </div>
    """

    return HTMLResponse(content=html)

