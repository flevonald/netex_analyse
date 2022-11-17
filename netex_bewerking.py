# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import xml.etree.ElementTree as xee
import pandas as pd
import os

import zlib

import gzip
#%%
netex_bestand = r"C:\data\Netex\NeTEx_CXX_VZ_20221117_2022-12-11_202300001_baseline.xml.gz"
ns = {'ns':'http://www.netex.org.uk/netex'}
#%% Uitpakken met ZLIB
f_out = gzip.open(netex_bestand, 'rb')    
'''
vervangen door zlib?
'''
#%%
doc = xee.parse(f_out)
root = doc.getroot()
dataObjects = root.find('ns:dataObjects', ns)
CompositeFrame = dataObjects.find('ns:CompositeFrame', ns)

versie = CompositeFrame.find('ns:versions', ns).find('ns:Version', ns)
StartDate = versie.find('ns:StartDate', ns).text
EndDate = versie.find('ns:EndDate', ns).text

frames = CompositeFrame.find('ns:frames', ns)

#serviceframe
ServiceFrame = frames.find('ns:ServiceFrame', ns)

lines = ServiceFrame.find('ns:lines', ns)
lijn = {<BrandingRef ref="CXX:Branding:HERMES"/>
x = lines[0]
def parse_line(x)
    {'branding': x.find('ns:BrandingRef',ns).attrib['ref'],
    'Name': x.find('ns:Name',ns).text,
    'TransportMode': x.find('ns:TransportMode',ns).text,
    'PublicCode': x.find('ns:PublicCode',ns).text,
    'PrivateCode': x.find('ns:PrivateCode',ns).text ,
    'TypeOfServiceRef': x.find('ns:TypeOfServiceRef',ns).text,
    'Monitored': x.find('ns:Monitored',ns).text,
    }
<Name>Wageningen Busstation - Ede-Wageningen Station</Name>
<TransportMode>bus</TransportMode>
<PublicCode>86</PublicCode>
<PrivateCode type="LinePlanningNumber">A086</PrivateCode>
<ExternalLineRef type="VetagLineNumber" ref="86"/>
<AuthorityRef ref="DOVA:Authority:GLD"/>
<TypeOfServiceRef ref="BISON:TypeOfService:Standaard"/>
<Monitored>true</Monitored>
<AccessibilityAssessment id="CXX:AccessibilityAssessment:A086">
<MobilityImpairedAccess>true</MobilityImpairedAccess>
</AccessibilityAssessment>}
branding

df_lines = 
routePoints

routeLinks


for child in lines :
    print(child.tag, child.attrib)

    #lijnen
#routes

#dru?