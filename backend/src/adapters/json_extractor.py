import json
import os
import sys

# Adiciona a pasta src ao caminho do sistema para o Python achar a pasta domain
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from domain.player_stats import PlayerPerformance

class RiotDataExtractor:
    """
    Adapter responsável por converter o JSON sujo da API
    na Entidade limpa do nosso Domínio.
    """
    
    @staticmethod
    def load_from_file(filepath: str, target_name: str) -> PlayerPerformance:
        # 1. Abre o arquivo e carrega o JSON para a memória
        with open(filepath, 'r', encoding='utf-8') as file:
            raw_data = json.load(file)
            
        # 2. Navega pelas Estruturas de Dados
        players_list = raw_data.get('data', [])[0].get('players', {}).get('all_players', [])
        
        for player in players_list:
            if player.get('name') == target_name:
                stats = player.get('stats', {})
                
                # 3. Mapeamento (Instanciando a Entidade Limpa)
                return PlayerPerformance(
                    kills=stats.get('kills', 0),
                    deaths=stats.get('deaths', 0),
                    headshots=stats.get('headshots', 0),
                    bodyshots=stats.get('bodyshots', 0),
                    ability_casts=player.get('ability_casts', {}).get('c_cast', 0).get('e_cast', 0).get('q_cast', 0), # Exemplo de sub-dicionário
                    economy_score=player.get('economy', {}).get('spent', {}).get('overall', 0)
                )
                
        raise ValueError(f"Jogador {target_name} não encontrado na partida.")