#!/usr/bin/env python

from datetime import datetime, timedelta
import time
import daylight

def testInit():
    print "---> testInit()"

    t = daylight.SunRange()

    print t.getNextSunrise(datetime.now())
    print t.getNextSunset(datetime.now())
    print t.getCurrMilestoneString()
    print "\tPASS\n"

def testMilestoneChange():
    print "---> testMilestoneChange()"

    t = daylight.SunRange()
    fake_now = datetime.now()

    hours = 92
    changeCnt = 0
    expectedCnt = (hours // 24)

    for i in range(0,hours):
        if t.milestoneComplete(fake_now):
            t.changeMilestone(fake_now)
            changeCnt += 1

        fake_now = fake_now + timedelta(hours=1)

    if changeCnt == expectedCnt:
        print "\tPASS\n"
    else:
        print "\tFAIL\n"


########################################################################
testInit()
testMilestoneChange()
