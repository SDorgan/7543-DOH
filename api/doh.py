from flask import abort, make_response, jsonify

from api.doh_dtos import Error
from resolver.dns_query_service import DnsQueryService
from resolver.get_domain_service import GetDomainService
from resolver.get_custom_domains_service import GetCustomDomainService
from resolver.push_domain_service import PushDomainService
from resolver.put_domain_service import PutDomainService


def get_domain(domain):
    service = GetDomainService(domain, DnsQueryService(domain))
    try:
        resolution = service.get_domain_resolution()
        return jsonify(resolution.serialize()), 201
    except Exception:
        error = Error('domain not found')
        return jsonify(error.serialize()), 404


def get_custom_domains(q=''):
    service = GetCustomDomainService(q)
    service.get_custom_domains()

    resolutions = service.get_response()
    answer = {'items': []}
    for element in resolutions:
        answer['items'].append(element.serialize())
    return answer, 200


def post_custom_domain(**kwargs):
    body = kwargs.get('body')
    if ('domain' not in body) or ('ip' not in body):
        #Specified Error. Could be changed to malformed 
        error = Error('custom domain already exists')
        return jsonify(error.serialize()), 404
    service = PushDomainService(body['domain'], body['ip'])
    domain = service.add_domain()
    if (domain is None):
        error = Error('custom domain already exists')
        return jsonify(error.serialize()), 404

    resolution = service.get_response()
    return jsonify(resolution.serialize()), 201


def put_custom_domain(domain = '', **kwargs):
    body = kwargs.get('body')
    if ('domain' not in body) or ('ip' not in body):
        error = Error('payload is invalid')
        return jsonify(error.serialize()), 400
    if (body['domain'] != domain): #TBD
        error = Error('payload is invalid')
        return jsonify(error.serialize()), 400
    service = PutDomainService(body['domain'], body['ip'])
    domain = service.modify_domain()
    if (domain is None):
        error = Error('domain not found')
        return jsonify(error.serialize()), 404

    resolution = service.get_response()
    return jsonify(resolution.serialize()), 200


def delete_custom_domain(domain):
    print(domain)
    pass

