from django.shortcuts import render,redirect
from django.views.static import serve
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from PIL import Image
import string
import os
import random
# Create your views here.
def home(request):
	return render(request, "index.html", {})
def Signup(request):
	return render(request, "signup.html", {})
def Auth(request):
	a = request.POST.get('f1')
	b = request.POST.get('f2')
	c = request.POST.get('f3')
	d = request.POST.get('f4')
	e = request.POST.get('f5')
	if a==None or b==None or c==None or d==None or e==None or a=='' or b=='' or c=='' or d=='' or e=='':
		return render(request, "signup_error_less.html", {})
	else:
		if not os.path.exists(os.path.join(os.path.dirname(settings.BASE_DIR),"users/")+c):
			if d==e:
				os.mkdir(os.path.join(os.path.dirname(settings.BASE_DIR),"users/")+c)
				os.mkdir(os.path.join(os.path.dirname(settings.BASE_DIR),"users/")+c+'/chat')
				# os.mkdir(os.path.join(os.path.dirname(settings.BASE_DIR),'users/')+c)
				im2 = Image.open(os.path.join(os.path.dirname(settings.BASE_DIR),"users/")+'image.jpg')
				im2.save(os.path.join(os.path.dirname(settings.BASE_DIR),"users/")+c+'/image.jpeg', "JPEG")
			else:
				return render(request, "signup_error_pass.html", {})
		else:
			return render(request, "signup_error_email.html", {})
		f=open(os.path.join(os.path.dirname(settings.BASE_DIR),"users/")+c+'/contacts.txt','w')
		f.close()
		f=open(os.path.join(os.path.dirname(settings.BASE_DIR),"users/")+c+'/requests.txt','w')
		f.close()
		f=open(os.path.join(os.path.dirname(settings.BASE_DIR),"users/")+c+'/new_message.txt','w')
		f.close()
		f=open(os.path.join(os.path.dirname(settings.BASE_DIR),"users/")+c+'/notifications.txt','w')
		f.close()
		f=open(os.path.join(os.path.dirname(settings.BASE_DIR),"users/")+c+'/broadcasts.txt','w')
		f.close()
		uu=User.objects.create_user(c,c,d)
		uu.first_name=a
		uu.last_name=b
		uu.save()	
		return render(request, "signin.html", {})
def Create(request):
	a = request.POST.get('g1')
	b = request.POST.get('g2')
	tr=authenticate(username=a,email=a,password=b)
	if tr is not None:
		login(request,tr)
		U=User.objects.get(username=a)
		usern=U.first_name
		user=a
		f=open(os.path.join(os.path.dirname(settings.BASE_DIR),"users/")+a+'/requests.txt')
		val=f.readlines()
		f.close()
		val=len(val)
		f=open(os.path.join(os.path.dirname(settings.BASE_DIR),"users/")+a+'/new_message.txt')
		nm=f.readlines()
		nm=len(nm)
		f.close()
		f=open(os.path.join(os.path.dirname(settings.BASE_DIR),"users/")+a+'/notifications.txt')
		noti=f.readlines()
		f.close()
		f=open(os.path.join(os.path.dirname(settings.BASE_DIR),"users/")+a+'/notifications.txt','w')
		f.close()
		f=open(os.path.join(os.path.dirname(settings.BASE_DIR),"users/")+user+'/broadcasts.txt')
		cast=f.readlines()
		cast=len(cast)
		f.close()
		for i in range(len(noti)):
			noti[i]=noti[i].rstrip('\n')
		return render(request, "loginpage2.html", {'user':usern,'val':val,'nm':nm,'man':user,'noti':noti,'cast':cast})
	else:
		return render(request, "wrong_pass.html", {})
@login_required(login_url='index.html')
def Try(request):
	usern=request.user.first_name
	return render(request, "tpage.html", {'user':usern})
@login_required(login_url='index.html')
def Logout(request):
	logout(request)
	return render(request, "index.html", {})
	#return redirect('try.html')
@login_required(login_url='index.html')
def Received(request):
	user=request.user.email
	f=open(os.path.join(os.path.dirname(settings.BASE_DIR),"users/")+user+'/requests.txt')
	val=f.readlines()
	f.close()
	for i in range(len(val)):
		val[i]=val[i].rstrip('\n')
	return render(request, "received.html", {'val':val,'man':user})
@login_required(login_url='index.html')
def Accept(request):
	b=str(request)
	flag=0
	kk=''
	for c in b:
		if flag==1:
			kk=kk+c
		if c=='-':
			flag=1
	kk=kk.rstrip("'>")
	user=request.user.email
	f=open(os.path.join(os.path.dirname(settings.BASE_DIR),"users/")+user+'/contacts.txt','a')
	f.write(kk+'\n')
	f.close()
	f=open(os.path.join(os.path.dirname(settings.BASE_DIR),"users/")+kk+'/contacts.txt','a')
	f.write(user+'\n')
	f.close()
	f=open(os.path.join(os.path.dirname(settings.BASE_DIR),"users/")+user+'/requests.txt')
	val=f.readlines()
	val.remove(kk+'\n')
	f.close()
	f=open(os.path.join(os.path.dirname(settings.BASE_DIR),"users/")+user+'/requests.txt','w')
	f.writelines(val)
	f.close()
	f=open(os.path.join(os.path.dirname(settings.BASE_DIR),"users/")+kk+'/notifications.txt','a')
	f.write(user+' accepted your BRO request\n')
	f.close()
	for i in range(len(val)):
		val[i]=val[i].rstrip('\n')
	return render(request, "accepted.html", {'val':val,'who':kk,'what':'Accepted','man':user})
@login_required(login_url='index.html')
def Decline(request):
	b=str(request)
	flag=0
	kk=''
	for c in b:
		if flag==1:
			kk=kk+c
		if c=='-':
			flag=1
	kk=kk.rstrip("'>")
	user=request.user.email
	f=open(os.path.join(os.path.dirname(settings.BASE_DIR),"users/")+user+'/requests.txt')
	val=f.readlines()
	val.remove(kk+'\n')
	f.close()
	f=open(os.path.join(os.path.dirname(settings.BASE_DIR),"users/")+user+'/requests.txt','w')
	f.writelines(val)
	f.close()
	for i in range(len(val)):
		val[i]=val[i].rstrip('\n')
	return render(request, "accepted.html", {'val':val,'who':kk,'what':"Declined",'man':user})
@login_required(login_url='index.html')
def Add(request):
	a = request.POST.get('g1')
	user=request.user.email
	f=open(os.path.join(os.path.dirname(settings.BASE_DIR),"users/")+user+'/requests.txt')
	val=f.readlines()
	f.close()
	for i in range(len(val)):
		val[i]=val[i].rstrip('\n')
	if not os.path.exists(os.path.join(os.path.dirname(settings.BASE_DIR),"users/")+a):
		return render(request, "error_email.html", {'val':val,'man':user})
	else:
		f=open(os.path.join(os.path.dirname(settings.BASE_DIR),"users/")+a+'/requests.txt')
		cnt=f.readlines()
		f.close()
		f=open(os.path.join(os.path.dirname(settings.BASE_DIR),"users/")+a+'/contacts.txt')
		cnt2=f.readlines()
		f.close()
		if user+'\n' not in cnt and user+'\n' not in cnt2 and user!=a:
			f=open(os.path.join(os.path.dirname(settings.BASE_DIR),"users/")+a+'/requests.txt','a')
			f.write(user+'\n')
			f.close()
			return render(request, "sent.html", {'val':val,'man':user})
		elif user+'\n' in cnt:
			error="Request already sent!"
			return render(request, "adderror.html", {'val':val,'error':error,'man':user})
		else:
			error="Person is already in your Bro list"
			return render(request, "adderror.html", {'val':val,'error':error,'man':user})
@login_required(login_url='index.html')
def Yourbro(request):
	user=request.user.email
	f=open(os.path.join(os.path.dirname(settings.BASE_DIR),"users/")+user+'/contacts.txt')
	val=f.readlines()
	f.close()
	for i in range(len(val)):
		val[i]=val[i].rstrip('\n')
	return render(request, "yourbro.html", {'val':val,'man':user})
@login_required(login_url='index.html')
def Bpage(request):
		usern=request.user.first_name
		user=request.user.email
		f=open(os.path.join(os.path.dirname(settings.BASE_DIR),"users/")+user+'/requests.txt')
		val=f.readlines()
		f.close()
		val=len(val)
		f=open(os.path.join(os.path.dirname(settings.BASE_DIR),"users/")+user+'/new_message.txt')
		nm=f.readlines()
		nm=len(nm)
		f.close()
		cast=0
		noti=[]
		return render(request, "loginpage2.html", {'user':usern,'val':val,'nm':nm,'man':user,'cast':cast,'noti':noti})
@login_required(login_url='index.html')
def Chat(request):
	user=request.user.email
	mn=os.walk(os.path.join(os.path.dirname(settings.BASE_DIR),"users/")+user+'/chat')
	for c in mn:
		vals=c[2]
		break
	f=open(os.path.join(os.path.dirname(settings.BASE_DIR),"users/")+user+'/new_message.txt')
	val=f.readlines()
	f.close()
	f=open(os.path.join(os.path.dirname(settings.BASE_DIR),"users/")+user+'/new_message.txt','w')
	f.close()
	n=0
	for c in val:
		i=vals.index(c.rstrip('\n')+'.txt')
		vals[i],vals[n]=vals[n],vals[i]
		n+=1
	for i in range(len(vals)):
		vals[i]=vals[i].rstrip('.txt')
	for i in range(n):
		vals[i]=vals[i]+'-------------NEW'
	return render(request, "chat.html", {'val':vals,'man':user})
@login_required(login_url='index.html')
def CreateChat(request):
	b=str(request)
	flag=0
	kk=''
	for c in b:
		if flag==1:
			kk=kk+c
		if c=='-':
			flag=1
	kk=kk.rstrip("'>")
	kk=kk.rstrip('-------------NEW')
	user=request.user.email
	U=User.objects.get(username=kk)
	name=U.first_name
	mn=os.walk(os.path.join(os.path.dirname(settings.BASE_DIR),"users/")+user+'/chat')
	for c in mn:
		vals=c[2]
		break
	if kk+'.txt' in vals:
		f=open(os.path.join(os.path.dirname(settings.BASE_DIR),"users/")+user+'/chat/'+kk+'.txt')
	else:
		f=open(os.path.join(os.path.dirname(settings.BASE_DIR),"users/")+user+'/chat/'+kk+'.txt','w')
	f.close()
	f=open(os.path.join(os.path.dirname(settings.BASE_DIR),"users/")+user+'/chat/'+kk+'.txt')
	val=f.readlines()
	for i in range(len(val)):
		val[i]=val[i].rstrip('\n')
	return render(request, "chatprofile.html", {'val':val,'kk':kk,'name':name,'man':user})
@login_required(login_url='index.html')
def Send(request):
	mes=request.POST.get('g1')
	user=request.user.email
	b=str(request)
	flag=0
	kk=''
	for c in b:
		if flag==1:
			kk=kk+c
		if c=='-':
			flag=1
	kk=kk.rstrip("'>")
	kk=kk.rstrip('-------------NEW')
	f=open(os.path.join(os.path.dirname(settings.BASE_DIR),"users/")+user+'/chat/'+kk+'.txt','a')
	f.write("m:"+mes+'\n')
	f.close()
	if os.path.isfile(os.path.join(os.path.dirname(settings.BASE_DIR),"users/")+kk+'/chat/'+user+'.txt'):
		f=open(os.path.join(os.path.dirname(settings.BASE_DIR),"users/")+kk+'/chat/'+user+'.txt','a')
	else:
		f=open(os.path.join(os.path.dirname(settings.BASE_DIR),"users/")+kk+'/chat/'+user+'.txt','a')
	f.write("y:"+mes+'\n')
	f.close()
	f=open(os.path.join(os.path.dirname(settings.BASE_DIR),"users/")+kk+'/new_message.txt')
	xx=f.readlines()
	f.close()
	if user+'\n' not in xx:
		f=open(os.path.join(os.path.dirname(settings.BASE_DIR),"users/")+kk+'/new_message.txt','a')
		f.write(user+'\n')
		f.close()
	f=open(os.path.join(os.path.dirname(settings.BASE_DIR),"users/")+user+'/chat/'+kk+'.txt')
	val=f.readlines()
	f.close()
	for i in range(len(val)):
		val[i]=val[i].rstrip('\n')
	U=User.objects.get(username=kk)
	name=U.first_name
	return render(request, "chatprofile.html", {'val':val,'kk':kk,'name':name,'man':user})
@login_required(login_url='index.html')
def DeleteChat(request):
	b=str(request)
	user=request.user.email
	flag=0
	kk=''
	for c in b:
		if flag==1:
			kk=kk+c
		if c=='-':
			flag=1
	kk=kk.rstrip("'>")
	kk=kk.rstrip('-------------NEW')
	os.remove(os.path.join(os.path.dirname(settings.BASE_DIR),"users/")+user+'/chat/'+kk+'.txt')
	mn=os.walk(os.path.join(os.path.dirname(settings.BASE_DIR),"users/")+user+'/chat')
	for c in mn:
		vals=c[2]
		break
	f=open(os.path.join(os.path.dirname(settings.BASE_DIR),"users/")+user+'/new_message.txt')
	val=f.readlines()
	f.close()
	f=open(os.path.join(os.path.dirname(settings.BASE_DIR),"users/")+user+'/new_message.txt','w')
	f.close()
	n=0
	for c in val:
		i=vals.index(c.rstrip('\n')+'.txt')
		vals[i],vals[n]=vals[n],vals[i]
		n+=1
	for i in range(len(vals)):
		vals[i]=vals[i].rstrip('.txt')
	for i in range(n):
		vals[i]=vals[i]+'-------------NEW'
	return render(request, "chat.html", {'val':vals,'man':user})
@login_required(login_url='index.html')
def Upload(request):
	a = request.FILES.get('f1')
	a=a.readlines()
	c=request.user.email
	f=open(os.path.join(os.path.dirname(settings.BASE_DIR),"users/")+c+"/test.jpeg",'w')
	f.writelines(a)
	f.close()
	usern=request.user.first_name
	user=request.user.email
	f=open(os.path.join(os.path.dirname(settings.BASE_DIR),"users/")+user+'/requests.txt')
	val=f.readlines()
	f.close()
	val=len(val)
	f=open(os.path.join(os.path.dirname(settings.BASE_DIR),"users/")+user+'/new_message.txt')
	nm=f.readlines()
	nm=len(nm)
	f.close()
	f=open(os.path.join(os.path.dirname(settings.BASE_DIR),"users/")+user+'/broadcasts.txt')
	cast=f.readlines()
	cast=len(cast)
	f.close()
	noti=[]
	try:
		im = Image.open(os.path.join(os.path.dirname(settings.BASE_DIR),"users/")+c+"/test.jpeg")
		im.save(os.path.join(os.path.dirname(settings.BASE_DIR),"users/")+c+"/image.jpeg","JPEG")
		os.remove(os.path.join(os.path.dirname(settings.BASE_DIR),"users/")+c+"/test.jpeg")
		return render(request, "loginpage2.html", {'user':usern,'val':val,'nm':nm,'man':user,'cast':cast,'noti':noti})
	except:
		return render(request, "picuperror.html", {'user':usern,'val':val,'nm':nm,'man':user,'cast':cast})
@login_required(login_url='index.html')
def Broadcast(request):
	usern=request.user.first_name
	user=request.user.email
	f=open(os.path.join(os.path.dirname(settings.BASE_DIR),"users/")+user+'/broadcasts.txt')
	val=f.readlines()
	val=val[::-1]
	f.close()
	for i in range(len(val)):
		val[i]=val[i].rstrip('\n')
	return render(request, "broadcast.html", {'val':val,'man':user})
@login_required(login_url='index.html')
def Broappend(request):
	cast=request.POST.get('g1')
	usern=request.user.first_name
	user=request.user.email
	cast=usern+":"+cast+'\n'
	f=open(os.path.join(os.path.dirname(settings.BASE_DIR),"users/")+user+'/broadcasts.txt','a')
	f.write(cast)
	f.close()
	f=open(os.path.join(os.path.dirname(settings.BASE_DIR),"users/")+user+'/contacts.txt')
	ppl=f.readlines()
	f.close()
	for i in range(len(ppl)):
		ppl[i]=ppl[i].rstrip('\n')
	for c in ppl:
		f=open(os.path.join(os.path.dirname(settings.BASE_DIR),"users/")+c+'/broadcasts.txt','a')
		f.write(cast)
		f.close()
	f=open(os.path.join(os.path.dirname(settings.BASE_DIR),"users/")+user+'/broadcasts.txt')
	val=f.readlines()
	val=val[::-1]
	f.close()
	for i in range(len(val)):
		val[i]=val[i].rstrip('\n')
	return render(request, "broadcast.html", {'val':val,'man':user})

