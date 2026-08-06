# ARP — Dashboard Gerencial 2025 vs 2026

Dashboard completo (Vendas, Faturamento, Recebimentos, Análise, Balanço, DRM) — arquivo único em HTML, servido via Streamlit.

## Arquivos

- `Dashboard_ADM.html` — o dashboard em si (HTML/CSS/JS autocontido)
- `app.py` — wrapper Streamlit que carrega o HTML e exige chave de acesso
- `requirements.txt` — dependência (só o Streamlit)

## Como subir no GitHub

1. Crie um repositório novo (ex: `dashboard-adm`)
2. Suba os 3 arquivos (`Dashboard_ADM.html`, `app.py`, `requirements.txt`) na raiz do repositório

## Como publicar no Streamlit Community Cloud

1. Acesse [share.streamlit.io](https://share.streamlit.io)
2. Clique em **New app**
3. Selecione o repositório que você acabou de criar
4. Em **Main file path**, coloque `app.py`
5. Clique em **Deploy**

## Acesso

O dashboard fica protegido por chave na URL. Depois de publicado, acesse assim:

```
https://SEU-APP.streamlit.app/?chave=prodentis2026
```

(Mesmo padrão de chave usado nos outros dashboards da ARP.)

## Atualizações futuras

Quando o Claude gerar uma nova versão do `Dashboard_ADM.html`, basta substituir esse arquivo no repositório GitHub (upload manual ou `git push`) — o Streamlit Cloud atualiza sozinho.
