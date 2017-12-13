'''
@auth: /Dalaylan

> quick hack prototype for python indentation fixer
> this version standardizes indentation based on inserting '{' and '}' characters into a copy of the broken file
> brackets must be on lines without any text on them (but multiple bracket can be placed on the same line)
> Takes arguments in the form "python fixIndent.py <broken_file_with_added_brackets> <outputFile>
'''

'''
Error codes:
    0 -> success
    1 -> bad arguments
    2 -> error with opening file
    3 -> error with reading indentation level
'''

import sys

ARGS = 3

#if '{' indent +=1 , if '}' indent -=1
def simpleVers(fin,fout):
    indent = 0

    try:
        read = open(fin,'r')
    except IOError:
        print("error opening source file")
        sys.exit(2)
    try:
        out = open(fout,'w+')
    except IOError:
        print("error occured when attempting to open/create output file")
        sys.exit(2)

    for line in read:
        addIndent = line.count('{')
        subIndent = line.count('}')
        change = addIndent - subIndent
        indent = indent + change
        if indent <0:
            print("indent level went under 0 while parsing, check brackets and try again")
            sys.exit(3)

        ind = indent
        if change !=0: 
            continue

        for i in range(0,ind):
            line = "\t" +line
        out.write(line)


def main(inFile,outFile):
    simpleVers(inFile,outFile)

if __name__ == '__main__':
    if len(sys.argv) < ARGS:
        print("insufficient arguments given, please give both an input and output file")
        sys.exit(1)
    elif len(sys.argv) > ARGS:
        print("too many arguments given, please give both an input and output file")
        sys.exit(1)
    main(sys.argv[1],sys.argv[2])

