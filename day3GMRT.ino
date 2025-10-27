#include <Adafruit_MPU6050.h> //library MPU6050
#include <Adafruit_Sensor.h>//library sensor
#include <ESP32Servo.h>

Servo myservo1;//inisialisasi servo
Servo myservo2;
Servo myservo3;
Servo myservo4;
Servo myservo5;

#define PIRMOS_PIN 5 //output sensor di pin 5
#define SERVO1_PIN 4 //
#define SERVO2_PIN 17
#define SERVO3_PIN 26
#define SERVO4_PIN 25
#define SERVO5_PIN 18

Adafruit_MPU6050 mpu;

void setup() {
  
  Serial.begin(115200);

  if(!mpu.begin()){
    Serial.println("Gagal menemukan MPU6050");
  }else 
    Serial.println("MPU6050 ditemukan");

  pinMode(PIRMOS_PIN, OUTPUT); //Servo dipasang ke variabel
  myservo1.attach(SERVO1_PIN);
  myservo2.attach(SERVO2_PIN);
  myservo3.attach(SERVO3_PIN);
  myservo4.attach(SERVO4_PIN);
  myservo5.attach(SERVO5_PIN);
  
  delay(1000);
}

void loop() {
  sensors_event_t a, g, t; //data untuk sensor
  mpu.getEvent(&a, &g, &t);
  bool motion=digitalRead(PIRMOS_PIN);
if(motion==true){//servo bergerak ke arah tertentu jika ada motion detected
  myservo1.write(35);
  myservo2.write(60);
  myservo3.write(85);
  myservo4.write(110);
  myservo5.write(135);
  delay(2500);

  myservo1.write(90);
  myservo1.write(90);
  myservo1.write(90);
  myservo1.write(90);
  myservo1.write(90);
  delay(2500);
}else{
  int SP1= map(g.gyro.x, +5, -5, 0, 180);
  int SP2= map(g.gyro.x, +5, -5, 0, 180);
  int SP3= map(g.gyro.y, -5, +5, 0, 180);
  int SP4= map(g.gyro.y, -5, +5, 0, 180);
  int SP5= map(g.gyro.z, +5, -5, 0, 180);
  Serial.print("x:");
  Serial.print(g.gyro.x);//searah
  myservo1.write(SP1);
  myservo2.write(SP2);
  Serial.print("y:");
  Serial.print(g.gyro.y);
  myservo3.write(SP3);
  myservo4.write(SP4);
  Serial.print("z:");
  Serial.print(g.gyro.z);  
  myservo5.write(SP5);
  if (abs(SP5 -90)>0){
    delay(1000);
      myservo5.write(90);
  }
  Serial.print("\n");
  delay(1250);
}
}
