from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm, UserUpdateForm, ProfileImagesForm
from django.contrib import messages # Через этот кдласс можем создавать разные сообщения для пользователя
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == "POST": # Получаем данные от позователя
        form = UserRegisterForm(request.POST) # Хранятся все данные полученные от позователя
        if form.is_valid(): # Проверка данных полученных о пользователя
            form.save() # Регестрируем полььзоваеля в базе данных
            username = form.cleaned_data.get('username') # Получаем данные с поля username
            messages.success(request, f'Ползователь {username} был успешно создан')
            return redirect('home') # Перебрасываем порльзователя на главную страницу после регистрации
    else:
        form = UserRegisterForm()

    return render(
        request,
        'users/register.html',
    {
        'title': 'Страница регистрации',
        'form': form
    }
)

@login_required
def profile(request):
    if request.method == 'POST':
        profileForm = ProfileImagesForm(request.POST, request.FILES, instance=request.user.profile)
        apdateUserForm = UserUpdateForm(request.POST, instance=request.user)

        if profileForm.is_valid() and apdateUserForm.is_valid():
            apdateUserForm.save()
            profileForm.save()
            messages.success(request, f'Ваш аккаунт был успешно обновлён')
            return redirect('profile')
    else:
        profileForm = ProfileImagesForm(instance=request.user.profile)
        apdateUserForm = UserUpdateForm(instance=request.user)

    data = {
        'profileForm': profileForm,
        'apdateUserForm': apdateUserForm
    }

    return render(request, 'users/profile.html', data)
