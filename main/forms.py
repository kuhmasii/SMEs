from django import forms
from django.core.exceptions import ValidationError
          
class LoanPredForm(forms.Form):
    firstname=forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Enter Firstname'}))
    lastname=forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Enter Lastname'}))
    Dependents=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter Number of Dependents'}))
    ApplicantIncome=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter Monthly Gross Income'}))
    CoapplicantIncome=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter Co-Applicant Monthly Gross Income'}))
    LoanAmount=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Requested Loan Amount'}))
    Loan_Amount_Term=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Loan Term in Months'}))
    Credit_History=forms.ChoiceField(choices=[('0', 0),('1', 1),('2', 2),('3', 3)])
    Gender=forms.ChoiceField(choices=[('Male', 'Male'),('Female', 'Female')])
    Married=forms.ChoiceField(choices=[('Yes', 'Yes'),('No', 'No')])
    Education=forms.ChoiceField(choices=[('Graduate', 'Graduate'),('Not Graduate', 'Not Graduate')])
    Self_Employed=forms.ChoiceField(choices=[('Yes', 'Yes'),('No', 'No')])
    Property_Area=forms.ChoiceField(choices=[('Rural', 'Rural'),('Semiurban', 'Semiurban'),('Urban', 'Urban')])


class GraphForm(forms.Form):
    labels = forms.CharField(max_length=100, 
        widget=forms.TextInput(attrs={'placeholder': 'Labels(Age, Year, Date, etc)'}))
    data = forms.CharField(max_length=100,
         widget=forms.TextInput(attrs={'placeholder': 'column to check on'}))
    file = forms.FileField()
    graph_type = forms.ChoiceField(choices=[('bar', 'bar'), ('line', 'line')])
       

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
