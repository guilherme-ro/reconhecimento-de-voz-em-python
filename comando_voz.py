import speech_recognition as sr
import serial # Biblioteca para comunicação serial, necessária em um projeto real (não no Tinkercad)

# Configuração serial (Conceitual - A porta COM e o baud rate dependem da sua configuração)
# ser = serial.Serial('COMx', 9600) 

def ouvir_e_enviar_comando():
    microfone = sr.Recognizer()

    with sr.Microphone() as source:
        try:
            microfone.adjust_for_ambient_noise(source)
            print("Diga 'Ligar LED' ou 'Desligar LED': ")
            audio = microfone.listen(source)
            
            # Reconhece a fala usando Google Speech Recognition em português
            frase = microfone.recognize_google(audio, language='pt-BR')
            print("Você disse: " + frase)
            
            # Lógica para traduzir o comando de voz em ação do Arduino
            if "ligar led" in frase.lower():
                comando_arduino = 'L'
                # ser.write(comando_arduino.encode()) # Envia o comando para o Arduino (no projeto real)
                print(f"Comando '{comando_arduino}' enviado para ligar o LED.")
            elif "desligar led" in frase.lower():
                comando_arduino = 'D'
                # ser.write(comando_arduino.encode()) # Envia o comando para o Arduino (no projeto real)
                print(f"Comando '{comando_arduino}' enviado para desligar o LED.")
            else:
                print("Comando não reconhecido.")

        except sr.UnknownValueError:
            print("Não entendi")
        except Exception as e:
            print(f"Erro: {e}")

# Chame a função para iniciar o reconhecimento de voz
# ouvir_e_enviar_comando()
