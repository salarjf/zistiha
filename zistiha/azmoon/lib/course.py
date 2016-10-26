from django.http import HttpResponse,Http404,HttpResponseRedirect
from ..models import Exam,ExamOrder,ExamSubmition,Bonus,Course,CourseOrder
from django.shortcuts import render
def check_payed(amount,code):
	return True


def courseenrolsingle(request):
	course_id=request.GET.get('id')
	try:
		course_id=int(course_id)
	except:
		response=render(request,"exam/error.html",{"title":"invalid parameter! try again!"})
		return response
	if(Course.objects.get(pk=course_id)):
		course=Course.objects.get(pk=course_id)
		response=render(request,"course/single_order_form.html",{'title':course.title,'course_id':course_id})
		return response
	else:
		response=render(request,"exam/error.html",{'title':"Course Not Found!"})

def courseenrolmultiple(request):
	course_id=request.GET.get('course_id')
	try:
		course_id=int(course_id)
	except:
		response=render(request,"exam/error.html",{"title":"invalid parameter! try again!"})
		return response
	if(Course.objects.get(pk=course_id)):
		course=Course.objects.get(pk=course_id)
		response=render(request,"course/multiple_order_form.html",{'title':course.title,'course_id':course_id})
		return response
	else:
		response=render(request,"exam/error.html",{'title':"Course Not Found!"})


def courseorderdone(request):
	name=request.POST.get("name")
	last_name=request.POST.get("last_name")
	phone_number=request.POST.get("phone_number")
	school_type=request.POST.get("school_type")
	school_name=request.POST.get("school_name")
	city=request.POST.get("city")
	provinence=request.POST.get("provinence")
	parent_phone=request.POST.get("parent_phone")
	payment_type=request.POST.get("payment_type")
	bonus_code=request.POST.get("Bonus")
	course_id=request.POST.get("course_id")
	course=None
	try:
		course=Course.objects.get(pk=int(course_id))
	except:
		response=render(request,"exam/error.html",{"title":"missing argument! try again!"})
		return response

	if(last_name=="" or name=="" or phone_number=="" or parent_phone=="" or school_type=="" or school_name=="" or city=="" or provinence=="" or payment_type==""):
		return HttpResponse("missing parameters! try again!")
	if(bonus_code!=None):
		try:
			bonus_code=Bonus.objects.get(code=bonus_code)
		except:
			response=render(request,"exam/error.html",{"title":"code takhfife eshtebah vared kardeid ya parametra kharab shodan! dobare say konid"})
			return response
	if(bonus_code==None and payment_type=='once'):
		order=CourseOrder(Bonus=bonus_code,name=name,last_name=last_name,phone_number=phone_number,parent_phone=parent_phone,school_name=school_name,school_type=school_type,city=city,provinence=provinence,payment_type=payment_type,course=course,session=request.COOKIES.get('csrftoken'),payed=False,rest_money=0,ordersnumber=1,should_pay=course.cost)
		order.save()
		return HttpResponseRedirect('http://google.com/?q=salam')
	if(bonus_code==None and payment_type=='chunked'):
		order=CourseOrder(Bonus=bonus_code,name=name,last_name=last_name,phone_number=phone_number,parent_phone=parent_phone,school_name=school_name,school_type=school_type,city=city,provinence=provinence,payment_type=payment_type,course=course,session=request.COOKIES.get('csrftoken'),payed=False,rest_money=2*(course.cost)/3,ordersnumber=1,should_pay=course.cost/3)
		order.save()
		return HttpResponseRedirect('http://google.com/?q=salam')
	if(payment_type=='once'):
		should_pay=(bonus_code.precent*(course.cost))/100
		order=CourseOrder(Bonus=bonus_code,name=name,last_name=last_name,phone_number=phone_number,parent_phone=parent_phone,school_name=school_name,school_type=school_type,city=city,provinence=provinence,payment_type=payment_type,course=course,session=request.COOKIES.get('csrftoken'),payed=False,rest_money=0,ordersnumber=1,should_pay=should_pay)
		order.save()
		return HttpResponseRedirect('http://google.com/?q=salam')
def courseorderdonemultiple(request):
	name=request.POST.getlist("name")
	last_name=request.POST.getlist("last_name")
	phone_number=request.POST.getlist("phone_number")
	school_type=request.POST.getlist("school_type")
	school_name=request.POST.getlist("school_name")
	city=request.POST.getlist("city")
	provinence=request.POST.getlist("provinence")
	parent_phone=request.POST.getlist("parent_phone")
	payment_type=request.POST.getlist("payment_type")
	course_id=request.POST.getlist("course_id")
	if(last_name=="" or name=="" or phone_number=="" or parent_phone=="" or school_type=="" or school_name=="" or city=="" or provinence=="" or payment_type==""):
		return HttpResponse("missing parameter!")
	return HttpResponse("salam")


def coursepayment(request):
	session=request.COOKIES.get('csrftoken')
	first_order=CourseOrder.objects.filter(session=session,payed=False).order_by('-id')[0]
	if (first_order.ordersnumber==1):
		if(check_payed(first_order.should_pay,"oijdsijoidsjoijds")):
			first_order.payed=True
			first_order.Bonus.used=True
			first_order.save()
			return HttpResponse('hallle :)')
	else:
		all_orders=CourseOrder.objects.filter(session=session,payed=False).order_by('-id')[:first_order.ordersnumber]
		total_cost=0
		for each in all_orders:
			total_cost+=each.course.cost
		if(check_payed(total_cost,'asdasijdasdasd')):
			for each in all_orders:
				each.payed=True
				each.save()
		else:
			return HttpResponse("payment went wrong!")



