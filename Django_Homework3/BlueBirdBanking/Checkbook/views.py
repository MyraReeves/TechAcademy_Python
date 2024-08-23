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


def balance(request, pk):
    # Retrieve the requested account using its primary key:
    account = get_object_or_404(Account, pk=pk)

    # Retrieve all of that account's transactions:
    transactions = Transaction.object.filter(account=pk)

    # Start the value of a "current total" variable as being the value of the initial deposit reported
    current_total = account.initial_deposit

    # Create a dictionary to place transaction information into:
    table_contents = {}

    for t in transactions:
        # For deposits, add the amount to the current total and then add the transaction to the dictionary:
        if t.type == 'Deposit':
            current_total += t.amount
            table_contents.update({t: current_total})

        # For withdrawals, subtract the amount from the current total and then add the transaction to the dictionary:
        else:
            current_total -= t.amount
            table_contents.update({t: current_total})

    # Pass the account, transaction dictionary, and current total balance to the template, and then return the info:
    content = {'account': account, 'table_contents': table_contents, 'balance': current_total}
    return render(request, 'checkbook/BalanceSheet.html', content)


def transaction(request):
    form = TransactionForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            pk = request.POST['account']
            form.save()
            return balance(request, pk)
        else:
            print(form.errors)
    else:
        return render(request, 'checkbook/AddTransaction.html', {'form': form})
