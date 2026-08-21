from flask import Flask
app=Flask(__name__)
@app.route("/")
def home():
	return "flask application running successfully"
if __name__==('__main__'):
    app.run(debug=True)
    app.run('0.0.0.0',5000)
