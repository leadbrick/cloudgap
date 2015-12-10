from django.shortcuts import render,render_to_response

def home(request):
	return render(request,'home.html')

def to_be_updated(request):
	return render_to_response("tbu.html")

#the main fn handling all api calls
#handles retrieve and update calls
#params=> (auth) , q=read/update 
#read params => tablename  
#def api_handler(request):
