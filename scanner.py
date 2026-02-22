import socket

def check_vulnerability(target_ip):
    # Portas críticas que costumam ser alvo de ataques
    critical_ports = {
        21: "FTP (Transferência de Arquivos)",
        22: "SSH (Acesso Remoto)",
        80: "HTTP (Web Unsecured)",
        445: "SMB (Potencial vulnerabilidade Ransomware)"
    }

    print(f"\n[!] INICIANDO VARREDURA DE SEGURANÇA EM: {target_ip}")
    
    for port, service in critical_ports.items():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target_ip, port))
        
        if result == 0:
            print(f"[ALERTA] Porta {port} ({service}) está EXPOSTA!")
        else:
            print(f"[OK] Porta {port} protegida.")
        s.close()

if __name__ == "__main__":
    # Exemplo: testando o localhost (sua própria máquina)
    check_vulnerability("127.0.0.1")