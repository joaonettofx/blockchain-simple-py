import hashlib
import json
from datetime import datetime


class Block:
    def __init__(self, index, data, previous_hash):
        self.index         = index
        self.timestamp     = datetime.now().isoformat()
        self.data          = data
        self.previous_hash = previous_hash
        self.nonce         = 0
        self.hash          = self.calculate_hash()

    def calculate_hash(self):
        block_string = json.dumps({
            "index":         self.index,
            "timestamp":     self.timestamp,
            "data":          self.data,
            "previous_hash": self.previous_hash,
            "nonce":         self.nonce
        }, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine(self, difficulty):
        target = "0" * difficulty
        print(f"Minerando bloco #{self.index}...")
        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"  Bloco #{self.index} minerado! Nonce={self.nonce} | Hash={self.hash[:30]}...")

    def __repr__(self):
        return (
            f"Block #{self.index}\n"
            f"  Timestamp : {self.timestamp}\n"
            f"  Data      : {self.data}\n"
            f"  Prev Hash : {self.previous_hash[:20]}...\n"
            f"  Hash      : {self.hash[:20]}...\n"
            f"  Nonce     : {self.nonce}"
        )


class Blockchain:
    def __init__(self, difficulty=4):
        self.difficulty = difficulty
        self.chain      = [self._create_genesis()]

    def _create_genesis(self):
        genesis = Block(0, "Bloco Genesis", "0")
        genesis.mine(self.difficulty)
        return genesis

    def get_last_block(self):
        return self.chain[-1]

    def add_block(self, data):
        last      = self.get_last_block()
        new_block = Block(
            index         = last.index + 1,
            data          = data,
            previous_hash = last.hash
        )
        new_block.mine(self.difficulty)
        self.chain.append(new_block)
        return new_block

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current  = self.chain[i]
            previous = self.chain[i - 1]
            if current.hash != current.calculate_hash():
                print(f"  [ERRO] Hash invalido no bloco #{current.index}")
                return False
            if current.previous_hash != previous.hash:
                print(f"  [ERRO] Cadeia quebrada entre #{previous.index} e #{current.index}")
                return False
        return True


if __name__ == "__main__":
    print("=" * 50)
    print("  PROJETO 1 — Blockchain em Python")
    print("=" * 50)

    print("\n[1] Criando blockchain (dificuldade=4)...\n")
    bc = Blockchain(difficulty=4)

    print("\n[2] Adicionando blocos de transacoes...\n")
    bc.add_block({"de": "Alice", "para": "Bob",   "valor": 50})
    bc.add_block({"de": "Bob",   "para": "Carol",  "valor": 25})
    bc.add_block({"de": "Carol", "para": "Alice",  "valor": 10})

    print("\n[3] Estado completo da cadeia:\n")
    for block in bc.chain:
        print(block)
        print()

    valida = bc.is_valid()
    print(f"[4] Blockchain valida? --> {valida}\n")

    print("[5] Simulando ataque: adulterando valor do bloco #1...\n")
    bc.chain[1].data = {"de": "Alice", "para": "Bob", "valor": 9999}
    valida_apos = bc.is_valid()
    print(f"[6] Blockchain valida após ataque? --> {valida_apos}")