from django.contrib.admin import site
from signage.models import *

site.register(UserProfile)
site.register(Template)
site.register(Block)
site.register(Campaign)
site.register(PanelCollection)
site.register(PanelCollectionStyles)
site.register(Panel)
site.register(PanelBlock)
site.register(PanelBlockConfiguration)