from django import forms


class RoomsForm(forms.Form):
    CHOICES = (
        ('travel', 'Travel',),
        ('music', 'Music',),
        ('movies', 'Movies',),
        ('sports', 'Sports',),
        ('food', 'Food',),
        ('gaming', 'Gaming',),
        ('books', 'Books',),
        ('fashion', 'Fashion',),
        ('technology', 'Technology',),
        ('politics', 'Politics',),
        ('science', 'Science',),
        ('art', 'Art',),
        ('other', 'Other',),
    )
    room_name = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
