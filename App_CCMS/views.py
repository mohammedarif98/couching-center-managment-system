from distutils.log import error
import os
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import *

# Create your views here.

'''-----------to load home page-------------'''
# @login_required(login_url='SignIn_Page')
def Index(request):
    # if request.user.is_authenticated:                  # is authenticated method
    #     return render(request,'user/index.html')      
    return render(request,'user/index.html')

'''-----------to load admin home page-------------'''
def Admin_Home(request):
    # if not request.user.is_staff:
    #     return redirect('SignIn_Page')
    return render(request,'admin/adminhome.html')

'''-----------to load signup page-------------'''
def SignUp_Page(request):
    return render(request,'user/signup.html')

'''-----------to load login page-------------'''
def SignIn_Page(request):
    return render(request,'user/signin.html')

'''---------- user registration ----------'''
def Registration(request):
    if request.method=='POST':
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        gender=request.POST['gender']
        password=request.POST['password']
        confirm_password=request.POST['confirmpassword']
        address=request.POST['address']
        contact=request.POST['contact']
        # if request.FILES.get('photo') is not None:
        photo=request.FILES.get('photo')
        # else:
        #     photo="static/images/download.png"
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'This Username Already Exists!')
                return redirect('SignUp_Page')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'This Email Already Exists!')
                return redirect('SignUp_Page')
            else:
                user=User.objects.create_user(first_name=fname,last_name=lname,email=email,username=username,password=password)
                user.save()
                messages.success(request, 'SuccessFully Registered')
                print("Successed...")

                user_data=User.objects.get(id=user.id)
                ext_user_data=User_Registration_Model(User_Gender=gender,User_Photo=photo,User_Address=address,User_Contact=contact,User_Forgn=user_data)
                ext_user_data.save()
                messages.success(request, 'SuccessFully Registered')
                print('success..')
                return redirect('SignIn_Page')

    # return render(request,'user/signup.html')
        else:
            # messages.info(request, 'Password doesnt match !')
            return redirect('SignUp_Page') 
            print("Password is not Matching.. ") 
        return redirect('User_Login')
    else:
        # return render(request,'user/signup.html')
        return redirect('SignUp_Page')


'''-------------user login functionality--------'''    
def User_Login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            if user.is_staff:
                return redirect('Admin_Home')
                print("admin logged")
            else:
                login(request,user)
                auth.login(request,user)
                return redirect('Index')
                print("user logged")
        else:
            return redirect('User_Login')
            print("incorrect")
    else:
        return redirect('Index')
        print("no")

'''----------user logout function----------'''
def User_Logout(request):
    # request.session['uid']=""             # session id method
    if request.user.is_authenticated:     # is authenticated method
        auth.logout(request)
    return redirect('Index')

'''-----------profile page------------'''
@login_required(login_url='SignIn_Page')
def Profile(request):
    users=User_Registration_Model.objects.get(User_Forgn=request.user)
    context={"users":users}
    return render(request,'user/profile.html',context)


'''---------profile edit page----------'''
def Edit_Page(request):
    user_data=User_Registration_Model.objects.get(User_Forgn=request.user)
    context={'edit':user_data}
    return render(request,"user/editprofile.html",context)

'''---------------profile editing function----------'''

def Edit_Profile(request):
    if request.method == 'POST':
        user_data=User_Registration_Model.objects.get(User_Forgn=request.user)
        user_data.User_Forgn.first_name=request.POST['firstname']
        user_data.User_Forgn.last_name=request.POST['lastname']
        user_data.User_Forgn.username=request.POST['username']
        user_data.User_Forgn.email=request.POST['email']
        user_data.User_Gender=request.POST['gender']
        user_data.User_Address=request.POST['address']
        user_data.User_Contact=request.POST['contact']
    
        # if request.method == "POST":
            # if len(request.FILES) != 0:
            #     if len(user_data.User_Photo) > 0:
            #         os.remove(user_data.User_Photo.path)
        user_data.User_Photo = request.FILES['photo']

        user_data.save()
        user_data.User_Forgn.save()
        return redirect('Profile')

'''-------------user detail in admin home----------'''
def User_Detail(request):
    # if not request.user.is_staff:
    #     return redirect('SignIn_Page')
    user_detail = User_Registration_Model.objects.all()
    return render(request,'admin/userdetail.html',{'user':user_detail})

'''------delete user in admin-------'''
def Delete_User(request,id):
    # if not request.user.is_staff:
    #     return redirect('SignIn_Page')
    user = User_Registration_Model.objects.get(id=id)
    user.delete()
    return redirect('User_Detail')

'''----------course adding page-------------'''
def Course_Add_Page(request):
     return render(request,'admin/addcourse.html')


'''-----------course adding function-------------'''
def Add_Course(request):
    if request.method == 'POST':
        cname=request.POST['coursename']
        cfee=request.POST['coursefee']
        cabout=request.POST['courseabout']
        cduration=request.POST['courseduration']
        cimage=request.FILES['bgimage']

        data=Course_Model(Course_Name=cname,Course_Fee=cfee,About_Course=cabout,Duration=cduration,BG_Image=cimage)
        data.save()
        return redirect('Admin_Home')



'''----------- course details showing -----------'''
def Course_Detail(request):
    #  if not request.user.is_staff:
    #     return redirect('SignIn_Page')
    course= Course_Model.objects.all()
    return render(request,'admin/coursedetail.html',{'cdata':course})


'''---------- course display in homepages -------------'''
# @login_required(login_url='SignIn_Page')
def Display_Course(request):
    # if request.user.is_authenticated:                  # is authenticated method
    #     return render(request,'Index.html')
    display = Course_Model.objects.all()
    return render(request,'user/displaycourse.html',{'course':display})


'''------delete course in admin-------'''
def Delete_Course(pk):
    # if not request.user.is_staff:
    #     return redirect('SignIn_Page')
    course = Course_Model.objects.get(id=pk)
    course.delete()
    return redirect('Course_Detail')

'''------- edit course details --------'''
def Course_Edit(request,pk):
    if request.method=='POST':
        course=Course_Model.objects.get(id=pk)
        course.Course_Name=request.POST['cname']
        course.Course_Fee=request.POST['cfee']
        course.About_Course=request.POST['cabout']
        course.Duration=request.POST['duration']
        course.BG_Image=request.FILES['bgimage']
        course.save()
        return redirect('Course_Detail')
    course=Course_Model.objects.get(id=pk)
    return render(request,'admin/editcourse.html',{'editcrs':course})


# def Course_Joining_Page(request):
#     courses=Course_Joining_Model.objects.all()
#     context={'courses':courses}
#     return render(request,'admin/crsjoining.html',context)

@login_required(login_url='SignIn_Page')
def Course_Joining(request,pk):
    crs_jng = Course_Model.objects.get(id=pk)
    # user = adduser_model.objects.get(user=request.user)
    data = Course_Joining_Model(Course_Joining_Forgn=crs_jng,User_Course_Joining_Forgn=request.user)
    data.save()
    return redirect('Index')

'''---------------------'''
def Teacher_Page(request):
    course=Course_Model.objects.all()
    context={'course':course}
    return render(request,'admin/addteacher.html',context)


'''-------------------'''
def Add_Teacher(request):
    if request.method == 'POST':
        Teacher_Name=request.POST['teachername']
        Teacher_Gender=request.POST['teachergender']
        Course=request.POST['coursename']

        crs_data=Course_Model.objects.get(id=Course)
        data = Teacher_Model(Name=Teacher_Name,Gender=Teacher_Gender,Teacher_Course_Name=crs_data)
        data.save()
        # messages.info(request, 'New User Added')
        return redirect('Admin_Home')

'''-------------Teacher detail in admin home----------'''
def Teacher_Detail(request):
    # if not request.user.is_staff:
    #     return redirect('SignIn_Page')
    teacher_detail = Teacher_Model.objects.all()
    return render(request,'admin/teacherdetail.html',{'teacher':teacher_detail})

'''--------- delete teacher ----------'''
def Delete_Teacher(request,pk):
    # if not request.user.is_staff:
    #     return redirect('SignIn_Page')
    teacher=Teacher_Model.objects.get(id=pk)
    teacher.delete()
    return redirect('Teacher_Detail')


'''----------- course note adding page --------'''
def Course_Note_Page(request):
    # if not request.user.is_staff:
    #     return redirect('SignIn_Page')
    course=Course_Model.objects.all()
    context={'cdata':course}
    return render(request,'admin/coursenote.html',context)


'''--------- Course note adding function ----------'''
def Add_Course_Note(request):
    if request.method=='POST':
        cnote_discription=request.POST['discription']
        cnote_image=request.FILES['bgimage']
        cnote_pdf=request.FILES['pdfnote']
        cnote_select=request.POST['select']
        courses=Course_Model.objects.get(id=cnote_select)
        crs_note = Course_Notes_Model(Course_Discription=cnote_discription,Bg_Image=cnote_image,PDF_Note=cnote_pdf,Course_Forgn=courses)
        crs_note.save()
        return redirect('Note_Detail')


'''----------- note details showing in admin -----------'''
def Note_Detail(request):
 
    product= Course_Notes_Model.objects.all()
    return render(request,'admin/notesdeatil.html',{'ndata':product})


'''---------- note display in user account -------------'''
# @login_required(login_url='SignIn_Page')
def Display_Note(request):
    # if request.user.is_authenticated:                  # is authenticated method
    #     return render(request,'Index.html')
    display = Course_Notes_Model.objects.all()
    # teacher= TeacherModel.objects.all()
    return render(request,'user/displaynote.html',{'crsnote':display})

'''--------- delete notes  ---------------'''

def Delete_Note(request,pk):
    if not request.user.is_staff:
        return redirect('Login_SignUp_Page')
    user = Course_Notes_Model.objects.get(id=pk)
    user.delete()
    return redirect('Note_Detail')

'''-------- edit Notes-------------'''

def Edit_Note(request,pk):
    if request.method=='POST':
        notes = Course_Notes_Model.objects.get(id=pk)
        notes.Course_Discription=request.POST['discription']
        notes.Bg_Image=request.FILES['bgimage']
        notes.PDF_Note=request.FILES['pdfnote']
    
        notes.save()
        return redirect('Note_Detail')
    notes=Course_Notes_Model.objects.get(id=pk)
    return render(request,'admin/editnote.html',{'editnotes':notes})


'''---------- course notes -----------------'''
# @login_required(login_url='SignIn_Page')
def Personal_Note(request): 
    try:
        userdata=User_Registration_Model.objects.get(User_Forgn=request.user)
        jcrs=Course_Joining_Model.objects.get(User_Course_Joining_Forgn=request.user)
        user_Note=Course_Notes_Model.objects.get(Course_Forgn=jcrs.Course_Joining_Forgn)
        context={'ndata':user_Note} 
    except:
        return HttpResponse(" YOU HAVE JOIN ONLY ONE COURSE AT A TIME.THANK YOU ")
    # return render(request,'user/personalnote.html',context)

    if userdata.status=='approve':
        return render(request,'user/personalnote.html',context)
    else:
        return HttpResponse(" Currently No Notes Are Available ")


'''----------------'''
def Permision(request,pk):
    user=User_Registration_Model.objects.get(id=pk)
    context={'user':user}
    return render(request,'admin/userpermision.html',context)


'''-----------------------'''
def edit_User_status(request,pk):
    if request.method == 'POST':
        member=User_Registration_Model.objects.get(id=pk)
        member.status=request.POST['status']
        member.save()
        return redirect('User_Detail')
