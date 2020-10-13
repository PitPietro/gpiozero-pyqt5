#define output 10

void setup(){
  Serial.begin(9600);   
  pinMode(output, OUTPUT);
}

void loop() {
  digitalWrite(output, HIGH);
  Serial.println("H");
  delay(5000);
  digitalWrite(output, LOW);
  Serial.println("L");
  delay(5000);
}
