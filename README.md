# Template de Segurança Python

Estrutura base para começar projetos Python com segurança desde o início.

## O que já vem pronto

- Pipeline no GitHub Actions
- SAST com Bandit
- SCA com pip-audit
- .gitignore protegendo senhas e arquivos locais
- DAST com OWASP ZAP (manual)

## Como usar

1. Clique em **Use this template**
2. Crie seu novo repositório
3. Troque o exemplo do `app.py` pelo código do seu projeto
4. Adicione as bibliotecas que você usar no `requirements.txt`
5. Atualize este README com o nome e a descrição do seu projeto
6. Faça um commit e veja a aba **Actions**

## DAST com OWASP ZAP (manual)

O DAST testa o **site rodando**. O Bandit confere o código do script e o pip-audit confere as bibliotecas, e o ZAP ataca as páginas do site para achar falhas como XSS.

### Quando usar

- Use quando o projeto tem um **site ou API** que abre uma porta (por exemplo, `python api.py` na porta 8000)
- Não use em scripts (como um que lê uma planilha) nem em chatbots de terminal: eles não abrem porta nenhuma, então o ZAP não tem o que atacar e o job falha

### Como rodar

1. Abra a aba **Actions** do repositório
2. Clique em **DAST ZAP (manual)** e depois em **Run workflow**
3. Em **Comando que liga o app**, escreva o comando do seu projeto (padrão: `python app.py`)
4. Em **Porta do app**, escreva a porta em que ele abre (padrão: `5000`)
5. Clique em **Run workflow** e espere uns 2 a 3 minutos

### Se ficar vermelho

Abra o job no Actions e leia o último passo:

- `ZAP achou XSS refletido ... ou cookie sem HttpOnly`: o ZAP achou uma falha. Corrija o código
- `Relatorio JSON nao encontrado`: o ZAP não chegou a rodar, normalmente porque o app não abriu. Confira o comando e a porta
