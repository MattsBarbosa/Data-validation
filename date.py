from datetime import datetime, timedelta

class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.format_data()

    def mes_cadastro(self):
        meses_do_ano = [
            "janeiro", "fevereiro", "março", "abril",
            "maio", "junho", "julho", "agosto", "setembro",
            "outubro", "novembro", "dezembro"
        ]
        mes_cadastro = self.momento_cadastro.month -1
        return meses_do_ano[mes_cadastro]

        #.month range de 1 a 12, usamos -1 porque
        # na list o index começa em 0.

    def dia_semana(self):
        dia_semana_lista = [
            "segunda", "terça",
            "quarta", "quinta", "sexta"
        ]
        dia_semana = self.momento_cadastro.weekday() #daqui recebemos o index
        return dia_semana_lista[dia_semana]
    
    def format_data(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada

    def tempo_cadastro(self):
        return (datetime.today() + timedelta(days= 30))- self.momento_cadastro 
        #exemplo se o usuario ja esta cadastrado a 30 dias