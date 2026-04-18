# ATS09---Testes-APIs# 🚀 Automação de Testes de API

Atividade desenvolvida afim de estruturar uma base de testes automatizados para APIs modernas, atendendo testes funcionais, declarativos e de performance assíncrona.

---

## 🛠️ Tecnologias

- Python 3.9+
- Pytest + pytest-asyncio
- HTTPX
- Tavern
- FastAPI

---

## 🧪 Testes implementados

### 🔹 Contrato de API (Tavern)
- Teste declarativo em YAML  
- Parametrização (`1, 5, 15`)  
- Encadeamento de requisições  
- Validação com função Python  

✔ Fluxo:
1. Busca tarefa (`/todos/{id}`)
2. Captura `userId`
3. Busca tarefas do usuário
4. Valida estrutura da resposta

---

### ⚡ Performance Assíncrona
- Testes com `pytest-asyncio`  
- Execução sem rede (`ASGITransport`)  
- Requisições simultâneas com `asyncio.gather`  

📊 Cenários:
- 5, 20 e 50 requisições simultâneas  

🎯 Resultado esperado:
> Tempo total < **3.5s**, comprovando execução não bloqueante

---

## ▶️ Como executar

```bash
# criar ambiente
python -m venv venv

# ativar (Windows)
venv\Scripts\activate

# instalar dependências
pip install pytest pytest-asyncio httpx tavern fastapi uvicorn

# rodar testes
pytest -v -s
```

---

## Autor

Uatila Dos Santos Silva

