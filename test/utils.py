from resolver.custom_domain import CustomDomain
from resolver.database import Database
from resolver.external_domain import ExternalDomain

DEFAULT_DOMAIN_NAME = 'custom.domain.ar'
DEFAULT_DOMAIN_IP_1 = '0.1.0.1'
DEFAULT_DOMAIN_IP_2 = '0.2.0.2'
DEFAULT_TTL = 1


def persist_custom_domain():
    domain = CustomDomain(DEFAULT_DOMAIN_NAME)
    domain.add_associated_ip(DEFAULT_DOMAIN_IP_1)
    domains = Database.get_instance().db['domains']
    domains[domain.name] = domain
    return domain


def persist_external_domain_with_one_ip():
    domain = ExternalDomain(DEFAULT_DOMAIN_NAME, DEFAULT_TTL)
    domain.add_associated_ip(DEFAULT_DOMAIN_IP_1)
    domains = Database.get_instance().db['domains']
    domains[domain.name] = domain
    return domain


def persist_external_domain_with_two_ips():
    domain = ExternalDomain(DEFAULT_DOMAIN_NAME, DEFAULT_TTL)
    domain.add_associated_ip(DEFAULT_DOMAIN_IP_1)
    domain.add_associated_ip(DEFAULT_DOMAIN_IP_2)
    domains = Database.get_instance().db['domains']
    domains[domain.name] = domain
    return domain


def do_expire_ttl(domain, new_ip):
    print('so expired :P')
