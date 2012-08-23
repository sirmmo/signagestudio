from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from signage.models import *
import json

def index(request):
	return render_to_response('index.html')

@login_required
def dashboard(request):
	return render_to_response('dashboard.html')

def create_block(request):
	panel = request.REQUEST.get('panel', None)
	if panel is None:
		return HttpResponse(json.dumps(None))
	panel = Panel.objects.get(name=panel, owner=request.user)
	p = PanelBlock()
	p.panel = panel
	p.name="Block"
	p.area_top=0
	p.area_left = 0
	p.area_width=32
	p.area_height=32
	p.save()
	obj = {
		'name':p.name,
		'x':p.area_left,
		'y':p.area_top,
		'w':p.area_width,
		'h':p.area_height,
		'id':p.id
		}
	return HttpResponse(json.dumps(obj))

def get_campaigns(request):
	cs = Campaign.objects.filter(owner = request.user).all()
	ret = []
	for c in cs:
		ret.append({
			'name':c.name,
			'id':c.id
		})
	return HttpResponse(json.dumps(ret))
		

def get_panels(request):
	campaign=request.REQUEST.get('campaign', None)
	ps = Panel.objects.filter(owner=request.user)
	if campaign is None:
		ps = ps.filer(collection__isnull=True)
	else:
		ps = ps.filter(collection__campaign__name=campaign)
	ret = []
	for p in ps	:
			obj = {
				'id':p.id,
				'name':p.name,
				'bg':p.background,
				'collection':p.collection.name,
				'collection_id':p.collection.id,
			}
			ret.append(obj)
	return HttpResponse(json.dumps(ret))
	
	
	