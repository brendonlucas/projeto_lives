from django import forms


class CreateFAC(forms.Form):
    nome = forms.CharField(max_length=200)

    def is_valid(self):
        valid = True
        return valid


class CreateStreamer(forms.Form):
    nome = forms.CharField(max_length=200)
    nick_player = forms.CharField(max_length=200)
    link_yt = forms.CharField(max_length=200)
    link_kick = forms.CharField(max_length=200)
    link_twitch = forms.CharField(max_length=200)

    def is_valid(self):
        valid = True
        return valid
