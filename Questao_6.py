import requests
from datetime import date
from unicodedata import normalize

def normalizar(texto):
    if not texto: return ""
    sem_acento = normalize("NFD", texto).encode("ascii", "ignore").decode("ascii")
    return sem_acento.upper().strip()

def coletar_dados_inmet(nome_municipio, sigla_estado):
    try:
        response = requests.get("https://apitempo.inmet.gov.br/estacoes/T", timeout=20)
        response.raise_for_status()
        estacoes = response.json()
    except Exception as e:
        print(f"Erro ao conectar com a API do INMET: {e}")
        return {}

    municipio_alvo = normalizar(nome_municipio)
    estado_alvo = sigla_estado.upper().strip()

    estacao = None
    for e in estacoes:
        nome_estacao = normalizar(e.get("DC_NOME", ""))
        sigla_e = e.get("SG_ESTADO", "").upper()
        situacao = e.get("CD_SITUACAO", "")

        if municipio_alvo in nome_estacao and sigla_e == estado_alvo and situacao == "Operante":
            estacao = e
            break

    if not estacao:
        print(f"Nenhuma estação operante encontrada para '{nome_municipio} - {sigla_estado}'.")
        return {}

    codigo_estacao = estacao["CD_ESTACAO"]
    print(f"Conectado à Estação: {estacao['DC_NOME']} ({codigo_estacao})")

    hoje = date.today().strftime("%Y-%m-%d")
    url_medicoes = f"https://apitempo.inmet.gov.br/estacao/{hoje}/{hoje}/{codigo_estacao}"
    
    try:
        medicoes = requests.get(url_medicoes, timeout=15).json()
        if not medicoes or "message" in medicoes:
            print("Nenhum dado disponível para a data de hoje ainda.")
            return {}
    except Exception as e:
        print(f"Erro ao buscar medições: {e}")
        return {}

    resultado = {}
    for m in medicoes:
        try:
            hr_raw = m.get("HR_MEDICAO")
            if not hr_raw: continue
            
            hora_utc = int(hr_raw[:2])
            minutos = hr_raw[2:]
            
            hora_bsb = (hora_utc - 3) % 24
            chave = f"{hora_bsb:02d}:{minutos}"
            
            temp = float(m.get("TEM_INS")) if m.get("TEM_INS") else 9999
            umid = float(m.get("UMD_INS")) if m.get("UMD_INS") else 9999
            
            if temp < 90 and umid < 101:
                resultado[chave] = (temp, umid)
        except (TypeError, ValueError):
            continue 

    return dict(sorted(resultado.items()))

if __name__ == "__main__":
    dados = coletar_dados_inmet("Belo Horizonte", "MG")
    if dados:
        print(f"{'HORA':<7} | {'TEMP':<7} | {'UMID'}")
        print("-" * 25)
        for hora, (temp, umid) in dados.items():
            print(f"{hora}  | {temp:>4}°C  | {umid:>3.0f}%")