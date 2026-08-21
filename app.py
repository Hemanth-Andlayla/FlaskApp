

from flask import Flask
app=Flask(__name__)
@app.route("/")
def home():
	#flask application running successfully
	return '''
	<html>
	    <body>
		 <h1>Hello RGUKT</h1>
	   </body>
	</html>
	'''
if __name__==('__main__'):
    app.run(debug=True)
    app.run('0.0.0.0',5000)
