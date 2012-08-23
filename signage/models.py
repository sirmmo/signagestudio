from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User)

class Block(models.Model):
	owner = models.ForeignKey(User, null=True, blank=True)
	js_code = models.TextField()
	url = models.URLField()

class Template(models.Model):
	owner = models.ForeignKey(User)
	template = models.TextField()
	name = models.CharField(max_length=255)
	block = models.ForeignKey(Block, related_name="templates")

class Campaign(models.Model):
	owner = models.ForeignKey(User)
	name = models.CharField(max_length=255)
	active=models.BooleanField(default=True)
	infos = models.TextField(blank=True, null=True)
	class Meta:
		unique_together = ("name","owner")


class PanelCollection(models.Model):
	name = models.CharField(max_length=255)
	campaign = models.ForeignKey(Campaign)	
	owner = models.ForeignKey(User, related_name="panels")

	class Meta:
		unique_together = ("name", "campaign")


class PanelCollectionStyles(models.Model):
	name = models.TextField()
	collection = models.ForeignKey(PanelCollection, null=True)
	key = models.TextField()
	value=models.TextField()
	class Meta:
		unique_together = (("name", "collection"), ('name', 'key'), )

class Panel (models.Model):
	name = models.CharField(max_length = 255)
	owner = models.ForeignKey(User)
	background = models.TextField(null=True, blank=True)
	collection = models.ForeignKey(PanelCollection, null=True, blank=True)
	panel_login = models.CharField(max_length=255, editable=False)
	panel_pw = models.CharField(max_length=255, editable=False)

	class Meta:
                unique_together = (("name", "collection"), ('name', 'owner'), )
	

class PanelBlock(models.Model):
	block = models.ForeignKey(Block, related_name = "panels", null=True, blank=True)
	area_top = models.IntegerField()
	area_left = models.IntegerField()
	area_width = models.IntegerField()
	area_height = models.IntegerField()
	name = models.CharField(max_length=555)
	panel = models.ForeignKey(Panel, related_name = "blocks")
	configuration = models.TextField(null=True, blank=True)


	class Meta:
                unique_together = (("block", "panel"), )

