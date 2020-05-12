from resolver.database import Database
from resolver.custom_domain import CustomDomain

class CreationService:
    __instance = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if CreationService.__instance is None:
            CreationService()
        return CreationService.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if CreationService.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            CreationService.__instance = self

    @staticmethod
    def add_domain(domain_name, domain_ip):
        if CreationService.get_instance().__custom_domain_already_exists(domain_name):
            return None
        return CreationService.get_instance().__add_domain_to_database(domain_name, domain_ip)

    def __custom_domain_already_exists(self, domain_name):
        domain = Database.get_instance().db['domains'].get(domain_name, None)
        if domain is not None and domain.is_custom():
            print("entra al if")
            return True
        return False

    def __add_domain_to_database(self, domain_name, domain_ip):
        new_domain = CustomDomain(domain_name)
        new_domain.add_associated_ip(domain_ip)
        Database.get_instance().db['domains'][domain_name] = new_domain
        return new_domain