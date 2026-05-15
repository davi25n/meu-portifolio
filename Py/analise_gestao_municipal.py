"""
Sistema de Análise de Gestão Municipal
Analisa a qualidade da gestão de prefeitos usando dados do Portal de Transparência
https://pacodolumiar.ma.gov.br/transparencia

Versão sem dependências externas - usa apenas bibliotecas padrão
"""

import json
from datetime import datetime
from typing import Dict, List

class AnalisadorGestaoMunicipal:
    """Analisador de gestão municipal baseado em dados de transparência"""
    
    # Pesos para cada área (podem ser ajustados)
    PESOS = {
        'saude': 0.20,
        'educacao': 0.20,
        'seguranca': 0.15,
        'transparencia': 0.15,
        'saneamento': 0.15,
        'estabilidade_fiscal': 0.10,
        'desenvolvimento_economico': 0.05
    }
    
    def __init__(self, url_portal: str = "https://pacodolumiar.ma.gov.br/transparencia"):
        self.url_portal = url_portal
        self.dados_coletados = {}
        
    def coletar_dados_portal(self) -> Dict:
        """Coleta dados do portal de transparência (versão simulada)"""
        # Nota: Para implementação real, seria necessário acesso à API do portal
        # ou web scraping estruturado. Esta versão usa dados de exemplo.
        
        print(f"\n📌 Portal configurado: {self.url_portal}")
        print("   (Dados de exemplo para demonstração)")
        
        dados = {
            'receitas': {
                'total': 50000000,
                'propria': 8000000,
                'transferencias': 42000000
            },
            'despesas': {
                'saude': 7500000,
                'educacao': 12500000,
                'seguranca': 2000000,
                'saneamento': 3000000,
                'administracao': 15000000,
                'outros': 10000000
            },
            'licitacoes': {
                'total': 45,
                'modalidades': {'tomada_preco': 20, 'pregão': 25},
                'valores': 15000000
            },
            'contratos': {
                'total': 120,
                'valor_total': 25000000
            },
            'diarias': {
                'total': 200,
                'valor': 80000
            },
            'folha_pagamento': {
                'total_servidores': 800,
                'massa_salarial': 5000000
            },
            'timestamp_coleta': datetime.now().isoformat()
        }
        
        self.dados_coletados = dados
        return dados
    
    def calcular_indicadores(self, dados: Dict) -> Dict:
        """Calcula indicadores de gestão baseados nos dados coletados"""
        
        indicadores = {
            'saude': self._calcular_indice_saude(dados),
            'educacao': self._calcular_indice_educacao(dados),
            'seguranca': self._calcular_indice_seguranca(dados),
            'transparencia': self._calcular_indice_transparencia(dados),
            'saneamento': self._calcular_indice_saneamento(dados),
            'estabilidade_fiscal': self._calcular_indice_fiscal(dados),
            'desenvolvimento_economico': self._calcular_indice_economico(dados)
        }
        
        return indicadores
    
    def _calcular_indice_saude(self, dados: Dict) -> float:
        """Calcula índice de saúde (0-100)"""
        despesas = dados.get('despesas', {})
        valor_saude = despesas.get('saude', 0)
        
        # Meta: 15% do orçamento para saúde (constitucional)
        indice = min(100, (valor_saude / 15000000) * 100)  # Exemplo: R$15M base
        return round(indice, 2)
    
    def _calcular_indice_educacao(self, dados: Dict) -> float:
        """Calcula índice de educação (0-100)"""
        despesas = dados.get('despesas', {})
        valor_educacao = despesas.get('educacao', 0)
        
        # Meta: 25% do orçamento para educação (constitucional)
        indice = min(100, (valor_educacao / 25000000) * 100)  # Exemplo: R$25M base
        return round(indice, 2)
    
    def _calcular_indice_seguranca(self, dados: Dict) -> float:
        """Calcula índice de segurança (0-100)"""
        despesas = dados.get('despesas', {})
        valor_seguranca = despesas.get('seguranca', 0)
        
        indice = min(100, (valor_seguranca / 5000000) * 100)  # R$5M base
        return round(indice, 2)
    
    def _calcular_indice_transparencia(self, dados: Dict) -> float:
        """Calcula índice de transparência (0-100)"""
        licitacoes = dados.get('licitacoes', {})
        contratos = dados.get('contratos', {})
        
        # Avalia quantidade e atualização dos dados
        qtd_licitacoes = licitacoes.get('total', 0)
        qtd_contratos = contratos.get('total', 0)
        
        indice = min(100, ((qtd_licitacoes + qtd_contratos) / 100) * 100)
        return round(indice, 2)
    
    def _calcular_indice_saneamento(self, dados: Dict) -> float:
        """Calcula índice de saneamento básico (0-100)"""
        despesas = dados.get('despesas', {})
        valor_saneamento = despesas.get('saneamento', 0)
        
        indice = min(100, (valor_saneamento / 8000000) * 100)  # R$8M base
        return round(indice, 2)
    
    def _calcular_indice_fiscal(self, dados: Dict) -> float:
        """Calcula índice de estabilidade fiscal (0-100)"""
        receitas = dados.get('receitas', {})
        despesas = dados.get('despesas', {})
        
        receita_total = receitas.get('total', 0)
        despesa_total = sum(despesas.values())
        
        if receita_total > 0:
            ratio = despesa_total / receita_total
            # Ratio ideal entre 0.85 e 1.0
            if ratio <= 0.85:
                return 100.0
            elif ratio <= 1.0:
                return round(100 - (ratio - 0.85) * 100, 2)
            else:
                return max(0, round(100 - (ratio - 1.0) * 50, 2))
        
        return 50.0  # Valor médio se não houver dados
    
    def _calcular_indice_economico(self, dados: Dict) -> float:
        """Calcula índice de desenvolvimento econômico (0-100)"""
        receitas = dados.get('receitas', {})
        
        # Baseado em receita própria (indicador de atividade econômica)
        receita_propria = receitas.get('propria', 0)
        
        indice = min(100, (receita_propria / 10000000) * 100)  # R$10M base
        return round(indice, 2)
    
    def calcular_nota_gestao(self, indicadores: Dict) -> float:
        """Calcula nota geral de gestão (0-100)"""
        nota = 0
        
        for area, peso in self.PESOS.items():
            nota += indicadores.get(area, 0) * peso
        
        return round(nota, 2)
    
    def identificar_deficiencias(self, indicadores: Dict) -> List[Dict]:
        """Identifica áreas mais deficientes para priorização"""
        deficiencias = []
        
        for area, indice in indicadores.items():
            if indice < 50:
                deficiencias.append({
                    'area': area,
                    'indice': indice,
                    'prioridade': 'alta',
                    'acao_recomendada': self._recomendar_acao(area, indice)
                })
            elif indice < 70:
                deficiencias.append({
                    'area': area,
                    'indice': indice,
                    'prioridade': 'media',
                    'acao_recomendada': self._recomendar_acao(area, indice)
                })
        
        # Ordenar por índice (mais deficiente primeiro)
        return sorted(deficiencias, key=lambda x: x['indice'])
    
    def _recomendar_acao(self, area: str, indice: float) -> str:
        """Recomenda ações baseadas na área e índice"""
        acoes = {
            'saude': "Aumentar investimento em unidades básicas, SAMU e atenção primária",
            'educacao': "Ampliar vagas em creches, melhorar infraestrutura escolar e capacitação de professores",
            'seguranca': "Investir em iluminação pública, câmeras de monitoramento e guardas municipais",
            'transparencia': "Publicar dados em formato aberto, atualizar portal com mais frequência",
            'saneamento': "Ampliar rede de água tratada, esgoto e coleta de lixo",
            'estabilidade_fiscal': "Reduzir despesas correntes, aumentar receita própria e criar reserva de emergência",
            'desenvolvimento_economico': "Fomentar pequenos negócios, atrair empresas e melhorar ambiente de negócios"
        }
        return acoes.get(area, "Analisar e planejar ações específicas")
    
    def gerar_relatorio(self, nome_prefeito: str, municipio: str) -> Dict:
        """Gera relatório completo de análise"""
        dados = self.coletar_dados_portal()
        indicadores = self.calcular_indicadores(dados)
        nota_gestao = self.calcular_nota_gestao(indicadores)
        deficiencias = self.identificar_deficiencias(indicadores)
        
        return {
            'prefeito': nome_prefeito,
            'municipio': municipio,
            'data_analise': datetime.now().strftime("%d/%m/%Y"),
            'nota_gestao': nota_gestao,
            'indicadores': indicadores,
            'deficiencias': deficiencias,
            'recomendacoes': self._gerar_recomendacoes(deficiencias),
            'dados_fonte': dados.get('timestamp_coleta', 'N/A')
        }
    
    def _gerar_recomendacoes(self, deficiencias: List[Dict]) -> List[str]:
        """Gera lista de recomendações priorizadas"""
        recomendacoes = []
        
        for deficiencia in deficiencias:
            recomendacoes.append(f"[{deficiencia['prioridade'].upper()}] {deficiencia['area'].upper()}: {deficiencia['acao_recomendada']}")
        
        return recomendacoes
    
    def comparar_municipios(self, relatorios: List[Dict]) -> List[Dict]:
        """Compara múltiplos municípios"""
        comparacao = []
        
        for relatorio in relatorios:
            comparacao.append({
                'municipio': relatorio['municipio'],
                'prefeito': relatorio['prefeito'],
                'nota': relatorio['nota_gestao'],
                'ranking': 0
            })
        
        # Ordenar por nota
        comparacao.sort(key=lambda x: x['nota'], reverse=True)
        
        # Atribuir ranking
        for i, item in enumerate(comparacao):
            item['ranking'] = i + 1
        
        return comparacao


def executar_analise():
    """Executa análise interativa"""
    print("=" * 60)
    print("  SISTEMA DE ANÁLISE DE GESTÃO MUNICIPAL")
    print("=" * 60)
    print()
    
    # Criar analisador
    analisador = AnalisadorGestaoMunicipal()
    
    # Coletar dados do portal
    print("Coletando dados do Portal de Transparência...")
    dados = analisador.coletar_dados_portal()
    
    if 'erro' in dados:
        print(f"Aviso: {dados['erro']}")
        print("Usando dados de exemplo para demonstração...")
        # Dados de exemplo para teste
        dados = {
            'receitas': {'total': 50000000, 'propria': 8000000, 'transferencias': 42000000},
            'despesas': {
                'saude': 7500000,
                'educacao': 12500000,
                'seguranca': 2000000,
                'saneamento': 3000000,
                'administracao': 15000000,
                'outros': 10000000
            },
            'licitacoes': {'total': 45, 'valores': 15000000},
            'contratos': {'total': 120, 'valor_total': 25000000},
            'diarias': {'total': 200, 'valor': 80000},
            'folha_pagamento': {'total_servidores': 800, 'massa_salarial': 5000000}
        }
    
    # Calcular indicadores
    indicadores = analisador.calcular_indicadores(dados)
    
    # Mostrar indicadores por área
    print("\n📊 INDICADORES POR ÁREA:")
    print("-" * 40)
    
    areas_formatadas = {
        'saude': 'Saúde',
        'educacao': 'Educação',
        'seguranca': 'Segurança',
        'transparencia': 'Transparência',
        'saneamento': 'Saneamento',
        'estabilidade_fiscal': 'Estabilidade Fiscal',
        'desenvolvimento_economico': 'Desenvolvimento Econômico'
    }
    
    for area, indice in indicadores.items():
        nome = areas_formatadas.get(area, area)
        barra = "█" * int(indice / 10) + "░" * (10 - int(indice / 10))
        print(f"  {nome:25} [{barra}] {indice:.1f}")
    
    # Calcular nota geral
    nota_gestao = analisador.calcular_nota_gestao(indicadores)
    
    print("\n" + "=" * 40)
    print(f"  NOTA GERAL DE GESTÃO: {nota_gestao:.1f}/100")
    print("=" * 40)
    
    # Classificação
    if nota_gestao >= 80:
        classificacao = "EXCELENTE"
    elif nota_gestao >= 60:
        classificacao = "BOA"
    elif nota_gestao >= 40:
        classificacao = "REGULAR"
    else:
        classificacao = "DEFICITÁRIA"
    
    print(f"  Classificação: {classificacao}")
    
    # Áreas deficientes
    deficiencias = analisador.identificar_deficiencias(indicadores)
    
    if deficiencias:
        print("\n⚠️  ÁREAS DEFICIENTES (Prioridade):")
        print("-" * 40)
        for i, defi in enumerate(deficiencias, 1):
            print(f"  {i}. {defi['area'].upper()} - Índice: {defi['indice']:.1f}")
            print(f"     → {defi['acao_recomendada']}")
    
    print("\n" + "=" * 60)
    print("  Análise concluída!")
    print("=" * 60)


if __name__ == "__main__":
    executar_analise()