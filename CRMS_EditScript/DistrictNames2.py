# CRMS string processor
# Replace District Names


# Code Compliance District
def DNames(textDN):
    text01_DN = textDN.replace('NORTHEASTC-Code Compliance Sub-Districts (SW NCSCNWSENECE - ABC) NORTHEAST-Code Compliance District ','NE_SubC_INXWW,')
    text02_DN = text01_DN.replace('NORTHEAST-Code Compliance District ','NE_INXWW,')
    text03_DN = text02_DN.replace('SOUTHWEST-Code Compliance District ','SW_INXWW,')
    

# Multi-Tenant District areas

    text01_MT = text03_DN.replace('WEST-Multi Tenant District ','W-MTD_INXZZ,')
    text02_MT = text01_MT.replace('EAST-Multi Tenant District ','E-MTD_INXZZ,')

# Inspector Areas
    text01_IA = text02_MT.replace('SOUTHWEST-Code Inspector Area ','SW-InspArea_INXYY,')
    text02_IA = text01_IA.replace('NORTHEAST-Code Inspector Area ','NE-InspArea_INXYY,')
    text03_IA = text02_IA.replace('-Code Inspector Area ','-InspArea_INXYY,')
    

# Departments
    text01_DE  = text03_IA.replace(' - AVI,',',AVI,')
    text1a_DE  = text01_DE.replace(' - BI/DCC,',',BI,')
    text1b_DE  = text1a_DE.replace(' -BI/DCC,',',BI,')
    text1c_DE  = text1b_DE.replace('  - CCS,',',CCS,')
    text2a_DE  = text1c_DE.replace(' - CCS,',',CCS,')
    text2b_DE  = text2a_DE.replace(' -CCS,',',CCS,')
    text2c_DE  = text2b_DE.replace(' -  CCS,',',CCS,')
    text2d_DE  = text2c_DE.replace('-CCS,',',CSS,')
    text2e_DE  = text2d_DE.replace('- CCS,',',CCS,')
    text2f_DE  = text2e_DE.replace(' - CTY,',',CTY,')
    text03_DE  = text2f_DE.replace(' - CAO,',',CAO,')
    text04_DE  = text03_DE.replace(' - CES,',',CES,')
    text4a_DE  = text04_DE.replace(' - DCC,',',DCC,')
    text05_DE  = text4a_DE.replace(' - DEV,',',DEV,')
    text06_DE  = text05_DE.replace(' - DFD,',',DFD,')
    text7a_DE  = text06_DE.replace(' -  DPD,',',DPD,')
    text7b_DE  = text7a_DE.replace(' - DPD,',',DPD,')
    text7c_DE  = text7b_DE.replace(' -DPD,',',DPD,')
    text7d_DE  = text7c_DE.replace(' - EBS,',',EBS,')
    text7e_DE  = text7d_DE.replace(' - FHG,',',FHG,')
    text08_DE  = text7e_DE.replace(' - FIN,',',FIN,')
    text09_DE  = text08_DE.replace(' - Hotel/Motel,',',H/M,')
    text09a_DE = text09_DE.replace(' - HOU,',',HOU,')
    text09b_DE = text09a_DE.replace(' - HRS,',',HRS,')
    text09c_DE = text09b_DE.replace(' - LIB,',',LIB,')
    text10_DE  = text09c_DE.replace(' - OEQ,',',OEQ,')
    text10a_DE = text10_DE.replace(' - OFS,',',OFS,')
    text11_DE  = text10a_DE.replace(' - PKR,',',PKR,')
    text11a_DE = text11_DE.replace(' - Parks,',',PKR,')
    text12_DE  = text11a_DE.replace(' - PWT,',',PWT,')
    text12a_DE = text12_DE.replace(' -PWT,',',PWT,')
    text13_DE  = text12a_DE.replace(' - SAN,',',SAN,')
    text13a_DE = text13_DE.replace(' - Missed SAN (GARBAGE),',' Missed,SAN,')
    text13b_DE = text13a_DE.replace('-Stop Service,',' Stop Svc,SAN,')
    text14_DE  = text13b_DE.replace(' - SCS,',',SCS,')
    text14a_DE = text14_DE.replace(' - SEC,',',SEC,')
    text15_DE  = text14a_DE.replace(' - SDC,',',SDC,')
    text16a_DE = text15_DE.replace('-STS,',',STS,')
    text16b_DE = text16a_DE.replace(' - STS,',',STS,')
    text16c_DE = text16b_DE.replace('-STS (DISPATCH),',',STS,')
    text17a_DE = text16c_DE.replace('-TWM,',',TWM,')
    text17b_DE = text17a_DE.replace(' - TWM,',',TWM,')
    text17c_DE = text17b_DE.replace(' -TWM-SWQ,',',TWM,')
    text18_DE  = text17c_DE.replace(' - Water Administration,',',WTR,')
    text18a_DE = text18_DE.replace(' - WTR,',',WTR,')
    return text18a_DE
