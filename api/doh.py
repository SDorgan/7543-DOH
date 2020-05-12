from flask import abort, make_response, jsonify

from resolver.creation_service import CreationService
from api.doh_dtos import Error
from resolver.dns_query_service import DnsQueryService
from resolver.get_domain_service import GetDomainService


def get_domain(domain):
    service = GetDomainService(domain, DnsQueryService(domain))
    try:
        resolution = service.get_domain_resolution()
        return jsonify(resolution.serialize()), 201
    except Exception:
        error = Error('domain not found')
        return jsonify(error.serialize()), 404


def get_custom_domains(q=''):
    print('[', q, ']', sep='')
    pass


def post_custom_domain(**kwargs):
    body = kwargs.get('body')
    if ('domain' not in body) or ('ip' not in body):
        #Specified Error. Could be changed to malformed 
        return abort(400, "custom domain already exists")

    domain = CreationService.get_instance().add_domain(body['domain'], body['ip'])
    if (domain is None):
        return abort(400, "custom domain already exists")

    response_body = {'domain': body['domain'], 'ip': body['ip'], 'custom': True}
    return make_response(response_body , 201)


def put_custom_domain(domain, **kwargs):
    print(domain)
    body = kwargs.get('body')
    print(body)
    pass


def delete_custom_domain(domain):
    print(domain)
    pass
