import socket as sk
for port in range(1, 1024):
    try:
        s = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
        s.settimeout(1000)
        s.connect(('127.0.0.1', port))
        print(f"Port {port} is open")
        s.close()
    except:
        continue
