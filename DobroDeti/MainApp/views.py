from django.shortcuts import render
from django.views.generic import View


class BaseView(View):
    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, 'base.html', context)

# @login_required
# def profileup(request):
#     if request.method == 'POST':
#         form = UpdateInfoForm(request.POST, request.FILES, instance=request.user)
#         if form.is_valid():
#             form.save()
#             messages.add_message(request, messages.SUCCESS,  f'Ваша информация была обновлена')
#             return redirect('profile')
#     else:
#         form = UpdateInfoForm(instance=request.user)
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'profile_edit.html', context)
# форма
# class UpdateInfoForm(forms.ModelForm):
#
#
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'username', 'email', 'phone', 'address', 'profile_pic']
