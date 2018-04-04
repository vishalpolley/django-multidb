from django.shortcuts import render

from .forms import TestForm2

def main2(request):
	form = TestForm2(request.POST or None)
	if request.method == 'POST':
		instance = form.save(commit = False)
		print(instance.father_name, instance.mother_name)
		if form.is_valid():
			form.save()
			print(form.cleaned_data.get("father_name"))
			print(form.cleaned_data.get("mother_name"))

	return render(request, "form2.html", {"form": form})