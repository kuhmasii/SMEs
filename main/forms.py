from django import forms
from . models import LoanPred

          
class LoanPredForm(forms.ModelForm):
    class Meta:
        model = LoanPred
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super(LoanPredForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            placeholder = field.help_text
            field.widget.attrs.update(
                {"class": "form-control bg-light border-0",
                "placeholder":placeholder,
                "style":{"height":"55px;"}})



class GraphForm(forms.Form):
    labels = forms.CharField(max_length=100, 
        widget=forms.TextInput(attrs={'placeholder': 'Labels; can be more than one columns ( Age, Year, Date, etc)'}))
    data = forms.CharField(max_length=100,
         widget=forms.TextInput(attrs={'placeholder': 'column to be checked on'}))
    indicator = forms.CharField(max_length=100, required=False,
         widget=forms.TextInput(attrs={'placeholder': 'indicator must be a column with unique data (Optional)'}))
    file = forms.FileField()       

    def __init__(self, *args, **kwargs):
        super(GraphForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update(
                {"class": "form-control bg-light border-0",
                "style":{"height":"55px;"}})

    def clean_file(self):
        file = self.cleaned_data.get('file')
        
        if not file.name.endswith('.csv'):
            raise ValidationError("Upload a CSV File.")

        return file
