from django.core.management.base import BaseCommand, CommandError
from signage.models import *

from django.conf import settings

class Command(BaseCommand):
    args = None
    help = 'Starts the Signage Bot'

    def handle(self, *args, **options):
        xmpp = EchoBot(settings.BOT_USERNAME, settings.BOT_PASSWORD)
        xmpp.connect()
        xmpp.process(block=True)
                
from sleekxmpp import ClientXMPP
from sleekxmpp.exceptions import IqError, IqTimeout


class EchoBot(ClientXMPP):

    def __init__(self, jid, password):
        ClientXMPP.__init__(self, jid, password)

        self.add_event_handler("session_start", self.session_start)
        self.add_event_handler("message", self.message)
    
    def session_start(self, event):
        self.send_presence()
        self.get_roster()
    
    def message(self, msg):
        if msg['type'] in ('chat', 'normal'):
            msg.reply("Thanks for sending\n%(body)s" % msg).send()