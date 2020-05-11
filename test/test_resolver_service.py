from unittest import TestCase

from resolver.database import Database
from resolver.resolver_service import ResolverService
from test import utils
from test.utils import do_expire_ttl


class TestResolverService(TestCase):

    def tearDown(self):
        super().tearDown()
        Database.get_instance().db = {'domains': {}}

    def test_resolve_for_custom_domain(self):
        domain_1 = utils.persist_custom_domain()
        resolver = ResolverService(domain_1.name)
        assert resolver.get_domain_ip() == domain_1.associated_ips[0]

    def test_resolve_for_external_domain_with_one_ip(self):
        domain = utils.persist_external_domain_with_one_ip()
        resolver = ResolverService(domain.name)
        assert resolver.get_domain_ip() == domain.associated_ips[0]

    def test_resolve_for_multiple_queries_external_domain_with_one_ip(self):
        domain = utils.persist_external_domain_with_one_ip()
        resolver = ResolverService(domain.name)
        assert resolver.get_domain_ip() == domain.associated_ips[0]
        assert resolver.get_domain_ip() == domain.associated_ips[0]

    # def test_resolve_for_external_domain_with_one_ip_and_expired_ttl(self):
    #     domain = utils.persist_external_domain_with_one_ip()
    #     resolver = ResolverService(domain.name)
    #     assert resolver.get_domain_ip() == utils.DEFAULT_DOMAIN_IP_1
    #     do_expire_ttl(domain, utils.DEFAULT_DOMAIN_IP_2)
    #     assert resolver.get_domain_ip() == utils.DEFAULT_DOMAIN_IP_2


