from machine import Pin, ADC   # Importa controle de pinos digitais (Pin) e analógicos (ADC)
import time                   # Importa biblioteca de tempo (para delay)

# =========================
# CONFIGURAÇÃO DOS LEDs
# =========================

led_verde = Pin(21, Pin.OUT)     # LED verde no pino 21 (indica tensão baixa)
led_amarelo = Pin(22, Pin.OUT)   # LED amarelo no pino 22 (tensão média)
led_vermelho = Pin(23, Pin.OUT)  # LED vermelho no pino 23 (tensão alta)

# =========================
# CONFIGURAÇÃO DO ADC
# =========================

pot = ADC(Pin(34))              # Define o pino 34 como entrada analógica (potenciômetro)

pot.atten(ADC.ATTN_11DB)        # Ajusta a faixa de leitura até ~3.3V
pot.width(ADC.WIDTH_12BIT)      # Define resolução de 12 bits (0 a 4095)

print("Voltímetro VU inicializado")  # Mensagem no console

# =========================
# LOOP PRINCIPAL
# =========================

while True:

    leitura_bruta = pot.read()  # Lê valor bruto do ADC (0 a 4095)

    # Converte valor para tensão (0V a 3.3V)
    tensao = (leitura_bruta / 4095) * 3.3

    # Desliga todos os LEDs antes de decidir qual ligar
    led_verde.off()
    led_amarelo.off()
    led_vermelho.off()

    # =========================
    # LÓGICA DE NÍVEL DE TENSÃO
    # =========================

    if tensao > 0.5:
        led_verde.on()      # Liga LED verde (nível baixo)

    if tensao > 1.5:
        led_amarelo.on()    # Liga LED amarelo (nível médio)

    if tensao > 2.5:
        led_vermelho.on()   # Liga LED vermelho (nível alto)

    # Mostra no terminal os valores lidos
    print(f"Bruto: {leitura_bruta} | Tensão: {tensao:.2f} V")

    time.sleep(0.1)  # Pequena pausa de 100ms