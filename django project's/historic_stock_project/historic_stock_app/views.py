# views.py

from django.shortcuts import render
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse 
from django.views.generic import TemplateView
from .models import HistoricalStockPrice
import requests
from .forms import StockSearchForm
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from django.db.models import Q
from .models import HistoricalStockPrice

class HistoricalStockListView(ListView):
    template_name = "historic_stock_list.html"
    form_class = StockSearchForm

    def get(self, request, *args, **kwargs):
        url = "https://financialmodelingprep.com/api/v3/historical-price-full/AAPL,GOOG,AMZN?apikey="
        api_key = "5e009bd5d66003ac7dfdd6782a94a295"
        if not api_key:
            return HttpResponse("API key not found.")
        
        response = requests.get(url + api_key)
        data = response.json()
        companies = data["historicalStockList"]

        if not HistoricalStockPrice.objects.all().exists():
            for company in companies:
                for historical_data in company["historical"]:
                    historical_stock_data = HistoricalStockPrice(
                        companySymbol=company["symbol"],
                        historicalDate=historical_data["date"],
                        historicalOpen=historical_data.get("open", None),
                        historicalHigh=historical_data.get("high", None),
                        historicalLow=historical_data.get("low", None),
                        historicalClose=historical_data.get("close", None),
                        historicalAdjClose=historical_data.get("adjClose", None),
                        historicalVolume=historical_data.get("volume", None),
                        historicalUnAdjustedVolume=historical_data.get("unadjustedVolume", None),
                        historicalChange=historical_data.get("change", None),
                        historicalChangePercent=historical_data.get("changePercent", None),
                        historicalVwap=historical_data.get("vwap", None),
                        historicalLabel=historical_data.get("label", None),
                        historicalChangeOverTime=historical_data.get("changeOverTime", None),
                    )
                    historical_stock_data.save()

        form = self.form_class(request.GET)
        search_query = form['search_query'].value()
        min_vwap = form['min_vwap'].value()
        max_vwap = form['max_vwap'].value()

        queryset = HistoricalStockPrice.objects.all()

        if search_query:
            queryset = queryset.filter(companySymbol__icontains=search_query)

        if min_vwap:
            queryset = queryset.filter(historicalVwap__gte=min_vwap)

        if max_vwap:
            queryset = queryset.filter(historicalVwap__lte=max_vwap)
        
        page = request.GET.get("page")
        paginator = Paginator(queryset, 100)

        try:
            page_obj = paginator.page(page)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)

        # Preserve search parameters in pagination links
        page_obj.query_params = f'&search_query={search_query}' if search_query else ''

        return render(request, self.template_name, {"page_obj": page_obj, "form": form, "search_query": search_query})
    
class StockChartView(TemplateView):
    template_name = "stock_charts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        
        api_key = "5e009bd5d66003ac7dfdd6782a94a295"
        url = f"https://financialmodelingprep.com/api/v3/historical-price-full/AAPL,GOOG,AMZN?apikey={api_key}"

        
        response = requests.get(url)
        data = response.json()

        
        companies = data["historicalStockList"]

        
        company_images = {}

        for company in companies:
            dates = [entry["date"] for entry in company["historical"]]
            close_prices = [entry["close"] for entry in company["historical"]]

            
            plt.figure(figsize=(10, 6))
            plt.plot(dates, close_prices, label="Stock Prices", color="blue")
            plt.xlabel("Date")
            plt.ylabel("Closing Price")
            plt.title(f"{company['symbol']} Stock Prices Over Time")
            plt.xticks(rotation=45)  
            plt.legend()

            
            buffer = BytesIO()
            plt.savefig(buffer, format="png")
            buffer.seek(0)
            image_base64 = base64.b64encode(buffer.read()).decode("utf-8")
            plt.close()  

            
            company_images[company['symbol']] = image_base64

        
        context["company_images"] = company_images

        return context

    def get(self, request, *args, **kwargs):
        
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)