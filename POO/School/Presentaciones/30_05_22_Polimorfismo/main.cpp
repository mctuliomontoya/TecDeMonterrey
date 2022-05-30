//Polimorfismo
#include <iostream>
#include <stdlib.h>
using namespace std;

#include "Heroe.h"
#include "Villano.h"

int main () {

    Heroe batman("Batman", "Ser rico", " ", 45);
    batman.mostrar();

    cout << endl;

    Villano andre("Andre Castillo", "Cabello de color", "si", 18);
    andre.mostrar();

    cout << endl;

    Persona* vector[1];

    vector[0] = new Villano("El hombre burro", "rebuznar", "", 18);
    vector[0]->mostrar();

}
