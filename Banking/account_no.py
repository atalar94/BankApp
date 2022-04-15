from .models import CustomUser
import random

def create_account_no():
    numbers = "1234567890"
    iban = ""
    for i in range(16):
        iban += random.choice(numbers)
    already_exists = [user.account_no for user in CustomUser.objects.all()]

    while iban in already_exists:
        iban = ""
        for i in range(16):
            iban += random.choice(numbers)
    return iban

