import re
def binaryToDecimal(binaryString):
    if not isinstance(binaryString,str):
        raise Exception("binaryString is not a string")
    else:
        result = re.match(r"^[0-1]+",binaryString)
        if result == None:
            raise Exception("String is not a binary string type")
        else:
            xyz = int(binaryString,2)
            print("BinaryString: " , binaryString , " to Decimal: ", xyz)
binaryToDecimal("31101")
