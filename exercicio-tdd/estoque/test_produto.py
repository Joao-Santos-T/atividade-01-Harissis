"""
Testes da classe Produto.
"""
import unittest
from datetime import datetime, timedelta
from produto import Produto

class TestProduto(unittest.TestCase):
    """Testa a classe Produto."""

    def setUp(self):
        """Configura o ambiente de teste."""
        self.hoje = datetime.now()
        self.amanha = self.hoje + timedelta(days=1)
        
        self.produto_valido = Produto(
            codigo="001",
            nome="Leite Integral",
            preco=5.99,
            quantidade=50,
            data_validade=self.amanha,
            estoque_minimo=10,
            estoque_maximo=100
        )
        
        self.produto_sem_validade = Produto(
            codigo="002",
            nome="Arroz",
            preco=15.90,
            quantidade=100
        )

    def test_inicializacao(self):
        """Verifica se o produto é inicializado corretamente."""
        self.assertEqual(self.produto_valido.codigo, "001")
        self.assertEqual(self.produto_valido.nome, "Leite Integral")
        self.assertEqual(self.produto_valido.preco, 5.99)
        self.assertEqual(self.produto_valido.quantidade, 50)
        self.assertEqual(self.produto_valido.data_validade, self.amanha)

    def test_adicionar_estoque(self):
        """Verifica se o estoque é adicionado corretamente."""
        self.produto_valido.adicionar_estoque(20)
        self.assertEqual(self.produto_valido.quantidade, 70)
        
        with self.assertRaises(ValueError):
            self.produto_valido.adicionar_estoque(-5)
            
        with self.assertRaises(ValueError):
            self.produto_valido.adicionar_estoque(50)  # Excederia o máximo de 100

    def test_remover_estoque(self):
        """Verifica se o estoque é removido corretamente."""
        self.assertTrue(self.produto_valido.remover_estoque(20))
        self.assertEqual(self.produto_valido.quantidade, 30)
        
        self.assertFalse(self.produto_valido.remover_estoque(50))  # Sem estoque suficiente
        self.assertEqual(self.produto_valido.quantidade, 30)  # Não deve alterar
        
        with self.assertRaises(ValueError):
            self.produto_valido.remover_estoque(-10)

    def test_verificar_estoque_baixo(self):
        """Verifica se a detecção de estoque baixo funciona corretamente."""
        self.assertFalse(self.produto_valido.verificar_estoque_baixo())
        
        self.produto_valido.quantidade = 5
        self.assertTrue(self.produto_valido.verificar_estoque_baixo())
        
        self.produto_valido.quantidade = 10
        self.assertFalse(self.produto_valido.verificar_estoque_baixo())

    def test_calcular_valor_total(self):
        """Verifica se o valor total é calculado corretamente."""
        self.assertAlmostEqual(self.produto_valido.calcular_valor_total(), 299.5)  # 50 * 5.99
        self.assertEqual(self.produto_sem_validade.calcular_valor_total(), 1590.0)  # 100 * 15.90

    def test_verificar_validade(self):
        """Verifica se a validação de data de validade funciona corretamente."""
        self.assertTrue(self.produto_valido.verificar_validade())
        
        # Testando com data futura (depois da validade)
        depois_validade = self.amanha + timedelta(days=1)
        self.assertFalse(self.produto_valido.verificar_validade(depois_validade))
        
        # Produto sem data de validade sempre válido
        self.assertTrue(self.produto_sem_validade.verificar_validade())

if __name__ == "__main__":
    unittest.main()