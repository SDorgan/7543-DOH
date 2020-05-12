from flask import abort, make_response
from resolver.creation_service import CreationService

def get_domain(domain):
    print(domain)
    pass


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

