from django.shortcuts import render
import pdb; 
from django.http import HttpResponse,Http404,HttpResponseRedirect
from ..models import Exam,ExamOrder,ExamSubmition,Bonus
from django.utils.crypto import get_random_string
from dateutil import tz
from prints import *

Tehran = tz.gettz('Asia/Tehran')
from datetime import datetime as dt
from datetime import time
from datetime import timedelta
safety_interval=2
golden_precent=20
silver_precent=10
batch_bonus_percent=50
def check_payment(cost,code):
	#check if code does not exist in payments model
	#store new payment in payment model
	print "payment  "+str(cost)+"  "+code
	return True

def calculate_score(answers,corrects):
	yes=0
	for idx, val in enumerate(answers):
		if (val==corrects[idx]):
			yes=yes+1
	return (yes/float(len(corrects)))*100

def rerank(ExamSubmition,exam):
	submitions=ExamSubmition.objects.filter(exam=exam).order_by('-score')
	count=0
	for each in submitions:
		count+=1
		each.rank=count
		each.save()

def get_bonus_code(submision):
	if submision.rank<11:
		bonus=None
		try:
			bonus=Bonus.objects.get(submition=submision)
		except:
			pass
		if(bonus != None):
			Bonus.objects.filter(submition=submision).percent=golden_precent
		else:
			code=get_random_string(length=10)
			while len(Bonus.objects.filter(code=code))>1:
				code=get_random_string(length=10)
			bonus=Bonus(submition=submision,percent=golden_precent,code=code)	
			bonus.save()
		print "vall"	
		return bonus.code
	elif submision.rank<41:
		bonus=None
		try:
			bonus=Bonus.objects.get(submition=submision)
		except:
			pass
		if(bonus != None):
			Bonus.objects.filter(submition=submision).percent=silver_precent
		else:
			code=get_random_string(length=10)
			while len(Bonus.objects.filter(code=code))>1:
				code=get_random_string(length=10)
			bonus=Bonus(submition=submision,percent=silver_precent,code=code)	
			bonus.save()		
		return bonus.code
	else:
		submision.Bonus=None
		submision.save()
		bonus=Bonus.objects.get(submition=submision)
		bonus.delete()
		return "no bonus"
#yeja chandta sumision dasht! nayad peyesho begiram
#age dobare update kone pasokhnamasho!
def examslist(request):
	exams=Exam.objects.filter()
	response = render(request,'exam/examslist.html',{
		'exams':exams,
		})
	return response

def examslistmultiple(request):
	exams=Exam.objects.filter()
	response = render(request,'exam/examslistmultiple.html',{
		'exams':exams,
	})
	return response

def examenroll(request):
	selected=Exam.objects.filter(id__in=request.POST.getlist("exam"))
	totalCost=0
	for each in selected:
		totalCost=totalCost+each.cost

	name=request.POST.get("name")
	last_name=request.POST.get("last_name")
	phone_number=request.POST.get("phone_number")
	school_type=request.POST.get("school_type")
	school_name=request.POST.get("school_name")
	city=request.POST.get("city")
	provinence=request.POST.get("provinence")
	
	# response= render(request,"exam/examconfirm.html",{'selected':selected, "totalCost":totalCost})
	for each in selected:
		code=get_random_string(length=10)
		while len(ExamOrder.objects.filter(seckey=code))>1:
			code=get_random_string(length=10)
		order=ExamOrder(seckey=code,name=name,last_name=last_name,phone_number=phone_number,school_type=school_type,school_name=school_name,city=city,provinence=provinence,session=request.COOKIES.get('csrftoken'),exam=each,examsnumber=len(selected))
		order.save()
	return HttpResponseRedirect('http://google.com')

def examenrollmultiple(request):
	exam_ids=request.POST.getlist("exam")
	try:
		exams=[]
		for each in exam_ids:
			print int(each)
			exams.append(Exam.objects.get(id=int(each)))
		name=request.POST.getlist("name")
		last_name=request.POST.getlist("last_name")
		phone_number=request.POST.getlist("phone_number")
		school_type=request.POST.getlist("school_type")
		school_name=request.POST.getlist("school_name")
		city=request.POST.getlist("city")
		provinence=request.POST.getlist("provinence")

		if(len(name)!=len(last_name) or len(name)!=len(phone_number) or len(name)!=len(school_type) or len(name)!=len(school_type) or len(name)!=len(city) or len(name)!=len(provinence)):
			return HttpResponse('missing argument! please try again')
		for exam in exams:
			total_cost=batch_bonus_percent* float(exam.cost)/100
			for idx,val in enumerate(name):
				code=get_random_string(length=10)
				while len(ExamOrder.objects.filter(seckey=code))>1:
					code=get_random_string(length=10)
				order=ExamOrder(seckey=code,name=name[idx],last_name=last_name[idx],phone_number=phone_number[idx],school_type=school_type[idx],school_name=school_name[idx],city=city[idx],provinence=provinence[idx],session=request.COOKIES.get('csrftoken'),exam=exam,examsnumber=len(exams),ordersnumber=len(name))
				order.save()
		return HttpResponseRedirect('http://google.com')
	except Exception, e:
		print e
		return HttpResponse('exam not found')



#kolli bayad test beshe ghablesh
#masalan check kone ke in random generatede ghablan nabashe
def payexam(request):
	all_orders=ExamOrder.objects.all()[:3]
	return render(request,'exam/showbuyresult.html',{"orders":all_orders})
	first_order=ExamOrder.objects.filter(session=request.COOKIES.get('csrftoken'),payed=False).order_by('-id')[0]
	if first_order.ordersnumber==1:
		all_orders=ExamOrder.objects.filter(session=request.COOKIES.get('csrftoken'),payed=False).order_by('-id')[:first_order.examsnumber]
		totalCost=0
		for each in all_orders:
			totalCost+=each.exam.cost
		if check_payment(totalCost,'sadoihasdijasd'):
			for each in all_orders:
				each.payed=True
				each.save()
		print_id=store_print('exam_order',all_orders)
		return render(request,{"orders":all_orders,"print_id":print_id})
	else:
		all_orders=ExamOrder.objects.filter(session=request.COOKIES.get('csrftoken'),payed=False).order_by('-id')[:first_order.examsnumber*first_order.ordersnumber]
		totalCost=0
		for each in all_orders:
			totalCost+=batch_bonus_percent*float(each.exam.cost)/100
			if check_payment(totalCost,'sadoihasdijasd'):
				for each in all_orders:
					each.payed=True
					each.save()
		return render(request,{"orders":all_orders})
def getexamform(request):
	response=render(request,"exam/getexamform.html",{})
	return response

def takeexam(request):
	order=ExamOrder.objects.filter(seckey=request.POST.get("seckey"),payed=True)[0]
	if(order is not None):
		exam=order.exam
		if(exam.start.date() > dt.today().date() or dt.now().time()<exam.start.astimezone(Tehran).time() ):
			response=render(request,"exam/error.html",{"title":"Aazmun shoru nashode"})
		else:	
			questions=[]
			for each in order.exam.key.split(" "):
				questions.append(each.split("-")[0])
			time=((order.exam.duration-(dt.now().minute-order.exam.start.minute))-safety_interval)*60000
			response=render(request,"exam/takeexam.html",{"seckey":request.POST.get("seckey"),"order": order,"questions":questions,"time":time})
			response.set_cookie('seckey',request.POST.get("seckey"))
	else:
		response=render(request,"exam/error.html",{"title":"Your register key is not submitted"})
	return response

def submitexam(request):
	order=ExamOrder.objects.get(seckey=request.POST.get('seckey'))
	exam=order.exam
	if(exam.start.astimezone(Tehran).date() < dt.now().date()):
		return HttpResponse("passed day!\n")
	if(exam.start.astimezone(Tehran).date() > dt.now().date()):
		return HttpResponse("not day yet!")
	else:
		end_of_exam=exam.start+timedelta(minutes=exam.duration)
		print end_of_exam
		print dt.now()
		print order.exam.start
		if (dt.now().time()>exam.start.time() and dt.now().time()< end_of_exam.time()):
			print "salam"
			answers=[]
			corrects=[]
			for each in exam.key.split(" "):
				corrects.append(int(each.split("-")[1]))
				try:
					answers.append(int(request.POST.get("q"+each.split("-")[0])))
				except:
					answers.append(0)
			score=calculate_score(answers,corrects)
			submitted=""
			for idx,val in enumerate(answers):
				submitted=submitted+str(idx)+"-"+str(val)+" "
			try:
				submision=ExamSubmition.objects.get(order=order)
				submision.score=score
			except:
				submision=ExamSubmition(order=order,score=score,rank=0,exam=exam)
			
			submision.submitted=submitted
			submision.save()
			return HttpResponse("Sabt Shod! :)")
		else:
			return HttpResponse("time passed!\n")


def resultsform(request):
	return render(request,"exam/resultsform.html")

def getresults(request):
	try:
		print request.POST.get("seckey")
		order=ExamOrder.objects.get(seckey=request.POST.get("seckey"))
		submision=ExamSubmition.objects.get(order=order)
		exam=order.exam
		end_of_exam=exam.start+timedelta(minutes=exam.duration)
		rerank(ExamSubmition,exam)
		if(exam.start.date() > dt.today().date() or (exam.start.date() == dt.today().date()) and end_of_exam.time()>dt.now().time()):
			print exam.title		
			response = render(request,"exam/error.html",{"title":"Exam is not passed yet"})
		else:
			code=get_bonus_code(submision)
			response=render(request,"exam/showresult.html",{"code":code,"rank":submision.rank,"score":submision.score,"submitted":submision.submitted,"key":order.exam.key})
	except Exception , e:
		print e
		response=render(request,"exam/error.html",{"title":"Your register key is not submitted"})
	return response

