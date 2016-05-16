# Unofficial SDK for MobileAppTracking Service APIs

Install from PyPi
```bash
pip install --upgrade umat
```

Configuration file contents:
```ini
[main]
api_key = YOUR_API_KEY

[export]
advertiser_id = YOUR_ADVERTISER_ID
timeout = 300  # seconde
delay = 30  # seconde
limit = 2000000
```

Sample:
```python
# -*- coding: utf-8 -*-
from umat import (
    AdvertiserReportCohortValues
    AdvertiserReportLogInstalls
)
from datetime import datetime


config_filename = 'config.ini'


log_endpoint = AdvertiserReportLogInstalls(config_filename)
log_endpoint.params.start_date = datetime(2016, 1, 10, 9)
log_endpoint.params.end_date = datetime(2016, 1, 10, 14)
log_endpoint.params.timezone = 'utc'
log_endpoint.params.fields = ['publisher_id', 'publisher.name', 'revenue_usd']
result_df = log_endpoint.get_dataframe()


cohort_endpoint = AdvertiserReportCohortValues(filename)
cohort_endpoint.params.end_date = datetime(2016, 1, 10)
cohort_endpoint.params.start_date = datetime(2016, 1, 10)
cohort_endpoint.params.timezone = 'UTC'
cohort_endpoint.params.fields = ['publisher_id', 'publisher.name', 'revenues_usd']
cohort_endpoint.params.update({
    'aggregation_type': 'cumulative',
    'cohort_type': 'install',
    'interval': 'year_day',
})
result_df = cohort_endpoint.get_dataframe()
```
