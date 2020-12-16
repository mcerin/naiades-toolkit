import requests
from datetime import datetime
from datetime import timedelta
import random

from create_data_models import consumption

idPrediction = "Consumption:Spain-Consumption-Alicante-Benalua" + datetime.now().strftime("%Y%m%d-%H")
value = random.random() + random.randint(5,10)
dateFrom = (datetime.now() + timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0).isoformat() + '.00Z+01'
dateTo = (datetime.now() + timedelta(days=2)).replace(hour=0, minute=0, second=0, microsecond=0).isoformat() + '.00Z+01'

data = consumption(idPrediction, value, dateFrom, dateTo)

headers = {
    'Fiware-Service': 'alicante',
    'Content-Type': 'application/json',
}

params = (
    ('options', 'keyValues'),
)

response = requests.post('http://5.53.108.182:1026/v2/entities/', headers=headers, params=params, data=data)

print(response.status_code, response.content)