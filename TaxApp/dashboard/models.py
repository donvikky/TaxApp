from django.db import models
from django.core.validators import RegexValidator


PHONE_REGEX = RegexValidator(
    regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")


class Payer(models.Model):
    MARITAL_STATUSE_CHOICES = (
        ('Single', 'Single'),
        ('Married', 'Married'),
    )
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    surname = models.CharField('Surname', max_length=75)
    firstname = models.CharField('First Name', max_length=75)
    othername = models.CharField('Other Name', max_length=75, null=True)
    maritalstatus = models.CharField(
        'Marital Status', max_length=20, choices=MARITAL_STATUSE_CHOICES)
    gender = models.CharField('Gender', max_length=20, choices=GENDER_CHOICES)
    dob = models.DateField('Date of Birth')
    jtbtin = models.CharField(
        'JTB TIN', max_length=10, unique=True, blank=True)
    # streetid = fk
    lgaoforigin = models.CharField('LGA', max_length=75)
    stateoforigin = models.CharField('State of Origin', max_length=75)
    nationality = models.CharField('Nationality', max_length=75)
    taxpayercompany = models.CharField('Company', max_length=150)
    occupation = models.CharField('Occupation', max_length=75)
    employstatus = models.CharField('Employment Status', max_length=20)
    phone = models.CharField('Phone', max_length=15, validators=[PHONE_REGEX])
    email = models.EmailField('Email')


class CorporatePayer(models.Model):
    COMPANY_SIZE_CHOICES = (
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
    )
    OWNERSHIP_TYPE_CHOICES = (
        ('Private Limited Company', 'Private Limited Company'),
        ('Public Limited Company', 'Public Limited Company'),
        ('Trusteeship', 'Trusteeship'),
        ('Companies Limited By Guarantee', 'Companies Limited By Guarantee'),
        ('Federal MDAs', 'Federal MDAs'),
        ('State MDAs', 'State MDAs'),
        ('Foreign/Non-resident Companies', 'Foreign/Non-resident Companies'),
        ('Partnership', 'Partnership'),
        ('Private Unlimited Company', 'Private Unlimited Company'),
        ('Sole Proprietorship', 'Sole Proprietorship'),
    )
    name = models.CharField('Company Name', max_length=150)
    address = models.TextField('Company Address')
