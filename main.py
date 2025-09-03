import sys
sys.dont_write_bytecode = True  # impede criação do __pycache__

from simulador import simulador

if __name__ == "__main__":
    simulador()
