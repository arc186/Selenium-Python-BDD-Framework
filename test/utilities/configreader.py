from configparser import ConfigParser


def read_configuration(category, key):
    config = ConfigParser()
    config.read("C:/Users/Archana/PycharmProjects/BDD/pythonProject/configuration/config.ini")
    return config.get(category, key)