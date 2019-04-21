from django import forms



class LoanForm(forms.Form):

    Businesses =  [
    ('food truck', 'Food Truck'),
    ('construction', 'Construction'),
    ('clothing', 'Clothing'),
    ('liquor/beer', 'Alcohol'),
    ('convenience', 'Convenience'),
    ('real estate', 'Real Estate'),
    ('coffee', 'Coffee'),
    ('other', 'Other'),
    ]

    name = forms.CharField(label='Full Name', max_length=100)
    amount = forms.FloatField(label="Request Amount");
    years = forms.FloatField(label="Years In Business  ");
    business = forms.CharField(label='Type of Business?', widget=forms.Select(choices=Businesses), initial="Select your business")
