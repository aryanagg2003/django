from django import forms


class StockSearchForm(forms.Form):
    SEARCH_CHOICES = [
        ('AAPL', 'AAPL'),
        ('GOOG', 'GOOG'),
        ('AMZN', 'AMZN'),
    ]

    search_query = forms.ChoiceField(label='Search by company Symbol', required=False, choices=SEARCH_CHOICES)
    min_vwap = forms.FloatField(label='Min VWAP', required=False)
    max_vwap = forms.FloatField(label='Max VWAP', required=False)