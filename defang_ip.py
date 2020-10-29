"""
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

 

Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
Example 2:

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"
"""

def Defang(address):
    check_address = address.split('.')
    if len(check_address ) != 4:
        return("Not a valid IP address")
    if False in [int(x) < 256 for x in check_address]:
        return("Not a valid IP address")
    return address.replace('.', '[.]')
    

