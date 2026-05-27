# Arquitetura do Sistema

## Visão Geral

O projeto foi desenvolvido utilizando uma arquitetura modular, permitindo separar responsabilidades e facilitar a manutenção do sistema.

A aplicação foi dividida em diferentes componentes responsáveis pela lógica do sistema, armazenamento dos dados e documentação.

---

## Estrutura do Projeto

| Pasta | Responsabilidade |
|---|---|
| data/ | Armazenamento dos ficheiros JSON |
| docs/ | Documentação do projeto |
| services/ | Regras de negócio do sistema |
| storage/ | Gestão da persistência dos dados |
| website/ | Site de documentação Docusaurus |

---

## Fluxo do Sistema

O funcionamento da aplicação segue o seguinte fluxo:

```txt
Utilizador
   ↓
Sistema de Bilheteria
   ↓
Services
   ↓
JSON Storage    