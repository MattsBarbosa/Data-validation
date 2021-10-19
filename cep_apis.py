import requests

class Buscaendereco:

    def __init__(self, cep):
        if self.cep_eh_valido(cep):
            self.cep = str(cep)
        else:
            raise ValueError("CEP inválido!!")
            
    def cep_eh_valido(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def __str__(self):
        return self.format_cep()

    def format_cep(self):
        return "{}-{}".format(self.cep[:5], self.cep[5:])

    def acessa_via_cep(self):
        url = "https://viacep.com.br/ws/{}/json/".format(self.cep)
        r = requests.get(url)
        dados = r.jason()
        return (
            dados['bairro'],
            dados['localidade'],
            dados['uf']
        )
