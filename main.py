from fastapi import FastAPI, Request, UploadFile, File
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates

from models import (
    calcular_rating,
    classificar_perfil_credito
)

app = FastAPI(
    title="Plataforma de Análise Financeira e Crédito Empresarial",
    description="Plataforma de pré-análise automática de crédito empresarial"
)

# ==========================
# CONFIGURAÇÃO DE TEMPLATES
# ==========================
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
# LOGIN
# ==========================
@app.get("/login", response_class=HTMLResponse)
def pagina_login(request: Request):
    return templates.TemplateResponse(
        "login.html",
        {"request": request}
    )


# ==========================
# UPLOAD (PÁGINA)
# ==========================
@app.get("/upload", response_class=HTMLResponse)
def pagina_upload(request: Request):
    return templates.TemplateResponse(
        "upload.html",
        {"request": request}
    )


# ==========================
# UPLOAD (RECEBER DOCUMENTO)
# ==========================
@app.post("/upload")
async def receber_documento(documento: UploadFile = File(...)):
    return {
        "status": "ok",
        "arquivo_recebido": documento.filename
    }


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
    <div style="font-family: Arial, sans-serif; padding: 30px; max-width: 900px; margin: auto;">
        <h2>Relatório de Crédito - {empresa}</h2>

        <h3>Dados da Empresa</h3>
        <p><strong>Setor:</strong> {setor}</p>
        <p><strong>Capacidade de Endividamento:</strong> R$ {capacidade:,.0f}</p>

        <h3>Análise Financeira</h3>
        <p><strong>Rating:</strong> {rating.nota} – {rating.justificativa}</p>
        <p><strong>Perfil de Crédito:</strong> {perfil.classificacao} – {perfil.justificativa}</p>

        <h3>Parecer Técnico</h3>
        <p>
            Empresa com estrutura financeira adequada, boa geração de caixa operacional
            e nível de endividamento compatível com o porte.
        </p>

        <h3>Proposta Indicativa</h3>
        <ul>
            <li>Valor: R$ 500.000</li>
            <li>Prazo: 36 meses</li>
            <li>Taxa estimada: 1,5% a.m.</li>
            <li>Garantias: Alienação fiduciária de recebíveis</li>
        </ul>

        <h3>Conclusão</h3>
        <p>Status: <strong>Aprovado com ressalvas</strong></p>
        <p>Observação: manutenção de covenants financeiros e garantias.</p>
    </div>
    """

    return HTMLResponse(content=html)


# ==========================
# STATUS DA API
# ==========================
@app.get("/api/status")
def status_api():
    return JSONResponse(
        {
            "status": "online",
            "mensagem": "Plataforma de Crédito Empresarial ativa"
        }
    )
