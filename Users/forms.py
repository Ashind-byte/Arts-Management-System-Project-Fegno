from django.contrib.auth.forms import UserCreationForm


from Users.models import users


class UserForm(UserCreationForm):
    class Meta:
        model = users
        fields = ['username','email','first_name','last_name','password1','password2','gender',]


