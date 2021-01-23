from django.db import models
import datetime
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class BaseIne(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=200)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name


class Country(BaseIne):
    ine_code = models.IntegerField()
    iso_code = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = _('country')
        verbose_name_plural = _('countries')
        ordering = ('name', )


class Province(BaseIne):
    ine_code = models.IntegerField()

    class Meta:
        verbose_name = _('province')
        verbose_name_plural = _('provinces')
        ordering = ('name', )


class City(BaseIne):
    ine_code = models.IntegerField()
    dc_code = models.IntegerField(null=True, blank=True)
    province = models.ForeignKey(Province, verbose_name=_('province'), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('city')
        verbose_name_plural = _('cities')
        ordering = ('name', )


class RoadType(BaseIne):
    ine_code = models.CharField(max_length=10)

    class Meta:
        verbose_name = _('road type')
        verbose_name_plural = _('road types')
        ordering = ('name', )


class IdentifierType(BaseIne):
    ine_code = models.IntegerField()

    class Meta:
        verbose_name = _('identifier type')
        verbose_name_plural = _('identifier types')

class ContactData(models.Model):
    is_foreign_address = models.BooleanField(_('is foreign address'), default=False)
    road_type = models.ForeignKey(RoadType, null=True, blank=True, on_delete=models.CASCADE)
    road_name = models.TextField(verbose_name=_('road name'))
    number = models.CharField(verbose_name=_('number'), max_length=20, null=True, blank=True)
    character = models.CharField(verbose_name=_('character'), max_length=5, blank=True)
    floor = models.CharField(verbose_name=_('floor'), max_length=10, blank=True)
    door = models.CharField(verbose_name=_('door'), max_length=10, blank=True)
    stair = models.CharField(verbose_name=_('stair'), max_length=10, blank=True)
    postal_code = models.CharField(max_length=50, verbose_name=_('postal code'), null=True, blank=True)
    landline_phone = models.CharField(verbose_name=_('landline phone'), max_length=30)
    mobile_phone = models.CharField(verbose_name=_('mobile phone'), max_length=30)
    email = models.CharField(verbose_name=_('email'), max_length=200, blank=True)
    email_doble_factor = models.CharField(verbose_name=_('email doble factor'), max_length=200, null=True, blank=True)
    country = models.ForeignKey(Country, null=True, blank=True, on_delete=models.CASCADE)
    region = models.CharField(verbose_name=_('region'), max_length=200, null=True, blank=True)
    town = models.CharField(verbose_name=_('town'), max_length=200, null=True, blank=True)
    province = models.ForeignKey(Province, null=True, blank=True, on_delete=models.CASCADE)
    city = models.ForeignKey(City, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('contact data')
        verbose_name_plural = _('contact data')

class Client(models.Model):
    ident_type = models.ForeignKey(IdentifierType, null=True, blank=True, on_delete=models.CASCADE)
    identifier = models.CharField(verbose_name=_('identifier'), max_length=25, blank=True)
    name = models.CharField(verbose_name=_('name'), max_length=200, blank=True)
    surname1 = models.CharField(verbose_name=_('first surname'), max_length=200, blank=True)
    surname2 = models.CharField(verbose_name=_('second surname'), max_length=200, blank=True)
    gender = models.CharField(verbose_name=_('gender'), max_length=200, blank=True)
    birth_date = models.CharField(verbose_name=_('birth date'), max_length=200, blank=True)
    contact_data = models.ForeignKey(ContactData, null=True, blank=True, on_delete=models.CASCADE)
    last_login = models.DateTimeField(verbose_name=_('last login'), auto_now_add=True, null=True, blank=True)
    username = models.CharField(
        verbose_name=_('username'), max_length=30, unique=True, blank=True, null=True,
        help_text=_('Required. 30 characters or fewer. Letters, numbers and '
                    '@/./+/-/_ characters'))
    password = models.CharField(
        verbose_name=_('password'), max_length=128, blank=True, null=True,)
    create_in = models.DateTimeField(verbose_name=_('discharge date'), auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name = _('cliente')
        verbose_name_plural = _('clientes')
        unique_together = ('identifier',)

    def update_last_login(self, **kwargs):
        self.last_login = datetime.datetime.now()
        self.save()

    def _get_full_name(self):
        return "%s %s %s" % (self.name, self.surname1, self.surname2)
    full_name = property(_get_full_name)

    def update_last_login(self, **kwargs):
        self.last_login = datetime.datetime.now()
        self.save()

