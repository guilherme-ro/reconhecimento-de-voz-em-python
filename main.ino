const int ledPin = 13; // Pino onde o LED está conectado

void setup() {
  pinMode(ledPin, OUTPUT); // Define o pino do LED como saída
  Serial.begin(9600); // Inicia a comunicação serial a 9600 bits por segundo
  Serial.println("Pronto para receber comandos de voz (L/D)...");
}

void loop() {
  if (Serial.available() > 0) { // Verifica se há dados disponíveis na serial
    char comando = Serial.read(); // Lê o byte recebido

    if (comando == 'L') { // Se o comando for 'L' (Ligar)
      digitalWrite(ledPin, HIGH); // Liga o LED
      Serial.println("LED Aceso!");
    } else if (comando == 'D') { // Se o comando for 'D' (Desligar)
      digitalWrite(ledPin, LOW); // Desliga o LED
      Serial.println("LED Apagado!");
    }
  }
}
