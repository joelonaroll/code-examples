"""===============================
This is homework assignment 7.

Joel Pantuso, 11/29/21
=================================="""
import re # import module

# Question 1

def countRESites(rs, str): # define function
    print(len(re.findall(rs, str))) # print number of times rs appears in str

# assumptions given
countRESites("AACGTT", "AAAAAACGTTAAAAA")
countRESites("GGCC", "AAGGCCTTCCAAGGCCTTCA")
countRESites("[AT]GCTC", "ATGCTCAGCTCAGTGT")

# Question 2

def applyREnzyme(rs, str): # define function
    print(re.split(rs, str)) # print list of substrings in str separated by rs

# assumptions given
applyREnzyme("AACGTT","ATGTACAACGTTTGCTGGTCAAACGTTATAGCGT")
applyREnzyme("AACGTT","TGTCAGA")
applyREnzyme("AACGTT","AACGTT")

# Question 3

def hasHgalRS(str): # define function
    match = re.search("GACGC", str) # see if the Hgal RS is in str
    if match:
        print("True")
    else:
        print("False")

# assumptions given
str = "ACGTACGACGCTACGT"
hasHgalRS(str)

str = "ACGTACGTACGTACGT"
hasHgalRS(str)

# Question 4

def hasEcoRIIRS(str): # define function
    match = re.search("CCAGG|CCTGG", str) # see if either variation of EcoRII RS is in str
    if match:
        print("True")
    else:
        print("False")

# assumptions given
str = "ACGTACCCAGGACGT"
hasEcoRIIRS(str)

str = "ACGTACCCTGGACGT"
hasEcoRIIRS(str)

str = "ACGTACCCCGGACGT"
hasEcoRIIRS(str)

# Question 5

Input = open("BIO256_hw7_Q5_in.txt", "r") # open file

for line in Input: # for loop to work with each line in the file
    match = re.search("[A-Za-z]+\s+[A-Za-z]+.*\d{3}.\d{2}.\d{4}", line) # create a proper pattern to search within each line
    if match:
        print(match.group().replace("-", " ")) # output matching results without any hyphens

Input.close() # close file

# Question 6

inFile = open("BIO256_hw7_Q6_in.txt", "r") # open file

for line in inFile: # for loop to work with each line in the file
    both = line.split() # make a list with sequence name and sequence

    # search sequences for RS
    XbaI = re.findall("TCTAGA", line)
    SmlI = re.findall("CTCAAG|CTCGAG|CTTAAG|CTTGAG", line)
    BglI = re.findall("GCC.{5}GGC", line)

    # count how many RS are in sequence
    NumXbaI = len(XbaI)
    NumSmlI = len(SmlI)
    NumBglI = len(BglI)

    # output in preferred format
    print("{} XbaI: {} SmlI: {} BglI: {}".format(both[0],NumXbaI,NumSmlI,NumBglI))

inFile.close() # close file
