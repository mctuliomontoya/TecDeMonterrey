#include "Persona.h"

class Villano : public Persona   {
    private:
        string bando;
        int edad;
    public:
        Villano(string, string, string, int);
        void mostrar();
};

Villano::Villano(string _nombre, string _poder, string _bando, int _edad) : Persona(_nombre, _poder)    {
    bando = "Villano";
    edad = _edad;
}

void Villano::mostrar()   {
    Persona::mostrar();
    cout << "Bando: " << bando << endl;
    cout << "Edad: " << edad << endl;
}
