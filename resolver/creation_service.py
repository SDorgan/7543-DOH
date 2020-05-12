from resolver.database import Database
from api.doh_dtos import Resolution
from resolver.custom_domain import CustomDomain

class CreationService:
    domain_name = None
    domain_ip = None

    def __init__(self, name, ip):
        self.domain_name = name
        self.domain_ip = ip

    def add_domain(self):
        if self.__custom_domain_already_exists():
            return None
        return self.__add_domain_to_database()

    def get_response(self):
        return Resolution(self.domain_name, self.domain_ip, True)

    def __custom_domain_already_exists(self):
        domain = Database.get_instance().db['domains'].get(self.domain_name, None)
        if domain is not None and domain.is_custom():
            print("entra al if")
            return True
        return False

    def __add_domain_to_database(self):
        new_domain = CustomDomain(self.domain_name)
        new_domain.add_associated_ip(self.domain_ip)
        Database.get_instance().db['domains'][self.domain_name] = new_domain
        return new_domain