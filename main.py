from config import MENUS
from src.utils.splash_screen import SplashScreen
from src.controller.controller_usuario import ControllerUsuario
from src.controller.controller_tarefa import ControllerTarefa
from src.reports.relatorios import Relatorio
from src.conexion.oracle_queries import OracleQueries

# Conexão única
oracle = OracleQueries(can_write=True)
oracle.connect()

# Instanciando controllers e relatórios com a mesma conexão
tela_inicial = SplashScreen()
ctrl_usuario = ControllerUsuario(oracle)
ctrl_tarefa = ControllerTarefa(oracle)
relatorio = Relatorio(oracle)  # ajuste necessário em relatorios.py para receber oracle

def exibir_contagem():
    """Exibe a contagem de registros das tabelas"""
    total_usuarios = oracle.sqlToMatrix("SELECT COUNT(1) FROM USUARIOS")[0][0]
    total_tarefas = oracle.sqlToMatrix("SELECT COUNT(1) FROM TAREFAS")[0][0]
    print(f"Total de Usuários: {total_usuarios}")
    print(f"Total de Tarefas: {total_tarefas}")

def confirmar_acao(msg: str) -> bool:
    """Pergunta ao usuário se deseja confirmar a ação"""
    resp = input(f"{msg} (S/N): ").strip().upper()
    return resp == "S"

def run():
    print(tela_inicial.get_updated_screen())
    exibir_contagem()

    while True:
        print(MENUS["principal"])
        opcao = input("Escolha uma opção [1-5]: ").strip()
        if not opcao.isdigit():
            continue
        opcao = int(opcao)

        # ---------- RELATÓRIOS ----------
        if opcao == 1:
            print(MENUS["relatorios"])
            opc_rel = input("Escolha o relatório: ").strip()
            if opc_rel == "1":
                relatorio.rel_usuarios()
            elif opc_rel == "2":
                relatorio.rel_tarefas()
            elif opc_rel == "3":
                relatorio.rel_tarefas_group_by()
            elif opc_rel == "4":
                relatorio.rel_tarefas_join()
            elif opc_rel == "0":
                continue

        # ---------- INSERIR ----------
        elif opcao == 2:
            while True:
                print(MENUS["entidades"])
                inserir_op = input("Escolha uma opção: ").strip()
                if inserir_op == "1":
                    ctrl_usuario.inserir()
                elif inserir_op == "2":
                    ctrl_tarefa.inserir()
                elif inserir_op == "0":
                    break
                else:
                    print("Opção inválida.")

        # ---------- ATUALIZAR ----------
        elif opcao == 3:
            while True:
                print(MENUS["entidades"])
                atualizar_op = input("Escolha uma opção: ").strip()
                if atualizar_op == "1":
                    ctrl_usuario.atualizar()  # usa método do controller que já lista bonito
                elif atualizar_op == "2":
                    ctrl_tarefa.atualizar()   # idem
                elif atualizar_op == "0":
                    break
                else:
                    print("Opção inválida.")

        # ---------- EXCLUIR ----------
        elif opcao == 4:
            while True:
                print(MENUS["entidades"])
                excluir_op = input("Escolha uma opção: ").strip()
                if excluir_op == "1":
                    ctrl_usuario.excluir()  # já lista e pede confirmação dentro
                elif excluir_op == "2":
                    ctrl_tarefa.excluir()   # já lista e pede confirmação dentro
                elif excluir_op == "0":
                    break
                else:
                    print("Opção inválida.")

        # ---------- SAIR ----------
        elif opcao == 5:
            print("Saindo do sistema. Obrigado!")
            break

        # Atualiza contagem após cada operação
        exibir_contagem()

if _name_ == "_main_":
    run()
