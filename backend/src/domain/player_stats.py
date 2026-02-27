from dataclasses import dataclass

@dataclass
class PlayerPerformance:
    """
    Entidade de Domínio que representa a performance filtrada de um jogador.
    Independente de APIs externas ou Bancos de Dados.
    """
    kills: int
    deaths: int
    headshots: int
    bodyshots: int
    ability_casts: int
    economy_score: int  # Pode ser a média de créditos gastos ou um score calculado

    @property
    def kd_ratio(self) -> float:
        if self.deaths == 0:
            return float(self.kills)
        return round(self.kills / self.deaths, 2)