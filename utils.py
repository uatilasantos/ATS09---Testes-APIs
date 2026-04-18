def validar_lista_tarefas(response):
    dados = response.json()

    # Verifica se é uma lista
    assert isinstance(dados, list), "A resposta não é uma lista!"

    # Verifica se existe pelo menos uma tarefa com 'completed'
    completed = any("completed" in tarefa for tarefa in dados)

    assert completed, "Nenhuma tarefa contém a chave 'completed'!"