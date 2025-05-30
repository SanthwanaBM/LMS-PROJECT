from django.shortcuts import render

from django.views import View

from courses.models import Courses

# Create your views here.

class EntrollConfirmationView(View):

    def get(self,request,*args,**kwargs):

        uuid = kwargs.get('uuid')

        course = Courses.objects.get(uuid=uuid)

        data = {'course':course}
        
        return render(request,'payments/entroll-confirmation.html',context=data) 

