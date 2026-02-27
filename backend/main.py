from src.adapters.json_extractor import RiotDataExtractor
import os

def run_analysis():
    # Caminho para o seu arquivo de pesquisa (ajustado para o ambiente Linux)
    # Suba um nível da pasta backend para chegar em docs/
    json_path = os.path.abspath("../docs/api_research/match_sample_raw.json")
    
    target_player = "Namorado da Sasa" 

    try:
        print(f"--- Iniciando Processamento do Arise ---")
        
        # O Adapter faz o trabalho sujo de ler o JSON e entregar a Entidade limpa
        performance = RiotDataExtractor.load_from_file(json_path, target_player)
        
        print(f"Jogador: {target_player}")
        print(f"Kills: {performance.kills} | Deaths: {performance.deaths}")
        print(f"K/D Ratio: {performance.kd_ratio}")
        print(f"Precisão (HS): {performance.headshots}")
        print(f"Economia (Gasto): {performance.economy_score}")
        
        print(f"--- Processamento Concluído com Sucesso ---")

    except Exception as e:
        print(f"Erro ao processar os dados: {e}")

if __name__ == "__main__":
    run_analysis()