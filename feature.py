from flask import Flask


# FAI stands for Flask Application Instance
# __name__ is used for current module name

FAI=Flask(__name__)

# In Django, URL mapping is called as Routing or Route

@FAI.route ('/strResponse') #urls
def strResponse(): #Views
    return ('<center><h1> Welcome User.... This is my 1st FLASK Project !!! <h1></center>')

@FAI.route ('/secstrResponse')
def secstrResponse():
    return ('<center><h1> Welcome User.... This is my 2nd FLASK Project !!! <h1></center>')


if __name__ == '__main__':
    FAI.run(debug=True)

# run command is used for run the server
# In debug, We give debug=True Before Development
# In debug, We give debug=False After Development