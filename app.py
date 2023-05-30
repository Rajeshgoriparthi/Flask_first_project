from flask import Flask 

FAI=Flask(__name__)

@FAI.route('/Raj')
def Raj():
    return "This is Rajesh's first Flask project.....!"

@FAI.route('/Rajesh')
def Rajesh():
    return "This is also Rajesh's first flask but second view"


if __name__=='__main__':
    FAI.run(debug=True)