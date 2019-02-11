
# 3rd party modules
from flask import make_response, abort
import pythonDevelopmersTest.model.authoize as authorize
import pythonDevelopmersTest.model.services as services


# login api get username and password and return response
def login ( userpass ) :

    # response body created but not field
    response = {
        'status':'',
        'token':''
    }
    # call model function to check authorization
    token = authorize.login(userpass)
    if token is None:
        response['status']='failed'
    else:
        response['status'] = 'success'
        response['token'] = token
    return response


# login api get token and return success of fail
def logout(tokenjson):
    # response body created but not field
    response = {
        'status':''
    }
    token = tokenjson['token']
    status = authorize.logout(token)
    if status is False:
        response['status'] = 'failed'
    else:
        response['status'] = 'success'
    return response


def query(query):
    response = {
        'status':'',
        'response':''
    }
    token = query["token"]
    request = query["request"]

    if authorize.tokencheck(token) is False:
        response['status']='failed'
    else:
        if request in services.SERVICES.keys() :
            response['response'] = services.SERVICES[request]()
            response['status'] = 'success'

    return response