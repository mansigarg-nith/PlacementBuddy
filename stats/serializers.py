from rest_framework import serializers

from company.models import *
class companyserializers(serializers.ModelSerializer):
    class Meta:
        model = CompanyDatabase
        fields = ["name","ctc","Btech","Mtech","MSC","MBA","total_offers","year","Dtech"]
