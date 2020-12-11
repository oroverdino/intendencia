#!/usr/bin/python
from configparser import ConfigParser


def config(filename, section):
    """Basic ini file reader config"""
    parser = ConfigParser()
    parser.read(filename)
    parametros = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            parametros[param[0]] = param[1]
    else:
        raise Exception('No se encuentra la seccion {0} en el archivo {1}'.format(section, filename))
    return parametros
