from django.db import models
from django.contrib.auth.models import User
from PIL import Image

TYPE_CHOICES = (
    ('Полный пакет', 'full'),
    ('Бесплатный пакет', 'free')
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField('Фото пользователя', default='default.jpg', upload_to='user_images')
    account_type = models.CharField(choices=TYPE_CHOICES, default='Бесплатный пакет', max_length=30)

    def __str__(self):
        return f'Профаил пользователя {self.user.username}'

    def svae(self, *args, **kwards):
        super().save()

        image = Image.open(self.img.path)

        if image.hight > 256 or image.width > 256:
            resize = (256, 256)
            image.thumbnail(resize)
            image.save(self.img.path)

    class Meta:
        verbose_name = 'Профаил'
        verbose_name_plural = 'Профайлы'
