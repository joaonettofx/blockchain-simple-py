# Blockchain Simples em Python

Uma implementação educacional de blockchain em Python, com **Proof of Work (PoW)**, validação da cadeia e demonstração prática de adulteração de dados.

> Projeto focado em aprendizado: entender como blocos são encadeados por hash e por que alterar um bloco quebra a integridade da rede.

---

## Funcionalidades

- Criação de bloco com:
  - `index`
  - `timestamp`
  - `data`
  - `previous_hash`
  - `nonce`
  - `hash`
- Cálculo de hash com **SHA-256**
- Mineração com dificuldade ajustável (`difficulty`)
- Geração automática do **bloco gênesis**
- Adição de novos blocos com referência ao hash anterior
- Verificação de integridade da blockchain (`is_valid()`)
- Simulação de ataque por alteração de transação

---

## Conceitos que este projeto demonstra

- **Imutabilidade prática**: ao alterar dados, o hash muda.
- **Encadeamento criptográfico**: cada bloco aponta para o hash do anterior.
- **Proof of Work**: encontrar `nonce` até o hash começar com N zeros.
- **Validação da cadeia**: detectar quebra de hash ou ligação entre blocos.

---

## Estrutura

```text
.
├── blockchain.py   # Código principal (Block + Blockchain + execução de exemplo)
└── README.md