#define output 10

void setup(){
  pinMode(output, OUTPUT);
}

void loop() {
  digitalWrite(output, HIGH);
  delay(500);
  digitalWrite(output, LOW);
  delay(500);
}
