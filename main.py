#!/usr/bin/env python
# -*-coding: utf-8 -*-

from consolemenu import *
from consolemenu.items import *

from interfaz import Interfaz


def menu():
    # Agentes
    submenu_agentes = ConsoleMenu(title="Agentes", exit_option_text="Volver")
    submenu_agentes.append_item(FunctionItem("Listar agentes activos", interfaz.proyectar_agentes_activos))
    submenu_agentes.append_item(FunctionItem("Buscar agente por legajo", interfaz.proyectar_nombre_apellido))
    submenu_agentes.append_item(FunctionItem("Buscar agentes por apellido", interfaz.proyectar_busqueda_por_apellido))

    # Lugares
    submenu_lugares = ConsoleMenu(title="Lugares", exit_option_text="Volver")
    submenu_lugares.append_item(FunctionItem("Listar lugares", interfaz.proyectar_lugares_y_responsables))
    submenu_lugares.append_item(FunctionItem("Listar puertas", interfaz.proyectar_puertas))
    submenu_lugares.append_item(FunctionItem("Asignar llave a agente", interfaz.asignar_llave))
    submenu_lugares.append_item(FunctionItem("Quitar llave a agente", interfaz.quitar_llave))

    # Incidentes
    submenu_incidentes = ConsoleMenu(title="Incidentes", exit_option_text="Volver")
    # submenu_incidentes.append_item(SelectionItem(["SITE", "UNDER", "CONSTRUCTION"]))

    # Limpieza
    submenu_limpieza = ConsoleMenu(title="Limpieza", exit_option_text="Volver")
    submenu_limpieza.append_item(FunctionItem("Listar eventos de limpieza", interfaz.proyectar_eventos_limpieza))
    submenu_limpieza.append_item(FunctionItem("Listar equipos de limpieza", interfaz.proyectar_equipos_limpieza))
    submenu_limpieza.append_item(FunctionItem("Listar eventos y equipo", interfaz.proyectar_eventos_y_equipos_limpieza))
    submenu_limpieza.append_item(FunctionItem("Crear nuevo evento de limpieza", interfaz.crear_evento_limpieza))
    submenu_limpieza.append_item(FunctionItem("Editar hora evento de limpieza", interfaz.editar_hora_evento_limpieza))
    submenu_limpieza.append_item(
        FunctionItem("Marcar evento de limpieza realizado", interfaz.set_evento_limpieza_completado))
    submenu_limpieza.append_item(
        FunctionItem("Sumar ordenanza a un evento de limpieza", interfaz.sumar_ordenanza_a_equipo_limpieza))
    submenu_limpieza.append_item(
        FunctionItem("Quitar ordenanza de un evento de limpieza", interfaz.restar_ordenanza_a_equipo_limpieza))

    # Menu principal
    menu_principal = ConsoleMenu("Intendencia", exit_option_text="Salir")
    menu_principal.append_item(SubmenuItem("Agentes", submenu=submenu_agentes))
    menu_principal.append_item(SubmenuItem("Lugar", submenu=submenu_lugares))
    menu_principal.append_item(SubmenuItem("Incidentes", submenu=submenu_incidentes))
    menu_principal.append_item(SubmenuItem("Limpieza", submenu=submenu_limpieza))

    # Activa el menu
    menu_principal.show()


if __name__ == "__main__":
    interfaz = Interfaz()

    menu()
