
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


# logout api get token and return success of fail
def logout(tokenjson):
    # response body created but not field
    response = {
        'status':''
    }
    token = tokenjson['token']
    # if there is not problem in logout it will be success
    status = authorize.logout(token)
    if status is False:
        response['status'] = 'failed'
    else:
        response['status'] = 'success'
    return response


# check the token and query , fail if token is invalid or the request is not in saved query
def query(query):
    response = {
        'status':'',
        'response':''
    }
    token = query["token"]
    request = query["request"]

    # the user token is not valid
    if authorize.tokencheck(token) is False:
        response['status']='failed'
    else:
        # the request is in services list
        if request in services.SERVICES.keys() :
            # correspondent function for this service will call
            response['response'] = services.SERVICES[request]()
            response['status'] = 'success'
        else:
            # the request is not in services list
            response['response'] = ".متاسفانه قادر به تشخیص درخواست شما نیستم"
            response['status'] = 'failed'

    return response