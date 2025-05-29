from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect

# Create your views here.

from django.views import View

from student.forms import ProfileForm


from .forms import  InstructorForm

from django.contrib.auth.hashers import make_password

from django.db import transaction

from lms.utility import send_email

import threading



class InstructorRegisterView(View):

    def get(self,request,*args,**kwargs):

        profile_form = ProfileForm()

        instructor_form = InstructorForm()

        data = {'profile_form' : profile_form,'instructor_form':instructor_form}

        return render(request,'instructor/instructor-register.html',context=data)
    

    def post(self,request,*args,**kwargs):

        profile_form =  ProfileForm(request.POST)

        instructor_form = InstructorForm(request.POST,request.FILES)

        print(profile_form.errors)
        print(instructor_form.errors)

        if profile_form.is_valid():

            with transaction.atomic():
                profile = profile_form.save(commit= False)

                email = profile_form.cleaned_data.get('email')

                password = profile_form.cleaned_data.get('password')

                profile.username =email

                profile.role = 'instructor'

                profile.password= make_password(password)

                profile.save()

                if instructor_form.is_valid():

                  instructor = instructor_form.save(commit=False)

                  instructor.Profile = profile

                  instructor.name = f'{profile.first_name} {profile.last_name} '

                  instructor.save()

                  subject = 'succesfully registered'

                  receipient = instructor.Profile.email

                  template = 'email/sucess-registerion.html'

                  context = {'name':instructor.name,'username':instructor.Profile.email,'password':password }

                #   thread = threading.Thread(target=send_email,args=(subject,receipient,template,context))

                #   thread.start()

                  send_email(subject,receipient,template,context)


                  return redirect('login')
            

        data ={'profile_form':profile_form,'instructor_form':instructor_form}

        return render(request,'instructor/instructor-register.html',context=data)    



