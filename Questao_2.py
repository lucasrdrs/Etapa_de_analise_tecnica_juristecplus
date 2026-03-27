import random
import numpy as np
import pandas as pd

class Televisao:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.ligada = False
        self.mudo = False
        
        self.volume = random.randint(10, 30)
        self.canal = 1
        self.volume_anterior = self.volume

    def ligar_desligar(self):
        self.ligada = not self.ligada
        status = "Ligada" if self.ligada else "Desligada"
        print(f"\n[SISTEMA] A TV {self.marca} está agora: {status}")

    def alterar_volume(self, novo_volume):
        if not self.ligada:
            return "A TV está desligada!"
        
        self.volume = np.clip(novo_volume, 0, 100)
        self.mudo = False                          
        print(f"[VOLUME] Volume alterado para: {self.volume}")

    def alternar_mudo(self):
        if not self.ligada:
            print("[AVISO] A TV está desligada!")
            return
        
        if not self.mudo:
            self.volume_anterior = self.volume
            self.volume = 0
            self.mudo = True
            print("[ÁUDIO] TV no Mudo.")
        else:
            self.volume = self.volume_anterior
            self.mudo = False
            print(f"[ÁUDIO] Mudo desativado. Volume: {self.volume}")

    def alterar_canal(self, novo_canal):
        if not self.ligada:
            print("[AVISO] A TV está desligada!")
            return
        
        self.canal = novo_canal
        print(f"[CANAL] Alterado para: {self.canal}")

    def status_atual(self):
        dados = {
            "Marca": [self.marca],
            "Modelo": [self.modelo],
            "Status": ["Ligada" if self.ligada else "Desligada"],
            "Canal": [self.canal],
            "Volume": [self.volume],
            "Mudo": [self.mudo]
        }
        return pd.DataFrame(dados)

minha_tv = Televisao("Samsung", "4K Ultra")

while True:
    print(" ")
    print(f" CONTROLE REMOTO - {minha_tv.marca}")
    print(" ")
    print("1. Ligar/Desligar")
    print("2. Alterar Canal")
    print("3. Alterar Volume")
    print("4. Mudo (On/Off)")
    print("5. Ver Status Detalhado (Pandas)")
    print("0. Sair")
    
    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        minha_tv.ligar_desligar()
    
    elif opcao == "2":
        if minha_tv.ligada:
            canal = int(input("Digite o número do canal: "))
            minha_tv.alterar_canal(canal)
        else:
            print("[AVISO] Ligue a TV primeiro!")

    elif opcao == "3":
        if minha_tv.ligada:
            vol = int(input("Digite o volume desejado (0-100): "))
            minha_tv.alterar_volume(vol)
        else:
            print("[AVISO] Ligue a TV primeiro!")

    elif opcao == "4":
        minha_tv.alternar_mudo()

    elif opcao == "5":
        print("\n--- STATUS ATUAL ---")
        print(minha_tv.status_atual())

    elif opcao == "0":
        print("Saindo...")
        break
    
    else:
        print("Opção inválida!")
