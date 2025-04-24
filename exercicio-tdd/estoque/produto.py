"""
Sistema de controle de estoque.
"""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Produto:
    """Representação de um produto no estoque."""

    codigo: str
    nome: str
    preco: float
    quantidade: int = 0
    data_validade: Optional[datetime] = None
    estoque_minimo: int = 10
    estoque_maximo: int = 100

    def adicionar_estoque(self, quantidade: int) -> None:
        """Adiciona quantidade ao estoque do produto."""
        if quantidade <= 0:
            raise ValueError("Quantidade deve ser positiva")
        if self.quantidade + quantidade > self.estoque_maximo:
            raise ValueError("Quantidade excede o estoque máximo")
        self.quantidade += quantidade

    def remover_estoque(self, quantidade: int) -> bool:
        """Remove quantidade do estoque do produto."""
        if quantidade <= 0:
            raise ValueError("Quantidade deve ser positiva")
        if self.quantidade - quantidade < 0:
            return False
        self.quantidade -= quantidade
        return True

    def verificar_estoque_baixo(self) -> bool:
        """Verifica se o estoque está abaixo do mínimo."""
        return self.quantidade < self.estoque_minimo

    def calcular_valor_total(self) -> float:
        """Calcula o valor total do produto em estoque."""
        return self.preco * self.quantidade

    def verificar_validade(self, data_referencia: datetime = None) -> bool:
        """Verifica se o produto está dentro da validade."""
        if self.data_validade is None:
            return True
        data_ref = data_referencia if data_referencia else datetime.now()
        return data_ref <= self.data_validade