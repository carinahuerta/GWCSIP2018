void setup() {
  // put your setup code here, to run once:
  pinMode (6, OUTPUT);
} 
/*
void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite (7, HIGH);
  delay (500);
  digitalWrite (7, LOW);
  delay (500);
}
*/

void o (){ 
  for (int i = 0; i < 3; i++){
    digitalWrite (7, HIGH);
    delay (500);
    digitalWrite (7, LOW);
    delay (500);
  }
}

