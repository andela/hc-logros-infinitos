from django.conf import settings
from djmail.template_mail import InlineCSSTemplateMail

def send(name, to, ctx):
    o = InlineCSSTemplateMail(name)
    ctx["SITE_ROOT"] = settings.SITE_ROOT
    o.send(to, ctx)
    
def alert(to, ctx):
    send("alert", to, ctx)