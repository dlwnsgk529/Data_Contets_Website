from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
	return "Hello!"
 
if __name__ == "__main__":
	   application.run(host='0.0.0.0', debug=True)
        

print("a")
print("b")
print("c")
print("d")
print("e")
print("f")
print("g")
print("hi")
print("h")
