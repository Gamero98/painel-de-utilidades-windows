import os
from colorama import Fore, Style, init

init(autoreset=True)

# Função para exibir o menu
def exibir_menu():
    print( Fore.LIGHTMAGENTA_EX + "\n========= Painel de utilidades Windows =========")
    print(Fore.LIGHTCYAN_EX + "1. Informações do sistema")
    print(Fore.LIGHTCYAN_EX + "2. Informações de rede")
    print(Fore.LIGHTCYAN_EX + "3. Fazer ping")
    print(Fore.LIGHTCYAN_EX + "4. Usuarios")
    print(Fore.LIGHTCYAN_EX + "5. Processos")
    print(Fore.LIGHTCYAN_EX + "6. Serviços")
    print(Fore.LIGHTCYAN_EX + "7. Ver log de eventos")
    print(Fore.LIGHTCYAN_EX + "8. Ver disco")
    print(Fore.LIGHTCYAN_EX + "9. Dispositivos e Impressoras")
    print(Fore.LIGHTCYAN_EX + "10. Gerenciador de dispositivos")
    print(Fore.LIGHTCYAN_EX + "11. Adaptadores de rede")
    print(Fore.LIGHTCYAN_EX + "12. Testar velocidade da internet")
    print(Fore.LIGHTCYAN_EX + "13. Segurança do Windows")
    print(Fore.LIGHTCYAN_EX + "14. Sair")
    print(Fore.LIGHTMAGENTA_EX + "================================================")

# Função para ver informações do sistema
def ver_infosistema():
     os.system(f"systeminfo")

# Função para ver informações de rede
def ver_inforede():
     os.system(f"ipconfig")

# Função para fazer ping
def fazer_ping():
        site = input(Fore.GREEN + "Digite o nome do site:")

        resposta = os.system(f"ping -c 1 {site}")

        if resposta == 0:
                print(Fore.YELLOW + f"{site} Esta online")
        
        else:
                print(Fore.RED + f"{site}  Esta offline")

# Função para ver usuarios                
def ver_usuarios():
     os.system(f"net user")

# Função para ver processos
def ver_processos():
    os.system(f"tasklist")

# Função para ver serviços
def ver_servicos():
    os.system(f"sc query")

# Função para ver log de eventos
def ver_logs():
     os.system(f"eventvwr")

# Função para ver disco
def ver_disco():
     os.system(f"wmic diskdrive get size")

# Função para abrir dispositivos e impressoras
def dispositivos_impressoras():
     os.system(f"control printers")

# Função para abrir gerenciador de dispositivos
def gerenciador_dispositivos():
     os.system(f"devmgmt.msc")

# Função para listar adaptadores de rede
def listar_adaptadores():
    os.system("wmic nic get name, macaddress")

# Função parar testar velocidade 
def testar_velocidade():
    os.system("speedtest")

# Função para abrir segurança do windows
def seguranca_windows():
     os.system("explorer windowsdefender://")

# Função para sair do programa
def sair():
    print(Fore.YELLOW + f"Saindo do programa...")

# Função principal do menu
def menu():
    while True:
        exibir_menu()
        escolha = input(Fore.GREEN + Style.BRIGHT + "Escolha uma opção: ")

        if escolha == '1':
            ver_infosistema()
        elif escolha == '2':
            ver_inforede()
        elif escolha == '3':
            fazer_ping()
        elif escolha == '4':
            ver_usuarios()
        elif escolha == '5':
            ver_processos()
        elif escolha == '6':
            ver_servicos()
        elif escolha == '7':
            ver_logs()
        elif escolha == '8':
            ver_disco()
        elif escolha == '9':
            dispositivos_impressoras()
        elif escolha == '10':
            gerenciador_dispositivos()
        elif escolha == '11':
            listar_adaptadores()
        elif escolha == '12':
            testar_velocidade()
        elif escolha == '13':
            seguranca_windows()
        elif escolha == '14':
            sair()
            break
        else:
            print(Fore.RED + "Opção inválida. Tente novamente.")

# Executar o menu
menu()
