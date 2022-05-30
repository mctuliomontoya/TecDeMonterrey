#ifndef Persona_h
#define Persona_h

class Persona   {
    private:
        string nombre;
        string poder;
    public:
        Persona(string, string);
        virtual void mostrar();
};

Persona::Persona(string _nombre, string _poder) {
    nombre = _nombre;
    poder = _poder;
}

void Persona::mostrar() {
    cout << "Nombre: " << nombre << endl;
    cout << "Poder: " << poder << endl;
}


#endif
