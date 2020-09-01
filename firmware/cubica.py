float targetSp;  #vel desiderata in giri/s
float mSpeed;    # vel motore in giri/s
float startSpeed;  #vel motore in al momento in cui viene settata una nuova velocità in giri/s
float deltaS; # (vel motore - vel desiderata) in giri/s
float slewRate;  #acceleraz rotore giri/s^2
float deltaT; #durata transizione da velocità attuale a velocità obbiettivo in s
float targetT; #tempo al quale il rotore raggiunge velocità obbiettivo in s
int speedThresh; #soglia di variazione di velocità minima sotto alla quale non viene computata alcuna traiettoria
float Ac3; #coeff cubica
float Ac2; #coeff cubica
int refSpeed; #flag di segnalazione per quando viene settata una nuova velocità
float t; #tempo exec, al posto di millis


void setup() {
  // put your setup code here, to run once:
  slewRate = 2;        # accellerazion da una velocità all'altra. 
  speedThresh = 10;    # variazione massami della velocitò 
  targetSp = 0;
  mSpeed = 0;
  deltaS = 0;
  deltaT = 0;
  targetT = 0;
  startSpeed = 0;
  Ac3 = 0;
  Ac2 = 0;
}

void loop() {
  
  ///////////////////////////////////////////////////////
  //algoritmo calcolo traiettoria in velocità
  if(refSpeed) //se viene settata una nuova velocità (targetSp) viene computata una traiettoria di velocità
  {
  deltaS = targetSp - mSpeed;
  deltaT = abs(deltaS / slewRate);
  startSpeed = mSpeed; //viene memorizzata la velocità alla quale gira il motore al momento al quale viene settato un nuovo riferimento in velocità
    //calcolo coeff cubica
    if (deltaS <= speedThresh && deltaS >= -speedThresh) //se la variazione settata è inferiore alla soglia non viene computata alcuna traiettoria
     {
     Ac3 = 0;
     Ac2 = 0;
     deltaT = 0;
     mSpeed = targetSp;
     }
     else{
     Ac3 = -2*deltaS/pow(deltaT,3);
     Ac2 = 3*deltaS/pow(deltaT,2);
     }
  refSpeed = 0;
  targetT = millis();
  targetT = targetT/1000;
  }
  
    t = millis();
    t = t/1000;
    
    if(targetT + deltaT >= t) //una volta computata la traiettoria viene variata la velocità
      {
        mSpeed = Ac3*pow((t),3) + Ac2*pow((t),2) + startSpeed; //set speed = old speed + transition to desired speed
      }
  //fine algoritmo calcolo traiettoria in velocità
  ///////////////////////////////////////////////////////
  
}