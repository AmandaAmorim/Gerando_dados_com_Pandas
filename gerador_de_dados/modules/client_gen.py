from faker import Faker
from gerador_de_dados.modules.utils import remove_accents
import numpy as np

fake = Faker('pt-br')

class ClientGenerator:
    def generate_client(self, id_cli):
        # Gerar primeiro nome e sobrenome separadamente para o e-mail ficar perfeito
        first_name = fake.first_name()
        last_name = fake.last_name()
        full_name = f"{first_name}.{last_name}"

        renda = round(np.random.uniform(1500, 15000), 2)
        score = self._calculate_score(renda)
        
        # Lógica de e-mail corrigida e limpa
        user = f"{first_name} {last_name}".lower()
        email = f"{remove_accents(user)}@example.com"

        # Retornar um dicionário com os dados do cliente
        return {
            "id_cli": id_cli,
            "nome_cli": full_name,
            "email_cli": email,
            "cpf_cli": fake.cpf(),
            "renda_mensal_cli": renda,
            "score_cli": score,
            "data_nascimento_cli": fake.date_of_birth(minimum_age=18, maximum_age=80).strftime('%d/%m/%Y')
        }
    
    def _calculate_score(self, renda_mensal_cli):
        score = 300
        bonus = renda_mensal_cli * 0.05
        ruido = np.random.randint(-100, 100)
    
        resultado = score + bonus + ruido
        return int(np.clip(resultado, 300, 1000))