
# 3rd party modules
import pythonDevelopmersTest.model.authoize as authorize


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
