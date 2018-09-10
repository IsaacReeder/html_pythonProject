from flask import Flask, render_template  
                                          
app = Flask(__name__)                     
                                          


@app.route('/', methods=['GET'])                         
                                          
def index():
    users = (
        {'number' : '1', 'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'number' : '2','first_name' : 'John', 'last_name' : 'Supsupin'},
        {'number' : '3','first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'number' : '4','first_name' : 'KB', 'last_name' : 'Tonel'}
    )
    print(users)
    return render_template("html_python.html",users1=users)      

if __name__=="__main__":
    app.run(debug=True)                   
