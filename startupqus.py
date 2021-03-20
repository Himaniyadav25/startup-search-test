
def qone():
    dkey = [1,2,3,4,5,6,7,8]
    dvalues=['rashi','komal','varsh','harry','harly','hira']
    reqdic={}
    for k in dkey:
        for v in dvalues:
            reqdic[k]=v
            dvalues.remove(v)
            break
        #print(reqdic)

    lk=len(dkey)
    lv=len(dvalues)
    ld=len(reqdic)

    while ld < lk:
        rk =dkey[ld]
        reqdic[rk]='none'
        ld+=1

    print(reqdic)
    return reqdic



qone()

"""
2. There is a restriction in the authorization system:
    * the password must begin with a latin letter,
    * the password can consist of Latin letters, numbers, dot and minuses,
    * the password must end only with a latin letter or number;
    * minimum password length is one character
    * maximum password length is 20 characters
Write a function that checks whether the input string matches this rule.
(Come up with several ways to solve the problem and compare them.)
Write a tests using unittest/pytest.
"""

# importing re library
import re


passwd= input("Enter the password")


def passcheck1():

    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{1,20}$"
    reg1 = "^[a-z0-9A-Z]+[\.-]?[a-z0-9A-Z]{1,20}$"

    # compiling regex
    pat = re.compile(reg1)
    # searching regex
    mat = re.search(pat, passwd)
    # validating conditions
    if mat:
        print("Password is valid.")
        #return True
    else:
        print("Password invalid !!")
        #return False
    # Driver Code

passcheck1()

def passcheck2(passwd):
    SpecialSym = [ '!','@','$','%','^','&','*','(',')','=','+','/']
    val = True

    lep= len(passwd)


    if lep < 1:
        print('length should be at least 1')
        val = False

    if lep > 20:
        print('length should be not be greater than 20')
        val = False

    if not any(char.isdigit() for char in passwd):
        print('Password should have at least one numeral')
        val = False

    if not any(char.isalpha() for char in passwd[0]):
        print('Password should start with letter')
        val = False

    if any(char in SpecialSym for char in passwd):
        print('Password can only have one of the symbols . or -')
        val = False

    if not any(char.isalpha() or char.isdigit() for char in passwd[lep-1]):
        print('Password should end with letter or digit')
        val = False

    if val:
        return val


def qtwo():

    if (passcheck2(passwd)):
        print("Password is valid")
    else:
        print("Invalid Password !!")



qtwo()

"""3. Suppose we have an access.log web server.
Write a function that receives file name and returns ten IP addresses from which there were most requests
Lib https://pypi.org/project/IPy/ could help u working with IPs
Write a tests using unittest/pytest.


"""

from itertools import groupby
import re,os

def logread():
    print(os.path.basename('access.log'))

    with open('access.log') as fh:
        fstring = fh.readlines()
    pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
    lst = []

    # extracting the IP addresses
    for line in fstring:
        lst.append(pattern.search(line)[0])
    # displaying the extracted IP adresses
    print(lst[:10])


logread()

"""
4. Please provide your github/gitlab/bitbacket account link.


Linkedin:-https://www.linkedin.com/in/himani-yadav-159b37ba/
github:-https://github.com/Himaniyadav25
"""




