# CRMS replace Module
# ReplaceScript
# replaces one time strings that are unique


def NamesUnique(AllNames):
    text01 = AllNames.replace('-City Service Area (Svc. Coor. Team) ','SVAr_IDXAA,')
    text1a = text01.replace('-Animal Control District ','-ACD_IDXAB,')
    text02 = text1a.replace('-Building Inspection District ','-BI_IDXBB,')
    text03 = text02.replace('-Census Tract ','-CT_IDXCC,')
    text04 = text03.replace('-Council District ','-CD_IDXDD,')
    text05 = text04.replace('-Mapsco Page-Zone ','_IDXEE,')
    text06 = text05.replace('-Multi-Tenant Inspector ','-MT_Insp_IDXFF,')
    text07 = text06.replace('-Police Beat ','-PB_IDXGG,')
    text08 = text07.replace('-Sanitation District ','-SD_IDXHH,')
    text09 = text08.replace('-Streets Customer Service Area ','-St_CSA_IDXII,')
    text10 = text09.replace('-Garbage Pick-up Day','-GPD_IDXJJ')
    text11 = text10.replace('-Brush Collection Week ','-BCW_IDXKK,')
    text12 = text11.replace('-Fire District ','-FD_IDXLL,')
    text13 = text12.replace('-Recycling Day ','-RD_IDXMM,')
    text14 = text13.replace('-Street Maint Area ','-SMA_IDXNN,')
    text15 = text14.replace('Graffiti Abatement Request,','Graffiti Abatement Request,CCS,')
    text16 = text15.replace('Graffiti Private Property - Residential/Commercial,','Graffiti Private Property - Residential/Commercial,CCS,')
    text17 = text16.replace('Graffiti Consent Form,','Graffiti Consent Form,CCS,')
    text18 = text17.replace('Vegetation Removal Request,','Vegetation Removal Request,CCS,')
    text19 = text18.replace('Heavy Clean Request,','Heavy Clean Request,CCS,')
    text20 = text19.replace('Litter Removal Request,','Litter Removal Request,CCS,')
    text21 = text20.replace('Closure Request,','Closure Request,CCS,')
    text22 = text21.replace('STEP License,','STEP License,CCS,')
    text23 = text22.replace('Graffiti Private Property -  Apartments,','Graffiti Private Property -  Apartments,CCS,')
    text24 = text23.replace('Pool Inspection - Apartments,','Pool Inspection - Apartments,CCS,')
    text25 = text24.replace('Delinquent M/F License fee,','Delinquent M/F License fee,CCS,')
    text26 = text25.replace('Urban Rehab CAO Docket,','Urban Rehab CAO Docket,CAO,')
    text27 = text26.replace('Code Environmental Compliance,','Code Environmental Compliance,CCS,')
    text28 = text27.replace('Mow Clean Tire Removal,','Mow Clean Tire Removal,CCS,')
    text29 = text28.replace(',311 Call Center Complaint,',',311 Call Center Complaint,C311,')
    text30 = text29.replace('STEP Decal,','STEP Decal,CCS,')
    text31 = text30.replace('Sign Removal Request,','Sign Removal Request,CCS,')
    text32 = text31.replace('Wood Vendor License,','Wood Vendor License,BI,')
    return text32

# not used
def CountFiles(Process):
    count = 0
    Execut = Process.readline()
    RunExecut = Execut.next()
    while 1:
        if "End of File" in RunExecut:
            break
        else:
            count += 1
            RunExecut = Execut.next()
        continue
    return count


