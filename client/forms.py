from django.forms import ModelForm
from .models import *

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'company_name','job_title','personal_contact','company_contact',
                  'email','location','address','product_name','product_category','product_price']
class personalInfoForm(ModelForm):
    class Meta:
        model = Client
        fields = ['name','company_name','location','job_title','personal_contact']

class companyInfoForm(ModelForm):
    class Meta:
        model = Client
        fields = ['company_name','product_category','company_contact','company_contact','location','address','company_website','email']

class profilepicForm(ModelForm):
    class Meta:
        model = Client
        fields = ['personal_image','company_image']