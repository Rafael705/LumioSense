int ledPin = D2;  // Define o pino do LED

void setup() {
  Serial.begin(115200);  // Inicia a comunicação serial
  pinMode(ledPin, OUTPUT);  // Configura o pino do LED como saída
}

void loop() {
  if (Serial.available()) {  // Verifica se há dados disponíveis na porta serial
    char command = Serial.read();  // Lê o comando enviado pelo Python
    if (command == '1') {  // Se o comando for '1', liga o LED
      digitalWrite(ledPin, HIGH);
      Serial.print("ligou");
    } 
    else if (command == '0')
    {
      digitalWrite(ledPin, LOW);
      Serial.print("desligou");
    }
 }
}
