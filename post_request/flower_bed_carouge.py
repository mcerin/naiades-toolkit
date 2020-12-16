import requests
from datetime import datetime
from datetime import timedelta
import random

from create_data_models import flower_bed

idPrediction = "PlantsWateringPredicted:CH-PlantsWateringPredicted-Carouge-" + datetime.now().strftime("%Y%m%d-%H")
date = (datetime.now() + timedelta(days=random.randint(0,7))).replace(hour=0, minute=0, second=0, microsecond=0).isoformat() + '.00Z'
data = flower_bed(idPrediction, date)

headers = {
    'Fiware-Service': 'carouge',
    'Content-Type': 'application/json',
}

params = (
    ('options', 'keyValues'),
)

response = requests.post('http://5.53.108.182:1026/v2/entities/', headers=headers, params=params, data=data)

print(response.status_code, response.content)