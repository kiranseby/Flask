from flask import Flask #importing Flask class

app = Flask(__name__)#creating an instance of Flask class

@app.route('/hello')#route decorator to tell flask which url to be triggered
def helloworld():
    return "Helloworld!"

if __name__=='__main__':
    app.run(debug=True)#If any change is made, server restarts and we can see the change