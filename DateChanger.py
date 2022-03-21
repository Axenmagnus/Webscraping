#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 17:44:42 2021

@author: magnusaxen
"""

import re


def DateChanger(drag,push,url,increment):
    '''
    

    Parameters
    ----------
    drag : Datetype
        Start date we want to check date between.
    push : Datetype
        End date we want to check date between.
    url : String
        Url of website.
    increment : Datetype
        1 day push between date.

    Returns
    -------
    newurl : String
        Adjusted string with new dates.
    drag : Datetype
        Drag pushed one day forward.
    push : Datetype
        Push pushed one day forward.

    '''
    
    yearDrag=drag.year
    monthDrag=drag.month
    dayDrag=drag.day
    yearPush=push.year
    monthPush=push.month
    dayPush=push.day
    seperation=url.split("min")
    split2=seperation[1].split("max")
    
    og=seperation[0]
    
    firstdate = split2[0]
    lastdate = split2[1]
    
    firstsplit = re.split("A|F",firstdate)
    lastsplit = re.split("A|F",lastdate)
    
    
    temp1=str(str(monthDrag) +firstsplit[1][firstsplit[1].find("%"):len(firstsplit[1])])
    temp2=str(str(dayDrag) +firstsplit[2][firstsplit[2].find("%"):len(firstsplit[2])])
    temp3=str(str(yearDrag) +firstsplit[3][firstsplit[3].find("&"):len(firstsplit[3])])
    
    temp4=str(str(monthPush) +lastsplit[1][lastsplit[1].find("%"):len(lastsplit[1])])
    temp5=str(str(dayPush) +lastsplit[2][lastsplit[2].find("%"):len(lastsplit[2])])
    temp6=str(str(yearPush) +lastsplit[3][lastsplit[3].find("&"):len(lastsplit[3])])
    temp4=temp1
    temp5=temp2
    #temp6=temp3
    
    newurl=(og + "min" + firstsplit[0] + "A" + temp1 + "F" +temp2 + "F" +temp3.replace("_", "")  + "%2Ccd_" + "max" + lastsplit[0]+ "A" +  temp4 + "F" + temp5 + "F" + temp6)
    
    
    push=push+increment
    drag=drag+increment
    
    
    return newurl,drag,push
