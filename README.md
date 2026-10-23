# Robô de avisos de cobrança por e-mail

Script em Python que lê uma planilha de cobranças, separa os clientes **em atraso** ou **com vencimento próximo** e envia um lembrete por e-mail para cada um.

> Todos os dados deste projeto são fictícios e gerados por `gerar_cobrança.py`.

## O problema que resolve
Lembrar clientes de pagamentos pendentes costuma ser manual, repetitivo e fácil de esquecer. Este robô faz esse trabalho em segundos e só avisa quem realmente precisa.

## O que ele faz
- Lê a planilha `cobrancas.xlsx` (nome, e-mail, valor, vencimento e se já pagou)
- Ignora quem já pagou, mesmo que esteja escrito "sim", "Sim" ou "SIM"
- Calcula quantos dias faltam para vencer ou quantos dias de atraso
- Seleciona os atrasados e quem vence nos próximos dias (configurável em `DIAS_AVISO`)
- Monta uma mensagem diferente para cada caso
- Envia o e-mail pelo Gmail

Exemplo de mensagem:

```
Olá, Ana! Sua cobrança de R$ 202.44 venceu em 14/10 e está com 9 dias de atraso.
```

## Segurança
- Usuário e senha ficam em um arquivo `.env`, **fora do código e fora do GitHub**
- Usa senha de app do Google, não a senha da conta
- `MODO_TESTE = True` por padrão: todos os e-mails vão para o endereço do próprio usuário, com `[TESTE para ...]` no assunto. Só mude para `False` com autorização de quem vai receber.

## Como usar
1. Instale as dependências:
   ```bash
   pip install pandas openpyxl python-dotenv
   ```
2. Gere uma planilha de exemplo:
   ```bash
   python gerar_cobrança.py
   ```
3. Crie um arquivo `.env` na mesma pasta:
   ```
   EMAIL_USUARIO=seuemail@gmail.com
   EMAIL_SENHA=sua_senha_de_app
   ```
   (No Gmail é preciso ativar a verificação em duas etapas e gerar uma "senha de app".)
4. Rode o robô:
   ```bash
   python avisos.py
   ```

## Tecnologias
Python, pandas, openpyxl, smtplib e python-dotenv.

## Possíveis melhorias
- Agendar a execução diária
- Registrar um histórico dos envios
- Deixar o texto das mensagens configurável
- Enviar também por WhatsApp
