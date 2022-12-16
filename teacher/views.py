from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
import smtplib,secrets,string
from branch.models import branch_detail, branch_subjects
from erp.models import subjects
from student.models import studentlogin
from attendance.models import mark_attendance
from .models import teacherlogin
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from erp.settings import password,sender


branch=None


def index(request):
	if request.user.is_active and request.user.groups.filter(name="teacher").exists():
		return render(request, 'dash1.html', {})
	else:
		return render(request,'login.html')

def login(request):
	if request.user.is_authenticated and request.user.groups.filter(name="teacher").exists():
		return render(request, 'dash1.html', {})
	elif request.method == 'POST':
		username = request.POST.get('teacherid')
		password = request.POST.get('teacherpwd')
		try:
			user = teacherlogin.teach_obj.get(teacherid=username,teacherpwd=password)
			# print(user)
			user2 = authenticate(request, username=username, password=password)
			if user is not None:
				auth_login(request,user2)
				return render(request, 'dash1.html', {})
			else:
				messages.error(request, 'Invalid Credentials')
				print("Someone tried to login and failed.")
				print("They used username: {} and password: {}".format(username,password))
				return redirect('/')
		except Exception as identifier:
			messages.error(request, 'Invalid Credentials')
			print("******\n",identifier,1,"\n******",39)
			return redirect('/teacher')
	
	else:
		return render(request,'login.html')

def coordinatorlogin(request):
	if request.user.is_authenticated and request.user.groups.filter(name="teacher").exists():
		return render(request, 'dash1.html', {})
	elif request.method == 'POST':
		username = request.POST.get('teacherid')
		password = request.POST.get('teacherpwd')
		try:
			user = teacherlogin.teach_obj.get(teacherid=username,teacherpwd=password)
			user2 = authenticate(request, username=username, password=password)
			if user is not None:
				global branch
				auth_login(request,user2)
				branch=teacherlogin.teach_obj.filter(teacherid=user)
				branch=branch[0].cc_of_branch
				if not branch:
					return redirect('/teacher')
				return render(request, 'dash1.html', {})
			else:
				print("Someone tried to login and failed.")
				messages.error(request, 'Invalid Credentials')
				print("They used username: {} and password: {}".format(username,password))
				return redirect('/')
		except Exception as identifier:
			messages.error(request, 'Invalid Credentials')
			return redirect('/teacher')
	else:
		return render(request,'login.html')

def logout(request):
	request.session.flush()
	auth_logout(request)
	return redirect('/teacher')

def timetable(request):
	global branch
	
	if request.user.is_authenticated and request.user.groups.filter(name="teacher").exists():
		branch_list=list(branch_detail.branch_obj.filter(department=teacherlogin.teach_obj.get(teacherid=request.user.username).department))
		if branch:
			# print(branch)
			subject_list=list(branch_subjects.branch_sub_obj.all())
			return render(request,'timetable.html',context={"branch_list":branch_list,"subject_list":subject_list})
		else:
			return render(request,'timetable.html',context={"branch_list":branch_list,"n":list(range(1,9))})
	else:
		return redirect('/teacher/login')

def update(request):
	if request.user.is_authenticated and request.user.groups.filter(name="teacher").exists():
		
	#print(branch,type(branch))
		if request.method=='POST':
			branch=request.POST.get("branch").split('-')
			branch=branch_detail.branch_obj.get(name=branch[0],batch=int(branch[1]))
			for i in ['mon','tues','wed','thurs','fri','sat']:
				for j in range(1,9):
					lecture_name=i+'_lec'+str(j)
					lecture_input=request.POST.get(lecture_name)
					# print(1,lecture_input,type(lecture_input))
					previous=getattr(branch,lecture_name)
					##print(lecture_input,previous)
					# print(2,previous,type(previous))
					# print(lecture_input,previous,type(lecture_input),11111111111111)
					if lecture_input=='':
						continue
					if lecture_input:
						lecture_input=lecture_input.split('-')
						subject_name=lecture_input[0]
						subject_name=subjects.sub_obj.get(subject_name=subject_name)
						subject_teacher=lecture_input[1]
						subject_teacher=teacherlogin.teach_obj.get(Name=subject_teacher)
						teacher_slot=getattr(subject_teacher,"teach_"+lecture_name)
						if teacher_slot and teacher_slot!=branch:
							raise Exception(subject_teacher.Name,"already occupied at",lecture_name)
						if previous and lecture_input!=previous:
							setattr(previous.subject_teacher,"teach_"+lecture_name,None)
							previous.subject_teacher.save()
							messages.info(request,"cleared {0} from {1} at slot {2}".format(branch,previous.subject_teacher.Name,lecture_name))
						setattr(subject_teacher,"teach_"+lecture_name,branch)
						
						subject_teacher.save()
						setattr(branch,lecture_name,branch_subjects.branch_sub_obj.get(subject_teacher=subject_teacher,branch_subject=subject_name))
						# print(1,subject_name,type(subject_name))
						# print(2,subject_teacher,type(subject_teacher))
					elif previous:
						setattr(previous.subject_teacher,"teach_"+lecture_name,None)
						previous.subject_teacher.save()
						setattr(branch,lecture_name,None)
					else:
						setattr(branch,lecture_name,None)
					branch.save()
					
					#messages.success(request,"Timetable Updated")
		print("****Success****")
		print(request.user,request.user.is_authenticated)
		return timetable(request)
	else:
		return redirect('/teacher/login')
from branch.forms import branch_subject_form
def subject(request):
	if request.user.is_authenticated and request.user.groups.filter(name="teacher").exists():
		if request.method=="POST":
			form=branch_subject_form(request.POST)
			if form.is_valid():
				form.save()
			request.method="GET"
			return subject(request)
		else:
			subject_list=list(branch_subjects.branch_sub_obj.all())
			current_dept=teacherlogin.teach_obj.get(teacherid=request.user.username).department
			for i in subject_list:
				if i.branch.department!=current_dept:
					subject_list.remove(i)
			form=branch_subject_form()
			return render(request,'subjects.html',context={"form":form,'branch_subject':subject_list})
	else:
		return redirect('/teacher/login')


def attendance(request):
	if request.user.is_authenticated and request.user.groups.filter(name="teacher").exists():
		branch_list=list(branch_detail.branch_obj.all())
		all_subjects=branch_subjects.branch_sub_obj.all()
		student={}
		for branch in branch_list:
			temp=User.objects.filter(groups__name=branch)
			for i in temp:
				student[branch]=student.get(branch,[])+[studentlogin.stud_obj.get(studentid=i)]
		print(student)
		return render(request,"attendance.html",context={'student':student,"all_subjects":all_subjects,"branch_list":branch_list})
	else:
		return redirect('/teacher/login')
def mark(request):
	if request.user.is_authenticated and request.user.groups.filter(name="teacher").exists():
		
		subject=subjects.sub_obj.get(subject_name=request.POST.get('subject_name'))
		date=request.POST.get('date')
		date=datetime.strptime(date,"%Y-%m-%d").date()
		branch=request.POST.get("branch")
		branch=User.objects.filter(groups__name=branch)
		if request.method=="POST":
			for i in branch:
				student=studentlogin.stud_obj.get(studentid=i)
				if student.studentid in request.POST:
					mark_attendance.attend_obj.create(student=student,subject=subject,present=True,date=date)
				else:
					mark_attendance.attend_obj.create(student=student,subject=subject,present=False,date=date)
		return attendance(request)
	else:
		return redirect('/teacher/login')

def about(request):
	if request.user.is_authenticated and request.user.groups.filter(name="teacher").exists():
		return render(request,"about.html",{})
	else:
		return redirect('/teacher/login')
def teachertimetable(request):
	if request.user.is_authenticated and request.user.groups.filter(name="teacher").exists():
		user = teacherlogin.teach_obj.get(teacherid=request.user.username)
		return render(request,"your-timetable.html",{"user":user})
	else:
		return redirect('/teacher/login')


def forget(request):
	return render(request,'forget-password.html')


def forgot_mail(request):
	try:
		if request.method=='POST':
			user=teacherlogin.teach_obj.get(email=request.POST.get('email'))

			letters = string.ascii_letters
			digits = string.digits
			special_chars = string.punctuation
			alphabet = letters + digits + special_chars
			pwd=''
			for _ in range(8):
				pwd += ''.join(secrets.choice(alphabet))
			setattr(user,'teacherpwd',pwd)
			# user2=User.objects.get(username=user.teacherid)
			# setattr(user2,'password',pwd)
			# user2.save()
			#for adding user to group
			user.save()
			#sending mails
			receiver=user.email
			user=user.Name
			user=user.title()
			email_body="Hello "+user+"\nYour password for erp portal is "+pwd+"\nThank you!"
			message=MIMEMultipart('alternative',None,[MIMEText(email_body,'text')])
			message['Subject']="Regarding ERP password"
			message['From']=sender
			message['To']=receiver
			try:
				server=smtplib.SMTP('smtp.gmail.com:587')
				server.ehlo()
				server.starttls()
				server.login(sender,password)
				server.sendmail(sender,receiver,message.as_string())
				server.quit()

			except:
				pass
		return index(request)
	except:
		messages.error(request, 'No user with this email found.')
		return forget(request)