from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect
from ..models import Course,HotelReserve
def check_payed(amount,code):
	return True
def hotelreserveform(request):
	course_id=request.GET.get('course_id')
	try:
		course=Course.objects.get(id=int(course_id))
		return render(request,'hotel/form.html',{'course':course})
	except Exception, e:
		return HttpResponse('matching course not found')
	

def hotelreserve(request):
	name=request.POST.getlist("name")
	last_name=request.POST.getlist("last_name")
	phone_number=request.POST.getlist("phone_number")
	parent_phone=request.POST.getlist("parent_phone")
	home_phone=request.POST.getlist("home_phone")
	city=request.POST.getlist("city")
	provinence=request.POST.getlist("provinence")
	sid=request.POST.getlist("sid")
	
	session=request.COOKIES.get('csrftoken')
	course_id=request.POST.get("course_id")
	if(len(name)==len(last_name) and len(name)==len(phone_number) and len(name)==len(parent_phone) and len(name)==len(home_phone) and len(name)==len(city) and len(name)==len(provinence) and len(name)==len(sid)):
		try:
			print len(name)
			for idx, val in enumerate(name):
				course=Course.objects.get(id=int(course_id))
				reserve=HotelReserve(name=name[idx],last_name=last_name[idx],phone_number=phone_number[idx],parent_phone=parent_phone[idx],home_phone=home_phone[idx],city=city[idx],provinence=provinence[idx],sid=sid[idx],course=course,ordersnumber=len(name),session=session)
				reserve.save()
			return HttpResponseRedirect('http://google.com/')
		except Exception, e:
			pass
	else:
		pass
	return HttpResponse("missing parameters")

def hotelpayment(request):
	try:
		session=request.COOKIES.get('csrftoken')
		first_order=HotelReserve.objects.filter(session=session,payed=False).order_by('-id')[0]
		all_orders=HotelReserve.objects.filter(session=session,payed=False).order_by('-id')[:first_order.ordersnumber]
		total_cost=0
		for each in all_orders:
			total_cost+=each.course.cost
		if(check_payed(total_cost,'asdasijdasdasd')):
			for each in all_orders:
				each.payed=True
				each.save()
			return HttpResponse("done! :)")
		else:
			return HttpResponse("payment went wrong!")
	except Exception, e:
		return HttpResponse("payment went wrong")
