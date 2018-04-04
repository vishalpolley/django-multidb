from django.shortcuts import render

from .forms import TestForm1

def main1(request):
	form = TestForm1(request.POST or None)
	if request.method == 'POST':
		instance = form.save(commit = False)
		print(instance.first_name, instance.last_name)
		if form.is_valid():
			form.save()
			print(form.cleaned_data.get("first_name"))
			print(form.cleaned_data.get("last_name"))

	return render(request, "form1.html", {"form": form})