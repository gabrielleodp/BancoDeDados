-- Consulta para retornar o total de tarefas cadastradas na base e o nome dos usuários que esão executando as tarefas

SELECT usuario_tarefa, COUNT(*) AS total_tarefas
FROM tarefas
GROUP BY usuario_tarefa;

