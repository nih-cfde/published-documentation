#!/usr/bin/env python3

##########################################################################################
#                                     AUTHOR INFO
##########################################################################################

# Arthur Brady (Univ. of MD Inst. for Genome Sciences) wrote this script to automatically
# load and summarize (via term-tracking TSV files) controlled-vocabulary term usage across
# all core resource entity records in a given C2M2 Level 1 ETL instance to assist with
# instance preparation prior to ingestion into a central CFDE database.

# Creation date: 2020-05-17
# Lastmod date unless I forgot to change it: 2020-05-29

# contact email: abrady@som.umaryland.edu

import os
import json
import re
import sys

##########################################################################################
##########################################################################################
##########################################################################################
#                          CONSTANT PARAMETERS: DO NOT MODIFY
##########################################################################################
##########################################################################################
##########################################################################################

##########################################################################################
# Map of CV names to reference files. These files should be present in cvRefDir before
# running this script.

cvFileTemplate = {
   
   'EDAM' : '{cvRefDir}/EDAM.version_1.21.tsv',
   'OBI' : '{cvRefDir}/OBI.version_2019-08-15.obo',
   'Uberon' : '{cvRefDir}/uberon.version_2019-06-27.obo',
}

##########################################################################################
# TSV filenames to scan for term usage. These files should be present in draftDir before
# running this script.

targetTSVs = ( 'file.tsv', 'biosample.tsv' )

##########################################################################################
# Term-tracker data structure.

termsUsed = {
   
   'file_format': {},
   'data_type': {},
   'assay_type': {},
   'anatomy': {}
}

##########################################################################################
##########################################################################################
##########################################################################################
#                   SUBROUTINES (in call order, including recursion)
##########################################################################################
##########################################################################################
##########################################################################################

####### progressReport ###################################################################
# 
# CALLED BY: main execution thread
# 
# Print a logging message to STDERR.
# 
#-----------------------------------------------------------------------------------------

def progressReport( message ):
   
   print('%s' % message, file=sys.stderr)

#-----------------------------------------------------------------------------------------
# end sub: progressReport( message )
##########################################################################################

def die(s):
    print(s, file=sys.stderr)
    raise Exception(s)
   

def identifyTermsUsed( termsUsed, draftDir, targetTSVs ):
   
   for basename in targetTSVs:
      
      inFile = draftDir + '/' + basename

      with open( inFile, 'r' ) as IN:
         
         header = IN.readline()

         colNames = re.split(r'\t', header.rstrip('\r\n'))

         currentColIndex = 0

         columnToCategory = dict()

         for colName in colNames:
            
            if colName in termsUsed:
               
               columnToCategory[currentColIndex] = colName

            currentColIndex += 1

         for line in IN:
            
            fields = re.split(r'\t', line.rstrip('\r\n'))

            for colIndex in columnToCategory:
               
               currentCategory = columnToCategory[colIndex]

               if fields[colIndex] != '':
                  
                  termsUsed[currentCategory][fields[colIndex]] = {}

# end sub: identifyTermsUsed(  )

def decorateTermsUsed( termsUsed, cvFile ):
   
   for categoryID in termsUsed:
      
      if categoryID == 'anatomy' or categoryID == 'assay_type':
         
         cv = ''

         if categoryID == 'anatomy':
            
            cv = 'Uberon'

         elif categoryID == 'assay_type':
            
            cv = 'OBI'

         # end if ( categoryID type check )

         refFile = cvFile[cv]

         with open( refFile, 'r' ) as IN:
            
            recording = False

            currentTerm = ''

            for line in IN:
               
               line = line.rstrip('\r\n')
            
               matchResult = re.search(r'^id:\s+(\S.*)$', line)

               if not( matchResult is None ):
                  
                  currentTerm = matchResult.group(1)

                  if currentTerm in termsUsed[categoryID]:
                     
                     recording = True

                     if 'synonyms' not in termsUsed[categoryID][currentTerm]:
                        
                        termsUsed[categoryID][currentTerm]['synonyms'] = ''

                  else:
                     
                     currentTerm = ''

                     # (Recording is already switched off by default.)

               elif not( re.search(r'^\[Term\]', line) is None ):
                  
                  recording = False

               elif recording:
                  
                  if not ( re.search(r'^name:\s+(\S*.*)$', line) is None ):
                     
                     termsUsed[categoryID][currentTerm]['name'] = re.search(r'^name:\s+(\S*.*)$', line).group(1)

                  elif not ( re.search(r'^def:\s+\"(.*)\"[^\"]*$', line) is None ):
                     
                     termsUsed[categoryID][currentTerm]['description'] = re.search(r'^def:\s+\"(.*)\"[^\"]*$', line).group(1)

                  elif not ( re.search(r'^def:\s+', line) is None ):
                     
                     die('Unparsed def-line in %s OBO file: "%s"; aborting.' % ( cv, line ) )

                  elif not ( re.search(r'^synonym:\s+\"(.*)\"[^\"]*$', line) is None ):
                     
                     synonym = re.search(r'^synonym:\s+\"(.*)\"[^\"]*$', line).group(1)

                     if termsUsed[categoryID][currentTerm]['synonyms'] != '':
                        
                        termsUsed[categoryID][currentTerm]['synonyms'] = termsUsed[categoryID][currentTerm]['synonyms'] + '|' + synonym

                     else:
                        
                        termsUsed[categoryID][currentTerm]['synonyms'] = synonym

               # end if ( line-type selector switch )

            # end for ( input file line iterator )

         # end with ( open refFile as IN )

      elif categoryID == 'file_format' or categoryID == 'data_type':
         
         cv = 'EDAM'

         refFile = cvFile[cv]

         with open( refFile, 'r' ) as IN:
            
            header = IN.readline()

            for line in IN:
               
               line = line.rstrip('\r\n')

               ( termURL, name, synonyms, definition ) = re.split(r'\t', line)[0:4]

               currentTerm = re.sub(r'^.*\/([^\/]+)$', r'\1', termURL)

               currentTerm = re.sub(r'data_', r'data:', currentTerm)
               currentTerm = re.sub(r'format_', r'format:', currentTerm)

               if currentTerm in termsUsed[categoryID]:
                  
                  # There are some truly screwy things allowed inside
                  # tab-separated fields in this file. Clean them up.

                  name = name.strip().strip('"\'').strip()

                  synonyms = synonyms.strip().strip('"\'').strip()

                  definition = definition.strip().strip('"\'').strip()

                  definition = re.sub( r'\|.*$', r'', definition )

                  termsUsed[categoryID][currentTerm]['name'] = name;
                  termsUsed[categoryID][currentTerm]['description'] = definition;
                  termsUsed[categoryID][currentTerm]['synonyms'] = synonyms;

               # end if ( currentTerm in termsUsed[categoryID] )

            # end for ( input file line iterator )

         # end with ( refFile opened as IN )

      # end if ( switch on categoryID )

   # end foreach ( categoryID in termsUsed )

# end sub decorateTermsUsed(  )

def writeTermsUsed( outDir, termsUsed ):
   
   for categoryID in termsUsed:
      outFile = '%s/%s.tsv' % ( outDir, categoryID )
      print(f'Writing to {outFile}')

      with open(outFile, 'w') as OUT:
         
         OUT.write( '\t'.join( [ 'id', 'name', 'description', 'synonyms' ] ) + '\n' )

         for termID in termsUsed[categoryID]:
            
#           OUT.write( '\t'.join( [ termID, termsUsed[categoryID][termID]['name'], termsUsed[categoryID][termID]['description'], termsUsed[categoryID][termID]['synonyms'] ] ) + '\n' )
            
            # The synonyms we loaded from the OBO files don't conform to the spec constraints. Punting to blank values for now.

            if 'name' not in termsUsed[categoryID][termID]:
                print(f'WARNING: no name/description for categoryID {categoryID}/termID {termID} in termsUsed; skipping', file=sys.stderr)
                print(f'(WARNING occurred when writing to {outFile})')
            else:
                OUT.write( '\t'.join( [ termID, termsUsed[categoryID][termID]['name'], termsUsed[categoryID][termID]['description'],                  ''                       ] ) + '\n' )

# end sub writeTermsUsed(  )

##########################################################################################
##########################################################################################
##########################################################################################
#                                       EXECUTION
##########################################################################################
##########################################################################################
##########################################################################################

def main():
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument('--cvRefDir', default='external_CV_reference_files',
                   help="""Directory containing full CV reference info (see 'cvFile' dictionary, for file list).""")
    p.add_argument('--draftDir', default='../draft-C2M2_example_submission_data/HMP__sample_C2M2_Level_1_bdbag.contents',
                   help="""Directory in which core-entity ETL instance TSVs (for the purposes of this script, this means 'file.tsv' and 'biosample.tsv') have been built and stored, prior to running this script.""")
    p.add_argument('--outDir', default='./007_HMP-specific_CV_term_usage_TSVs',
                   help="""Directory into which TSVs will be written (by this script) summarizing all controlled vocabulary term usage throughout this Level 1 C2M2 instance (as prescribed by the Level 1 specification).""")

    args = p.parse_args()

    cvRefDir = args.cvRefDir
    draftDir = args.draftDir
    outDir = args.outDir

    cvFile = {}
    for k, v in cvFileTemplate.items():
        cvFile[k] = v.format(cvRefDir=cvRefDir)

    # Create the output directory if need be.

    if not os.path.isdir(outDir) and os.path.exists(outDir):

       die('%s exists but is not a directory; aborting.' % outDir)

    elif not os.path.isdir(outDir):

       os.mkdir(outDir)

    # Find all the CV terms used in the ETL draft instance in "draftDir".
    identifyTermsUsed( termsUsed, draftDir, targetTSVs )

    # Load data from CV reference files to fill out needed columns in Level 1 C2M2
    # term-tracker tables.

    decorateTermsUsed( termsUsed, cvFile )

    # Write the term-tracker tables.

    writeTermsUsed( outDir, termsUsed )


if __name__ == '__main__':
    main()
