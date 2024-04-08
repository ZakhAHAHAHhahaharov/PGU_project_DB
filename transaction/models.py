from django.db import models
from django.contrib.auth.models import AbstractUser


class Transactions(models.Model):

    pass


class Client(AbstractUser):
    type = models.IntegerField(
        choices=models.IntegerChoices(
            "ClientType", "JURIDICAL PHYSICAL"
        ))


class PassportData(models.Model):
    user = models.OneToOneField(Client, on_delete=models.CASCADE)
    passport_series = models.CharField(max_length=4)
    passport_number = models.CharField(max_length=6)
    issue_date = models.DateField()
    department_code = models.CharField(max_length=6)
    issued_by = models.CharField(max_length=100)
    birth_date = models.DateField()
    gender = models.BooleanField(default=False)
    birth_place = models.CharField(max_length=100)


class ClientAccounts(models.Model):
    # type = models.Choi
    type = models.IntegerField(
        choices=models.IntegerChoices(
            "AccountType", "SALARY VALUTE CAMULATIVE"
        )
    )
    # client = models.ForeignKey(Client, on_delete=models.SET_NULL)
    balance = models.DecimalField(
        verbose_name="Balance",
        default=0
    )


class Comissions(models.Model):
    pass


class PartnerBanks(models.Model):
    bank_name = models.CharField(max_length=100, default="Bank Name")
    bank_country = models.CharField(max_length=100, default="Bank Country")
    type = models.IntegerField(
        choices=models.IntegerChoices(
            "PartnerBankType", "Foreign Local"
        )
    )

