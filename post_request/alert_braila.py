import requests
from datetime import datetime
from datetime import timedelta
import random

from create_data_models import alert

idAlert = "urn:ngsi-ld:BrailaWaterLeakage:BrailaWaterLeakage-" + datetime.now().strftime("%Y%m%d-%H")
dateFrom = (datetime.now() + timedelta(days=random.randint(0,7))).replace(hour=0, minute=0, second=0, microsecond=0).isoformat() + '.00Z'
dateTo = (datetime.now() + timedelta(days=30)).replace(hour=0, minute=0, second=0, microsecond=0).isoformat() + '.00Z'
dateIssued = datetime.now().replace(microsecond=0).isoformat() + '.00Z'
severity = random.choice(['informational', 'low', 'medium', 'high', 'critical'])
description = "water leakage"

data = alert(idAlert, dateFrom, dateTo, dateIssued, severity,  description)

headers = {
    'Fiware-Service': 'braila',
    'Content-Type': 'application/json',
}

params = (
    ('options', 'keyValues'),
)

response = requests.post('http://5.53.108.182:1026/v2/entities/', headers=headers, params=params, data=data)

print(response.status_code, response.content)