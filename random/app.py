from flask import Flask
import random
import webbrowser
app = Flask(__name__)
@app.route('/')
def four_d():
	four_d = str(random.sample(range(0,9),4))
	toto = str(random.sample(range(1,49),6))
	i1= str(random.randint(0,9))
	i2= str(random.randint(0,9))
	i3= str(random.randint(0,9))
	i4= str(random.randint(0,9))
	manual = i1+i2+i3+i4
	print("four_d:",four_d," ToTo:",toto," 4D manual:",manual)
	return '<br><br><center><h1><font color=blue>Lucky 4D : '+four_d+'<br><br> ToTo : '+toto +'<br><br> 4d :'+ manual
if __name__ == '__main__':
	webbrowser.open_new("http://127.0.0.1:5000")
	app.run()