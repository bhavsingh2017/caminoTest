from django.shortcuts import render, render_to_response, HttpResponseRedirect
from django.http import HttpResponseRedirect
from django.template import RequestContext
from .forms import LoanForm
from .models import Loan

# Create your views here.
status = "Your application is currently being processed";

def index(request):
    if request.method == 'POST':
        form = LoanForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print("form is valid!")
            ##we can do the logic here##
        if(form.cleaned_data["years"]<1 and form.cleaned_data["amount"]>=50000):
            status="We regret to inform you that your financial applicaition has been denied.";
        elif (form.cleaned_data["years"]>=1 and form.cleaned_data["amount"]<50000):
            status="Congrats your financial applicaition has been pre-approved!";
        else:
            status="Your application is currently being processed!";
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
        name = form.cleaned_data["name"];
        years = form.cleaned_data["years"];
        amount = form.cleaned_data["amount"];
        business = form.cleaned_data["business"];
        loan = Loan(my_field_name=name, amount=amount, years=years, business=business);
        loan.save();

        print("the status is", status)
        request.session['status'] = status;
        context = {'status': status};
        return HttpResponseRedirect('thank-you', context)
    # if a GET (or any other method) we'll create a blank form
    else:
    	form = LoanForm()
    return render(request, 'index.html', {'form': form})

def thankyou(request):
    status = request.session['status'];
    context = {'status': status};
    return render(request, 'thankyou.html', context);
