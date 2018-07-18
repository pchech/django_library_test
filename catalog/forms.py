from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime #for checking renewal date range.
    
class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']
        
        #Проверка того, что дата не выходит за "нижнюю" границу (не в прошлом). 
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))

        #Проверка того, то дата не выходит за "верхнюю" границу (+4 недели).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

        # Помните, что всегда надо возвращать "очищенные" данные.
        return data
class SplitCalcForm(forms.Form):
	def __init__(self,*args,**kwargs):
		tk_cnt=kwargs.pop('tk_cnt',None)
		super(SplitCalcForm,self).__init__(*args,**kwargs)
		
		if tk_cnt:
			for i in range(1,tk_cnt+1):
				self.fields['tk_{}'.format(i)]=forms.CharField(help_text="Tk",required=False)
				self.fields['rate_{}'.format(i)]=forms.CharField(help_text="Rate",required=False)
				self.fields['cost_{}'.format(i)]=forms.CharField(help_text="Cost",required=False)
	#TK1=forms.CharField(help_text="Tk1")
	#Rate1=forms.CharField(help_text="Rate1")
	#Cost1=forms.CharField(help_text="Cost1")
	#TK2=forms.CharField(help_text="Tk2")
	#Rate2=forms.CharField(help_text="Rate2")
	#Cost2=forms.CharField(help_text="Cost2")
	Ship=forms.CharField(help_text="Num ships",required=False)
	def clean_TK1(self):
		return self.cleaned_data['TK1']
	