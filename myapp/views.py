from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from myapp.models import *
from django.core.mail import send_mail
from django.conf import settings
# from django.views.generic import TemplateView
from myapp.forms import *

# Create your views here.
def welcome(request):
    return render(request, "base.html")
    # today = datetime.datetime.now().date()
    # daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    # return render(request, "hello.html",{
    #     "today":today, 
    #     "daysOfWeek":daysOfWeek,
    #     })

def viewArticleId(request, articleId):
    text = "<h1>Display article ID : %s</h1>" %articleId
    # return HttpResponse(text)
    return redirect(viewArticle, year = "2045", month = "02")

def viewArticle(request, year, month):
    text = "<h1>Display article year %s month %s</h1>" %(year,month)
    return HttpResponse(text)

def crudops(request):
    # add entry
    dreamreal = Dreamreal(
      website = "www.polo.com", 
      mail = "sorex@polo.com", 
      name = "sorex", 
      phonenumber = "002376970"
    )
    dreamreal.save()

    # get ALL entries
    objects = Dreamreal.objects.all()
    res ='Printing all Dreamreal entries in the DB : <br>'
    
    for elt in objects:
        res += elt.name+"<br>"

    #Read a specific entry:
    sorex = Dreamreal.objects.get(name = "sorex")
    res += 'Printing One entry <br>'
    res += sorex.name

    #Delete an entry
    res += '<br> Deleting an entry <br>'
    sorex.delete()

    #Update
    dreamreal = Dreamreal(
        website = "www.polo.com", mail = "sorex@polo.com", 
        name = "sorex", phonenumber = "002376970"
    )
    dreamreal.save()
    res += 'Updating entry<br>'
    dreamreal = Dreamreal.objects.get(name = 'sorex')
    dreamreal.name = 'thierry'
    dreamreal.save()

    return HttpResponse(res)

def datamanipulation(request):
    res = ''
    
    #Filtering data:
    qs = Dreamreal.objects.filter(name = "paul")
    res += "Found : %s results<br>"%len(qs)
    
    #Ordering results
    qs = Dreamreal.objects.order_by("name")
    
    for elt in qs:
        res += elt.name + '<br>'
    
    return HttpResponse(res)

def sendSimpleEmail(request,emailto):
    # subject = 'Myapp email'
    # contact_message = "Ini isinya"
    # from_email = settings.EMAIL_HOST_USER
    # to_email = [emailto,]
    # res = send_mail(subject, contact_message, from_email, to_email, fail_silently=False)
    res = send_mail("hello paul", "comment tu vas?", "paul@polo.com", [emailto])
    return HttpResponse('%s'%res)

# def static(request):
#    return render(request, 'static.html', {})

# class StaticView(TemplateView):
#    template_name = "static.html"

def login(request):
    username = "not logged in"
    
    if request.method == "POST":
        #Get the posted form
        MyLoginForm = LoginForm(request.POST)
        
        if MyLoginForm.is_valid():
            username = MyLoginForm.cleaned_data['username']
            # if request.session.has_key('username'):
            #     del request.session['username']
            request.session['username'] = username
            
            return render(request, 'loggedin.html', {"username" : username})
        else:
            form = LoginForm()
            return render(request, 'login.html', {"form" : form})
    else:
        MyLoginForm = LoginForm()
        return render(request, 'login.html', {"form" : MyLoginForm})

# def login(request):
#    username = "not logged in"
   
#    if request.method == "POST":
#       #Get the posted form
#       MyLoginForm = LoginForm(request.POST)
   
#    if MyLoginForm.is_valid():
#       username = MyLoginForm.cleaned_data['username']
#    else:
#       MyLoginForm = LoginForm()
   
#    response = render_to_response(request, 'loggedin.html', {"username" : username}, 
#       context_instance = RequestContext(request))
   
#    response.set_cookie('last_connection', datetime.datetime.now())
#    response.set_cookie('username', datetime.datetime.now())
	
#    return response

def SaveProfile(request):
   saved = False
   
   if request.method == "POST":
      #Get the posted form
      MyProfileForm = ProfileForm(request.POST, request.FILES)
      
      if MyProfileForm.is_valid():
         profile = Profile()
         profile.name = MyProfileForm.cleaned_data["name"]
         profile.picture = MyProfileForm.cleaned_data["picture"]
         profile.save()
         saved = True
   else:
      MyProfileForm = Profileorm()
		
   return render(request, 'saved.html', locals())
            