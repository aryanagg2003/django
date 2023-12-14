from django.db import models

# Historical Stock Price Model
class HistoricalStockPrice(models.Model):
    companySymbol = models.CharField(verbose_name="Company Symbol", max_length=4, blank=True, null=True)
    historicalDate = models.CharField(verbose_name="Date", max_length=10, blank=True, null=True)
    historicalOpen = models.FloatField(verbose_name="Open", blank=True, null=True)
    historicalHigh = models.FloatField(verbose_name="High", blank=True, null=True)
    historicalLow = models.FloatField(verbose_name="Low", blank=True, null=True)
    historicalClose = models.FloatField(verbose_name="Close", blank=True, null=True)
    historicalAdjClose = models.FloatField(verbose_name="Adj. Close", blank=True, null=True)
    historicalVolume = models.FloatField(verbose_name="Volume", blank=True, null=True)
    historicalUnAdjustedVolume = models.FloatField(verbose_name="UnAdjusted Volume", blank=True, null=True)
    historicalChange = models.FloatField(verbose_name="Change", blank=True, null=True)
    historicalChangePercent = models.FloatField(verbose_name="Change Percent", blank=True, null=True)
    historicalVwap = models.FloatField(verbose_name="VWAP", blank=True, null=True)
    historicalLabel = models.CharField(verbose_name="Label", max_length=20, blank=True, null=True)
    historicalChangeOverTime = models.FloatField(verbose_name="Change OverTime", blank=True, null=True)

    def __str__(self):
        return self.companySymbol