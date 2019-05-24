from flask import make_response, abort

ACCOUNT = {
    "User" : {
        "pseudo" : "pseudo",
        "password" : "password"
    }
}

def submit(pseudo, password):
    return 'le pseudo est : {} et le mdp est : {}'.format(pseudo, password), 200