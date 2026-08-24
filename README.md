# 📝 Task Manager (Gerenciador de Tarefas em CLI)

Um gerenciador de tarefas simples e direto executado via linha de comando (CLI), desenvolvido inteiramente em **Python**. 

Este projeto foi construído para aplicar conceitos fundamentais da linguagem, como manipulação de listas e dicionários, laços de repetição, funções e estruturação de menus interativos utilizando a estrutura `match/case` (introduzida no Python 3.10).

---

## 🚀 Funcionalidades

O sistema possui um CRUD (Create, Read, Update, Delete) completo de tarefas em memória. Através do menu interativo, o usuário pode:

- [x] **Adicionar tarefas:** Criar novas tarefas (que iniciam com o status pendente por padrão).
- [x] **Visualizar tarefas:** Listar todas as tarefas cadastradas, exibindo seus índices e o status de conclusão (um check `✓` visual).
- [x] **Atualizar tarefas:** Modificar o nome/descrição de uma tarefa já existente através do seu número de índice.
- [x] **Completar tarefas:** Marcar uma tarefa específica como concluída.
- [x] **Deletar tarefas completadas:** Fazer a limpeza da lista, removendo de uma só vez todas as tarefas que já possuem o status de concluídas.

---

## 💻 Como executar o projeto

### Pré-requisitos
Como o projeto utiliza a estrutura `match/case`, é necessário ter o **Python 3.10** ou uma versão superior instalada na sua máquina.

### Passos para rodar localmente

1. Clone este repositório para o seu ambiente local:
```bash
git clone https://github.com/adlerjose/task-manager.git