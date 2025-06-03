# Sistema de Gerenciamento Acadêmico (CRUD)💼

Este projeto é um sistema simples de **gerenciamento acadêmico**, desenvolvido em Python, com foco em praticar lógica de programação, estruturas de repetição, condicionais e manipulação de listas. O sistema segue o padrão CRUD (Create, Retrieve, Update, Delete) e está preparado para ser expandido no futuro.

## Funcionalidades 

- **Menu Principal:** 
  Permite ao usuário escolher entre gerenciar estudantes, disciplinas, professores, turmas, matrículas ou sair do sistema.

- **Menu de Operações (Estudantes):**  
  - **Incluir:** Permite cadastrar o nome de um estudante.
  - **Listar:** Exibe todos os estudantes cadastrados ou uma mensagem caso não haja nenhum.
  - **Atualizar/Excluir:** Exibe mensagem de "EM DESENVOLVIMENTO".
  - **Voltar:** Retorna ao menu principal.

- **Outros módulos (Disciplinas, Professores, Turmas, Matrículas):**  
  Exibem mensagem de "Funcionalidade em desenvolvimento" e retornam ao menu principal.

- **Tratamento de Erros:**  
  O sistema trata entradas inválidas, evitando que o programa seja interrompido por erros de digitação.

## Como usar 📢

1. Execute o arquivo CRUD.py em um ambiente Python 3.
2. Navegue pelo menu principal usando os números das opções.
3. Para estudantes, utilize as opções de incluir e listar.
4. Para as demais funcionalidades, aguarde as próximas versões.

## Estrutura do Código 🧬

- **Função `menu_principal()`:**  
  Controla o fluxo do menu principal e direciona para o menu de operações ou exibe mensagens de desenvolvimento.

- **Função `menu_operacoes(nome)`:**  
  Gerencia as operações CRUD para estudantes, com possibilidade de expansão para outros módulos.

- **Lista `estudantes`:**  
  Armazena os nomes dos estudantes cadastrados.

## Possíveis melhorias futuras 👨‍💻

- Implementar cadastro completo para todos os módulos (disciplinas, professores, turmas, matrículas).
- Adicionar atualização e exclusão de estudantes.
- Salvar e carregar dados em arquivos (txt, csv, json).
- Criar relatórios e filtros.
- Adicionar interface gráfica ou web.
- Implementar autenticação de usuários.
- Escrever testes automatizados.

## Sobre o desenvolvimento

Durante a preparação deste projeto de programação, o autor usou Visual Studio Code, Python 3.10 e Git para desenvolver, testar e versionar o código de forma organizada e eficiente. Após usar essas ferramentas, o autor revisou e editou o conteúdo conforme necessário e assume total responsabilidade pelo conteúdo.

---

Sinta-se à vontade para adaptar conforme sua necessidade!
