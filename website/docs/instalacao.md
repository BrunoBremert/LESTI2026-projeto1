---
id: instalacao
title: Instalacao e execucao
sidebar_position: 3
---

# Instalacao e execucao

## Requisitos

- Python 3.10 ou superior
- Git
- Node.js 18 ou superior, apenas para o site Docusaurus

## Executar a aplicacao

Na raiz do repositorio:

```bash
python main.py
```

Os dados sao guardados em ficheiros JSON, por exemplo:

```text
eventos.json
data/eventos.json
data/usuarios.json
```

## Executar o site

Dentro da pasta `website`:

```bash
npm install
npm run start
```

Para gerar a versao final:

```bash
npm run build
```

:::info
O comando `npm run build` e o melhor teste rapido para confirmar que a
configuracao do Docusaurus esta valida.
:::

## Estrutura do projeto

```text
LESTI2026-projeto1/
├── main.py
├── services/
├── storage/
├── data/
├── docs/
└── website/
    ├── docs/
    ├── src/
    ├── static/
    └── docusaurus.config.js
```
