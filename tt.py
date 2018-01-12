

from xml.dom.minidom import parse
import xml.dom.minidom
import csv

def writeToCSV(myDatas):
    with open('output3.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['FirstName','LastName','Premium','Age','Town','Country','Pincode','PolicyNumber'])
        for myData in myDatas:
            Insurers = myData.getElementsByTagName("Insurer")

        for Insurer in Insurers:
            #For Name Tag

            Fn,Ln=nameFun(Insurer)
            #for Premium Tag
            pr=premiumFun(Insurer)
            #for Age Tag
            ag=ageFun(Insurer)
            #for address tag
            tn,cn,pn=addressFun(Insurer)
            #for Policy NUmber tag
            pnum=policyFun(Insurer)
            writer.writerow([Fn] +[Ln] + [pr] + [ag]+[tn]+[cn]+[pn] + [pnum] ) # write to csv

def nameFun(Insurer):
    names = Insurer.getElementsByTagName("Name")
    for Name in names:
        FirstNames = Name.getElementsByTagName("FirstName")
        for FirstName in FirstNames:
            Fn = FirstName.childNodes[0].data
        LastNames = Name.getElementsByTagName("LastName")
        for LastName in LastNames:
            Ln = LastName.childNodes[0].data
    return Fn,Ln

def  premiumFun(Insurer):
    premiums = Insurer.getElementsByTagName("Premium")
    for premium in premiums:
        pr = premium.childNodes[0].data
    return pr

def ageFun(Insurer):
    Ages = Insurer.getElementsByTagName("Age")
    for age in Ages:
        ag = age.childNodes[0].data
    return ag

def addressFun(Insurer):
    addresses = Insurer.getElementsByTagName("Address")
    for address in addresses:
        Towns = address.getElementsByTagName("Town")
        for town in Towns:
            tn = town.childNodes[0].data
        Countries = address.getElementsByTagName("Country")
        for country in Countries:
            cn = country.childNodes[0].data
        Pincodes = address.getElementsByTagName("Pincode")
        for pincode in Pincodes:
            pn = pincode.childNodes[0].data
    return tn,cn,pn

def policyFun(Insurer):
    PolicyNumbers = Insurer.getElementsByTagName("PolicyNumber")
    for policyNumber in PolicyNumbers:
        pnum = policyNumber.childNodes[0].data
    return pnum

import validation
xml_result,xsd_result=validation.validate()
if xml_result==1&xsd_result==1:
    doc = parse('user_data.xml')
    myDatas = doc.getElementsByTagName("Hcsc")
    writeToCSV(myDatas)


