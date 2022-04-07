from django.db import models
from account.models import SalesContact
from django.core.validators import RegexValidator

class Client(models.Model):
    sales_contact = models.ForeignKey(SalesContact, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=70, blank=True, unique=True)
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phoneNumber = models.CharField(validators=[phoneNumberRegex], max_length=16, unique=True)
    mobile = models.CharField(max_length=10) # Here
    company_name = models.CharField(max_length=70, blank=True)
    created_date = models.DateField(auto_now=True)
    update_date = models.DateField(auto_now=True)
    def __str__(self):
        return self.company_name

class Contract(models.Model):
    sales_contact = models.ForeignKey(SalesContact, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now=True)
    update_date = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True) # not clear how to set it. internet recherche is request
    amount = models.DecimalField(max_digits=20, decimal_places=2) # request internet recherche to set between bracket value
    payment_due = models.DateField()

    def __str__(self):
        return str(self.client) + " contrat N°:  {}".format(self.id)

"""
Business owner: who owns this contract commercially
Legal owner: who owns this contract in the legal team
Reference number
Counterparty
Contract type
Approval 1, 2, 3 (etc): this reflects each key stakeholder's sign-off
Status: fully signed, approved, draft, and so on
Buy-side or sell-side
Total value
Annualized value
Duration (years)
Termination date
Give notice date
Liability cap
Personal data: yes/no as to whether the contract contains personal data
Jurisdiction
Notes: for example, whether termination is planned at the end of the term

"""






