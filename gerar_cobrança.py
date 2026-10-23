import random
from datetime import date, timedelta

import pandas as pd

nomes = ["Ana Souza", "Bruno Lima", "Carla Dias", "Diego Rocha",
         "Elisa Costa", "Fabio Alves", "Gabi Nunes", "Hugo Melo"]
hoje = date.today()

linhas = []
for nome in nomes:
    primeiro = nome.split()[0].lower()
    linhas.append({
        "nome": nome,
        "email": f"{primeiro}@exemplo.com",
        "valor": round(random.uniform(80, 900), 2),
        "vencimento": hoje + timedelta(days=random.randint(-10, 15)),
        "pago": random.choice(["sim", "nao", "nao"]),
    })

pd.DataFrame(linhas).to_excel("cobrancas.xlsx", index=False)
print("cobrancas.xlsx criado!")