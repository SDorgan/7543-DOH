from api.doh_dtos import Resolution
from resolver.database import Database

class GetCustomDomainService:
    domain_substring = None
    domains = None

    def __init__(self, domain_substring):
        self.domain_substring = domain_substring
        self.domains = []

    def get_custom_domains(self):
        database_domains = Database.get_instance().db['domains'].values()
        for current_domain in database_domains:
            if current_domain.is_custom() and self.domain_substring in current_domain.name:
                self.domains.append(current_domain)
    
    def get_response(self):
        resolutions = []
        for current_domain in self.domains:
            new_resolution = Resolution(current_domain.name, current_domain.associated_ips[0], True)
            resolutions.append(new_resolution)
        return resolutions
