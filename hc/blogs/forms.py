from django import forms
from hc.blogs.models import Blog, Category
from pagedown.widgets import PagedownWidget


class CreateBlogForm(forms.Form):
    body = forms.CharField(widget = PagedownWidget)

class CreateCategoryForm(forms.Form):
    name = forms.CharField()

class LowercaseEmailField(forms.EmailField):

    def clean(self, value):
        value = super(LowercaseEmailField, self).clean(value)
        return value.lower()
    
class ShareBlogForm(forms.Form):
    email = LowercaseEmailField(required=True)