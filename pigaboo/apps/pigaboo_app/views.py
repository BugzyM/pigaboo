from django.shortcuts import get_object_or_404, render_to_response, redirect, HttpResponseRedirect, render, RequestContext
from django.contrib.auth import authenticate, login
from pigaboo.apps.pigaboo_app.forms import AuthenticationForm, SignUp_Form , Chat_Form
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.views import password_reset, password_reset_confirm
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.context_processors import csrf
from .models import UserProfile
from .models import ChatMessage
from .models import ProfileInvites
from .forms import UploadFileForm

@csrf_exempt
def pg_login_user(request):
    login_form = AuthenticationForm(prefix="pg_lgn")
    form = SignUp_Form(prefix="pg_join")

    if request.POST:
        login_form = AuthenticationForm(request.POST, prefix="pg_lgn")

        if (request.POST.get("pg_lgn-username","_") != "_" and request.POST.get("pg_lgn-password","_") != "_"):
            if login_form.is_valid():
                username = login_form.cleaned_data["username"]
                password = login_form.cleaned_data["password"]
                user = authenticate(username=username, password=password)
                
                if user is not None:

                    UserProfile.objects.filter(user=user).update(status="online")
                    return render_to_response("index_chat.html",
                            locals(),
                            context_instance=RequestContext(request))
                else:
                    messages.error(request, 'Your login credentials are incorect.')
            
            elif (request.POST.get("pg_lgn-username","_") == "" or request.POST.get("pg_lgn-password","_") == ""):
                messages.error(request, 'We need both your email and password to log you in!')
                
            elif (request.POST.get("pg_lgn-username","_") == "" and request.POST.get("pg_lgn-password","_") != "_"):
                messages.error(request, 'What is your email address?')
 
            elif request.POST.get("pg_lgn-username","_") != "" and request.POST.get("pg_lgn-password","_") == "":
                email = request.POST.get('pg_lgn-username')
                try:
                    validate_email(email)
                except ValidationError:
                    messages.error(request, 'Your email address is invalid.')
            else:
                    messages.error(request, 'Your login credentials are incorect.')

    if request.POST:
        form = SignUp_Form(request.POST, prefix="pg_join")
        org = request.POST.get('org')

        if (request.POST.get("pg_lgn-username","_") == "_" and request.POST.get("pg_lgn-password","_") == "_"):
            email    = request.POST.get("pg_join-email","_")
            
            
            if form.is_valid():
                if not User.objects.filter(email=email).exists():
                    user = User.objects.create_user(
                    username = form.cleaned_data['email'],
                    first_name = form.cleaned_data['username'],
                    password = form.cleaned_data['confirm_password'],
                    email    = form.cleaned_data['email'])
                   
                    a = UserProfile(user=user, firstname=request.POST.get("pg_join-username"))
                    a.save()
                    
                    messages.success(request, 'Your account was successfully created.')
            
            elif (User.objects.filter(email=email).exists()):
                messages.error(request, "User '" + email + "' already exists!")
                    
            elif (request.POST.get("pg_lgn-username","_") == "_" and request.POST.get("pg_lgn-password","_") == "_"
            and request.POST.get("pg_join-username","_") == ""):
                messages.error(request, 'Please type in your First Name or Company Name')
                
            elif (request.POST.get("pg_lgn-username","_") == "_" and request.POST.get("pg_lgn-password","_") == "_"
            and request.POST.get("pg_join-email","_") == ""):
                messages.error(request,'What is your email address?')

            elif (request.POST.get("pg_lgn-username","_") == "_" and request.POST.get("pg_lgn-password","_") == "_"
            and (request.POST.get("pg_join-password","_") == "" or request.POST.get("pg_join-confirm_password","_") == "")):
                messages.error(request, 'Please enter and confirm your password.')
            
            elif (request.POST.get("pg_lgn-username","_") == "_" and request.POST.get("pg_lgn-password","_") == "_"
            and (request.POST.get("pg_join-password","_") != request.POST.get("pg_join-confirm_password","_"))):
                messages.error(request, 'Passwords MUST match!')
            
            elif (request.POST.get("pg_lgn-username","_") == "_" and request.POST.get("pg_lgn-password","_") == "_" and
              request.POST.get("pg_join-email","_") != ""):
               email = request.POST.get('pg_join-email')
               try:
                   validate_email(email)
               except ValidationError:
                   messages.error(request, "Please check your email address, it's invalid.")

    return render_to_response("pg_user_signup.html",
                            locals(),
                            context_instance=RequestContext(request))

@login_required   
def pg_account(request):
    user = User.objects.get(pk=request.user.id)
    pg_user_profile = UserProfile.objects.get(pk=1)
    chats_msg = ChatMessage.objects.reverse()
    profiles = UserProfile.objects.reverse()
    form = Chat_Form(prefix="pg_chat")
    if request.method == 'POST':
        if (request.POST.get("pg_chat-message","_") != "_") :
            a = ChatMessage(user = pg_user_profile, message = request.POST.get("pg_chat-message","_"))
            a.save()
        return render_to_response('index_chat.html',{'pg_user_profile':pg_user_profile},
                              context_instance=RequestContext(request))
    else:
        if (request.GET.get("invitee","_") != "_") :
            inviteeuser = User.objects.get(pk=request.GET.get("invitee","_"))
            a = ProfileInvites(profile=pg_user_profile,invitee=inviteeuser)
            try:
                a.save()
            except ValidationError:
                messages.error(request, "Please check your email address, it's invalid.")
        elif (request.GET.get("accept","_") != "_") :
            inviteeuser = User.objects.get(pk=request.GET.get("accept","_"))
            a = ProfileInvites.objects.get(invitee=inviteeuser)
            a.status = 'ACCEPT'
            try:
                a.save()
            except ValidationError:
                messages.error(request, "Please check your email address, it's invalid.")
        elif (request.GET.get("reject","_") != "_") :
            inviteeuser = User.objects.get(pk=request.GET.get("reject","_"))
            a = ProfileInvites.objects.get(invitee=inviteeuser)
            a.status = 'REJECT'
            try:
                a.save()
            except ValidationError:
                messages.error(request, "Please check your email address, it's invalid.")
        return render_to_response('index_chat.html',{'pg_user_profile':pg_user_profile,'chats_msg':chats_msg,'profiles':profiles},
                              context_instance=RequestContext(request))

    return render_to_response("index_chat.html",
                            locals(),
                            context_instance=RequestContext(request))

@login_required   
def pg_upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return render_to_response("pg_upload.html",
                            locals(),
                            context_instance=RequestContext(request))
    else:
        form = UploadFileForm()
        return render_to_response("pg_upload.html",
                            locals(),
                            context_instance=RequestContext(request))
    return render_to_response("pg_upload.html",
                            locals(),
                            context_instance=RequestContext(request))
