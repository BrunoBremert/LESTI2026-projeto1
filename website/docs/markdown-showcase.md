---
id: markdown-showcase
title: Markdown usado
sidebar_position: 5
---

# Markdown usado no site

Esta pagina demonstra varias tags Markdown e recursos MDX/Docusaurus usados no
site, um dos pontos referidos no enunciado.

## Texto

Texto com **negrito**, _italico_, `codigo inline` e link para a
[documentacao oficial do Docusaurus](https://docusaurus.io/).

## Lista ordenada

1. Criar ramo.
2. Implementar alteracoes.
3. Abrir pull request.
4. Fazer merge apos revisao.

## Lista nao ordenada

- Homepage de produto
- Documentacao tecnica
- Guia Git
- Blog de novidades

## Tabela

| Recurso | Estado |
| --- | --- |
| Navbar | Concluido |
| Footer | Concluido |
| Tema claro/escuro | Concluido |
| Build estatico | Validar com `npm run build` |

## Bloco de codigo

```python title="main.py"
if __name__ == "__main__":
    app = SistemaBilheteria()
    app.executar()
```

## Callouts

:::info Informacao
Docusaurus suporta blocos especiais para destacar conteudo.
:::

:::caution Atencao
Antes de entregar, confirmar que o site compila e que o repositorio remoto esta
atualizado.
:::

## Checklist

- [x] Criar configuracao Docusaurus
- [x] Criar landing page
- [x] Criar documentacao do produto
- [x] Criar pagina de evidencias Git
- [ ] Publicar ou anexar link do repositorio remoto
