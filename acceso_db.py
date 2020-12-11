import logging
import psycopg2
from config import config


class AccesoPG:
    """Acceso a la db intendecia en PostgreSQL"""
    def __init__(self):
        """ Connect to the PostgreSQL database server """
        self.conn = None
        try:
            params = config(filename='database.ini', section='postgresql')
            self.conn = psycopg2.connect(**params)
        except (psycopg2.OperationalError, psycopg2.DatabaseError):
            logging.error('Error en los parametros de psycopg2.', exc_info=True)
        except Exception:
            logging.error('Error al intentar la conexion.', exc_info=True)
        else:
            self.conn.autocommit = True
            self.cur = self.conn.cursor()

    def __del__(self):
        if self.conn is not None:
            self.cur.close()
            self.conn.close()

    # AGENTES # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def get_agentes_activos(self):
        if self.conn is not None:
            self.cur.execute('select * from agentes_activos')
            agentes = self.cur.fetchall()
            return agentes
        else:
            return []

    def search_agente_por_legajo(self, flegajo):
        if self.conn is not None:
            self.cur.execute("select get_nombre_apellido('{0}')".format(flegajo))
            nombre_apellido = self.cur.fetchall()
            return nombre_apellido
        else:
            return []

    def search_agente_por_apellido(self, fapellido):
        if self.conn is not None:
            self.cur.execute("select * from get_nombre_apellido_legajo_cargo('{0}')".format(fapellido))
            agentes = self.cur.fetchall()
            return agentes
        else:
            return []

    def get_nombre_apellido_legajo(self):
        if self.conn is not None:
            sql = 'select * from get_nombre_apellido_legajo'
            self.cur.execute(sql)
            agentes = self.cur.fetchall()
            return agentes
        else:
            return []

# LUGARES # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def get_lugares(self):
        if self.conn is not None:
            self.cur.execute('select * from lugares_y_responsables')
            lugares = self.cur.fetchall()
            return lugares
        else:
            return []

    def get_puertas(self):
        if self.conn is not None:
            self.cur.execute('select * from listar_puertas')
            puertas = self.cur.fetchall()
            return puertas
        else:
            return []

    def set_llave_asignar(self, pllave, plegajo):
        if self.conn is not None:
            try:
                self.cur.execute('call set_llave_asignar(%s, %s)', (pllave, plegajo))
                return True
            except (Exception, psycopg2.Error) as error:
                print('\n', 'Error al asignar la llave: ', '\n\n', error)
                return False
        else:
            print('No conectado')
            return False

    def set_llave_quitar(self, pllave, plegajo):
        if self.conn is not None:
            try:
                self.cur.execute('call set_llave_quitar(%s, %s)', (pllave, plegajo))
                return True
            except (Exception, psycopg2.Error) as error:
                print('\n', 'Error al quitar la llave: ', '\n\n', error)
                return False
        else:
            print('No conectado')
            return False

# LIMPIEZA # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def get_eventos_limpieza(self):
        if self.conn is not None:
            self.cur.execute('select * from eventos_limpieza')
            eventos_limpieza = self.cur.fetchall()
            return eventos_limpieza
        else:
            return []
    
    def get_equipos_limpieza(self):
        if self.conn is not None:
            self.cur.execute('select * from equipos_de_limpieza')
            equipos_limpieza = self.cur.fetchall()
            return equipos_limpieza
        else:
            return []

    def get_eventos_y_equipos_limpieza(self):
        if self.conn is not None:
            self.cur.execute('select * from eventos_y_equipos_de_limpieza')
            eventos_equipos_limpieza = self.cur.fetchall()
            return eventos_equipos_limpieza
        else:
            return []

    def get_lugar_id(self):
        if self.conn is not None:
            self.cur.execute('select id, denominacion from lugar')
            lugar_id = self.cur.fetchall()
            return lugar_id
        else:
            return []

    def get_ordenanzas(self):
        if self.conn is not None:
            self.cur.execute('select * from ordenanzas')
            ordenanzas = self.cur.fetchall()
            return ordenanzas
        else:
            return []

    def set_limpieza_nueva(self, plugar_id, pfecha, phora, plegajo):
        if self.conn is not None:
            try:
                self.cur.execute('call set_limpieza_nueva(%s, %s, %s, %s)',
                                 (plugar_id, pfecha, phora, plegajo))
                return True
            except (Exception, psycopg2.Error) as error:
                print('\n', 'Error al crear nuevo evento de limpieza: ', '\n\n', error)
                return False
        else:
            print('No conectado')
            return False

    def get_eventos_y_equipos_limpieza_futuros(self):
        if self.conn is not None:
            self.cur.execute(
                "select e.evento, e.denominacion, e.ordenanza, e.fecha, e.hora "
                "from eventos_y_equipos_de_limpieza as e "
                "where iscompleta is not true "
                "and fecha >= current_date"
            )
            eventos_equipos_limpieza_futuros = self.cur.fetchall()
            return eventos_equipos_limpieza_futuros
        else:
            return []

    def set_limpieza_editar_hora(self, pid, phora):
        if self.conn is not None:
            try:
                self.cur.execute('call set_limpieza_editar_hora(%s, %s)', (pid, phora))
                return True
            except (Exception, psycopg2.Error) as error:
                print('\n', 'Error al editar la hora de un evento de limpieza: ', '\n\n', error)
                return False
        else:
            print('No conectado')
            return False

    def get_eventos_y_equipos_limpieza_incompletos(self):
        if self.conn is not None:
            self.cur.execute(
                "select e.evento, e.denominacion, e.ordenanza, e.fecha, e.hora "
                "from eventos_y_equipos_de_limpieza as e "
                "where iscompleta is false"
            )
            eventos_equipos_limpieza_incompletos = self.cur.fetchall()
            return eventos_equipos_limpieza_incompletos
        else:
            return []

    def set_limpieza_completada(self, pid):
        if self.conn is not None:
            try:
                self.cur.execute('call set_limpieza_completada(%s)', pid)
                return True
            except (Exception, psycopg2.Error) as error:
                print('\n', 'Error al marcar como realizado un evento de limpieza: ', '\n\n', error)
                return False
        else:
            print('No conectado')
            return False

    def set_equipo_limpieza_sumar(self, plimpieza_id, plegajo):
        if self.conn is not None:
            try:
                self.cur.execute('call set_equipo_limpieza_sumar(%s, %s)', (plimpieza_id, plegajo))
                return True
            except (Exception, psycopg2.Error) as error:
                print('\n', 'Error al agregar un ordenanza a un evento de limpieza: ', '\n\n', error)
                return False
        else:
            print('No conectado')
            return False

    def set_equipo_limpieza_restar(self, plimpieza_id, plegajo):
        if self.conn is not None:
            try:
                self.cur.execute('call set_equipo_limpieza_restar(%s, %s)', (plimpieza_id, plegajo))
                return True
            except (Exception, psycopg2.Error) as error:
                print('\n', 'Error al retirar un ordenanza de un evento de limpieza: ', '\n\n', error)
                return False
        else:
            print('No conectado')
            return False
