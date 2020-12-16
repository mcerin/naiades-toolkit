import json

def alert(idAlert, dateFrom, dateTo, dateIssued, severity,  description):
    alert_template = {
        "id": "",
        "type": "Alert",
        "category": {
            "value": "water"
        },
        "subCategory": {
            "value": "water_leakage"
        },
        "validTo": {
            "value": "2017-01-02T10:25:55.00Z"
        },
        "description": {
            "value": ""
        },
        "location": {
            "type": "geo:json",
            "value": {
                "type": "Point",
                "coordinates": [27.9595, 45.2652]
            }
        },
        "dateIssued": {
            "type": "DateTime",
            "value": "2017-01-02T09:25:55.00Z"
        },
        "alertSource": {
            "value": ""
        },
        "validFrom": {
            "type": "DateTime",
            "value": "2017-01-02T09:25:55.00Z"
        },
        "severity": {
            "value": ""
        }
    }

    alert_template["id"] = idAlert
    alert_template["validTo"]["value"] = dateTo
    alert_template["validFrom"]["value"] = dateFrom
    alert_template["dateIssued"]["value"] = dateIssued
    
    alert_template["severity"]["value"] = severity
    alert_template["description"]["value"] = description
    
    json_alert = json.dumps(alert_template)
    
    return json_alert

def consumption(idPrediction, value, dateFrom, dateTo):
    consumption_def = {
        "id": None,
        "type": "Consumption",
        "category": {
            "type": "Text",
            "value": "water",
            "metadata": {}
        },
        "subCategory": {
            "type": "Text",
            "value": "water-consumptiopn-prediction",
            "metadata": {}
        },
        "consumption": {
            "type": "Number",
            "value": None,
            "metadata": {},
        },
        "consumptionMax": {
            "type": "Number",
            "value": None,
            "metadata": {},
        },
        "consumptionMin": {
            "type": "Number",
            "value": None,
            "metadata": {},
        },
        "consumptionUnit": {
            "type": "Text",
            "value": "m3",
            "metadata": {}
        },
        "consumptionFrom": {
            "type": "DateTime",
            "dateFrom": "",
            "metadata": {}
        },
        "consumptionTo": {
            "type": "DateTime",
            "dateTo": "",
            "metadata": {}
        },
        "location": {
            "type": "geo:json",
            "value": {
                "type": "Point",
                "coordinates": [38.3402844,-0.5022438]
            },
            "metadata": {}
        },
        "address": {
            "type": "PostalAddress",
            "value": {
                "addressCountry": "Spain",
                "postalCode": "03007",
                "addressRegion": "Alicante",
                "addressLocality": "Benalua"
            },
            "metadata": {}
        }
    }
    consumption_def['id'] = idPrediction
    consumption_def['consumption']['value'] = value
    consumption_def['consumptionFrom']['dateFrom'] = dateFrom
    consumption_def['consumptionTo']['dateTo'] = dateTo
    
    json_consumption = json.dumps(consumption_def)
    
    return json_consumption

def flower_bed(idPrediction, date):
    flower_bed_template = {
        "id": "",
        "type": "FlowerBed",
        "category": {
            "value": ["FlowerBed"]
        },
        "soilMoistureVwc": {
            "value": None
        },
        "dateNextWatering": {
            "type": "DateTime",
            "value": "2017-03-31T08:00"
        },
        "soilTemperature": {
            "value": None
        },
        "address": {
            "type": "PostalAddress",
            "value": {
                "addressCountry": "",
                "streetAddress": "",
                "adressLocality": ""
            }
        },
        "location": {
        "type": "GeoProperty",
        "value": {
            "type": "Point",
            "coordinates": [0.000, 0.000]
        }
    }
    }

    flower_bed_template['id'] = idPrediction
    flower_bed_template['dateNextWatering']['value'] = date
    
    json_consumption = json.dumps(flower_bed_template)
    
    return json_consumption

