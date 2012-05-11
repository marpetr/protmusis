import json
import datetime
import mimetypes

from django.http import *
from django.shortcuts import *
from django.core.urlresolvers import *
from collection.models import *
from django.views.decorators.http import *
from django.views.decorators.cache import never_cache

import events

def frontpage(request):
	team_id = request.session.get('team_id')
	if team_id:
		team = get_object_or_404(Team, pk=team_id)
		return render(request, 'collection/main.html', { 'team': team })
	else:
		error = ''
		if request.method == 'POST':
			password = request.POST.get('password')
			teams = list(Team.objects.filter(password=password))
			if len(teams) == 1:
				team = teams[0]
				request.session['team_id'] = team.id
				return redirect(reverse(frontpage))
			else:
				error = 'Raktas neteisingas'
		return render(request, 'collection/login.html', { 'error': error })

def free_view(request):
	return render(request, 'collection/freeview.html')

def logout(request):
	if 'team_id' in request.session:
		del request.session['team_id']
	return redirect(reverse(frontpage))

@require_POST
@never_cache
def sync_state(request):
	team = get_object_or_404(Team, pk=request.session.get('team_id'))
	team.last_activity = datetime.datetime.now()
	team.save()
	active = list(Question.objects.filter(show_until__gt=datetime.datetime.now()))
	response = {}
	if active:
		q = active[0]
		if 'currentQID' in request.POST and request.POST['currentQID'] == str(q.id):
			txt = request.POST.get('currentText')
			if len(txt) > 500:
				txt = ''
			ans, created = Answer.objects.get_or_create(team=team, question=q)
			ans.text = txt
			ans.save()
		ans = list(Answer.objects.filter(team=team, question=q))
		response["view"] = "question"
		response["qid"] = q.id
		response["time_left"] = q.time_left()
		response["num"] = q.number
		response["cur_answer"] = "" if not ans else ans[0].text
	else:
		response["view"] = "idle"
	return HttpResponse(json.dumps(response), content_type='application/json')

@never_cache
def free_view_state(request):
	active = list(Question.objects.filter(show_until__gt=datetime.datetime.now()))
	response = {}
	if active:
		q = active[0]
		response["view"] = "question"
		response["qid"] = q.id
		response["time_left"] = q.time_left()
		response["num"] = q.number
	else:
		response["view"] = "idle"
	return HttpResponse(json.dumps(response), content_type='application/json')

@never_cache
def get_image(request):
	try:
		q = Question.objects.get(show_until__gt=datetime.datetime.now())
		f = q.question_image
		f.open()
		data = f.read()
		f.close()
		ctype = mimetypes.guess_type(f.name)[0]
		return HttpResponse(data, content_type=ctype)
	except: pass
	return HttpResponse()

import threading
msg_lock = threading.Lock()
wait_events = []
pub_msg = 'not set yet'

def test_view(request):
	global msg_lock, wait_events, pub_msg
	if request.GET.get('state'):
		with msg_lock:
			resp = HttpResponse('queue len: {0}<br />queue id: {2}<br />msg: {1}'.format(len(wait_events), pub_msg, id(wait_events)))
		return resp
	elif request.GET.get('put_message'):
		with msg_lock:
			pub_msg = request.GET.get('msg', '--')
			for e in wait_events:
				e.set()
			wait_events = []
		return HttpResponse('notified')
	else:
		ev = threading.Event()
		with msg_lock:
			wait_events.append(ev)
		ev.wait()
		with msg_lock:
			msg = pub_msg
		return HttpResponse('<title>'+msg+'</title>')
