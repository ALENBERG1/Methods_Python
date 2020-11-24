

def rotEncryption(strToEncrypt: str, rotShift: int) -> str:
    """
     Rot Encryption
        this function shift the character in the string

     parameters:
        string toEncrypt
        integer rot_num

     return:
        string
    """
    # declarations
    newstring = ""
    strList = [char for char in strToEncrypt]  # char list generator
    rotShift %= 25  # if rotShift given is grater than 25 it take the reminder

    for i in range(0, len(strList)):  # analize each character of the char list
        if (65 <= ord(strList[i]) <= 90 and ord(strList[i]) + rotShift > 90) or \
                (97 <= ord(strList[i]) <= 122 and ord(strList[i]) + rotShift > 122):
            newstring += chr(ord(strList[i]) - 26 + rotShift)
        # if the character is between 65 and 90 (and grater than 90 with added rotShift number) or
        # between 97 and 122 (and grater than 122 with added rotShift number)
        # the program subtract 26 and add the given number

        elif (65 <= ord(strList[i]) and ord(strList[i]) + rotShift <= 90) or \
                (ord(strList[i]) >= 97 and ord(strList[i]) + rotShift <= 122):
            newstring += chr(ord(strList[i]) + rotShift)
        # if the character is between 65 and 90 (with added rotShift number) or
        # between 97 and 122 (with added rotShift number) the program add the char to string newstring

        elif 0 <= ord(strList[i]) <= 47 or 58 <= ord(strList[i]) <= 64 or\
                91 <= ord(strList[i]) <= 96 or ord(strList[i]) >= 123:
            newstring += strList[i]
        # if the character is a special character remains unchanged

        elif 48 <= ord(strList[i]) <= 57:
            newstring += chr(ord(strList[i]) + (rotShift % 10)) if 48 <= ord(strList[i]) + (rotShift % 10) <= 57 \
                else chr(ord(strList[i]) + (rotShift % 10) - 10)
        # if the character is a number the program, add the remainder of rotShift number
        # divided by 10

    return newstring

