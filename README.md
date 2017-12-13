# PythonIndentFixer
hacked together indentation fixer/standardizer for python code   
this version standardizes indentation based on inserting '{' and '}' characters into a copy of the broken file  
brackets must be on lines without any text on them (but multiple bracket can be placed on the same line)  
Takes arguments in the form "python fixIndent.py <broken_file_with_added_brackets> <outputFile>  

Error codes:  
  0 -> success  
  1 -> bad arguments  
  2 -> error with opening file  
  3 -> error with reading indentation level  
