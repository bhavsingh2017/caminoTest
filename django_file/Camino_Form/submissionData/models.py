from django.db import models

class Loan(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    my_field_name = models.CharField(max_length=20, help_text='Please Enter Your Full Name')
    created_at = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField(help_text='Please Enter Loan Amount Required')
    years = models.FloatField(null=True, help_text='Please Enter Years in Business')
    business = forms.CharField(label='Type of Business?', widget=forms.Select(choices=Businesses), initial="Select your business")

    LOAN_STATUS = (
    	'loan application denied',
        'loan application is preapproved',
        'loan application is currently being processed',
        'loan has never been applied for',
    )
    ...

    # Metadata
    class Meta:
        ordering = ['-created_at']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.my_field_name
