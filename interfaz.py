from acceso_db import AccesoPG
from tabulate import tabulate


class Interfaz:

    def __init__(self):
        self.pg = AccesoPG()

    # AGENTES # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def proyectar_agentes_activos(self):
        if self.pg.conn is not None:
            agentes_activos = self.pg.get_agentes_activos()
            print(tabulate(agentes_activos,
                           headers=['Nombre', 'Apellido', 'Genero', 'eMail institucional', 'Cargo']))
        else:
            print('No conectado')
        input('\nPresione cualquier tecla para continuar...')

    def proyectar_nombre_apellido(self):
        if self.pg.conn is not None:
            flegajo = input('Legajo: ')
            nombre_apellido = self.pg.search_agente_por_legajo(flegajo)
            print('\n', nombre_apellido)
        else:
            print('No conectado')
        input('\nPresione cualquier tecla para continuar...')

    def proyectar_busqueda_por_apellido(self):
        if self.pg.conn is not None:
            fapellido = input('Ingrese algunas letras del apellido: ')
            agentes = self.pg.search_agente_por_apellido(fapellido)
            print(tabulate(agentes,
                           headers=['Nombre', 'Apellido', 'Legajo', 'Cargo']))
        else:
            print('No conectado')
        input('\nPresione cualquier tecla para continuar...')

    # LUGARES # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def proyectar_lugares_y_responsables(self):
        if self.pg.conn is not None:
            lugares = self.pg.get_lugares()
            print(tabulate(lugares,
                           headers=['Lugar', 'Tipo de lugar', 'Agente responsable']))
        else:
            print('No conectado')
        input('\nPresione cualquier tecla para continuar...')

    def proyectar_puertas(self):
        if self.pg.conn is not None:
            puertas = self.pg.get_puertas()
            print(tabulate(puertas,
                           headers=['Numero llave', 'Lugar', 'Agente con llave']))
        else:
            print('No conectado')
        input('\nPresione cualquier tecla para continuar...')

    def asignar_llave(self):
        if self.pg.conn is not None:

            llave_lugar = self.pg.get_puertas()
            print(tabulate(llave_lugar,
                           headers=['Numero llave', 'Lugar', 'Agente con llave']))
            print()
            llave = input('Seleccione el numero de llave: ')
            print()

            agentes = self.pg.get_nombre_apellido_legajo()
            print(tabulate(agentes,
                           headers=['Nombre', 'Apellido', 'Legajo']))
            print()
            legajo = input('Seleccione el numero de legajo: ')
            print()

            if self.pg.set_llave_asignar(llave, legajo):
                print('\n', 'Llave asignada')
        else:
            print('No conectado')
        input('\nPresione cualquier tecla para continuar...')

    def quitar_llave(self):
        if self.pg.conn is not None:

            llave_lugar = self.pg.get_puertas()
            print(tabulate(llave_lugar,
                           headers=['Numero llave', 'Lugar', 'Agente con llave']))
            print()
            llave = input('Seleccione el numero de llave: ')
            print()

            agentes = self.pg.get_nombre_apellido_legajo()
            print(tabulate(agentes,
                           headers=['Nombre', 'Apellido', 'Legajo']))
            print()
            legajo = input('Seleccione el numero de legajo: ')
            print()

            if self.pg.set_llave_quitar(llave, legajo):
                print('\n', 'Llave quitada')
        else:
            print('No conectado')
        input('\nPresione cualquier tecla para continuar...')

    # LIMPIEZA # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def proyectar_eventos_limpieza(self):
        if self.pg.conn is not None:
            eventos = self.pg.get_eventos_limpieza()
            print(tabulate(eventos,
                           headers=['Numero evento limpieza', 'Lugar', 'Fecha', 'Hora', 'Realizada']))
        else:
            print('No conectado')
        input('\nPresione cualquier tecla para continuar...')

    def proyectar_equipos_limpieza(self):
        if self.pg.conn is not None:
            equipo_limpieza = self.pg.get_equipos_limpieza()
            print(tabulate(equipo_limpieza,
                           headers=['Numero evento limpieza', 'Lugar', 'Ordenanza']))
        else:
            print('No conectado')
        input('\nPresione cualquier tecla para continuar...')

    def proyectar_eventos_y_equipos_limpieza(self):
        if self.pg.conn is not None:
            eventos_equipo_limpieza = self.pg.get_eventos_y_equipos_limpieza()
            print(tabulate(eventos_equipo_limpieza,
                           headers=['Numero evento', 'Lugar', 'Ordenanza', 'Fecha', 'Hora', 'Realizada']))
        else:
            print('No conectado')
        input('\nPresione cualquier tecla para continuar...')

    def crear_evento_limpieza(self):
        if self.pg.conn is not None:

            lugar_id = self.pg.get_lugar_id()
            print(tabulate(lugar_id, headers=['Id del lugar', 'Lugar']))
            print()
            pid = input('Seleccione el id del lugar: ')
            print()

            pfecha = input('Ingrese la fecha (yyyy-mm-dd): ')
            print()

            phora = input('Ingrese la hora (HH:MM:SS): ')
            print()

            ordenanzas = self.pg.get_ordenanzas()
            print(tabulate(ordenanzas, headers=['Nombre', 'Apellido', 'Legajo']))
            print()
            plegajo = input('Seleccione el legajo del ordenanza: ')

            if self.pg.set_limpieza_nueva(pid, pfecha, phora, plegajo):
                print('\n', 'Creado nuevo evento de limpieza')
        else:
            print('No conectado')
        input('\nPresione cualquier tecla para continuar...')

    def editar_hora_evento_limpieza(self):
        if self.pg.conn is not None:

            eventos_limpieza = self.pg.get_eventos_y_equipos_limpieza_futuros()
            print(tabulate(eventos_limpieza,
                           headers=['Numero evento', 'Lugar', 'Ordenanza', 'Fecha', 'Hora']))
            print()
            pid = input('Seleccione el numero de evento de limpieza: ')
            print()
            phora = input('Ingerese la nueva hora (HH:MM:SS): ')

            if self.pg.set_limpieza_editar_hora(pid, phora):
                print('\n', 'Modificada la fecha del evento de limpieza')
        else:
            print('No conectado')
        input('\nPresione cualquier tecla para continuar...')

    def set_evento_limpieza_completado(self):
        if self.pg.conn is not None:

            eventos_limpieza = self.pg.get_eventos_y_equipos_limpieza_incompletos()
            print(tabulate(eventos_limpieza,
                           headers=['Numero evento', 'Lugar', 'Ordenanza', 'Fecha', 'Hora']))
            print()
            pid = input('Seleccione el numero de evento de limpieza: ')

            if self.pg.set_limpieza_completada(pid):
                print('\n', 'Evento marcado como realizado')
        else:
            print('No conectado')
        input('\nPresione cualquier tecla para continuar...')

    def sumar_ordenanza_a_equipo_limpieza(self):
        if self.pg.conn is not None:

            eventos_equipo_limpieza = self.pg.get_eventos_y_equipos_limpieza()
            print(tabulate(eventos_equipo_limpieza,
                           headers=['Numero evento', 'Lugar', 'Ordenanza', 'Fecha', 'Hora', 'Realizada']))
            print()
            pid = input('Seleccione el numero de evento de limpieza: ')

            ordenanzas = self.pg.get_ordenanzas()
            print(tabulate(ordenanzas, headers=['Nombre', 'Apellido', 'Legajo']))
            print()
            plegajo = input('Seleccione el legajo del ordenanza: ')

            if self.pg.set_equipo_limpieza_sumar(pid, plegajo):
                print('\n', 'Ordenanza agregado a un evento de limpieza')
        else:
            print('No conectado')
        input('\nPresione cualquier tecla para continuar...')

    def restar_ordenanza_a_equipo_limpieza(self):
        if self.pg.conn is not None:

            eventos_equipo_limpieza = self.pg.get_eventos_y_equipos_limpieza()
            print(tabulate(eventos_equipo_limpieza,
                           headers=['Numero evento', 'Lugar', 'Ordenanza', 'Fecha', 'Hora', 'Realizada']))
            print()
            pid = input('Seleccione el numero de evento de limpieza: ')

            ordenanzas = self.pg.get_ordenanzas()
            print(tabulate(ordenanzas, headers=['Nombre', 'Apellido', 'Legajo']))
            print()
            plegajo = input('Seleccione el legajo del ordenanza: ')

            if self.pg.set_equipo_limpieza_restar(pid, plegajo):
                print('\n', 'Ordenanza retirado de un evento de limpieza')
        else:
            print('No conectado')
        input('\nPresione cualquier tecla para continuar...')
