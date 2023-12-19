
# rot13/main.py

class Rot13:
    
    
    def __init__(self):
        self.cipherString = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_nSkgmDJE}"
        self.cipherStringDecrypt = ""
        self.alphaStringLower = "abcdefghijklmnopqrstuvwxyz"
        self.alphaStringUpper = self.alphaStringLower.upper()
        self.alphaDictLower = {}
        self.alphaDictUpper = {}
        
        self.__create_alphaDict(self.alphaStringLower, self.alphaStringUpper)
        self.__get_cipherChar(self.cipherString)


    def __create_alphaDict(self, alphaStringLower, alphaStringUpper):

        for index, char in enumerate(alphaStringLower, start=1):
            self.alphaDictLower.update({char : index})

        for index, char in enumerate(alphaStringUpper, start=1):
            self.alphaDictUpper.update({char : index})
        

    def __get_cipherChar(self, cipherString):

        for cipherChar in cipherString:
            
            upper = 0
            lower = 0

            if cipherChar.isupper():
                searchResult = self.alphaDictUpper.get(cipherChar)
                upper = 1

            elif cipherChar.islower():
                searchResult = self.alphaDictLower.get(cipherChar)
                lower = 1

            else:
                searchResult = self.alphaDictLower.get(cipherChar)
            
            #print(searchResult)

            if searchResult == None:
                self.cipherStringDecrypt += cipherChar
            else:
                rot13Index = searchResult + 13
                if rot13Index > 26:
                    rot13Index = rot13Index - 26
                if lower == 1:
                    for key, value in self.alphaDictLower.items():
                        if value == rot13Index:
                            self.cipherStringDecrypt += key

                elif upper == 1:
                    for key, value in self.alphaDictUpper.items():
                        if value == rot13Index:
                            self.cipherStringDecrypt += key
                                               
                        



##############################################################
if __name__ == "__main__":
    rot13 = Rot13()
    print(rot13.cipherStringDecrypt)
##############################################################
