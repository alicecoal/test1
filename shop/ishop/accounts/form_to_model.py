def get_user_from_form(form):
    user = form.save()
    user.refresh_from_db()
    user.profile.first_name = form.cleaned_data.get('first_name')
    user.profile.last_name = form.cleaned_data.get('last_name')
    user.profile.email = form.cleaned_data.get('email')
    user.profile.age = form.cleaned_data.get('age')
    user.profile.country = form.cleaned_data.get('country')
    user.profile.level = 0
    user.is_active = False
    user.profile.is_seller = False
    user.save()
    return user
