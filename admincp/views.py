import datetime
import mimetypes

from django.http import *
from django.shortcuts import *
from django.core.urlresolvers import *
from collection.models import *
from django.views.decorators.http import *
from protmusis.admin import site

@site.admin_view
def controlpanel(request, qid=None):
	try:
		active = Question.objects.get(show_until__gt=datetime.datetime.now())
	except Question.DoesNotExist:
		active = None
	if qid:
		sq = Question.objects.get(number=qid)
	else:
		sq = None
	context = {
		'title': 'Control Panel',
		'teams': Team.objects.all(),
		'questions': Question.objects.all(),
		'cur_question': active,
		'sel_q': sq,
	}
	if sq:
		context['answers_list'] = sq.answer_set.order_by('team__name')
	return render(request, 'myadmin/controlpanel.html', context, current_app=site.name)

@site.admin_view
def show_question(request):
	q = get_object_or_404(Question, number=request.GET['qnum'])
	try:
		time = int(request.GET['secs'])
	except:
		time = 60
	if time <= 0 or time > 30*60:
		time = 60
	Question.objects.update(show_until=datetime.datetime.now())
	q.show_for(time)
	return redirect(reverse('admin:admincp_index_wqnum', args=(q.number,)))

@site.admin_view
def hide_question(request):
	Question.objects.update(show_until=datetime.datetime.now())
	return redirect(reverse('admin:admincp_index'))

@site.admin_view
def get_question_image(request, id):
	q = Question.objects.get(pk=id)
	f = q.question_image
	f.open()
	data = f.read()
	f.close()
	ctype = mimetypes.guess_type(f.name)[0]
	return HttpResponse(data, content_type=ctype)

@require_POST
@site.admin_view
def put_static_image(request):
	pass


