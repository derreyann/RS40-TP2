# -*- coding: utf-8 -*-
"""

Created on May 2022
@author: Mr ABBAS-TURKI

"""

from flask import Flask, request
import ssl

#write a quick function to hash and salt the password
def hash_password(password):
    salt = "16"
    return salt + password + salt

# définir le message secret
SECRET_MESSAGE = "bigjoe bigman" # A modifier
app = Flask(__name__)
USER1_LOGIN = "bigjoe"
USER1_PASSWORD = hash_password("bigman") 



@app.route("/", methods=['GET', 'POST'])

def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username == USER1_LOGIN and hash_password(password) == USER1_PASSWORD:
            return ("Logged in successfully! \n" + SECRET_MESSAGE)
        else:
            return 'Wrong username or password!'
    
    return '<form action="" method="post">\n <p><input type=text name=username /></p>\n <p><input type=password name=password /></p>\n <p><input type=submit value=Login /></p>\n </form>'

if __name__ == "__main__":
    # HTTP version
    app.run(debug=True, host="0.0.0.0", port=8081)
    # HTTPS
    #ssl_context = ("server-public-key.pem", "server-private-key.pem")
    #app.run(debug=True, host="0.0.0.0", port=8082, ssl_context=ssl_context)
