from flask import Flask,request,render_template  # "flask" is module # "Flask" is class

## I need to create an 'object' for this particular class 'Flask'

obj=Flask(__name__)  # Inside the parentheses u have to put module name and it is "main" which stores in "name" variable
# So bydefault module name is "main" # "__name__" variable is initialised by "main"


# To create URL u have to call "route" method with decorator
@obj.route('/')
def welcome():   # Then create a function 
    return "Welcome to Flask"  # This is return statement and u can put HTML tags here and HTML file also

@obj.route('/calculator',methods=["GET"])  # Creating calculator application
def math_operation():    # Inside this route we r going to create method and the method name is "math_operation"
    operation=request.json["operation"]            # Inside this method u can do any sort of operation
    number1=request.json["number1"]       # This time we r requesting from "postman" not from "HTML"
    number2=request.json["number2"]                         

    if operation=="add":
        result=number1+number2
    elif operation=="substraction":
        result=number1-number2
    elif operation=="multiplication":
        result=number1*number2
    else:
        result=number1/number2
        return result



print(__name__)

if __name__=='__main__': # If u want to run this file as stand alone file then put condition
    obj.run()  # To Run the functions in Flask u have to call another ".run()" function