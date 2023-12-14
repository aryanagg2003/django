# views.py

from django.shortcuts import render
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse 
from django.views.generic import TemplateView
from .models import HistoricalStockPrice
import requests
import json
import matplotlib.pyplot as plt
from io import BytesIO
import base64

from .models import HistoricalStockPrice

class HistoricalStockListView(ListView):

    template_name = "historic_stock_list.html"

    def get(self, request, *args, **kwargs):
        url = "https://financialmodelingprep.com/api/v3/historical-price-full/AAPL,GOOG,AMZN?apikey="
        api_key = "3WEkwtszQC3TEHEuUtnBU0MTnQm09xEs"
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

        all_historical_stock = HistoricalStockPrice.objects.all().order_by("id")
        page_obj = self.paginate_query(request, all_historical_stock, 100)
        # Print the values in page_obj
        # for historical_stock in page_obj:
        #     print(f"Company: {historical_stock.companySymbol}, Date: {historical_stock.historicalDate}, ...")  # Add other fields as needed
        

         
        return render(request, self.template_name, {"page_obj": page_obj})


    def paginate_query(self, request, queryset, count):
        paginator = Paginator(queryset, count)
        page = request.GET.get("page")

        try:
            page_obj = paginator.page(page)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)
      
        return page_obj
    
class StockChartView(TemplateView):
    template_name = "stock_charts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Replace 'YOUR_API_KEY' with your actual API key
        api_key = "3WEkwtszQC3TEHEuUtnBU0MTnQm09xEs"
        url = f"https://financialmodelingprep.com/api/v3/historical-price-full/AAPL,GOOG,AMZN?apikey={api_key}"

        # Make an API request to get stock data
        response = requests.get(url)
        data = response.json()

        # Extract relevant data for plotting
        companies = data["historicalStockList"]

        # Create a dictionary to store base64-encoded images for each company
        company_images = {}

        for company in companies:
            dates = [entry["date"] for entry in company["historical"]]
            close_prices = [entry["close"] for entry in company["historical"]]

            # Create a line chart using Matplotlib
            plt.figure(figsize=(10, 6))
            plt.plot(dates, close_prices, label="Stock Prices", color="blue")
            plt.xlabel("Date")
            plt.ylabel("Closing Price")
            plt.title(f"{company['symbol']} Stock Prices Over Time")
            plt.xticks(rotation=45)  # Rotate x-axis labels by 45 degrees for better readability
            plt.legend()

            # Convert the plot to a base64-encoded image
            buffer = BytesIO()
            plt.savefig(buffer, format="png")
            buffer.seek(0)
            image_base64 = base64.b64encode(buffer.read()).decode("utf-8")
            plt.close()  # Close the Matplotlib figure

            # Store the base64-encoded image in the dictionary
            company_images[company['symbol']] = image_base64

        # Pass the dictionary of base64-encoded images to the template
        context["company_images"] = company_images

        return context

    def get(self, request, *args, **kwargs):
        # Call the parent get method to set up the context data
        context = self.get_context_data(**kwargs)

        # Return the rendered template
        return self.render_to_response(context)