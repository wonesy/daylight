#!/usr/bin/env python

import bibliopixel
import json
import urllib2
from datetime import datetime, timedelta
import ephem
import time

class SunRange:

    """
    """
    def __init__(self, lon='-122.6819', lat='45.52'):
        self.timeStart = datetime.now()
        self.timeEnd = datetime.now()
        self.hourLag = 0
        self.sun = ephem.Sun()
        self.obs = ephem.Observer()
        self.obs.lon = lon
        self.obs.lat = lat

        '''
        Start the initial milestone upon initialization
        '''
        tmp_rise = self.getNextSunrise(datetime.now())
        tmp_set  = self.getNextSunset(datetime.now())

        yesterday = datetime.now() - timedelta(1)
        self.obs.date = yesterday
        self.sun.compute()

        # Whichever comes next in time is our current milestone
        if (tmp_rise < tmp_set):
            self.currMilestone = self._SUNRISE_MILESTONE()
            self.timeEnd = tmp_rise
            self.timeStart = ephem.localtime(self.obs.next_setting(self.sun))
        else:
            self.currMilestone = self._SUNSET_MILESTONE()
            self.timeEnd = tmp_set
            self.timeStart = ephem.localtime(self.obs.next_rising(self.sun))

    """
    """
    def changeMilestone(self, date):
        self.timeStart = self.timeEnd

        # When we change the next timeEnd, we need to get tomorrow's information
        if self.currMilestone == self._SUNSET_MILESTONE():
            self.currMilestone = self._SUNRISE_MILESTONE()
            self.timeEnd = self.getNextSunset(date + timedelta(1))
            print "CHANGE TO SUNRISE MILESTONE"
        else:
            self.currMilestone = self._SUNSET_MILESTONE()
            self.timeEnd = self.getNextSunrise(date + timedelta(1))
            print "CHANGE TO SUNSET MILESTONE"
            
    """
    """
    def milestoneComplete(self, date):
        if date >= self.timeEnd:
            return True

        return False
    """
    """
    def getNextSunrise(self, date):
        now = date.strftime("%Y/%m/%d %H:%M:%S")
        self.obs.date = now
        self.sun.compute()

        return ephem.localtime(self.obs.next_rising(self.sun))

    """
    """
    def getNextSunset(self, date):
        now = date.strftime("%Y/%m/%d %H:%M:%S")
        self.obs.date = now
        self.sun.compute()

        return ephem.localtime(self.obs.next_setting(self.sun))

    """
    """
    def getCurrMilestoneString(self):
        if self.currMilestone == self._SUNRISE_MILESTONE():
            return "sunrise"
        elif self.currMilestone ==self._SUNSET_MILESTONE():
            return "sunset"
        else:
            return "error"

    """
    """
    def getCurrMilestone(self):
        return self.currMilestone

    """
    """
    def _SUNRISE_MILESTONE(self):
        return 0xFFFFFFFF

    """
    """
    def _SUNSET_MILESTONE(self):
        return 0x00000000



'''
algorithm:

1) start = either sunset or sunrise
2) determine time/px (this will be the rate at which we can update)
    *NOTE* possible that colors can be adjusted to achieve more of a continuum & a finer update cadence
3) 
'''
