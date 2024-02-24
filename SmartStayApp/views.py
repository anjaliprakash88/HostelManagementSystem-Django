from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, logout
from django.contrib import auth, messages
from django.contrib.auth.hashers import make_password
from .models import User, Location, Hostel, Room, Student
from .forms import StudentForm
from django.http import HttpResponse


def login_form(request):
    return render(request, 'login.html')


def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            if user.is_staff or user.is_superuser:
                return redirect('admin1')
            elif user.is_warden:
                return redirect('warden')
            else:
                return redirect('student')
        else:
            # messages.info(request, "Invalid username or password")
            return redirect('home')


def register_form(request):
    return render(request, 'register.html')


def registerView(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password = make_password(password)
        a = User(username=username, email=email, password=password)
        a.save()
        # messages.success(request, "account created successfully")
        return redirect('home')
    else:
        # messages.error(request, "registration failed. try again")
        return redirect('regform')


def logoutView(request):
    logout(request)
    return redirect('home')


def student(request):
    location = Location.objects.all()
    return render(request, 'student/home.html', {'loc': location})


def hostel_view(request, location_id):
    location = get_object_or_404(Location, pk=location_id)
    hostels = Hostel.objects.filter(location=location)
    context = {'location': location, 'hostels': hostels}
    return render(request, 'student/hostel_view.html', context)


def booking_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.user = request.user
            student.save()
            return redirect('profile_view')  # Redirect to a success page or home page
    else:
        form = StudentForm()

    return render(request, 'student/booking_form.html', {'form': form})


def hostel_room_list(request, hostel_id):
    hostel = get_object_or_404(Hostel, pk=hostel_id)
    rooms = Room.objects.filter(hostel=hostel, is_available=True)
    return render(request, 'student/room_list.html', {'hostel': hostel, 'rooms': rooms})


def book_room(request, room_id):
    room = get_object_or_404(Room, pk=room_id)

    if room.is_available:
        # Use select_for_update to lock the row for update
        room = Room.objects.select_for_update().get(pk=room_id)

        # Double-check availability in case another user booked it just before the lock
        if room.is_available:
            # Update availability status
            room.is_available = False
            room.save()
            return HttpResponse(f'Room {room.room_number} booked successfully!')
        else:
            return HttpResponse('Room not available for booking.')
    else:
        return HttpResponse('Room not available for booking.')





def warden(request):
    return render(request, 'warden/home.html')


def admin1(request):
    return render(request, 'admin/home.html')
