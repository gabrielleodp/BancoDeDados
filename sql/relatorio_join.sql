-- Consulta para retornar quantidade de tarefas relacionadas a cada usuário. 

SELECT t.id_tarefa, t.titulo, t.status, u.nome
FROM tarefas t
JOIN usuarios u ON t.usuario_tarefa = u.id_usuario;

