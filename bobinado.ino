int c=0, val = 0, out=0;
void setup() {
  Serial.begin(9600);
  pinMode(6, INPUT);
  pinMode(9, OUTPUT);
  
}

void loop() {
  digitalWrite(9, HIGH);
  val = digitalRead(6);
  while(val){
    c++;
    val = digitalRead(6);
  }
  if(c >= 10000){
    out++;
    Serial.println(out); 
  }
  c=0;
  
  /*for(int i = 0; i<10000;i++){
    val = digitalRead(6);
    if(val == 1)
        c++;
     else
      c=0;
  }
  Serial.println(c);
  if(c == 10000){
    out++;
    Serial.println(out);   
  }*/
  
}
