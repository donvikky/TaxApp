from django.db import models
from django.core.validators import RegexValidator
from django.forms import model_to_dict
from audit_log.models.managers import AuditLog


PHONE_REGEX = RegexValidator(
    regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")


class Country(models.Model):
    '''Countries of the world'''
    name = models.CharField('Country', max_length=75, unique=True)
    code = models.CharField('Code', max_length=2, unique=True)

    class Meta:
        verbose_name_plural = 'Countries'


class State(models.Model):
    '''Nigerian States'''
    name = models.CharField('State', max_length=75, unique=True)


class Lga(models.Model):
    '''Nigerian Local Government Areas'''
    name = models.CharField('LGA', max_length=75)
    state = models.ForeignKey(
        State, related_name='lgas', on_delete=models.CASCADE)
    
    class Meta:
        unique_together = (('name', 'state'),)
        verbose_name = 'LGA'


class TaxPayer(models.Model):
    MARITAL_STATUSE_CHOICES = (
        ('Single', 'Single'),
        ('Married', 'Married'),
    )
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    EMPLOYMENT_STATUS_CHOICES = (
        ('Unemployed', 'Unemployed'),
        ('Self Employed', 'Self Employed'),
        ('Employed', 'Employed'),
    )
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='tax_payers')
    surname = models.CharField('Surname', max_length=75)
    first_name = models.CharField('First Name', max_length=75)
    other_name = models.CharField('Other Name', max_length=75, null=True)
    marital_status = models.CharField(
        'Marital Status', max_length=20, choices=MARITAL_STATUSE_CHOICES)
    gender = models.CharField('Gender', max_length=20, choices=GENDER_CHOICES)
    dob = models.DateField('Date of Birth')
    tin = models.CharField('JTB TIN', max_length=10, unique=True, blank=True)
    lga_of_origin = models.CharField('LGA', max_length=75)
    state_of_origin = models.CharField('State of Origin', max_length=75)
    nationality = models.CharField('Nationality', max_length=75)
    tax_payer_company = models.CharField('Company', max_length=150)
    occupation = models.CharField('Occupation', max_length=75)
    employment_status = models.CharField(
        'Employment Status', max_length=20, choices=EMPLOYMENT_STATUS_CHOICES)
    phone = models.CharField('Phone', max_length=15, validators=[PHONE_REGEX])
    email = models.EmailField('Email')

    history = AuditLog()

    @property
    def full_name(self):
        name_parts = [self.first_name, self.other_name, self.surname]
        return ' '.join([i for i in name_parts if i])

    def __str__(self):
        return '{} (TIN: {})'.format(self.full_name, self.tin or 'N/A')

    class Meta:
        verbose_name = 'Individual Tax Payer'


class CorporateTaxPayer(models.Model):
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
    REGISTRATION_STATUS_CHOICES = (
        ('Registered', 'Registered'),
        ('Unregistered', 'Unregistered'),
    )
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='corporate_tax_payers')
    name = models.CharField('Company Name', max_length=150)
    phone = models.CharField('Phone', max_length=15, validators=[PHONE_REGEX])
    email = models.EmailField('Email')
    start_date = models.DateField('Business Start Date')
    tin = models.CharField(
        'JTB TIN', max_length=10, unique=True, blank=True)
    company_size = models.CharField(
        'Company Size', max_length=20, choices=COMPANY_SIZE_CHOICES)
    ownership_type = models.CharField(
        'Ownership Type', max_length=75, choices=OWNERSHIP_TYPE_CHOICES)
    reg_status = models.CharField(
        'Registration Status', max_length=20, choices=REGISTRATION_STATUS_CHOICES)
    reg_no = models.CharField('Registration Number', max_length=20, null=True)

    def __str__(self):
        return '{} (TIN: {})'.format(self.name, self.tin or 'N/A')

    class Meta:
        verbose_name = 'Corporate Tax Payer'


class AddressBase(models.Model):
    house_no = models.CharField('House Number', max_length=75)
    street = models.CharField('Street', max_length=75)
    city = models.CharField('City', max_length=75)
    ward = models.CharField('Ward', max_length=75, null=True)
    lga = models.CharField('LGA', max_length=75)
    state = models.CharField('State', max_length=75)
    country = models.CharField(
        'Country', max_length=75, choices=(), default='Nigeria')

    history = AuditLog()

    def __str__(self):
        '''
        String representation of an instance of this model
        '''
        return '%(house_no)s, %(street)s, %(city)s, %(ward)s, %(lga)s, %(state), %(country)s' % model_to_dict(self)

    class Meta:
        abstract = True


class Biometric(models.Model):
    tax_payer = models.OneToOneField(TaxPayer, on_delete=models.CASCADE, related_name='biometrics')


class ResidentialAddress(AddressBase):
    tax_payer = models.OneToOneField(TaxPayer, on_delete=models.CASCADE, related_name='residential_address')

    history = AuditLog()

    class Meta:
        verbose_name = 'Residential Address'
        verbose_name_plural = 'Residential Addresses'


class CompanyAddress(AddressBase):
    tax_payer = models.OneToOneField(CorporateTaxPayer, on_delete=models.CASCADE, related_name='company_address')

    history = AuditLog()

    class Meta:
        verbose_name = 'Company Address'
        verbose_name_plural = 'Company Addresses'
