from django.shortcuts import render_to_response

def index(request):
	return render_to_response('index.html')

def image(request, image_id):
	return render_to_response('image.html')
	
