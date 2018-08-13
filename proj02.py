####################################
#Computer Project #2
#
#Decompressing a string
#   prompt user for string input
#   count number of occurances for left parentheses
#   initiate variables x (number of loops), decomp (empty string for printing\
#       decompressed string), and pos (position where copied string is to be \
#       printed)
#   find index of left and right parentheses and comma
#   slice string between left parentheses and comma, which is the number of \
#       characters to go back in the string, and right parentheses and comma, \
#       which is the number of characters to copy starting from the first sliced\
#       value
#   slice input string based on these values and add the sliced string to decomp
#   keep track of position for where the new sliced decompressed string should
#       be added to decomp; also for calculating the index for which the program\
#   should begin counting back within the string
#   if backslashes are present in the string, replace all with "\n", or carriage\
#       return 
####################################
#prompt user for string input
comp_str = input("Input a string to decompress: ")

#initiate variables x and pos. Create empty string decomp for decompressed\
#string to print
left_count = comp_str.count("(")
x = 0
decomp = ""
pos = 0

#loops while x is left than the number of left parentheses counted in comp_str
while x < left_count:
#add 1 to x per loop
    x += 1

#finds index of left and right parentheses as well as the comma    
    left = int(comp_str.find("("))
    comma = int(comp_str.find(",",left + 1))
    right = int(comp_str.find(")",comma + 1))

#slices the number between the left/right parentheses and comma        
    left_num = int(comp_str[left + 1:comma])
    right_num = int(comp_str[comma + 1:right])

#adds sliced text from comp_str to decomp until the left parentheses and also\
#slices comp_str from the right parentheses until the end of the string
    decomp += comp_str[:left]
    comp_str = comp_str[right + 1:]

#pos is the length of decomp. Pointer is calculate by pos subtracted by the left\
#number (between left parentheses and comma)
    pos = len(decomp)
    pointer = pos - left_num

#slices decomp based on value calculated from the pointer variable and the right\
#number sliced from between the comma and right parentheses    
    copy_txt = decomp[pointer:pointer + right_num]

#adds copy_txt to decomp    
    decomp += copy_txt

#adds the rest of comp_str to decomp when the loop is done 
decomp += comp_str

#if there is a backslash in decomp, replace it with "n\", or carriage return
if "\\" in decomp:
    decomp = decomp.replace("\\","\n")

#print "Decompressed string" and decomp
print()
print("Decompressed String")
print()                 
print(decomp)