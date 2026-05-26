---
id: funcionalidades-detalhes
title: Detalhes das Funcionalidades Avançadas
sidebar_position: 2
---

# Funcionalidades Avançadas do EventFlow

O **EventFlow** não se limita apenas à venda básica de bilhetes. Implementámos uma série de lógicas baseadas em Programação Orientada a Objetos (POO) para garantir uma gestão robusta tanto para os Organizadores como para os Clientes.

---

## 1. Setores e Controlo de Lotação (VIP, Plateia, Geral)

A flexibilidade é o núcleo do EventFlow. Cada evento pode ser segmentado em vários setores, cada um com as suas próprias regras de negócio.

* **Preços Dinâmicos:** Um evento pode ter um setor "VIP" com 10 lugares a 100€ e um setor "Geral" com 100 lugares a 20€.
* **Bloqueio Automático:** O sistema monitoriza as vagas em tempo real. Se o setor VIP esgotar, a compra é bloqueada para esse setor específico, não afetando o setor Geral.

> **Nota de Migração:** Eventos antigos na base de dados que não possuam setores definidos são automaticamente encapsulados num setor padrão "Geral" pelo nosso motor de inicialização.

---

## 2. Dashboard Operacional

Para o Organizador, a informação é poder. A opção `9. Dashboard de Vendas` no menu principal lê os dados do ficheiro JSON e gera estatísticas instantâneas:

* **💰 Receita Total:** Soma calculada dinamicamente (`vendidos * preco_do_setor`).
* **🎟️ Taxa de Check-ins:** Comparação entre os bilhetes efetivamente validados na porta pelo Staff e o total vendido.
* **📍 Performance:** Identificação clara de quais eventos e setores estão a gerar mais lucro.

---

## 3. Gestão Pessoal do Cliente (Cancelamentos)

O EventFlow oferece autonomia aos clientes.

1. **Histórico Transparente:** O cliente digita o seu nome e vê imediatamente todos os bilhetes associados ao seu perfil.
2. **Reembolsos e Libertação de Vagas:** Caso o cliente decida cancelar um bilhete, o sistema elimina o registo do seu histórico e **devolve automaticamente a vaga à lotação do evento**, permitindo que outra pessoa compre esse bilhete.