from django.contrib.messages import get_messages
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from . forms import CustomRegistrationForm, LoginForm, ContactForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from .models import CustomUser,FriendRequest
from datetime import date
from django.db.models import Q


def register_view(request):
  if request.method == "POST":
    form = CustomRegistrationForm(request.POST, request.FILES)
    if form.is_valid():
      user = form.save(commit = False)
      user.set_password(form.cleaned_data['password'])
      user.save()
      return redirect('login')

    else:
      form =CustomRegistrationForm()
      return render(request, 'registration/register.html',{'form' : form})
  else:
    form = CustomRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
  if request.method == "POST":
    form = LoginForm(data = request.POST)
    if form.is_valid():
      user = form.get_user()
      login(request, user)
      return redirect('/')
  else:
    form = LoginForm()
    return render(request, 'registration/login.html', {'form' : form})

def logout_view(request):
  logout(request)
  return redirect('login')

def index(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())

def about(request):
  template = loader.get_template('about.html')
  return HttpResponse(template.render())

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')  # Replace with the name of your contact page
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def story(request):
  template = loader.get_template('stories.html')
  return HttpResponse(template.render())

def story_details(request):
  template = loader.get_template('story_details.html')
  return HttpResponse(template.render())

def members(request):
  today = date.today()
  gender = ''
  if request.user.is_authenticated:
    if request.user.gender == "Male":
      gender = "Female"
    else:
      gender = "Male"
    users = CustomUser.objects.filter(is_staff=False, is_superuser=False, gender=gender)
  else:
    users = CustomUser.objects.filter(is_staff=False, is_superuser=False)


  for user in users:
    if user.dob:
      today = date.today()
      user.age = today.year - user.dob.year - ((today.month, today.day) < (user.dob.month, user.dob.day))
    else:
      user.age = None

  context = {
    'users' : users,
    'today' : today
  }
  return render(request, 'members.html', context)

@login_required
def my_profile(request):

  user = request.user
  if user.dob:
    today = date.today()
    user.age = today.year - user.dob.year - ((today.month, today.day) < (user.dob.month, user.dob.day))
  else:
    user.age = None

  received_request = FriendRequest.objects.filter(receiver=request.user, status='pending')
  received_requests = [fr.sender for fr in received_request]

  sent_request = FriendRequest.objects.filter(sender=request.user, status='pending')
  sent_requests = [fr.receiver for fr in sent_request]

  friends_list = FriendRequest.objects.filter(Q(sender=request.user) | Q(receiver=request.user), status='accepted')

  accepted_users = []
  for fr in friends_list:
      if fr.sender == request.user:
          accepted_users.append(fr.receiver)
      else:
          accepted_users.append(fr.sender)


  # accepted_users = [fr.receiver for fr in friends_list]


  context = {
    'user': user,
    'received_requests': received_requests,
    'sent_requests': sent_requests,
    'friends_list' : accepted_users,
  }
  return render(request, 'my_profile.html', context)

@login_required
def send_friend_request(request, receiver_id):
  if receiver_id == request.user.id:
    return redirect('members')
  else:
    receiver = get_object_or_404(CustomUser, id=receiver_id)
    friend_request, created = FriendRequest.objects.get_or_create(
      sender=request.user,
      receiver=receiver
    )
    messages.success(request, 'Friend Request send successfully!')
    if not created:
        # Friend request already exists
      return redirect('my_profile')

    return redirect('my_profile')

@login_required
def respond_to_friend_request(request, request_id, action):
  friend_request = get_object_or_404(FriendRequest, id=request_id)

  if action == 'accept':
    friend_request.status = 'accepted'
    friend_request.save()

    messages.success(request, 'Friend Request accepted successfully!')
      # Additional logic: Add the sender and receiver as friends if needed

  elif action == 'reject':
    friend_request.status = 'rejected'
    friend_request.save()

    messages.success(request, 'Friend Request rejected successfully!')

  return redirect('my_profile')


