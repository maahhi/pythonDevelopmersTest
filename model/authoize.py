# the database contain username and password
DATABASE = {
    'test' : 'test'
}

TOKEN = []


# return None for incorrect username-password and return token for correct
def login(userpass):
    username = userpass['username']
    password = userpass['password']

    # checking username exist
    if username in DATABASE.keys():
        # checking password for this username
        if DATABASE[username] == password:
            # for correct usename and password a token will create
            return token()

    # username may not exist or password may not match
    return None

# check the token if valid
def logout(token):
    # if token in list of tokens remove it, else there is problem in logout process
    if tokencheck(token) :
        if tokenremove(token) :
            return True
    return False


# it calls by login function in authorize file and return a new token
def token():
    newtoken = "123456"
    TOKEN.append(newtoken)
    return newtoken


# check the token with private key and will return True or False
def tokencheck(token):
    if token in TOKEN:
        return True
    else:
        return False

# remove token from token list, it will be called only in logout func and tokencheck called before it
def tokenremove(token):
    TOKEN.remove(token)
    return True