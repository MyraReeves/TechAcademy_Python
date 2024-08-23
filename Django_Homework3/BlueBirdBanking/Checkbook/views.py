from django.shortcuts import render, redirect, get_object_or_404
from .forms import AccountForm, TransactionForm
from .models import Account, Transaction


# Create your views here.
def home(request):
    form = TransactionForm(data=request.POST or None)
    if request.method == 'POST':
        # Retrieve which account the user wants to view...
        pk = request.POST['account']
        # ...and call the balance function to render that primary key's Balance Sheet
        return balance(request, pk)
    else:
        return render(request, 'checkbook/index.html', {'form': form})


def create_account(request):
    form = AccountForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print(form.errors)
    else:
        # Save the content as a dictionary onto the AccountForm template and add the content of the form to the page:
        content = {'form': form}
        return render(request, 'checkbook/CreateNewAccount.html', content)


def balance(request):
    return render(request, 'checkbook/BalanceSheet.html')


def transaction(request):
    form = TransactionForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print(form.errors)
    else:
        return render(request, 'checkbook/AddTransaction.html', {'form': form})
