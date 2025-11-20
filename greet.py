from datetime import datetime
GREEN = "\033[92m"
RESET = "\033[0m"

def greet():
    hour = datetime.now().hour
    if hour < 12:
        print("Bom dia! Este programa é uma calculadora básica de valores de frete.")
        print("="*50)
        print(GREEN + " CALCULADORA DE FRETE 1.0 (made by viniciusnunesleites)" + RESET)
        print("="*50)
    elif hour >12:
        print("Bom tarde! Este programa é uma calculadora básica de valores de frete.")
        print("="*50)
        print(GREEN + " CALCULADORA DE FRETE 1.0 (made by viniciusnunesleites)" + RESET)
        print("="*50)