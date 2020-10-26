from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'home.html', {})


def add(request):
	from random import randint
	
	num_1 = randint(0,10)
	num_2 = randint(0,10)
	



	if request.method == "POST":
		answer = request.POST['box']
		old_num_1 = request.POST['old_num_1']
		old_num_2  = request.POST['old_num_2']

		if not answer :
			my_answer =" your forgot to fill the form"
			color = "warning"
			return render(request, 'add.html' ,{
			
				'num_1': num_1,
				'num_2': num_2,
				'answer':answer,
				'my_answer': my_answer,
				"color":color,
			})

		correct_answer = int(old_num_1) + int(old_num_2)
		if int(answer) == correct_answer:
			my_answer  = "Correct"+ " "  +str(old_num_1) + " + " +str(old_num_2) + "  =  " + str(answer) 
			color ="success" 
		else:
			my_answer  = "Incorrect"+ " "  +str(old_num_1) + " + "  +str(old_num_2) + "  Not  " + str(answer) + "  it is " + str(correct_answer) 
			color ="danger" 


		return render(request, 'add.html' ,{
			'my_answer': my_answer,
				'num_1': num_1,
				'num_2': num_2,
				'answer':answer,
				"color":color,
		

			})
	return render(request, 'add.html', {

		'num_1': num_1,
		'num_2': num_2,
		


		})

def subtract(request):
	from random import randint
	
	num_1 = randint(0,10)
	num_2 = randint(0,10)
	



	if request.method == "POST":
		answer = request.POST['box']
		old_num_1 = request.POST['old_num_1']
		old_num_2  = request.POST['old_num_2']

		if not answer :
			my_answer =" your forgot to fill the form"
			color = "warning"
			return render(request, 'subtract.html' ,{
			
				'num_1': num_1,
				'num_2': num_2,
				'answer':answer,
				'my_answer': my_answer,
				"color":color,
			})


		correct_answer = int(old_num_1) - int(old_num_2)
		if int(answer) == correct_answer:
			my_answer  = "Correct"+ " "  +str(old_num_1) + " - " +str(old_num_2) + "  =  " + str(answer) 
			color ="success" 
		else:
			my_answer  = "Incorrect"+ " "  +str(old_num_1) + " - "  +str(old_num_2) + "  Not  " + str(answer) + "  it is " + str(correct_answer) 
			color ="danger" 


		return render(request, 'subtract.html' ,{
			'my_answer': my_answer,
				'num_1': num_1,
				'num_2': num_2,
				'answer':answer,
				"color":color,
		

			})
	return render(request, 'subtract.html', {

		'num_1': num_1,
		'num_2': num_2,
		


		})

def multiply(request):
	from random import randint
	
	num_1 = randint(0,10)
	num_2 = randint(0,10)
	



	if request.method == "POST":
		answer = request.POST['box']
		old_num_1 = request.POST['old_num_1']
		old_num_2  = request.POST['old_num_2']

		if not answer :
			my_answer =" your forgot to fill the form"
			color = "warning"
			return render(request, 'multiply.html' ,{
			
				'num_1': num_1,
				'num_2': num_2,
				'answer':answer,
				'my_answer': my_answer,
				"color":color,
			})

		correct_answer = int(old_num_1) * int(old_num_2)
		if int(answer) == correct_answer:
			my_answer  = "Correct"+ " "  +str(old_num_1) + " X " +str(old_num_2) + "  =  " + str(answer) 
			color ="success" 
		else:
			my_answer  = "Incorrect"+ " "  +str(old_num_1) + " X "  +str(old_num_2) + "  Not  " + str(answer) + "  it is " + str(correct_answer) 
			color ="danger" 


		return render(request, 'multiply.html' ,{
			'my_answer': my_answer,
				'num_1': num_1,
				'num_2': num_2,
				'answer':answer,
				"color":color,
		

			})
	return render(request, 'multiply.html', {

		'num_1': num_1,
		'num_2': num_2,
		


		})

def divide(request):
	from random import randint
	
	num_1 = randint(0,10)
	num_2 = randint(1,10)
	



	if request.method == "POST":
		answer = request.POST['box']
		old_num_1 = request.POST['old_num_1']
		old_num_2  = request.POST['old_num_2']

		if not answer :
			my_answer =" your forgot to fill the form"
			color = "warning"
			return render(request, 'divide.html' ,{
			
				'num_1': num_1,
				'num_2': num_2,
				'answer':answer,
				'my_answer': my_answer,
				"color":color,
			})

		correct_answer = int(old_num_1) / int(old_num_2)
		if float(answer) == correct_answer:
			my_answer  = "Correct"+ " "  +str(old_num_1) + " / " +str(old_num_2) + "  =  " + str(answer) 
			color ="success" 
		else:
			my_answer  = "Incorrect"+ " "  +str(old_num_1) + " / "  +str(old_num_2) + "  Not  " + str(answer) + "  it is " + str(correct_answer) 
			color ="danger" 


		return render(request, 'divide.html' ,{
			'my_answer': my_answer,
				'num_1': num_1,
				'num_2': num_2,
				'answer':answer,
				"color":color,
		

			})
	return render(request, 'divide.html', {

		'num_1': num_1,
		'num_2': num_2,
		


		})