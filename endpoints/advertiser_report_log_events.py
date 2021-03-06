# -*- coding: utf-8 -*-
from .advertiser_report_log import AdvertiserReportLog


class AdvertiserReportLogEvents(AdvertiserReportLog):
    # I don't like long hierarchy of properties
    @property
    def export_url(self):
        url = 'http://api.mobileapptracking.com/v3/logs/advertisers/{id}/exports/events'
        return url.format(id=self.advertiser_id)
