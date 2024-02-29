from django import forms
from .models import Teachers

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teachers
        fields = ('fullname','mobile','teach_code','position')
        
    def __init__(self, *args, **kwargs):
        super(TeacherForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "select"
        self.fields['teach_code'].required = False
        