from lib.exam import *
from lib.hotel import *
from lib.course import *
from lib.prints import*


from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle


def printreport(request):
	try:
	    response = HttpResponse(content_type='application/pdf')
	    response['Content-Disposition'] = 'attachment; filename=somefilename.pdf'
	    doc = SimpleDocTemplate(response, rightMargin=0, leftMargin=6.5 * cm, topMargin=0.3 * cm, bottomMargin=0)
	    get_print(doc,request.GET.get('print_id'))
	    return response
	except Exception, e:
		return HttpResponse('error in print!')

def testprint(request):
	return HttpResponse(store_print('exam_order','salam'))