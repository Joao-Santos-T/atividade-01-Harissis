"""
Testes da classe Funcionario.
"""
import unittest
from funcionario import Funcionario


class TestFuncionario(unittest.TestCase):
    """Testes da classe Funcionario."""

    def test_calcular_salario_bruto(self):
        """Testa o cálculo do salário bruto."""
        funcionario = Funcionario(nome="João", matricula=1, salario_hora=50.0, horas_trabalhadas=160)
        self.assertEqual(funcionario.calcular_salario_bruto(), 8000.0)

    def test_calcular_custo_total(self):
        """Testa o cálculo do custo total."""
        funcionario = Funcionario(nome="Maria", matricula=2, salario_hora=50.0, 
                                 horas_trabalhadas=160, custo_empregador=1500)
        self.assertEqual(funcionario.calcular_custo_total(), 9500.0)

    def test_calcular_comissao(self):
        """Testa o cálculo da comissão."""
        funcionario = Funcionario(nome="Ana", matricula=3, tem_comissao=True, 
                                 valor_comissao=200.0, contratos_fechados=3)
        self.assertEqual(funcionario.calcular_comissao(), 600.0)

    def test_comissao_desativada(self):
        """Testa funcionário que não recebe comissão."""
        funcionario = Funcionario(nome="Carlos", matricula=4, tem_comissao=False, 
                                 valor_comissao=200.0, contratos_fechados=5)
        self.assertEqual(funcionario.calcular_comissao(), 0.0)

    def test_valores_negativos(self):
        """Testa se valores negativos são rejeitados."""
        with self.assertRaises(ValueError):
            Funcionario(nome="Erro", matricula=5, salario_hora=-100)
        with self.assertRaises(ValueError):
            Funcionario(nome="Erro", matricula=6, horas_trabalhadas=-10)
        with self.assertRaises(ValueError):
            Funcionario(nome="Erro", matricula=7, horas_extras=-5)
        with self.assertRaises(ValueError):
            Funcionario(nome="Erro", matricula=8, contratos_fechados=-2)
        with self.assertRaises(ValueError):
            Funcionario(nome="Erro", matricula=9, vale_refeicao=-100)
        with self.assertRaises(ValueError):
            Funcionario(nome="Erro", matricula=10, vale_transporte=-50)

    def test_horas_extras(self):
        """Testa cálculo de horas extras."""
        funcionario = Funcionario(nome="Pedro", matricula=11, salario_hora=50, horas_extras=10)
        self.assertEqual(funcionario.calcular_horas_extras(), 750.0)  # 10 * 50 * 1.5

    def test_salario_com_horas_extras(self):
        """Testa cálculo do salário bruto com horas extras."""
        funcionario = Funcionario(nome="Teresa", matricula=12, salario_hora=50, 
                                 horas_trabalhadas=160, horas_extras=10)
        self.assertEqual(funcionario.calcular_salario_bruto(), 8750.0)  # (160*50) + (10*50*1.5)

    def test_beneficios(self):
        """Testa cálculo de benefícios."""
        funcionario = Funcionario(nome="José", matricula=13, vale_refeicao=300, vale_transporte=200)
        self.assertEqual(funcionario.calcular_beneficios(), 500.0)

    def test_custo_total_completo(self):
        """Testa cálculo completo do custo total."""
        funcionario = Funcionario(
            nome="Marta", matricula=14,
            salario_hora=50,
            horas_trabalhadas=160,
            horas_extras=5,
            custo_empregador=1500,
            tem_comissao=True,
            valor_comissao=200,
            contratos_fechados=3,
            vale_refeicao=300,
            vale_transporte=200
        )
        # Salário: (160*50) + (5*50*1.5) = 8000 + 375 = 8375
        # Comissão: 3*200 = 600
        # Benefícios: 300 + 200 = 500
        # Custo empregador: 1500
        # Total: 8375 + 600 + 500 + 1500 = 10975
        self.assertEqual(funcionario.calcular_custo_total(), 10975.0)


if __name__ == "__main__":
    unittest.main()