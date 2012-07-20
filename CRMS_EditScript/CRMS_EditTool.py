#CRMS_EditTool.py
#
###Changes made: Added Header. Added complete address field 

################################################################

# Open files and report to runlog

# Version 4: 

import sys
from datetime import date
DateNow = date.today()

KeyPath = 'D:/CRMStestFile/InputFile'
ScriptPath = 'D:/CRMStestFile/CRMS_EditScript'
OutputPath = 'D:/CRMStestFile/OutputFile'
getFile = ''

#input_file = sys.argv[1]     |
#output_path = sys.argv[2]    |
#print input_file             |  option input
#print output_path            |
#print sys.argv               |

#sys.exit()                   |

# runlog is file to print header/date of input file ran.
runlog = open(ScriptPath + '/' + 'runlog.txt' ,'a')
print >> runlog, 'Script attempt begins:'


################################################################
####  Pre-Process script to obtain correct file name,
####  help or terminate script.

while 1:
    try:
        getFile = raw_input('Enter file name to process. File Example: NE2009.txt.  Or type \
"TERMINATE" or "HELP":')
        Str1 = open(KeyPath + '/' + getFile,'r')
        print >> runlog,'\t', getFile + " file found. " + str(DateNow)
        print >> runlog, '\t', Str1
        Str1.close()
        break
    except:
        if 'TERMINATE' in getFile:
            print >> runlog, '\t', "Request has been made to terminate." + str(DateNow)
            print >> runlog, '\n'
            runlog.close()
            sys.exit()
        elif 'HELP' in getFile:
            print >> runlog, '\t', "Request for HELP has been made."
            raw_input('Check folder for correct file name and extention. \
Also check pathway.  \n \n Was this script downloaded?\n\n \
Then the pathway "KeyPath" needs to be corrected.   Hit enter to continue.\n\n \
Or hit enter to continue and type "MORE" for more help information.\n')
        elif 'MORE' in getFile:
            raw_input('Text files to be processed are to be placed in an input \
folder. Change pathway for input folder at KeyPath.  getFile variable will be the \
file it will be looking for on this pathway or the script will continue to prompt \
for a correct file name.\n\n The runlog.txt will document bad file names and pathways \
used as well as other information such as the header file of the input file. \
The specific source used of input files always has a header file.\n\n Change the \
ScriptPath path also used for the script location as well as log pathways.\n\n \
TERMINATE will ask "Yes" or "No" to exit and it is okay to say \
yes as a no may hang up or keep script running but now allow restart of the script. \
If program gets hung up, close and restart.\n\n  Other problems that may occur is the \
pathway of the Python shell which will show up as an error when trying to read the \
and import the UniqueNames and DNames module.  See Learning Python for explanation. \
Hit enter to continue.')
        else:
            print >> runlog, '\t', getFile + " is not a valid file or pathway, "

#################################################3
        
Str1 = open(KeyPath + '/' + getFile,'r')
# Read first line and report to runlog with date stamp
ReportStr = Str1.readline()

# The .readline() method includes a line return that is not wanted.
# So a replace method to the ReportStr object is used to replace
# \n with "", or nothing.

ReportInfo = ReportStr.replace("\n",",")
ReportInfo += str(DateNow)

# Report to runlog header file and date
print >> runlog,'\tRan script: ' + ReportInfo

# Run count file module
ReportInfo = Str1.next()
getFilePt = getFile.replace('.txt','')
################################################################


# Open output files.  MainText1.txt for fields 1-13.
MainText1 = open(OutputPath + '/' + getFilePt + '_1MnTx' + str(DateNow) + '.txt','w')

# Open output files GeoText1.txt for fields 1 and 14.
GeoText1  = open(OutputPath + '/' + getFilePt + '_1GeoTx' + str(DateNow) + '.txt','w')

# Open output files OtherText1.txt for fields 15 - 22.
OtherText1 = open(OutputPath + '/' + getFilePt + '_1OthTx' + str(DateNow) + '.txt','w')


print >> runlog, '\t', MainText1
print >> runlog, '\t', GeoText1
print >> runlog, '\t', OtherText1
##################################################################
##################################################################

# Read next lines should be data.  If the header is greater than
# one line, then next line will read entire header is outputted to
# runlog.
##################################################################
##################################################################

# add header to outputfile
print >> MainText1,"FILEID,SR,SR_TYPE,DEPT,ADDRESS,ST_NUM,ST_DIR,ST_NAME,ST_TYPE,OTH1,CITY,ST,ZIP,OTH2,OTH3,OTH4,OTH5"
print >> GeoText1,"FILEID,SR,F3,F4,F5,F6,F7,F8,F9,F10,F11,F12,F13,F14,F15,F16,F17"
print >> OtherText1, "FILEID,SR,F3,F4,F5,F6,F7"
##################################################################
##################################################################
# Second line is inputted into while statement and the while statement

NewLine = Str1.next()
count = 0
# While statement used to run all lines
while NewLine:
        # check NewLine object meets condition in "if" statement
        # for end of line.
    if "End of File" in NewLine:
        print >> MainText1, "EndOfLineCodeBreak"
        print >> GeoText1, "EndOfLineCodeBreak"
        print >> OtherText1, "EndOfLineCodeBreak"
        Str1.close()
        MainText1.close()
        GeoText1.close()
        OtherText1.close()
        # break will terminate if statement within while
        # statement and bypass else statement.
        break
    # If statement not true, else statement will process each line.
    else:
        # start count after header added
        count += 1
        # New object LineChg to receive change to NewLine, removal of \n
        LineChg = NewLine.replace('\n','')
        # LineSplit new object to receive change of LineChg split
        LineSplit = LineChg.split(',')
        # New oject OutGeoData to recieve new string arrangement in split.
        OutGeoData = LineSplit[0] + ',' + LineSplit[14]
        # New object OutMainData to receive new string arrangment in split.
        # The use of list may have be possilbe but object type different
        # than OutGeoData
        
        if 'E' in LineSplit[3]:
            ChgLineHere = LineSplit[2] + ' ' + LineSplit[3] + ' ' + LineSplit[4] + ' ' + LineSplit[5] + ','
        elif 'W' in LineSplit[3]:
            ChgLineHere = LineSplit[2] + ' ' + LineSplit[3] + ' ' + LineSplit[4] + ' ' + LineSplit[5] + ','
        elif 'S' in LineSplit[3]:
            ChgLineHere = LineSplit[2] + ' ' + LineSplit[3] + ' ' + LineSplit[4] + ' ' + LineSplit[5] + ','
        elif 'N' in LineSplit[3]:
            ChgLineHere = LineSplit[2] + ' ' + LineSplit[3] + ' ' + LineSplit[4] + ' ' + LineSplit[5] + ','
        else:
            ChgLineHere = LineSplit[2] + ' ' + LineSplit[4] + ' ' + LineSplit[5] + ','
        
        OutMainData = (LineSplit[0] + ',' +
               LineSplit[1] + ',' +
               ChgLineHere  +
               LineSplit[2] + ',' +
               LineSplit[3] + ',' +
               LineSplit[4] + ',' +
               LineSplit[5] + ',' +
               LineSplit[6] + ',' +
               'DALLAS'     + ',' +
               'TX'         + ',' +
               LineSplit[9] + ',' +
               LineSplit[10] + ',' +
               LineSplit[11] + ',' +
               LineSplit[12] + ',' +
               LineSplit[13])
        # New object OtherData to receive string arrangement in split
        OtherData = (LineSplit[0] + ',' +
               LineSplit[15] + ',' +
               LineSplit[16] + ',' +
               LineSplit[17] + ',' +
               LineSplit[18] + ',' +
               LineSplit[19] + ',' +
               LineSplit[20] + ',' +
               LineSplit[21] + ',' +
               LineSplit[22])
        # Print outputs of new objects to individual text files.
        print >> MainText1, str(count) + "," + OutMainData
        print >> GeoText1, str(count) + "," + OutGeoData
        print >> OtherText1, str(count) + "," + OtherData
        NewLine = Str1.next()
    continue




# Begin Part II
MainText1 = open(OutputPath + '/' + getFilePt + '_1MnTx' + str(DateNow) + '.txt','r')
GeoText1  = open(OutputPath + '/' + getFilePt + '_1GeoTx' + str(DateNow) + '.txt','r')
OtherText1 = open(OutputPath + '/' + getFilePt + '_1OthTx' + str(DateNow) + '.txt','r')

MainText2 = open(OutputPath + '/' + getFilePt + '_2MnTx' + str(DateNow) + '.txt','w')
GeoText2  = open(OutputPath + '/' + getFilePt + '_2GeoTx' + str(DateNow) + '.txt','w')
OtherText2 = open(OutputPath + '/' + getFilePt + '_2OthTx' + str(DateNow) + '.txt','w')

print >> runlog, "\tPart II of script engaged."

# Read line and skip header
NewLine = MainText1.readline()

# Read line for line input
while NewLine:
    if "EndOfLineCodeBreak" in NewLine:
        print >> MainText2, "EndOfLineCodeBreak"
        MainText1.close()
        MainText2.close()
        break
    else:
        from DistrictNames import DNames
        from UniqueNames1 import NamesUnique
        LineChg = NewLine.replace('\n','')
        NameChg = NamesUnique(LineChg)
        NameChg2 = DNames(NameChg)
        print >> MainText2, NameChg2
        NewLine = MainText1.next()
    continue


NewLine = GeoText1.readline()
while NewLine:
    if "EndOfLineCodeBreak" in NewLine:
        print >> GeoText2, "EndOfLineCodeBreak"
        GeoText1.close()
        GeoText2.close()
        break
    else:
        from UniqueNames1 import NamesUnique
        from DistrictNames2 import DNames
        LineChg = NewLine.replace('\n','')
        NameChg = NamesUnique(LineChg)
        NameChg2 = DNames(NameChg)
        print >> GeoText2, NameChg2
        NewLine = GeoText1.next()
    continue

NewLine = OtherText1.readline()
while NewLine:
    if "EndOfLineCodeBreak" in NewLine:
        print >> OtherText2, "EndOfLineCodeBreak"
        OtherText1.close()
        OtherText2.close()
        break
    else:
        LineChg = NewLine.replace('\n','')
        print >> OtherText2, LineChg
        NewLine = OtherText1.next()
    continue

print >> runlog, "\tProcess completed ",  str(DateNow)
print >> runlog, "\tSee output file for new files created."
print >> runlog, '\n'
runlog.close()

            
