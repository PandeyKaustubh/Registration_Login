from django.http import HttpResponse

def index(request):
	return HttpResponse("<h1> Hey Bruh")
def test(request):
	return HttpResponse("<h1> Chalo re lunch kar lo")
