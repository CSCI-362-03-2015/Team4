
import sys
import re
import webbrowser
from os import listdir
import os
import helper

    
    
################################################################
#####Main
################################################################
def main():
         
    testCasesPath="../testCases/"   

    os.chdir(testCasesPath)#changes current directory 

    testCaseList = helper.filterDir(sorted(os.listdir(testCasesPath)))# Store a list of files in the directory

    pyFiles =[]# List to store py execuable file
    
    pyInput =[]# List of inputs for each testCase file
    testMethodList=[]# list of methods for each testCase
    testReqs=[]# List of Tested Requirements from each file testCase file

    
    ###########################################################

    #iterates through each file in the dir
    #finds the data needed
    # and appends it to its related list 
    i=0
    for file in testCaseList: 
        
        fil = open(file, "r")

        string = fil.read()

        pyFiles.append(helper.findPyfiles(string)) 
          
        pyInput.append(helper.findTestInput(string))
        testMethodList.append(helper.findMethod(string))
        
        i=i+1
        fil.close()
    
    #########################################################    

    #Search path for modules
    
    sys.path.insert(0,"../testCaseExecutables/")
    for i in range(len(testCaseList)):
        
        arg = pyInput[i].split(",")

        ###use to import a string as module
        importedM = __import__(pyFiles[i][:-3])
        
        
        exceptedOutput = importedM.testDriver(eval(arg[0]),eval(arg[1]))
        oPath= "../Output/"+ testCaseList[i][:-4]+"Output.txt"
        
        outfile =open(oPath,"w")
        outfile.write(str(exceptedOutput))
        
        outfile.close()
        
  ######################################################## 

    pathOracle="../oracles/"
    pathOutput="../Output/"
        
    oraclesFiles= helper.filterDir(sorted(os.listdir(pathOracle)))# Creates a list of the files in the oracle directory
    outputFiles= helper.filterDir(sorted(os.listdir(pathOutput))) #Creates a list of the files in the Output directory
    
    
    
    outputList=[]#List of contents in each output file
    oracleList=[]#List of contents in each oracle file
    resultList=[]#List of Pass/Fail
        
    for i in range(len(outputFiles)):
        

        oracleContents=open(pathOracle+oraclesFiles[i],"r") #opens oracle file
        
        outContents=open(pathOutput+outputFiles[i],"r")# opens output put file

        OracleString= oracleContents.read().replace('\n','') #reads oracle file

        OutcontentString=outContents.read().replace('\n','')#reads output file
        
        
        oracleList.append(OracleString)
        outputList.append(OutcontentString)
 
        
        #Compares the tested result with the oracle 
        #and appends Pass to $resultList if they are equal 
        #and Fail if not
        outString = str(OutcontentString)
        outOracle = str(OracleString)

        
        if outOracle == outString:
            
            resultList.append("Pass")
        else:
            
            resultList.append("Fail")


    # creates a html file and write to it.   
    helper.writeHtml()# see method
    
    
    # appends  to the report.html file
    with open("../reports/report.html","a") as htmlfile:
        htmlfile.write(helper.firstTableRow())

        #Creates a row in the table for each test case
        for i in range(len(pyFiles)):


            #Create a row in the table and writes in the data from the lists
            htmlfile.write(helper.addTableRow(i+1,testMethodList[i], pyInput[i], pyFiles[i], outputList[i],oracleList[i], resultList[i]))

        #writes the closing to the  file html(</html>)     
        htmlfile.write(helper.endHtml())

        htmlfile.close()
        
        
    url= "../reports/report.html"
        
    webbrowser.open(url)
        

main()
