def electric_current_function():
    voltage = float(input("Ingresa Voltaje: "))
    resistance = float(input("Ingresa Resistencia: "))
    electric_current = (voltage / resistance)
    return electric_current


def voltage_function():
    electric_current = float(input("Ingresa la Intensidad de corriente: "))
    resistance = float(input("Ingresa Resistencia: "))
    voltage = (electric_current * resistance)
    return voltage


def resistance():
    voltage = float(input("Ingresa Voltaje: "))
    electric_current = float(input("Ingresa la Intensidad de corriente: "))
    resistance = (voltage / electric_current)
    return resistance


def potencia_function(intensidad, voltaje):
    pass


def process_functions(menu):
    if menu == 1:
        print(f'Intensidad de corriente = {round((electric_current_function()), 2)} Amperes')
    elif menu == 2:
        print(f'Voltaje = {round((voltage_function()), 2)} Volts')
    elif menu == 3:
        print(f'Resistance = {round((resistance()), 2)} ohms')
    elif menu == 4:
        pass
    elif menu == 0:
        print('Adios')
        exit()    
    else:
        print(f"You have not selected a valid option, please try again")
        

def menu_options():
    menu = int(input(r'''
    Esta aplicación te permite calcular:
    1) La intensidad de corriente

    2) El voltaje

    3) La resistecia

    4) Potencia

    Esta basado en la ley de Ohm que va así:  i = v / r
    Presiona la opcion que deseas calcular:
    '''))
    return menu


def run():
    while True:
        menu = menu_options()
        process_functions(menu)
    


if __name__ == '__main__':
    run()


