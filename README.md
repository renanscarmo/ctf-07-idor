# CTF 07: IDOR (acesso a dados de outro usuário)

Projeto criado a partir do [template-seguranca](https://github.com/renanscarmo/template-seguranca)
para praticar segurança em Python.

## Objetivo

Ver o pedido de outra pessoa trocando o número no endereço e depois corrigir a falha.

## Como foi

1. **Antes:** a rota `/pedido/<numero>` conferia que havia alguém logado, mas não conferia se o pedido era dessa pessoa. Logada como `ana`, bastou trocar `/pedido/1` por `/pedido/3` para ver o pedido da Carla, com a flag.
2. **Detecção:** o Bandit e o pip-audit ficaram verdes, e o DAST manual (OWASP ZAP) também não achou nada. O ZAP não faz login e não sabe de quem é cada pedido. Quem achou a falha foi o teste manual.
3. **Depois:** a rota passou a comparar o dono do pedido com o usuário logado (`pedido["dono"] != session["usuario"]`) e responde **403 Forbidden** quando não são a mesma pessoa.

## O que aprendi

- IDOR acontece quando o site usa um identificador do endereço (como o número do pedido) sem conferir se aquele dado pertence a quem está logado
- Estar logado não é o mesmo que ter permissão para ver aquele dado específico
- A verificação do dono precisa estar em toda rota que mostra dados de um usuário
- O Bandit, o pip-audit e o ZAP não conhecem as regras do negócio, então falhas de permissão dependem de teste manual
- Esconder os números dos pedidos não substitui a verificação do dono

## Ferramentas

- SAST com Bandit
- SCA com pip-audit
- DAST manual com OWASP ZAP
- GitHub Actions
