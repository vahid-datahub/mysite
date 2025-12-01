from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# request is the arguman that our user required 
# def http_test(request):
#     return HttpResponse("<h1> this is a test</h1>") 

def index_view(request):
    return HttpResponse({'<h1>home page</h1>'})
 
def about_view(request):
    return HttpResponse({'<h1>about page</h1>'}) 

def contact_view(request):
    return HttpResponse({'<h1>contact page</h1>'}) 