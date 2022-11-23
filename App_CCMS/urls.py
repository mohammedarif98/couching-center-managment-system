from App_CCMS import views
from django.urls import path

urlpatterns=[
    path("",views.Index,name="Index"),
    path('Admin_Home',views.Admin_Home,name="Admin_Home"),
    path('SignUp_Page',views.SignUp_Page,name="SignUp_Page"),
    path('SignIn_Page',views.SignIn_Page,name="SignIn_Page"),
    path('Registration',views.Registration,name='Registration'),
    path('User_Login',views.User_Login,name='User_Login'),
    path('User_Logout',views.User_Logout,name='User_Logout'),
    path('Profile',views.Profile,name='Profile'),
    path("Edit_Page",views.Edit_Page,name='Edit_Page'),
    path('Edit_Profile',views.Edit_Profile,name="Edit_Profile"),
    path('User_Detail',views.User_Detail,name='User_Detail'),
    path('Delete_User/<int:id>',views.Delete_User,name="Delete_User"),
    path('Course_Add_Page',views.Course_Add_Page,name='Course_Add_Page'),
    path('Add_Course',views.Add_Course,name='Add_Course'),
    path('Course_Detail',views.Course_Detail,name='Course_Detail'),
    path('Display_Course',views.Display_Course,name="Display_Course"),
    path('Delete_Course/<int:pk>',views.Delete_Course,name="Delete_Course"),
    path('Course_Edit/<int:pk>',views.Course_Edit,name="Course_Edit"),
    path('Course_Joining/<int:pk>',views.Course_Joining,name="Course_Joining"),
    path('Teacher_Page',views.Teacher_Page,name="Teacher_Page"),
    path('Add_Teacher',views.Add_Teacher,name="Add_Teacher") ,
    path('Teacher_Detail',views.Teacher_Detail,name='Teacher_Detail'),
    path('Delete_Teacher/<int:pk>',views.Delete_Teacher,name="Delete_Teacher"),
    path('Course_Note_Page',views.Course_Note_Page,name="Course_Note_Page"),
    path('Add_Course_Note',views.Add_Course_Note,name="Add_Course_Note"),
    path('Note_Detail',views.Note_Detail,name='Note_Detail'),
    path('Display_Note',views.Display_Note,name='Display_Note'),
    path('Delete_Note/<int:pk>',views.Delete_Note,name="Delete_Note"),
    path('Edit_Note/<int:pk>',views.Edit_Note,name='Edit_Note'),
    path('Personal_Note',views.Personal_Note,name='Personal_Note'),
    path('Permision/<int:pk>',views.Permision,name="Permision"),
    path('edit_User_status/<int:pk>',views.edit_User_status,name="edit_User_status"),
   




]