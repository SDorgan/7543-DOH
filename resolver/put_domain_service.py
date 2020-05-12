from resolver.database import Database
from api.doh_dtos import Resolution
from resolver.custom_domain import CustomDomain

class PutDomainService:
    domain_name = None
    domain_ip = None

    def __init__(self, name, ip):
        self.domain_name = name
        self.domain_ip = ip

    def modify_domain(self):
        if self.__custom_domain_already_exists():
            return self.__modify_domain_in_database()
        return None

    def get_response(self):
        return Resolution(self.domain_name, self.domain_ip, True)

    def __custom_domain_already_exists(self):
        domain = Database.get_instance().db['domains'].get(self.domain_name, None)
        if domain is not None and domain.is_custom():
            return True
        return False

    def __modify_domain_in_database(self):
        modified_domain = Database.get_instance().db['domains'].get(self.domain_name, None)
        modified_domain.add_associated_ip(self.domain_ip)
        Database.get_instance().db['domains'][self.domain_name] = modified_domain
        return modified_domain