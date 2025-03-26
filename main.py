from consulta_processo_selenium import realizar_consulta
from envio_email import enviar_email

if __name__ == "__main__":
    
    # Realizar a consulta
    resultados = realizar_consulta()
    print(f"Resultado da consulta: {resultados}")

    # Enviar o resultado por email
    enviar_email(resultados)