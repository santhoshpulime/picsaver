from django.shortcuts import render,redirect
from .forms import picform
from .models import pics,password
from django.contrib.auth.models import User,auth
from django.contrib import messages


def home(request):

	form = picform()
	if request.method == 'POST':
		img = request.FILES['picphoto']
		title = request.POST['title']
		data = pics(photo=img,title=title,username=request.user)
		data.save()

	return render(request,'home.html',{'form':form})

def gallery(request):
	return redirect('lock')
	photos = pics.objects.all()
	return render(request,'gallery.html',{'photos':photos})

def signup(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		if User.objects.filter(username=username):
			messages.info(request,'username already exists')
			print('already exists')
			return redirect('signup')
		else:
			userdata = User.objects.create_user(username=username,password=password)
			userdata.save()	
			return redirect('login')

	return render(request,'signup.html')
 
def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		userdata = auth.authenticate(username=username,password=password)
		if userdata is not None:
			auth.login(request,userdata)
			return redirect('createpassword')
		else:
			messages.info(request,'you entered a wrong username')
			return redirect('login')
	return render(request,'login.html')

def logout(request):
	auth.logout(request)
	return redirect('/')
	return render(request,'logout.html')



#create password
def createpassword(request):

	if request.method == 'POST':
		usern = request.POST['user']
		password_text = request.POST['password']
		if password.objects.filter(usern=request.user):
			return redirect('/')
		data = password(usern=usern,password_text=password_text)
		data.save()
		return redirect('/')
	return render(request,'createpassword.html')


def lock(request):
	if request.method == 'POST':
		lock_g=request.POST['lock_pass']
		print(lock_g)
		if password.objects.filter(usern=request.user,password_text=lock_g):
			return redirect('originalgallery')
		else:
			return redirect('lock')
		
	return render(request,'passwords.html')


def originalgallery(request):
	
	photos = pics.objects.filter(username=request.user)
	return render(request,'originalgalary.html',{'photos':photos})

def editpassword(request):
	usernameget = password.objects.get(usern=request.user)
	uid=usernameget.id
	if request.method == 'POST':
		u = request.POST['user']
		l = request.POST['password']
		i = request.POST['userid']
		f = request.POST['fassword']
		if (usernameget.password_text == f):

			data = password(id=i,usern=u,password_text=l)
			data.save()
			return redirect('/')
		else:
			messages.info(request,'sorry wrong password')
			return redirect('editpassword')

	return render(request,'editpassword.html',{'uid':uid})