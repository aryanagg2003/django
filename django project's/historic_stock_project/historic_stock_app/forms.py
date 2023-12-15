from django import forms


class StockSearchForm(forms.Form):
    search_query = forms.CharField(label='search by company Symbol', required=False)