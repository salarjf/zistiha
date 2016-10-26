# - *- coding: utf- 8 - *-
from django.shortcuts import render
import pdb; 
from django.http import HttpResponse,Http404,HttpResponseRedirect
from ..models import PrintObject,ExamOrder
from django.utils.crypto import get_random_string
import reshaper
from bidi.algorithm import get_display

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
cm = 2.54

def get_print(doc,print_id):
    elements = []
    # text=PrintObject.objects.get(print_id=print_id).text
    text=PrintObject.objects.all()[1].text
    rows=text.split("%%%")
    data=[]
    for row in rows:
    	cols=row.split('&&&')
    	data.append(tuple(cols))
    # data=[(1,2,"sala"),(3,4,"sa;a")]
    table = Table(data, colWidths=80, rowHeights=79)
    elements.append(table)
    doc.build(elements) 

def store_print(type,data):
	data=ExamOrder.objects.all()[:3]
	header=""
	if(type=='exam_order'):
		header=u"نام &&& نام‌‌خانوادگی &&& شماره تماس &&& نوع دبیرستان &&& نام دبیرستان &&& شهر &&& استان &&& آزمون &&& کد شرکت"
		text=''
		for row in data:
			join_data=[row.name,row.last_name,row.phone_number,row.school_type,row.school_name,row.city,row.provinence,row.exam.title,row.seckey]
			# join_data.append(row.name,row.last_name,row.phone_number,row.school_type,row.school_name,row.city,row.provinence,row.exam.title,row.seckey)
			text+="%%%"+"&&&".join(join_data)
	print text
	text=header.encode('utf-8')+text.encode('utf-8')
	code=get_random_string(length=30)
	while len(PrintObject.objects.filter(print_id=code))>1:
		code=get_random_string(length=30)
	printobject=PrintObject(text=text,print_id=code)
	printobject.save()
	return code