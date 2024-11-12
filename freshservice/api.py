from freshservice.v2 import api as v2_api
 


class FreshserviceAPI(object):
    def __init__(self, domain, api_key):
        """Creates a wrapper to perform API actions.

        Arguments:
          domain:    the Freshservice domain (not custom). e.g. company.freshservice.com
          api_key:   the API key 
        """


def API(domain, api_key, **kwargs): 
    client_class = v2_api.API
    return client_class(domain, api_key, **kwargs)
