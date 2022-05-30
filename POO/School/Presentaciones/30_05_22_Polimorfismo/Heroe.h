#include "Persona.h"

class Heroe : public Persona    {
    private:
        string bando;
        int edad;
    public:
        Heroe(string, string, string, int);
        void mostrar();
};

Heroe::Heroe(string _nombre, string _poder, string _bando, int _edad) : Persona(_nombre, _poder)    {
    bando = "Heroe";
    edad = _edad;
}

void Heroe::mostrar()   {
    Persona::mostrar();
    cout << "Bando: " << bando << endl;
    cout << "Edad: " << edad << endl;
}
