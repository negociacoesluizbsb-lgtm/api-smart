from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates

from models import (
    Empresa,
    ParecerCredito,
    PropostaCredito,
    RegistroDecisao,
    RelatorioCredito,
    calcular_rating,
    classificar_perfil_credito
)

app = FastAPI(
    title="Plataforma de Análise Financeira e Crédito Empresarial",
    description="Plataforma para pré-análise automática de crédito empresarial"
)

# Templates HTML
templates = Jinja2Templates(directory="templates")


# ==========================
# PÁGINA PRINCIPAL
# ==========================
@app.get("/", response_class=HTMLResponse)
def pagina_inicial(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


# ==========================
# RELATÓRIO HTML
# ==========================
@app.get("/relatorio/credito-html", response_class=HTMLResponse)
def relatorio_credito_html():
    empresa = "Empresa Exemplo Ltda"
    setor = "Indústria"
    capacidade = 750000

    rating = calcular_rating(capacidade)
    perfil = classificar_perfil_credito(rating)

    html = f"""
    <div style="font-family: Arial, sans-serif; padding: 30px;">
        <h2>Relatório de Crédito - {empresa}</h2>

        <h3>Dados da Empresa</h3>
        <p><strong>Setor:</strong> {setor}</p>
        <p><strong>Capacidade de Endividamento:</strong> R$ {capacidade}</p>

        <h3>Análise de Crédito</h3>
        <p><strong>Rating:</strong> {rating.nota} - {rating.justificativa}</p>
        <p><strong>Perfil:</strong> {perfil.classificacao} - {perfil.justificativa}</p>

        <h3>Parecer</h3>
        <p>Aprovado com ressalvas. Boa capacidade financeira, com dependência moderada de capital de giro.</p>

        <h3>Proposta Indicativa</h3>
        <ul>
            <li>Valor: R$ 500.000</li>
            <li>Prazo: 36 meses</li>
            <li>Taxa: 1.5% a.m.</li>
            <li>Garantias: Alienação fiduciária de recebíveis</li>
        </ul>

        <h3>Decisão</h3>
        <p>Status: Aprovado</p>
        <p>Condições: Manutenção das garantias e covenants financeiros</p>
    </div>
    """
    return HTMLResponse(content=html)


# ==========================
# EXEMPLO JSON (API)
# ==========================
@app.get("/api/status")
def status_api():
    return {"status": "online", "mensagem": "Plataforma de Crédito Empresarial ativa"}
