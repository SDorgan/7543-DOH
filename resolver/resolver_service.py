from resolver.database import Database
from resolver.dns_query_service import DnsQueryService


class ResolverService:
    domain_name = None

    def __init__(self, domain_name):
        self.domain_name = domain_name

    def get_domain_ip(self):
        domain = self.get_domain_by_name()
        return domain.resolve()

    def get_domain_by_name(self):
        domain = Database.get_instance().db['domains'].get(self.domain_name)
        return self.validate_time_to_live(domain)

    @staticmethod  # TODO ESTO ASI ESTA FEO
    def validate_time_to_live(domain):
        valid_domain = domain.is_valid()
        if not valid_domain:
            Database.get_instance().db['domains'].popitem(domain)
            new_domain = DnsQueryService(domain.name).get_response_as_external_domain()
            Database.get_instance().db['domains'][domain.name] = new_domain
            return new_domain

        return domain
