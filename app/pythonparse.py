# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 22:24:52 2020

@author: student
"""
from flask import render_template
from app import app
import re
import datetime
from datetime import timedelta
@app.route('/result')
def pythonparse(myfile):
    c =0
    datepattern = '%m/%d/%y: %H:%M'
     
    datalist = []

    spenttime = datetime.time(hour = 0,minute =0)
   
    with open(myfile, 'r') as f:
        file = f.read()
    r = re.findall(r'(\d+/\d+\d+/\d+\d+: \d+:\d+\d+pm - \d+:\d+\d+am)',file)
    x = re.findall(r'(\d+/\d+\d+/\d+\d+: \d+:\d+\d+am - \d+:\d+\d+pm)',file)
    y = re.findall(r'(\d+/\d+\d+/\d+\d+: \d+:\d+\d+am - \d+:\d+\d+am)',file)
    z = re.findall(r'(\d+/\d+\d+/\d+\d+: \d+:\d+\d+pm - \d+:\d+\d+pm)',file)
    difftimer = datetime.datetime(100,1,1,0,0)
    for elementr in r:
        r1 = elementr.split(" ")
   
        if('12' in r1[1]):
            r[1] = r[1].replace('12','00')
        beginingtimer = datetime.datetime.strptime(r1[0]+' '+r1[1].strip('pm'),datepattern)
        endtimer = datetime.datetime.strptime(r1[0]+' '+r1[3].strip('am'),datepattern)
   
        second1 =((12- beginingtimer.hour)+endtimer.hour)*3600
   
        second2 = endtimer.minute*60-beginingtimer.minute*60
        c = second1+second2
    
           
    
    
    for element in y:
        y1 = element.split(' ')
        beginingtime = datetime.datetime.strptime(y1[0]+' '+y1[1].strip('am'),datepattern)
        endtime = datetime.datetime.strptime(y1[0]+' '+y1[3].strip('am'), datepattern)
       
        difftime= endtime-beginingtime
        
        c = c + difftime.seconds
    
    for elementz in z:
        z1 = elementz.split(" ")
        if('12'in z1[1]):
            z1[1] = z1[1].replace('12','00')

        beginingtimez = datetime.datetime.strptime(z1[0]+' '+z1[1].strip('pm'),datepattern)
        endtimez = datetime.datetime.strptime(z1[0]+' '+z1[3].strip('pm'),datepattern)
        difftimez =endtimez - beginingtimez
       
        c = c+difftimez.seconds
    
    
    for elementx in x:
        x1 = elementx.split(" ")
        if('12'in x1[1]):
            x1[1] = x1[1].replace('12','00')
    
        character = x1[3][0:x1[3].find(':')]
        f = int(x1[3][0:x1[3].find(':')])
    
        if(int(f)<12):
            f = f+12
        x1[3]= x1[3].replace(character,str(f))
        beginingtimex = datetime.datetime.strptime(x1[0]+' '+x1[1].strip('am'),datepattern)
        endtimex = datetime.datetime.strptime(x1[0]+' '+x1[3].strip('pm'),datepattern)
        difftimex =endtimex - beginingtimex
        c = c+ difftimex.seconds
        
    a = c/3600
    return render_template('result.html',a =a)
    
    
    
