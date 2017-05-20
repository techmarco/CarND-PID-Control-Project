#include <iostream>
#include "PID.h"

using namespace std;

/*
* TODO: Complete the PID class.
*/

PID::PID() {}

PID::~PID() {}

void PID::Init(double Kp, double Ki, double Kd) {
  p_error = 0;
  i_error = 0;
  d_error = 0;

  this->Kp = Kp;
  this->Ki = Ki;
  this->Kd = Kd;

  cout << "Kp = " << Kp << " Ki = " << Ki << " Kd = " << Kd << endl;
}

void PID::UpdateError(double cte) {
  d_error = cte - p_error;
  p_error = cte;
  i_error += cte;
  cout << "p_error = " << p_error << " i_error = " << i_error << " d_error = " << d_error << endl;
}

double PID::TotalError() {
  return p_error + d_error + i_error;
}

