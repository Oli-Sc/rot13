
# rot13/main.py

class Rot13:
    
    
    def __init__(self):
        self.cipherString = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_nSkgmDJE}"
        self.cipherStringDecrypt = ""
        self.alphaString = "abcdefghijklmnopqrstuvwxyz"
        self.alphaList = []
        self.alphaDict = {}
        
        self.__create_alphaDict(self.alphaString)
        self.__get_cipherChar(self.cipherString)


    def __create_alphaDict(self, alphaString):

        for index, char in enumerate(alphaString, start=1):
            self.alphaDict.update({char : index})
        

    def __get_cipherChar(self, cipherString):

        for cipherChar in cipherString:
            searchResult = self.alphaDict.get(cipherChar)
            print(searchResult)
            if searchResult == None:
                self.cipherStringDecrypt.join(cipherChar)
            else:
                rot13Index = searchResult + 13
                if rot13Index > 26:
                    rot13Index = rot13Index - 26
                for key, value in self.alphaDict.items():
                    if value == rot13Index:
                        #print(key)
                        self.cipherStringDecrypt.join(key)
        print(self.cipherStringDecrypt)
                        



##############################################################
if __name__ == "__main__":
    rot13 = Rot13()
    print(rot13.cipherStringDecrypt)
##############################################################
