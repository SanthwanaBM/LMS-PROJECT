from django.urls import path

from.import views

urlpatterns=[

    path('courses-list/',views.coursesListView.as_view(),name='courses-list'),

    path('course-details/<str:uuid>/',views.CoursesDetailView.as_view(),name='course-details'),
    
    path('home/',views.HomeView.as_view(),name='home'),

    path('instrutor-courses-list/',views.InstructorCourseListView.as_view(),name='instructor-courses-list'),
    path('create-course/',views.CourseCreateView.as_view(),name='create-course'),
    path('instructor-course-details/<str:uuid>/',views.InstructorCoursesDetailView.as_view(),name='instructor-course-details'),
    path('instructor-course-delete/<str:uuid>/',views.InstructorCoursesDeleteView.as_view(),name='instructor-course-delete'),
    path('instructor-course-update/<str:uuid>/',views.InstructorCoursesUpdateView.as_view(),name='instructor-course-update'),
    
]
