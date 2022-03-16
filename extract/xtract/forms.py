from django import forms
from PIL import Image
from django.core.files import File
from .models import Photo




class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('file1', 'description' )


    def save(self):
        photo = super(PhotoForm, self).save()


        image = Image.open(photo.file1)
        cropped_image1 = image.crop((436,432, 610, 550))
        resized_image = cropped_image1.resize((200, 200), Image.ANTIALIAS)
        resized_image.save(photo.file1.path)
        


        return photo

