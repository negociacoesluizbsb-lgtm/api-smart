from fastapi import FastAPI
from models import Empresa, InstituicaoFinanceira, AnaliseCredito, ParecerCredito, PropostaCredito, RegistroDecisao
from models import RelatorioCredito



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

from fastapi.responses import FileResponse
from jinja2 import Environment, FileSystemLoader
import pdfkit

@app.get("/relatorio/credito-pdf")
def relatorio_credito_pdf():
    # Pega dados do relatório final
    relatorio = relatorio_credito_final()

    # Configura template
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('relatorio.html')

    # Renderiza HTML
    html_out = template.render(**relatorio)

    # Cria PDF temporário
    pdf_path = "relatorio_credito.pdf"
    pdfkit.from_string(html_out, pdf_path)

    # Retorna PDF
    return FileResponse(pdf_path, media_type='application/pdf', filename='relatorio_credito.pdf')


