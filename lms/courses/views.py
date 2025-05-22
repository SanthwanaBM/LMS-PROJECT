from django.shortcuts import render,redirect

# Create your views here.

from django.views import View

from .models import Courses,CategoryChoices,LevelChoices

from .forms import CourseCreateForm
from instructors.models import Instructors

from django.db.models import Q

from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator

from authentication.permissions import permission_role




# courses list and create
# @method_decorator(login_required(login_url='login'),name='dispatch')

class coursesListView(View):
    def get(self,request,*args,**kwargs):
        # fetching all courses from  courses model

        query = request.GET.get('query')

        courses =Courses.objects.all()


        if query:
             courses =Courses.objects.filter(Q(title__icontains=query)|
                                             Q(description__icontains=query)|
                                             Q(instructor__name__icontains=query)|
                                             Q(category__icontains=query)|
                                             Q(type__icontains=query)|
                                             Q(level__icontains=query)|
                                             Q(fees__icontains=query))
                                             


        print(query)

        

        data = {'courses':courses ,'page':'coursespage', 'query':query , 'value':query }

        return render(request,'courses/courses-list.html',context=data)

# @method_decorator(login_required(login_url='login'),name='dispatch')
# @method_decorator(permission_role(roles=['Instructor']),name='dispatch')

class HomeView(View):
        def get(self,request,*args,**kwargs):

            data= {'page' : 'home-page'}
               
            return render(request,'courses/home.html',context=data)
        

# @login_required (login_url='login') 
# @method_decorator(login_required(login_url='login'),name='dispatch')
@method_decorator(permission_role(roles=['Instructor']),name='dispatch')


class InstructorCourseListView(View):
     def get(self,request,*args,**kwargs):

          instructor=Instructors.objects.get(id=1)
          
          courses = Courses.objects.filter(instructor=instructor)
          
          data = {'page': 'instructor-courses-page','courses' : courses}
          return render(request,'courses/instructor-courses-list.html' ,context= data)        
     
# @method_decorator(login_required(login_url='login'),name='dispatch')

@method_decorator(permission_role(roles=['Instructor']),name='dispatch')


class InstructorCoursesDetailView(View):
     
     def get(self,request,*args,**kwargs):
          
          uuid =kwargs.get('uuid')

          course = Courses.objects.get(uuid=uuid)

          data = {'course': course}
          
          return render(request,'courses/instructor-course-details.html',context=data )        
     

@method_decorator(permission_role(roles=['Instructor']),name='dispatch')
     

class InstructorCoursesDeleteView(View):
     
     def get(self,request,*args,**kwargs):
          
          uuid =kwargs.get('uuid')

          course = Courses.objects.get(uuid=uuid)

          course.delete()
          return redirect('instructor-courses-list')
     

# @method_decorator(login_required(login_url='login'),name='dispatch')
@method_decorator(permission_role(roles=['Instructor']),name='dispatch')


class InstructorCoursesUpdateView(View):
     
     def get(self,request,*args,**kwargs):
          
          uuid = kwargs.get('uuid')

          course = Courses.objects.get(uuid=uuid)

          form = CourseCreateForm(instance=course)
          
          data = {'form':form}           

          return render(request,'courses/instructor-course-update.html', context= data)


     def post(self,request,*args,**kwargs):
           
           uuid = kwargs.get('uuid')

           course = Courses.objects.get(uuid=uuid)

           form = CourseCreateForm(request.POST,request.FILES,instance=course)

           if form.is_valid():
                
                form.save()
                
                return redirect('instructor-courses-list')
           
           data = {'form':form}

           return render(request,'courses/instructor-course-update.html', context= data)

           

          
     
           


# class CourseCreateView(View):

#      def get(self,request,*args,**kwargs):
          
#           data = {"categories":CategoryChoices,'levels': LevelChoices}
          
#           return render(request,'courses/course-create.html',context=data)    


#      def post(self,request,*args,**kwargs):
          
#           form_data = request.POST
#           image = request.FILES.get('image')
#           title = form_data.get('title')
#           description = form_data.get('description')
#           category = form_data.get('category')
#           level = form_data.get('level')
#           fees  = form_data.get('fee')
#           offer_fee = form_data.get('offer_fee')

#           instructor = 'jhon doe'

#           course=Courses.objects.create(title=title,description=description,image=image,
#                                         category=category,level=level,instructor=instructor,
#                                         fees=fees,offer_fee=offer_fee)
          
#           course.save() 
#           # print(title,image,title,description,category,level,fees,offer_fee)

#           return redirect('instrutor-courses-list')



# class CourseCreateView(View):

#      def get(self,request,*args,**kwargs):
          
#           data = {"categories":CategoryChoices,'levels': LevelChoices}
          
#           return render(request,'courses/course-create.html',context=data)    


#      def post(self,request,*args,**kwargs):
          
#           form_data = request.POST
#           image = request.FILES.get('image')
#           title = form_data.get('title')
#           description = form_data.get('description')
#           category = form_data.get('category')
#           level = form_data.get('level')
#           fees  = form_data.get('fee')
#           offer_fee = form_data.get('offer_fee')

#           instructor = 'jhon doe'

#           course=Courses.objects.create(title=title,description=description,image=image,
#                                         category=category,level=level,instructor=instructor,
#                                         fees=fees,offer_fee=offer_fee)
          
#           course.save() 
#           # print(title,image,title,description,category,level,fees,offer_fee)

#           return redirect('instrutor-courses-list')


   

   # with django form

# @method_decorator(login_required(login_url='login'),name='dispatch')
@method_decorator(permission_role(roles=['Instructor']),name='dispatch')


class CourseCreateView(View):

    def get(self, request):

        form = CourseCreateForm()
        data = {'form': form, }
        return render(request, 'courses/course-create.html',context=data)
    
    def post(self, request):

        form = CourseCreateForm(request.POST, request.FILES)

        instructor = Instructors.objects.get(id=1)
        
        if form.is_valid():

            course = form.save(commit=False)

            course.instructor = instructor

            course.save()

            return redirect('instructor-courses-list')
        

        data = {'form': form, }
        # If the form is not valid, render the form again with error messages


        return render(request, 'courses/course-create.html',context={'form': form})
#         # Redirect to the instructor courses page after creating the course
#         return redirect('instructor_courses')
#         return render(request, 'courses/courses-create.html',context={'form': form})



