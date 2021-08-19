from django import forms
from artportal.art_app.models import Art, Comment


class ArtCreateForm(forms.ModelForm):
    class Meta:
        model = Art
        exclude = ('user',)
        fields = '__all__'


class CreateArtForm(ArtCreateForm):
    pass


class EditArtForm(ArtCreateForm):
    class Meta:
        model = Art
        exclude = ('user', 'image',)
        fields = '__all__'


class DeleteArtForm(ArtCreateForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
            field.widget.attrs['disabled'] = 'disabled'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
