from django import forms 
from .models import Defect
# in here we are going to design a form with the required html


class DefectForm(forms.ModelForm):
    
    class Meta:
        model = Defect
        fields = '__all__'
        labels = {
            'Product_name' : 'أسم المنتج'
        }
        
    def __init__(self, *args, **kwargs):
        super(DefectForm, self).__init__(*args, **kwargs)
        self.fields['Defect_weight'].empty_label = "select"