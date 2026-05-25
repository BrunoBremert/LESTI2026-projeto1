---
id: intro
title: Visao geral
sidebar_position: 1
---

# EventFlow

O **EventFlow** e uma aplicacao de consola para gestao de eventos e bilhetes.
Foi criada no ambito do projeto LESTI 2026 e junta num unico fluxo:

- registo e login de utilizadores;
- criacao, edicao e remocao de eventos;
- venda de bilhetes;
- validacao de entradas pela equipa de staff;
- dashboard com receita, lotacao e check-ins;
- persistencia de dados em ficheiros JSON.

:::tip Proposta de valor
O objetivo e permitir que uma pequena organizacao consiga controlar o ciclo do
evento sem depender de folhas de calculo soltas.
:::

## Publico-alvo

| Perfil | Necessidade | Resposta do EventFlow |
| --- | --- | --- |
| Organizador | Criar eventos e gerir capacidade | CRUD de eventos e setores |
| Cliente | Comprar bilhete com confirmacao simples | Compra guiada no terminal |
| Staff | Validar entrada na porta | Validacao por codigo de bilhete |
| Gestor | Acompanhar resultados | Dashboard de vendas e ocupacao |

## Identidade do produto

> EventFlow transforma uma bilheteira de trabalho manual numa operacao
> organizada, rastreavel e pronta para evoluir.

O site em Docusaurus serve como camada publica do projeto: apresenta o produto,
documenta a instalacao e mostra evidencias do processo Git pedido no TP3.
