from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (Row, Column, Submit, Layout)
from .models import Chat

class ChatForm(forms.ModelForm):
    quiz = forms.Textarea()
    #lang = forms.CharField(label='to language', widget=(forms.TextInput()))
    class Meta:
        model = Chat
        fields = ['quiz']

    def __init__(self, *args, **kwargs):
        super(ChatForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Row(
                Column('quiz')
            ),
            # Row(
            #     Column('lang')
            # ),
            Row(
                Submit('submit', 'Submit', css_class="form_button submit")
            ),
        )
