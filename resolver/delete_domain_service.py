from api.doh_dtos import Resolution
from resolver.database import Database

class DeleteCustomDomainService:
    domain_name = None
    domain_ip = None

    def __init__(self, domain_name):
        self.domain_name = domain_name

    def delete_custom_domains(self):
        return self.__delete_domain_from_database()

    def get_response(self):
        return Resolution(self.domain_name, self.domain_ip, True)

    def __delete_domain_from_database(self):
        deleted_domain = Database.get_instance().db['domains'].pop(self.domain_name, None)
        return deleted_domain