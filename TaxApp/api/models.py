from django.conf import settings
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db import models
from django.db.models import signals
from django.db.models.functions import ExtractMonth
from django.core.validators import RegexValidator
from django.utils import timezone
from audit_log.models.managers import AuditLog


User = get_user_model()

PHONE_REGEX = RegexValidator(
    regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")


class Country(models.Model):
    '''Countries of the world'''
    name = models.CharField('Country', max_length=75, unique=True)
    code = models.CharField('Code', max_length=2, unique=True)
    created_at = models.DateTimeField('Created At', auto_now_add=True)
    updated_at = models.DateTimeField('Last Modified', auto_now=True)

    class Meta:
        verbose_name_plural = 'Countries'


class State(models.Model):
    '''Nigerian States'''
    name = models.CharField('State', max_length=75, unique=True)
    created_at = models.DateTimeField('Created At', auto_now_add=True)
    updated_at = models.DateTimeField('Last Modified', auto_now=True)


class Lga(models.Model):
    '''Nigerian Local Government Areas'''
    name = models.CharField('LGA', max_length=75)
    state = models.ForeignKey(
        State, related_name='lgas', on_delete=models.CASCADE)
    created_at = models.DateTimeField('Created At', auto_now_add=True)
    updated_at = models.DateTimeField('Last Modified', auto_now=True)

    class Meta:
        unique_together = (('name', 'state'),)
        verbose_name = 'Local Government Area'


class Serial(models.Model):
    '''
    Maintains a serial counter for generating Tax Identification Numbers (TIN)
    '''
    next_serial = models.IntegerField()
    created_at = models.DateTimeField('Created At', auto_now_add=True)
    updated_at = models.DateTimeField('Last Modified', auto_now=True)

    @staticmethod
    def create_instance():
        '''Returns the singleton instance. Creates one if none exists.'''
        if Serial.objects.count():
            return Serial.objects.first()

        return Serial.objects.create(next_serial=settings.JTB_NEXT_TIN or 1)

    @staticmethod
    def get_next_serial():
        '''Get and update next serial with row locking'''
        if not Serial.objects.count():
            Serial.create_instance()

        serial = Serial.objects.select_for_update().first()

        next_serial = serial.next_serial
        serial.next_serial += 1
        serial.save()

        return next_serial


class EnrollmentAnnotationMixin(object):

    @classmethod
    def get_enrollments_per_month(cls):
        '''Gets number of enrollments per month for one year to date'''
        one_year_ago = timezone.now() - timezone.timedelta(days=365)
        return cls.objects.filter(
            created_at__gte=one_year_ago
        ).annotate(
            month=ExtractMonth('created_at')
        ).values('month').annotate(
            count=models.Count('id')
        ).values('month', 'count')


class TaxPayer(EnrollmentAnnotationMixin, models.Model):
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
    surname = models.CharField('Surname', max_length=75)
    first_name = models.CharField('First Name', max_length=75)
    other_name = models.CharField(
        'Other Name', max_length=75, blank=True, null=True)
    marital_status = models.CharField(
        'Marital Status', max_length=20, choices=MARITAL_STATUSE_CHOICES)
    gender = models.CharField('Gender', max_length=20, choices=GENDER_CHOICES)
    dob = models.DateField('Date of Birth')
    tin = models.CharField('JTB TIN', max_length=10,
                           blank=True, null=True, unique=True)
    lga_of_origin = models.CharField('LGA', max_length=75)
    state_of_origin = models.CharField('State of Origin', max_length=75)
    nationality = models.CharField('Nationality', max_length=75)
    tax_payer_company = models.CharField('Company', max_length=150)
    occupation = models.CharField('Occupation', max_length=75)
    employment_status = models.CharField(
        'Employment Status', max_length=20, choices=EMPLOYMENT_STATUS_CHOICES)
    phone = models.CharField('Phone', max_length=15, validators=[PHONE_REGEX])
    email = models.EmailField('Email', unique=True)
    created_at = models.DateTimeField('Created At', auto_now_add=True)
    updated_at = models.DateTimeField('Last Modified', auto_now=True)

    history = AuditLog()

    @property
    def full_name(self):
        name_parts = [self.first_name, self.other_name, self.surname]
        return ' '.join([i for i in name_parts if i])

    def __str__(self):
        return '{} (TIN: {})'.format(self.full_name, self.tin or 'N/A')

    class Meta:
        verbose_name = 'Individual Tax Payer'
        ordering = ('-created_at',)


class CorporateTaxPayer(EnrollmentAnnotationMixin, models.Model):
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
    name = models.CharField('Registration Name', max_length=150)
    trade_name = models.CharField('Trade Name', max_length=150)
    phone = models.CharField('Phone', max_length=15, validators=[PHONE_REGEX])
    email = models.EmailField('Email')
    tin = models.CharField(
        'JTB TIN', max_length=10, blank=True, null=True, unique=True)
    company_size = models.CharField(
        'Company Size', max_length=20, choices=COMPANY_SIZE_CHOICES)
    ownership_type = models.CharField(
        'Organization Type', max_length=75, choices=OWNERSHIP_TYPE_CHOICES)
    reg_status = models.CharField(
        'Registration Status', max_length=20, choices=REGISTRATION_STATUS_CHOICES)
    reg_date = models.DateField('CAC Registration Date', blank=True, null=True)
    start_date = models.DateField('Business Start Date')
    reg_no = models.CharField('Registration Number',
                              max_length=20, blank=True, null=True)
    line_of_business = models.CharField('Line of Business', max_length=75)
    sector = models.CharField('Sector', max_length=75)
    contact_name = models.CharField('Contact Name', max_length=150)
    created_at = models.DateTimeField('Created At', auto_now_add=True)
    updated_at = models.DateTimeField('Last Modified', auto_now=True)

    def __str__(self):
        return '{} (TIN: {})'.format(self.name, self.tin or 'N/A')

    class Meta:
        verbose_name = 'Corporate Tax Payer'


class IdentificationDocument(models.Model):
    tax_payer = models.OneToOneField(
        CorporateTaxPayer, on_delete=models.CASCADE, related_name='identification_document')
    type = models.CharField('ID Type', max_length=75)
    issuer = models.CharField('Issuer', max_length=75)
    issuance_date = models.DateField('Issuance Date')
    expiry_date = models.DateField('Expiry Date', null=True)
    created_at = models.DateTimeField('Created At', auto_now_add=True)
    updated_at = models.DateTimeField('Last Modified', auto_now=True)

    history = AuditLog()

    class Meta:
        verbose_name = 'Identification Document'


class AddressBase(models.Model):
    house_no = models.CharField('House Number', max_length=75)
    street = models.CharField('Street', max_length=75)
    city = models.CharField('City', max_length=75)
    ward = models.CharField('Ward', max_length=75, blank=True, null=True)
    lga = models.CharField('LGA', max_length=75)
    state = models.CharField('State', max_length=75)
    country = models.CharField(
        'Country', max_length=75, choices=(), default='Nigeria')
    created_at = models.DateTimeField('Created At', auto_now_add=True)
    updated_at = models.DateTimeField('Last Modified', auto_now=True)

    def __str__(self):
        '''
        String representation of an instance of this model
        '''
        parts = [
            self.house_no, self.street, self.city, self.ward, self.lga, self.state, self.country
        ]
        return ', '.join(p for p in parts if p)

    class Meta:
        abstract = True


class Biometric(models.Model):
    '''Biometric data of individual tax payers. Biometric fields are base64 encoded strings.'''
    tax_payer = models.OneToOneField(
        TaxPayer, on_delete=models.CASCADE, related_name='biometrics')
    pic = models.TextField('Passport Photo')
    f1 = models.TextField('Finder #1')
    f2 = models.TextField('Finder #2')
    f3 = models.TextField('Finder #3')
    f4 = models.TextField('Finder #4')
    f5 = models.TextField('Finder #5')
    f6 = models.TextField('Finder #6')
    f7 = models.TextField('Finder #7')
    f8 = models.TextField('Finder #8')
    f9 = models.TextField('Finder #9')
    f10 = models.TextField('Finder #10')
    created_at = models.DateTimeField('Created At', auto_now_add=True)
    updated_at = models.DateTimeField('Last Modified', auto_now=True)

    history = AuditLog()


class ResidentialAddress(AddressBase):
    tax_payer = models.OneToOneField(
        TaxPayer, on_delete=models.CASCADE, related_name='residential_address')

    history = AuditLog()

    class Meta:
        verbose_name = 'Residential Address'
        verbose_name_plural = 'Residential Addresses'


class CompanyAddress(AddressBase):
    tax_payer = models.OneToOneField(
        CorporateTaxPayer, on_delete=models.CASCADE, related_name='company_address')

    history = AuditLog()

    class Meta:
        verbose_name = 'Company Address'
        verbose_name_plural = 'Company Addresses'


@receiver(signals.post_save, sender=TaxPayer)
@receiver(signals.post_save, sender=CorporateTaxPayer)
def generate_tax_identification_number(sender, instance, created, **kwargs):
    if not created:
        return

    next_tin = Serial.get_next_serial()

    control_digit = settings.JTB_CONTROL_DIGIT_CORPORATE
    if isinstance(instance, TaxPayer):
        control_digit = settings.JTB_CONTROL_DIGIT_INDIVIDUAL

    instance.tin = '%09d%d' % (next_tin, control_digit)
    instance.save()
