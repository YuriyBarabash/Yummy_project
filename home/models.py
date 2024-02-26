
from django.db import models
from django.core.validators import RegexValidator
from ckeditor.fields import RichTextField


class DishCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    position = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Dish Categories'
        ordering = ('position',)

    def __iter__(self):
        dishes = self.dishes.filter(is_visible=True)
        for dish in dishes:
            yield dish

    def __str__(self):
        return f'{self.name}'


class Dish(models.Model):
    name = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey(DishCategory, on_delete=models.PROTECT, related_name='dishes')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='url')
    ingredients = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    photo = models.ImageField(upload_to='dishes/', blank=True)
    position = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Dishes'
        ordering = ('position',)
        constraints = [
            models.UniqueConstraint(fields=['position', 'category'], name='unique_position_per_each_category'),]
        unique_together = ['id', 'slug']


class Chefs(models.Model):
    name = models.CharField(max_length=255)
    specialisation = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='chefs/')
    description = models.TextField(blank=True)
    is_visible = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Chefs'

    def __str__(self):
        return f'{self.name}'


class Gallery(models.Model):
    photo = models.ImageField(upload_to='gallery/')
    tittle = models.CharField(max_length=255, blank=True)
    is_visible = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Gallery Images'

    def __str__(self):
        return f'{self.tittle}'


class Events(models.Model):
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Price ($)')
    photo = models.ImageField(upload_to='events/')
    is_visible = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Events'

    def __str__(self):
        return f'{self.name}'


class FooterItem(models.Model):
    address = RichTextField()
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    working_hours = RichTextField()
    twitter = models.URLField(max_length=255, blank=True)
    facebook = models.URLField(max_length=255, blank=True)
    instagram = models.URLField(max_length=255, blank=True)
    youtube = models.URLField(max_length=255, blank=True)


class Reservation(models.Model):
    name = models.CharField(max_length=255)

    phone_regex = RegexValidator(
        regex=r'^\+?380\d{9}$',
        message="Phone number must be entered in the format: '+380xxxxxxxxx'."
    )
    phone = models.CharField(max_length=255, validators=[phone_regex])
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    people_number = models.PositiveSmallIntegerField()
    message = models.TextField(blank=True)

    is_confirmed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)




