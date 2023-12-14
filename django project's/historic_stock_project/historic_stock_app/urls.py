from django.urls import path
from historic_stock_app.views import HistoricalStockListView, StockChartView
# from . import views

urlpatterns = [
    path('', HistoricalStockListView.as_view(), name="get_historical_stock"),
    path('stock_charts/', StockChartView.as_view(), name='stock_charts'),
]