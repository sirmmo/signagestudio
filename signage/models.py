from django.db import models
from multitenant.models import TenantModel

from django.contrib.auth.models import User

class ICHTemplate(models.Model):
	template = models.TextField()
	name = models.CharField(max_length=255)
	block = models.ForeignKey('Block', related_name="ich_templates")

class Block(models.Model):
	owner = models.ForeignKey(User)
	cs_code = models.TextField()
	ss_code = models.TextField()
	



class Panel (TenantModel):
	name = models.CharField(max_length = 255)
	owner = models.ForeignKey(User)
	background = models.TextField()

class PanelBlock(TenantModel):
	block = models.ForeignKey(Block, related_name = "panels")
	area_top = models.IntegerField()
	area_left = models.IntegerField()
	area_width = models.IntegerField()
	area_height = models.IntegerField()
	panel = models.ForeignKey(Panel, related_name = "blocks")

class PanelBlockConfiguration(TenantModel):
	panel_block = models.ForeignKey(PanelBlock)
	
