from django.shortcuts import render
from homepage.forms import InputForm
from homepage.models import UserInput
import subprocess

# used https://www.youtube.com/watch?v=2Fp1N6dof0Y as refernce
# got help from Drew Radcliff, and Matt SE Facilitator
def index_view(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            output = subprocess.run(['cowsay', '{}'.format(data.get('text'))], capture_output=True, text=True)
            UserInput.objects.create(
                text = data.get('text')
            )  
            form = InputForm()
            return render(request, 'index.html', {'form': form, 'output': output.stdout})
    form = InputForm()
    return render(request, 'index.html', {'form': form})

def most_recent(request):
    most_recent = UserInput.objects.all()
    return render(request, 'history.html', {'most_recent': most_recent})