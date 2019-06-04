from django.urls import path

from .models import Pitches
from .serializers import PitchesSerializerget, PitchesSerializer
from .views import prodcutsListCreate
from . import views


urlpatterns = [
    path('fileupload/',views.excel_handle), # Upload file AIP
    path('get_piches_data/',views.data_view), # filter api for Sku_code, name, brand and products
    path('listcreate/', prodcutsListCreate.as_view(queryset=Pitches.objects.all(),
                    serializer_class=PitchesSerializer), name='product-list') # APi to list and create prodcuts

]