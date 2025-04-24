"""
Sistema de gerenciamento de funcionários.
"""
from dataclasses import dataclass


@dataclass
class Funcionario:
    """Representação de um funcionário com foco em custos trabalhistas e comissões.
    
    Attributes:
        nome: Nome do funcionário
        matricula: Número de matrícula do funcionário
        salario_hora: Valor do salário por hora trabalhada
        horas_trabalhadas: Quantidade de horas trabalhadas no mês
        horas_extras: Quantidade de horas extras trabalhadas no mês
        custo_empregador: Custo fixo mensal do empregador (INSS, FGTS, etc)
        tem_comissao: Indica se o funcionário recebe comissão
        valor_comissao: Valor da comissão por contrato fechado
        contratos_fechados: Número de contratos fechados no mês
        vale_refeicao: Valor do vale-refeição mensal
        vale_transporte: Valor do vale-transporte mensal
    """

    nome: str
    matricula: int
    salario_hora: float = 100.0
    horas_trabalhadas: float = 0.0
    horas_extras: float = 0.0
    custo_empregador: float = 1000.0
    tem_comissao: bool = True
    valor_comissao: float = 100.0
    contratos_fechados: int = 0
    vale_refeicao: float = 0.0
    vale_transporte: float = 0.0

    def __post_init__(self):
        """Valida os valores após inicialização."""
        if self.salario_hora < 0:
            raise ValueError("Salário por hora não pode ser negativo")
        if self.horas_trabalhadas < 0:
            raise ValueError("Horas trabalhadas não podem ser negativas")
        if self.horas_extras < 0:
            raise ValueError("Horas extras não podem ser negativas")
        if self.contratos_fechados < 0:
            raise ValueError("Contratos fechados não podem ser negativos")
        if self.vale_refeicao < 0:
            raise ValueError("Vale-refeição não pode ser negativo")
        if self.vale_transporte < 0:
            raise ValueError("Vale-transporte não pode ser negativo")

    def calcular_salario_bruto(self) -> float:
        """Calcula o salário bruto do funcionário (horas normais + extras)."""
        return (self.salario_hora * self.horas_trabalhadas) + self.calcular_horas_extras()

    def calcular_custo_total(self) -> float:
        """Calcula o custo total do funcionário para a empresa."""
        return (self.calcular_salario_bruto() + self.custo_empregador + 
                self.calcular_beneficios())

    def calcular_comissao(self) -> float:
        """Calcula o valor total da comissão do funcionário."""
        if self.tem_comissao:
            return self.valor_comissao * self.contratos_fechados
        return 0.0

    def calcular_horas_extras(self) -> float:
        """Calcula o valor das horas extras (1.5x o valor normal)."""
        return self.horas_extras * self.salario_hora * 1.5

    def calcular_beneficios(self) -> float:
        """Calcula o total de benefícios."""
        return self.vale_refeicao + self.vale_transporte