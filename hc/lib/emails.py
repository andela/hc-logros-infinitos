from django.conf import settings
from djmail.template_mail import InlineCSSTemplateMail


def send(name, to, ctx, cat_id=None, blog_id=None):
    o = InlineCSSTemplateMail(name)
    ctx["SITE_ROOT"] = settings.SITE_ROOT
    o.send(to, ctx)


def login(to, ctx):
    send("login", to, ctx)


def set_password(to, ctx):
    send("set-password", to, ctx)


def alert(to, ctx):
    send("alert", to, ctx)


def verify_email(to, ctx):
    send("verify-email", to, ctx)


def report(to, ctx):
    send("report", to, ctx)


def share_blog(to, ctx, cat_id, blog_id):
    send("blog", to, ctx, cat_id, blog_id)
