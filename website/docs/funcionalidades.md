---
id: funcionalidades
title: Funcionalidades
sidebar_position: 2
---

# Funcionalidades principais

## Gestao de eventos

Os organizadores podem criar eventos com data, capacidade e preco. A versao
mais recente tambem suporta **setores**, permitindo diferenciar zonas como:

1. Geral
2. VIP
3. Plateia
4. Balcao

Cada setor guarda:

- preco;
- capacidade;
- bilhetes vendidos.

## Compra de bilhetes

O cliente escolhe um evento e confirma a compra. Se houver vagas, o sistema:

- incrementa os bilhetes vendidos;
- guarda a alteracao no ficheiro JSON;
- gera um codigo de entrada para validacao.

```text title="Exemplo de codigo gerado"
Tech Summit-VIP
```

## Validacao pela equipa de staff

A validacao controla se os check-ins ainda nao ultrapassaram os bilhetes
vendidos. Isto ajuda a evitar entradas duplicadas.

:::warning Nota academica
O codigo atual simula QR Codes em texto. Uma evolucao natural seria gerar QR
Codes reais e associar cada bilhete a um identificador unico.
:::

## Dashboard

O dashboard resume informacao util para a gestao:

| Indicador | Como ajuda |
| --- | --- |
| Receita por evento | Mede o impacto financeiro |
| Bilhetes vendidos | Mostra procura e lotacao |
| Check-ins | Mostra ocupacao real na porta |
| Evento mais popular | Apoia decisoes futuras |

## Checklist logistico

A aplicacao inclui um checklist para tarefas operacionais como som, luzes,
seguranca e limpeza.

- [x] Som testado
- [x] Luzes preparadas
- [ ] Equipa de seguranca confirmada
- [ ] Limpeza pos-evento planeada


## Tabela de Funcionalidades

| Funcionalidade | Descrição | Estado |
|---|---|---|
| Login de utilizadores | Permite autenticação no sistema | ✅ |
| Criação de eventos | Permite criar novos eventos | ✅ |
| Listagem de eventos | Mostra todos os eventos disponíveis | ✅ |
| Compra de bilhetes | Permite comprar bilhetes | ✅ |
| Check-in | Validação de entrada nos eventos | ✅ |
| Dashboard | Exibe métricas e estatísticas | ✅ |
| Armazenamento JSON | Guarda os dados do sistema | ✅ |
| Banco de dados SQL | Integração futura | ❌ |
| Interface gráfica | Planeado para futuras versões | ❌ |