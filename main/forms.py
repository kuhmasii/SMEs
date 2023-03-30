from django import forms

# class LoanPredForm(ModelForm):
#     class Meta:
#         model=LoanPred
#         fields = '__all__'


            
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
    Education=forms.ChoiceField(choices=[('Graduate', 'Graduate'),('Not_Graduate', 'Not_Graduate')])
    Self_Employed=forms.ChoiceField(choices=[('Yes', 'Yes'),('No', 'No')])
    Property_Area=forms.ChoiceField(choices=[('Rural', 'Rural'),('Semiurban', 'Semiurban'),('Urban', 'Urban')])
       
    # def __init__(self, *args, **kwargs):
    #     super(LoanPredForm, self).__init__(*args, **kwargs)
    #     for name,field in self.fields.items():

    #         field.widget.attrs.update({
    #             "class":"form-control bg-white border-0",
    #             "placeholder":field.label, 
    #             "style":{"height":"55px"}
    #         }
    #         )