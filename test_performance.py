import pytest
import httpx
import time
import asyncio

from api_pagamentos import app

@pytest.mark.asyncio
@pytest.mark.parametrize("qtd_requisicoes", [5, 20, 50])
async def test_performance_pagamentos(qtd_requisicoes):
    inicio = time.time()

    transport = httpx.ASGITransport(app=app)

    async with httpx.AsyncClient(
        transport=transport,
        base_url="http://test"
    ) as client:

        tarefas = [
            client.get("/processar")
            for i in range(qtd_requisicoes)
        ]

        respostas = await asyncio.gather(*tarefas)

        # Valida status
        for res in respostas:
            assert res.status_code == 200

    #                fim      - inicio
    tempo_total = time.time() - inicio

    print(f"\n{qtd_requisicoes} requisições -> {tempo_total:.2f}s")

    
    assert tempo_total < 3.5