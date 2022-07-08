import os

encode_mode = 'euc-kr'
file_path = os.getcwd()
os.chdir(file_path)

f_result = None
f_error  = None
f_newline = "\n"

def createDirectory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("Error: Failed to create the directory. (" + directory + ")" )

def getstring(txt, idx, encoding=encode_mode):
    return txt.encode(encoding)[:idx].decode(encoding)
    
def getlength(txt, encoding=encode_mode):
    return str(len(txt.encode(encode_mode))-1)

def substring(txt, idx, encoding=encode_mode):
    try:
        return txt.encode(encoding)[:idx].decode(encoding), txt.encode(encoding)[idx:].decode(encoding)
    except UnicodeDecodeError:
        try:
            return txt.encode(encoding)[:idx-1].decode(encoding), txt.encode(encoding)[idx-1:].decode(encoding)
        except UnicodeDecodeError:        
            return txt.encode(encoding)[:idx-2].decode(encoding), txt.encode(encoding)[idx-2:].decode(encoding)
            
def LogFunc(txt):
    f_result.write(txt+f_newline)
    
def ErrorFunc(line_num, line, error, txt):
    f_error.write("=================="+error+"======================" + f_newline)
    f_error.write("line_num : " + str(line_num) + f_newline + txt + f_newline)
    
    

class Vat_Function:
    def __init__(self, file):
        global f_result
        global f_error 
        self.business_no = ""
        self.file = file

        #로그폴더생성
        createDirectory(os.path.join(file_path,"Result"))
        createDirectory(os.path.join(file_path,"Error"))

        #로그파일 오픈
        f_result = open(os.path.join(file_path,"Result","result_"+self.file+".txt"), "w")
        f_error  = open(os.path.join(file_path,"Error","error_"+self.file+".txt"), "w")
        
    def __del__(self):
        if f_result != None:
            f_result.close()
            
        if f_error != None:
            f_error.close()
            
    def getBusinessNo(self):
        return str(self.business_no)

    def check_head(self, line_num, txt):
        len_txt = getlength(txt)
        if len_txt != "600":
            LogFunc("헤더 길이 오류 :"+ len_txt)
            return
        else:
            LogFunc("헤더 길이 :"+ len_txt)
        
        tmp, txt = substring(txt,2)
        
        if tmp == "11":
            LogFunc("========일반과세신고========")
        elif tmp == "12":
            LogFunc("========간이과세신고========")
        else:
            ErrorFunc(line_num,"","부가가치세 신고서 HEAD 자료구분 코드 오류",txt)
            return
            
        LogFunc("1. 자료구분 :"+ tmp)
        
        tmp, txt = substring(txt,7)
        LogFunc("2. 서식코드 :"+ tmp)
        
        tmp, txt = substring(txt,13)
        self.business_no = str(tmp) #사업자번호 저장
        LogFunc("3. 납세자ID :"+ tmp)
        
        tmp, txt = substring(txt,2)
        LogFunc("4. 세목코드 :"+ tmp)
        
        tmp, txt = substring(txt,2)
        LogFunc("5. 신고구분코드 :"+ tmp)
        
        tmp, txt = substring(txt,2)
        LogFunc("6. 신고구분상세코드 :"+ tmp)
        
        tmp, txt = substring(txt,6)
        LogFunc("7. 과세기간_년기(월) :"+ tmp)
        
        tmp, txt = substring(txt,3)
        LogFunc("8. 신고서종류코드 :"+ tmp)
        
        tmp, txt = substring(txt,20)
        LogFunc("9. 사용자ID :"+ tmp)
        
        tmp, txt = substring(txt,13)
        LogFunc("10. 납세자번호 :"+ tmp)
        
        tmp, txt = substring(txt,30)
        LogFunc("11. 세무대리인성명 :"+ tmp)

        tmp, txt = substring(txt,4)
        LogFunc("12. 세무대리인전화번호1 (지역번호):"+ tmp)

        tmp, txt = substring(txt,5)
        LogFunc("13. 세무대리인전화번호2 (국번) :"+ tmp)

        tmp, txt = substring(txt,5)
        LogFunc("14. 세무대리인전화번호3 (지역번호,국번을제외한번호) :"+ tmp)
        
        tmp, txt = substring(txt,30)
        LogFunc("15. 상호(법인명) :"+ tmp)

        tmp, txt = substring(txt,30)
        LogFunc("16. 성명(대표자명) :"+ tmp)
        
        tmp, txt = substring(txt,70)
        LogFunc("17. 사업장소재지 :"+ tmp)

        tmp, txt = substring(txt,14)
        LogFunc("18. 사업장전화번호 :"+ tmp)    

        tmp, txt = substring(txt,70)
        LogFunc("19. 사업자주소 :"+ tmp)
            
        tmp, txt = substring(txt,14)
        LogFunc("20. 사업자전화번호 :"+ tmp)
        
        tmp, txt = substring(txt,30)
        LogFunc("21. 업태명 :"+ tmp)
        
        tmp, txt = substring(txt,50)
        LogFunc("22. 종목명 :"+ tmp)
        
        tmp, txt = substring(txt,7)
        LogFunc("23. 업종코드 :"+ tmp)
        
        tmp, txt = substring(txt,8)
        LogFunc("24. 과세기간시작일자 :"+ tmp)
        
        tmp, txt = substring(txt,8)
        LogFunc("25. 과세기간종료일자 :"+ tmp)
        
        tmp, txt = substring(txt,8)
        LogFunc("26. 작성일자 :"+ tmp)
        
        tmp, txt = substring(txt,1)
        LogFunc("27. 보정신고구분 :"+ tmp)
        
        tmp, txt = substring(txt,14)
        LogFunc("28. 사업자휴대전화 :"+ tmp)
        
        tmp, txt = substring(txt,4)
        LogFunc("29. 세무프로그램코드 :"+ tmp)
        
        tmp, txt = substring(txt,13)
        LogFunc("30. 세무대리인사업자번호 :"+ tmp)
        
        tmp, txt = substring(txt,50)
        LogFunc("31. 전자메일주소 :"+ tmp)
        
        tmp, txt = substring(txt,65)
        LogFunc("32. 공란 :"+ tmp)

    def function_I103200(self, f_type, txt):
        if f_type == "17":
            tmp, txt = substring(txt, 15)
            LogFunc("3. 매출과세세금계산서발급금액  :"+ tmp)
            
            tmp, txt = substring(txt, 13)
            LogFunc("4. 매출과세세금계산서발급세액  :"+ tmp)
            
            tmp, txt = substring(txt, 13)
            LogFunc("5. 매출과세매입자발행세금계산서금액  :"+ tmp)
            
            tmp, txt = substring(txt, 13)
            LogFunc("6. 매출과세매입자발행세금계산서세액  :"+ tmp)
            
            tmp, txt = substring(txt, 15)
            LogFunc("7. 매출과세카드현금발행금액 :"+ tmp)
            
            tmp, txt = substring(txt, 15)
            LogFunc("8. 매출과세카드현금발행세액 :"+ tmp)
            
            tmp, txt = substring(txt, 13)
            LogFunc("9. 매출과세기타금액 :"+ tmp)
            
            tmp, txt = substring(txt, 13)
            LogFunc("10. 매출과세기타세액 :"+ tmp)
            
            tmp, txt = substring(txt, 13)
            LogFunc("11. 매출영세율세금계산서발급금액 :"+ tmp)
            
            tmp, txt = substring(txt, 15)
            LogFunc("12. 매출영세율기타금액 :"+ tmp)
            
            tmp, txt = substring(txt, 13)
            LogFunc("13. 매출예정누락합계금액 :"+ tmp)
            
            tmp, txt = substring(txt, 13)
            LogFunc("14. 매출예정누락합계세액 :"+ tmp)
            
            tmp, txt = substring(txt, 13)
            LogFunc("15. 예정누락매출세금계산서금액 :"+ tmp)
            
            tmp, txt = substring(txt, 13)
            LogFunc("16. 예정누락매출세금계산서세액 :"+ tmp)
            
            tmp, txt = substring(txt, 13)
            LogFunc("17. 예정누락매출과세기타금액 :"+ tmp)
            
            tmp, txt = substring(txt, 13)
            LogFunc("18. 예정누락매출과세기타세액 :"+ tmp)
            
            tmp, txt = substring(txt, 13)
            LogFunc("19. 예정누락매출영세율세금계산서금액 :"+ tmp)
            
            tmp, txt = substring(txt, 13)
            LogFunc("20. 예정누락매출영세율기타금액 :"+ tmp)
            
            tmp, txt = substring(txt, 13)
            LogFunc("21. 예정누락매출명세합계금액 :"+ tmp)
            
            tmp, txt = substring(txt, 13)
            LogFunc("22. 예정누락매출명세합계세액 :"+ tmp)
            
            tmp, txt = substring(txt, 13)
            LogFunc("23. 매출대손세액가감세액 :"+ tmp)
            
            tmp, txt = substring(txt, 15)
            LogFunc("24. 과세표준금액 :"+ tmp)
            
            tmp, txt = substring(txt, 15)
            LogFunc("25. 산출세액 :"+ tmp)
            
            tmp, txt = substring(txt, 15)
            LogFunc("26. 매입세금계산서수취일반금액 :"+ tmp)
            
            tmp, txt = substring(txt, 13)
            LogFunc("27. 매입세금계산서수취일반세액 :"+ tmp)
            
            tmp, txt = substring(txt, 13)
            LogFunc("28. 매입세금계산서수취고정자산금액 :"+ tmp)
            
            tmp, txt = substring(txt, 13)
            LogFunc("29. 매입세금계산서수취고정자산세액 :"+ tmp)
            
            tmp, txt = substring(txt, 13)
            LogFunc("30. 매입예정누락합계금액 :"+ tmp)
            
            tmp, txt = substring(txt, 13)
            LogFunc("31. 매입예정누락합계세액 :"+ tmp)
            
            tmp, txt = substring(txt, 13)
            LogFunc("32. 예정누락매입신고세금계산서금액 :"+ tmp)
            
            tmp, txt = substring(txt, 13)
            LogFunc("33. 예정누락매입신고세금계산서세액 :"+ tmp)
            
            tmp, txt = substring(txt, 13)
            LogFunc("34. 예정누락매입기타공제금액 :"+ tmp)
            
            tmp, txt = substring(txt, 13)
            LogFunc("35. 예정누락매입기타공제세액 :"+ tmp)
            
            tmp, txt = substring(txt, 13)
            LogFunc("36. 예정누락매입명세합계금액 :"+ tmp)
            
            tmp, txt = substring(txt, 13)
            LogFunc("37. 예정누락매입명세합계세액 :"+ tmp)
            
            tmp, txt = substring(txt, 13)
            LogFunc("38. 매입자발행세금계산서매입금액 :"+ tmp)
            
            tmp, txt = substring(txt, 13)
            LogFunc("39. 매입자발행세금계산서매입세액 :"+ tmp)
            
            tmp, txt = substring(txt, 13)
            LogFunc("40. 매입기타공제매입금액 :"+ tmp)
            
            tmp, txt = substring(txt, 13)
            LogFunc("41. 매입기타공제매입세액 :"+ tmp)
            
            tmp, txt = substring(txt, 13)
            LogFunc("42. 그밖의공제매입명세합계금액 :"+ tmp)
            
            tmp, txt = substring(txt, 13)
            LogFunc("43. 그밖의공제매입명세합계세액 :"+ tmp)
            
            tmp, txt = substring(txt, 15)
            LogFunc("44. 매입세액합계금액 :"+ tmp)
            
            tmp, txt = substring(txt, 13)
            LogFunc("45. 매입세액합계세액 :"+ tmp)
            
            tmp, txt = substring(txt, 13)
            LogFunc("46. 공제받지못할매입합계금액 :"+ tmp)
            
            tmp, txt = substring(txt, 13)
            LogFunc("47. 공제받지못할매입합계세액 :"+ tmp)
            
            tmp, txt = substring(txt, 13)
            LogFunc("48. 공제받지못할매입금액 :"+ tmp)
            
            tmp, txt = substring(txt, 13)
            LogFunc("49. 공제받지못할매입세액 :"+ tmp)
            
            tmp, txt = substring(txt, 13)
            LogFunc("50. 공제받지못할공통매입면세사업금액 :"+ tmp)
            
            tmp, txt = substring(txt, 13)
            LogFunc("51. 공제받지못할공통매입면세사업세액 :"+ tmp)
            
            tmp, txt = substring(txt, 13)
            LogFunc("52. 공제받지못할대손처분금액 :"+ tmp)
            
            tmp, txt = substring(txt, 13)
            LogFunc("53. 공제받지못할대손처분세액 :"+ tmp)
            
            tmp, txt = substring(txt, 13)
            LogFunc("54. 공제받지못할매입명세합계금액 :"+ tmp)
            
            tmp, txt = substring(txt, 13)
            LogFunc("55. 공제받지못할매입명세합계세액 :"+ tmp)
            
            tmp, txt = substring(txt, 15)
            LogFunc("56. 차감합계금액 :"+ tmp)
            
            tmp, txt = substring(txt, 13)
            LogFunc("57. 차감합계세액 :"+ tmp)
            
            tmp, txt = substring(txt, 13)
            LogFunc("58. 납부 :"+ tmp)
            
            tmp, txt = substring(txt, 15)
            LogFunc("59. 그밖의경감공제세액 :"+ tmp)
            
            tmp, txt = substring(txt, 15)
            LogFunc("60. 그밖의경감공제명세합계세액 :"+ tmp)
            
            tmp, txt = substring(txt, 13)
            LogFunc("61. 경감공제합계세액 :"+ tmp)
            
            tmp, txt = substring(txt, 13)
            LogFunc("62. 예정신고미환급세액 :"+ tmp)
            
            tmp, txt = substring(txt, 13)
            LogFunc("63. 예정고지세액 :"+ tmp)
            
            tmp, txt = substring(txt, 13)
            LogFunc("64. 사업양수자의대리납부기납부세액 :"+ tmp)
            
            tmp, txt = substring(txt, 13)
            LogFunc("65. 매입자납부특례기납부세액 :"+ tmp)
            
            tmp, txt = substring(txt, 13)
            LogFunc("66. 가가산세액계 :"+ tmp)
            
            tmp, txt = substring(txt, 15)
            LogFunc("67. 차감납부할세액 :"+ tmp)
            
            tmp, txt = substring(txt, 13)
            LogFunc("68. 과세표준명세수입금액제외금액 :"+ tmp)
            
            tmp, txt = substring(txt, 15)
            LogFunc("69. 과세표준명세합계수입금액 :"+ tmp)
            
            tmp, txt = substring(txt, 13)
            LogFunc("70. 면세사업수입금액제외금액 :"+ tmp)
            
            tmp, txt = substring(txt, 15)
            LogFunc("71. 면세사업합계수입금액 :"+ tmp)
            
            tmp, txt = substring(txt, 15)
            LogFunc("72. 계산서교부금액 :"+ tmp)
            
            tmp, txt = substring(txt, 15)
            LogFunc("73. 계산서수취금액 :"+ tmp)
            
            tmp, txt = substring(txt, 2)
            LogFunc("74. 환급구분코드 :"+ tmp)
            
            tmp, txt = substring(txt, 3)
            LogFunc("75. 은행코드 :"+ tmp)
            
            tmp, txt = substring(txt, 20)
            LogFunc("76. 계좌번호 :"+ tmp)
            
            tmp, txt = substring(txt, 9)
            LogFunc("77. 총괄납부승인번호 :"+ tmp)
            
            tmp, txt = substring(txt, 30)
            LogFunc("78. 은행지점명 :"+ tmp)
            
            tmp, txt = substring(txt, 8)
            LogFunc("79. 폐업일자 :"+ tmp)
            
            tmp, txt = substring(txt, 3)
            LogFunc("80. 폐업사유 :"+ tmp)
            
            tmp, txt = substring(txt, 1)
            LogFunc("81. 기한후 :"+ tmp)
            
            tmp, txt = substring(txt, 15)
            LogFunc("82. 실차감납부할세액 :"+ tmp)
            
            tmp, txt = substring(txt, 1)
            LogFunc("83. 일반과세자구분 :"+ tmp)
            
            tmp, txt = substring(txt, 1)
            LogFunc("84. 조기환급취소구분 :"+ tmp)
            
            tmp, txt = substring(txt, 15)
            LogFunc("85. 수출기업 수입 납부유예 :"+ tmp)
            
            tmp, txt = substring(txt, 13)
            LogFunc("86. 신용카드업자의 대리납부 기납부세액 :"+ tmp)
            
            tmp, txt = substring(txt, 13)
            LogFunc("87. 소규모 개인사업자 부가가치세 감면세액 :"+ tmp)
            
            tmp, txt = substring(txt, 1)
            LogFunc("88. 영세율상호주의여부 :"+ tmp)
            
            tmp, txt = substring(txt, 1)
            LogFunc("89. 공란 :"+ tmp)
            
        elif f_type == "15":
            tmp, txt = substring(txt, 2)
            LogFunc("3. 수입금액종류구분코드 :"+ tmp)
            
            tmp, txt = substring(txt, 30)
            LogFunc("4. 업태명 :"+ tmp)
            
            tmp, txt = substring(txt, 50)
            LogFunc("5. 종목명 :"+ tmp)
            
            tmp, txt = substring(txt, 7)
            LogFunc("6. 업종코드 :"+ tmp)
            
            tmp, txt = substring(txt, 15)
            LogFunc("7. 수입금액 :"+ tmp)
            
            tmp, txt = substring(txt, 37)
            LogFunc("8. 공란 :"+ tmp)
            
        elif f_type == "14":
            tmp, txt = substring(txt, 3)
            LogFunc("3. 공제감면코드 :"+ tmp)
            
            tmp, txt = substring(txt, 12)
            LogFunc("4. 등록일련번호 :"+ tmp)
            
            tmp, txt = substring(txt, 15)
            LogFunc("5. 공제감면금액 :"+ tmp)
            
            tmp, txt = substring(txt, 15)
            LogFunc("6. 공제감면세액 :"+ tmp)
            
            tmp, txt = substring(txt, 46)
            LogFunc("7. 공란 :"+ tmp)
            
        elif f_type == "13":
            tmp, txt = substring(txt, 10)
            LogFunc("3. 가산세코드 :"+ tmp)
            
            tmp, txt = substring(txt, 12)
            LogFunc("4. 등록일련번호 :"+ tmp)
            
            tmp, txt = substring(txt, 15)
            LogFunc("5. 가산세금액 :"+ tmp)
            
            tmp, txt = substring(txt, 15)
            LogFunc("6. 가산세액 :"+ tmp)
            
            tmp, txt = substring(txt, 39)
            LogFunc("7. 공란 :"+ tmp)
            
        elif f_type == "16":
            tmp, txt = substring(txt, 2)
            LogFunc("3. 영세율상호주의적용구분코드 :"+ tmp)
            
            tmp, txt = substring(txt, 6)
            LogFunc("4. 업종코드 :"+ tmp)
            
            tmp, txt = substring(txt, 2)
            LogFunc("5. 국가코드 :"+ tmp)
            
            tmp, txt = substring(txt, 31)
            LogFunc("6. 공란 :"+ tmp)
        
        else:
            LogFunc("Error : 신규타입 추가 필요 (" + f_type +")", "")
            
    def function_I103600(self, f_type, txt):
        if f_type == "17":
            tmp, txt = substring(txt, 6)
            LogFunc("3. 일련번호구분 :"+ tmp)
            
            tmp, txt = substring(txt, 70)
            LogFunc("4. 부동산소재지 :"+ tmp)
            
            tmp, txt = substring(txt, 15)
            LogFunc("5. 임대계약내용보증금합계 :"+ tmp)
            
            tmp, txt = substring(txt, 15)
            LogFunc("6. 임대계약내용월세등합계 :"+ tmp)
            
            tmp, txt = substring(txt, 15)
            LogFunc("7. 임대료수입금액합계 :"+ tmp)
            
            tmp, txt = substring(txt, 15)
            LogFunc("8. 임대료수입보증금이자합계 :"+ tmp)
            
            tmp, txt = substring(txt, 15)
            LogFunc("9. 임대료수입월세등합계 :"+ tmp)
            
            tmp, txt = substring(txt, 10)
            LogFunc("10. 임대인사업자등록번호 :"+ tmp)
            
            tmp, txt = substring(txt, 6)
            LogFunc("11. 임대건수 :"+ tmp)
            
            tmp, txt = substring(txt, 4)
            LogFunc("12. 종사업자일련번호 :"+ tmp)
            
            tmp, txt = substring(txt, 70)
            LogFunc("13. 공란 :"+ tmp)
            
        elif f_type == "18":
            tmp, txt = substring(txt, 6)
            LogFunc("3. 일련번호구분 :"+ tmp)
            
            tmp, txt = substring(txt, 6)
            LogFunc("4. 일련번호 :"+ tmp)

            tmp, txt = substring(txt, 10)
            LogFunc("5. 층주소 :"+ tmp)

            tmp, txt = substring(txt, 30)
            LogFunc("6. 동주소 :"+ tmp)

            tmp, txt = substring(txt, 10)
            LogFunc("7. 호주소 :"+ tmp)

            tmp, txt = substring(txt, 10)
            LogFunc("8. 건축물면적 :"+ tmp)

            tmp, txt = substring(txt, 30)
            LogFunc("9. 임차인상호(성명) :"+ tmp)

            tmp, txt = substring(txt, 13)
            LogFunc("10. 임차인사업자등록번호 :"+ tmp)

            tmp, txt = substring(txt, 8)
            LogFunc("11. 임대계약입주일자 :"+ tmp)

            tmp, txt = substring(txt, 8)
            LogFunc("12. 임대계약퇴거일자 :"+ tmp)

            tmp, txt = substring(txt, 13)
            LogFunc("13. 임대계약보증금 :"+ tmp)

            tmp, txt = substring(txt, 13)
            LogFunc("14. 임대계약월세금액 :"+ tmp)

            tmp, txt = substring(txt, 13)
            LogFunc("15. 임대료수입합계금액(과세표준) :"+ tmp)

            tmp, txt = substring(txt, 13)
            LogFunc("16. 임대료보증금이자금액 :"+ tmp)

            tmp, txt = substring(txt, 13)
            LogFunc("17. 임대료수입월세금액 :"+ tmp)

            tmp, txt = substring(txt, 4)
            LogFunc("18. 종사업자일련번호 :"+ tmp)

            tmp, txt = substring(txt, 8)
            LogFunc("19. 임대차내역변경일자 :"+ tmp)

            tmp, txt = substring(txt, 33)
            LogFunc("20. 공란 :"+ tmp)
        else:
            LogFunc("Error : 신규타입 추가 필요 (" + f_type +")", "")
            
    def function_I103300(self, f_type, txt):
        if f_type == "17":
            tmp, txt = substring(txt, 11)
            LogFunc("3. 매수합계_세금계산서 :"+ tmp)
            
            tmp, txt = substring(txt, 15)
            LogFunc("4. 공급가액합계_세금계산서 :"+ tmp)
            
            tmp, txt = substring(txt, 15)
            LogFunc("5. 매입세액합계_세금계산서 :"+ tmp)
            
            tmp, txt = substring(txt, 15)
            LogFunc("6. 공통매입공급가액합계_안분계산 :"+ tmp)
            
            tmp, txt = substring(txt, 15)
            LogFunc("7. 공통매입세액합계_안분계산 :"+ tmp)
            
            tmp, txt = substring(txt, 15)
            LogFunc("8. 불공제매입세액합계_안분계산 :"+ tmp)
            
            tmp, txt = substring(txt, 15)
            LogFunc("9. 불공제매입세액총액합계_정산내역 :"+ tmp)
            
            tmp, txt = substring(txt, 15)
            LogFunc("10. 기불공제매입세액합계_정산내역 :"+ tmp)
            
            tmp, txt = substring(txt, 15)
            LogFunc("11. 가산·공제매입세액합계_정산내역 :"+ tmp)
            
            tmp, txt = substring(txt, 15)
            LogFunc("12. 가산·공제매입세액합계_납부재계산 :"+ tmp)
            
            tmp, txt = substring(txt, 45)
            LogFunc("13. 공란 :"+ tmp)
            
        elif f_type == "18":
            tmp, txt = substring(txt, 2)
            LogFunc("3. 불공제사유구분 :"+ tmp)
            
            tmp, txt = substring(txt, 11)
            LogFunc("4. 세금계산서매수 :"+ tmp)
            
            tmp, txt = substring(txt, 13)
            LogFunc("5. 공급가액 :"+ tmp)
            
            tmp, txt = substring(txt, 13)
            LogFunc("6. 매입세액 :"+ tmp)
            
            tmp, txt = substring(txt, 52)
            LogFunc("7. 공란 :"+ tmp)
        else:
            LogFunc("Error : 신규타입 추가 필요 (" + f_type +")", "")
            
    def check_taxbill(self, f_type, txt):
        len_txt = str(len(txt.encode(encode_mode))-1)
        '''
        if f_type.isdigit and len_txt != 170:
            LogFunc("레코드 길이 오류 :"+ len_txt)
        elif f_type.isalpha and len_txt != 230:
            LogFunc("레코드 길이 오류 :"+ len_txt)
        '''
        LogFunc("======================")
        if f_type == "7":
            tmp, txt = substring(txt, 1)
            LogFunc("1. 자료구분 :"+ tmp)
            
            tmp, txt = substring(txt, 10)
            LogFunc("2. 보고자등록번호 :"+ tmp)
            
            tmp, txt = substring(txt, 30)
            LogFunc("3. 보고자상호 :"+ tmp)
            
            tmp, txt = substring(txt, 15)
            LogFunc("4. 보고자성명 :"+ tmp)
            
            tmp, txt = substring(txt, 45)
            LogFunc("5. 보고자사업장소재지 :"+ tmp)
            
            tmp, txt = substring(txt, 17)
            LogFunc("6. 보고자업태 :"+ tmp)
            
            tmp, txt = substring(txt, 25)
            LogFunc("7. 보고자종목 :"+ tmp)
            
            tmp, txt = substring(txt, 12)
            LogFunc("8. 거래기간 :"+ tmp)
            
            tmp, txt = substring(txt, 6)
            LogFunc("9. 작성일자 :"+ tmp)
            
            tmp, txt = substring(txt, 9)
            LogFunc("10. 공란 :"+ tmp)

        elif f_type == "1":
            tmp, txt = substring(txt, 1)
            LogFunc("1. 자료구분 :"+ tmp)
            
            tmp, txt = substring(txt, 10)
            LogFunc("2. 보고자등록번호 :"+ tmp)
            
            tmp, txt = substring(txt, 4)
            LogFunc("3. 일련번호 :"+ tmp)
            
            tmp, txt = substring(txt, 10)
            LogFunc("4. 거래자등록번호 :"+ tmp)
            
            tmp, txt = substring(txt, 30)
            LogFunc("5. 거래자상호 :"+ tmp)
            
            tmp, txt = substring(txt, 17)
            LogFunc("6. 거래자업태 :"+ tmp)
            
            tmp, txt = substring(txt, 25)
            LogFunc("7. 거래자종목 :"+ tmp)
            
            tmp, txt = substring(txt, 7)
            LogFunc("8. 세금계산서매수 :"+ tmp)
            
            tmp, txt = substring(txt, 2)
            LogFunc("9. 공란수 :"+ tmp)
            
            tmp, txt = substring(txt, 14)
            LogFunc("10. 공급가액 :"+ tmp)
            
            tmp, txt = substring(txt, 13)
            LogFunc("11. 세액 :"+ tmp)
            
            tmp, txt = substring(txt, 1)
            LogFunc("12. 주류여부 :"+ tmp)
            
            tmp, txt = substring(txt, 1)
            LogFunc("13. 주류코드(소매) :"+ tmp)
            
            tmp, txt = substring(txt, 4)
            LogFunc("14. 권번호 :"+ tmp)
            
            tmp, txt = substring(txt, 3)
            LogFunc("15. 제출서 :"+ tmp)
            
            tmp, txt = substring(txt, 28)
            LogFunc("16. 공란 :"+ tmp)

        elif f_type == "3":
            tmp, txt = substring(txt, 1)
            LogFunc("1. 자료구분 :"+ tmp)
            
            tmp, txt = substring(txt, 10)
            LogFunc("2. 보고자등록번호 :"+ tmp)
            
            tmp, txt = substring(txt, 7)
            LogFunc("3. 거래처수 :"+ tmp)
            
            tmp, txt = substring(txt, 7)
            LogFunc("4. 세금계산서매수 :"+ tmp)
            
            tmp, txt = substring(txt, 15)
            LogFunc("5. 공급가액 :"+ tmp)
            
            tmp, txt = substring(txt, 14)
            LogFunc("6. 세액 :"+ tmp)
            
            tmp, txt = substring(txt, 7)
            LogFunc("7. 거래처수 :"+ tmp)
            
            tmp, txt = substring(txt, 7)
            LogFunc("8. 세금계산서매수 :"+ tmp)
            
            tmp, txt = substring(txt, 15)
            LogFunc("9. 공급가액 :"+ tmp)
            
            tmp, txt = substring(txt, 14)
            LogFunc("10. 세액 :"+ tmp)
            
            tmp, txt = substring(txt, 7)
            LogFunc("11. 거래처수 :"+ tmp)
            
            tmp, txt = substring(txt, 7)
            LogFunc("12. 세금계산서매수 :"+ tmp)
            
            tmp, txt = substring(txt, 15)
            LogFunc("13. 공급가액 :"+ tmp)
            
            tmp, txt = substring(txt, 14)
            LogFunc("14. 세액 :"+ tmp)
            
            tmp, txt = substring(txt, 30)
            LogFunc("15. 공란 :"+ tmp)
            
        elif f_type == "5":
            tmp, txt = substring(txt, 1)
            LogFunc("1. 자료구분 :"+ tmp)
            tmp, txt = substring(txt, 10)
            LogFunc("2. 보고자등록번호 :"+ tmp)
            tmp, txt = substring(txt, 7)
            LogFunc("3. 거래처수 :"+ tmp)
            tmp, txt = substring(txt, 7)
            LogFunc("4. 세금계산서매수 :"+ tmp)
            tmp, txt = substring(txt, 15)
            LogFunc("5. 공급가액 :"+ tmp)
            tmp, txt = substring(txt, 14)
            LogFunc("6. 세액 :"+ tmp)
            tmp, txt = substring(txt, 7)
            LogFunc("7. 거래처수 :"+ tmp)
            tmp, txt = substring(txt, 7)
            LogFunc("8. 세금계산서매수 :"+ tmp)
            tmp, txt = substring(txt, 15)
            LogFunc("9. 공급가액 :"+ tmp)
            tmp, txt = substring(txt, 14)
            LogFunc("10. 세액 :"+ tmp)
            tmp, txt = substring(txt, 7)
            LogFunc("11. 거래처수 :"+ tmp)
            tmp, txt = substring(txt, 7)
            LogFunc("12. 세금계산서매수 :"+ tmp)
            tmp, txt = substring(txt, 15)
            LogFunc("13. 공급가액 :"+ tmp)
            tmp, txt = substring(txt, 14)
            LogFunc("14. 세액 :"+ tmp)
            tmp, txt = substring(txt, 30)
            LogFunc("15. 공란 :"+ tmp)
            
        elif f_type == "2":
            tmp, txt = substring(txt, 1)
            LogFunc("1. 자료구분 :"+ tmp)
            tmp, txt = substring(txt, 10)
            LogFunc("2. 보고자등록번호 :"+ tmp)
            tmp, txt = substring(txt, 4)
            LogFunc("3. 일련번호 :"+ tmp)
            tmp, txt = substring(txt, 10)
            LogFunc("4. 거래자등록번호 :"+ tmp)
            tmp, txt = substring(txt, 30)
            LogFunc("5. 거래자상호 :"+ tmp)
            tmp, txt = substring(txt, 17)
            LogFunc("6. 거래자업태 :"+ tmp)
            tmp, txt = substring(txt, 25)
            LogFunc("7. 거래자종목 :"+ tmp)
            tmp, txt = substring(txt, 7)
            LogFunc("8. 세금계산서매수 :"+ tmp)
            tmp, txt = substring(txt, 2)
            LogFunc("9. 공란수 :"+ tmp)
            tmp, txt = substring(txt, 14)
            LogFunc("10. 공급가액 :"+ tmp)
            tmp, txt = substring(txt, 13)
            LogFunc("11. 세액 :"+ tmp)
            tmp, txt = substring(txt, 1)
            LogFunc("12. 신고자주류코드(도매) :"+ tmp)
            tmp, txt = substring(txt, 1)
            LogFunc("13. 주류코드(소매) :"+ tmp)
            tmp, txt = substring(txt, 4)
            LogFunc("14. 권번호 :"+ tmp)
            tmp, txt = substring(txt, 3)
            LogFunc("15. 제출서 :"+ tmp)
            tmp, txt = substring(txt, 28)
            LogFunc("16. 공란 :"+ tmp)
            
        elif f_type == "4":
            tmp, txt = substring(txt, 1)
            LogFunc("1. 자료구분 :"+ tmp)
            tmp, txt = substring(txt, 10)
            LogFunc("2. 보고자등록번호 :"+ tmp)
            tmp, txt = substring(txt, 7)
            LogFunc("3. 거래처수 :"+ tmp)
            tmp, txt = substring(txt, 7)
            LogFunc("4. 세금계산서매수 :"+ tmp)
            tmp, txt = substring(txt, 15)
            LogFunc("5. 공급가액 :"+ tmp)
            tmp, txt = substring(txt, 14)
            LogFunc("6. 세액 :"+ tmp)
            tmp, txt = substring(txt, 7)
            LogFunc("7. 거래처수 :"+ tmp)
            tmp, txt = substring(txt, 7)
            LogFunc("8. 세금계산서매수 :"+ tmp)
            tmp, txt = substring(txt, 15)
            LogFunc("9. 공급가액 :"+ tmp)
            tmp, txt = substring(txt, 14)
            LogFunc("10. 세액 :"+ tmp)
            tmp, txt = substring(txt, 7)
            LogFunc("11. 거래처수 :"+ tmp)
            tmp, txt = substring(txt, 7)
            LogFunc("12. 세금계산서매수 :"+ tmp)
            tmp, txt = substring(txt, 15)
            LogFunc("13. 공급가액 :"+ tmp)
            tmp, txt = substring(txt, 14)
            LogFunc("14. 세액 :"+ tmp)
            tmp, txt = substring(txt, 30)
            LogFunc("15. 공란 :"+ tmp)
            
        elif f_type == "6":
            tmp, txt = substring(txt, 1)
            LogFunc("1. 자료구분 :"+ tmp)
            tmp, txt = substring(txt, 10)
            LogFunc("2. 보고자등록번호 :"+ tmp)
            tmp, txt = substring(txt, 7)
            LogFunc("3. 거래처수 :"+ tmp)
            tmp, txt = substring(txt, 7)
            LogFunc("4. 세금계산서매수 :"+ tmp)
            tmp, txt = substring(txt, 15)
            LogFunc("5. 공급가액 :"+ tmp)
            tmp, txt = substring(txt, 14)
            LogFunc("6. 세액 :"+ tmp)
            tmp, txt = substring(txt, 7)
            LogFunc("7. 거래처수 :"+ tmp)
            tmp, txt = substring(txt, 7)
            LogFunc("8. 세금계산서매수 :"+ tmp)
            tmp, txt = substring(txt, 15)
            LogFunc("9. 공급가액 :"+ tmp)
            tmp, txt = substring(txt, 14)
            LogFunc("10. 세액 :"+ tmp)
            tmp, txt = substring(txt, 7)
            LogFunc("11. 거래처수 :"+ tmp)
            tmp, txt = substring(txt, 7)
            LogFunc("12. 세금계산서매수 :"+ tmp)
            tmp, txt = substring(txt, 15)
            LogFunc("13. 공급가액 :"+ tmp)
            tmp, txt = substring(txt, 14)
            LogFunc("14. 세액 :"+ tmp)
            tmp, txt = substring(txt, 30)
            LogFunc("15. 공란 :"+ tmp)
            
    def check_sumReport(self, f_type, txt):
        LogFunc("======================")
        if f_type == "A":
            tmp, txt = substring(txt, 1)
            LogFunc("1. 레코드구분 :"+ tmp)
            tmp, txt = substring(txt, 3)
            LogFunc("2. 세무서 :"+ tmp)
            tmp, txt = substring(txt, 8)
            LogFunc("3. 제출년월일 :"+ tmp)
            tmp, txt = substring(txt, 1)
            LogFunc("4. 제출자구분 :"+ tmp)
            tmp, txt = substring(txt, 6)
            LogFunc("5. 세무대리인관리번호 :"+ tmp)
            tmp, txt = substring(txt, 10)
            LogFunc("6. 사업자등록번호 :"+ tmp)
            tmp, txt = substring(txt, 40)
            LogFunc("7. 법인명(상호) :"+ tmp)
            tmp, txt = substring(txt, 13)
            LogFunc("8. 주민(법인)등록번호 :"+ tmp)
            tmp, txt = substring(txt, 30)
            LogFunc("9. 대표자(성명) :"+ tmp)
            tmp, txt = substring(txt, 10)
            LogFunc("10. 소재지(우편번호)법정동 코드 :"+ tmp)
            tmp, txt = substring(txt, 70)
            LogFunc("11. 소재지(주소) :"+ tmp)
            tmp, txt = substring(txt, 15)
            LogFunc("12. 전화번호 :"+ tmp)
            tmp, txt = substring(txt, 5)
            LogFunc("13. 제출건수계 :"+ tmp)
            tmp, txt = substring(txt, 3)
            LogFunc("14. 사용한한글코드종류 :"+ tmp)
            tmp, txt = substring(txt, 15)
            LogFunc("15. 공란 :"+ tmp)
        elif f_type == "B":
            tmp, txt = substring(txt, 1)
            LogFunc("1. 레코드구분 :"+ tmp)
            tmp, txt = substring(txt, 3)
            LogFunc("2. 세무서 :"+ tmp)
            tmp, txt = substring(txt, 6)
            LogFunc("3. 일련번호 :"+ tmp)
            tmp, txt = substring(txt, 10)
            LogFunc("4. 사업자등록번호 :"+ tmp)
            tmp, txt = substring(txt, 40)
            LogFunc("5. 법인명(상호) :"+ tmp)
            tmp, txt = substring(txt, 30)
            LogFunc("6. 대표자(성명) :"+ tmp)
            tmp, txt = substring(txt, 10)
            LogFunc("7. 사업장(우편번호)법정동코드 :"+ tmp)
            tmp, txt = substring(txt, 70)
            LogFunc("8. 사업장소재지(주소) :"+ tmp)
            tmp, txt = substring(txt, 60)
            LogFunc("9. 공란 :"+ tmp)
        elif f_type == "C":
            tmp, txt = substring(txt, 1)
            LogFunc("1. 레코드구분 :"+ tmp)
            tmp, txt = substring(txt, 2)
            LogFunc("2. 자료구분 :"+ tmp)
            if tmp == "17":
                tmp, txt = substring(txt, 1)
                LogFunc("3. 기구분 :"+ tmp)
                tmp, txt = substring(txt, 1)
                LogFunc("4. 신고구분 :"+ tmp)
                tmp, txt = substring(txt, 3)
                LogFunc("5. 세무서 :"+ tmp)
                tmp, txt = substring(txt, 6)
                LogFunc("6. 일련번호 :"+ tmp)
                tmp, txt = substring(txt, 10)
                LogFunc("7. 사업자등록번호 :"+ tmp)
                tmp, txt = substring(txt, 4)
                LogFunc("8. 귀속년도 :"+ tmp)
                tmp, txt = substring(txt, 8)
                LogFunc("9. 거래기간시작년월일 :"+ tmp)
                tmp, txt = substring(txt, 8)
                LogFunc("10. 거래기간종료년월일 :"+ tmp)
                tmp, txt = substring(txt, 8)
                LogFunc("11. 작성일자 :"+ tmp)
                tmp, txt = substring(txt, 6)
                LogFunc("12. 매출처수합계 :"+ tmp)
                tmp, txt = substring(txt, 6)
                LogFunc("13. 계산서매수합계 :"+ tmp)
                tmp, txt = substring(txt, 1)
                LogFunc("14. 매출(수입)금액합계음수표시 :"+ tmp)
                tmp, txt = substring(txt, 14)
                LogFunc("15. 매출(수입)금액합계 :"+ tmp)
                tmp, txt = substring(txt, 6)
                LogFunc("16. 사업자등록번호발행분매출처수 :"+ tmp)
                tmp, txt = substring(txt, 6)
                LogFunc("17. 사업자등록번호발행분계산서매수 :"+ tmp)
                tmp, txt = substring(txt, 1)
                LogFunc("18. 사업자등록번호발행분매출(수입)금액음수표시 :"+ tmp)
                tmp, txt = substring(txt, 14)
                LogFunc("19. 사업자등록번호발행분매출(수입)금액 :"+ tmp)
                tmp, txt = substring(txt, 6)
                LogFunc("20. 주민등록번호발행분매출처수 :"+ tmp)
                tmp, txt = substring(txt, 6)
                LogFunc("21. 주민등록번호발행분계산서매수 :"+ tmp)
                tmp, txt = substring(txt, 1)
                LogFunc("22. 주민등록번호발행분매출(수입)금액음수표시 :"+ tmp)
                tmp, txt = substring(txt, 14)
                LogFunc("23. 주민등록번호발행분매출(수입)금액 :"+ tmp)
                tmp, txt = substring(txt, 97)
                LogFunc("24. 공란 :"+ tmp)
            elif tmp == "18":
                tmp, txt = substring(txt, 1)
                LogFunc("3. 기구분 :"+ tmp)
                tmp, txt = substring(txt, 1)
                LogFunc("4. 신고구분 :"+ tmp)
                tmp, txt = substring(txt, 3)
                LogFunc("5. 세무서 :"+ tmp)
                tmp, txt = substring(txt, 6)
                LogFunc("6. 일련번호 :"+ tmp)
                tmp, txt = substring(txt, 10)
                LogFunc("7. 사업자등록번호 :"+ tmp)
                tmp, txt = substring(txt, 4)
                LogFunc("8. 귀속년도 :"+ tmp)
                tmp, txt = substring(txt, 8)
                LogFunc("9. 거래기간시작년월일 :"+ tmp)
                tmp, txt = substring(txt, 8)
                LogFunc("10. 거래기간종료년월일 :"+ tmp)
                tmp, txt = substring(txt, 8)
                LogFunc("11. 작성일자 :"+ tmp)
                tmp, txt = substring(txt, 6)
                LogFunc("12. 매입처수합계 :"+ tmp)
                tmp, txt = substring(txt, 6)
                LogFunc("13. 계산서매수합계 :"+ tmp)
                tmp, txt = substring(txt, 1)
                LogFunc("14. 매입금액합계음수표시 :"+ tmp)
                tmp, txt = substring(txt, 14)
                LogFunc("15. 매입금액합계 :"+ tmp)
                tmp, txt = substring(txt, 151)
                LogFunc("16. 공란 :"+ tmp)
                
        elif f_type == "D":
            tmp, txt = substring(txt, 1)
            LogFunc("1. 레코드구분 :"+ tmp)
            tmp, txt = substring(txt, 2)
            LogFunc("2. 자료구분 :"+ tmp)
            if tmp == "17":
                tmp, txt = substring(txt, 1)
                LogFunc("3. 기구분 :"+ tmp)
                tmp, txt = substring(txt, 1)
                LogFunc("4. 신고구분 :"+ tmp)
                tmp, txt = substring(txt, 3)
                LogFunc("5. 세무서 :"+ tmp)
                tmp, txt = substring(txt, 6)
                LogFunc("6. 일련번호 :"+ tmp)
                tmp, txt = substring(txt, 10)
                LogFunc("7. 사업자등록번호 :"+ tmp)
                tmp, txt = substring(txt, 10)
                LogFunc("8. 매출처사업자등록번호 :"+ tmp)
                tmp, txt = substring(txt, 40)
                LogFunc("9. 매출처법인명(상호) :"+ tmp)
                tmp, txt = substring(txt, 5)
                LogFunc("10. 계산서매수 :"+ tmp)
                tmp, txt = substring(txt, 1)
                LogFunc("11. 매출(수입)금액음수표시 :"+ tmp)
                tmp, txt = substring(txt, 14)
                LogFunc("12. 매출(수입)금액 :"+ tmp)
                tmp, txt = substring(txt, 136)
                LogFunc("13. 공란 :"+ tmp)
            elif tmp == "18":
                tmp, txt = substring(txt, 1)
                LogFunc("3. 기구분 :"+ tmp)
                tmp, txt = substring(txt, 1)
                LogFunc("4. 신고구분 :"+ tmp)
                tmp, txt = substring(txt, 3)
                LogFunc("5. 세무서 :"+ tmp)
                tmp, txt = substring(txt, 6)
                LogFunc("6. 일련번호 :"+ tmp)
                tmp, txt = substring(txt, 10)
                LogFunc("7. 사업자등록번호 :"+ tmp)
                tmp, txt = substring(txt, 10)
                LogFunc("8. 매입처사업자등록번호 :"+ tmp)
                tmp, txt = substring(txt, 40)
                LogFunc("9. 매입처법인명(상호) :"+ tmp)
                tmp, txt = substring(txt, 5)
                LogFunc("10. 계산서매수 :"+ tmp)
                tmp, txt = substring(txt, 1)
                LogFunc("11. 매입금액음수표시 :"+ tmp)
                tmp, txt = substring(txt, 14)
                LogFunc("12. 매입금액 :"+ tmp)
                tmp, txt = substring(txt, 136)
                LogFunc("13. 공란 :"+ tmp)
            
        elif f_type == "E":
            tmp, txt = substring(txt, 1)
            LogFunc("1. 레코드구분 :"+ tmp)
            tmp, txt = substring(txt, 2)
            LogFunc("2. 자료구분 :"+ tmp)
            if tmp == "17":
                tmp, txt = substring(txt, 1)
                LogFunc("3. 기구분 :"+ tmp)
                tmp, txt = substring(txt, 1)
                LogFunc("4. 신고구분 :"+ tmp)
                tmp, txt = substring(txt, 3)
                LogFunc("5. 세무서 :"+ tmp)
                tmp, txt = substring(txt, 6)
                LogFunc("6. 일련번호 :"+ tmp)
                tmp, txt = substring(txt, 10)
                LogFunc("7. 사업자등록번호 :"+ tmp)
                tmp, txt = substring(txt, 4)
                LogFunc("8. 귀속년도 :"+ tmp)
                tmp, txt = substring(txt, 8)
                LogFunc("9. 거래기간시작년월일 :"+ tmp)
                tmp, txt = substring(txt, 8)
                LogFunc("10. 거래기간종료년월일 :"+ tmp)
                tmp, txt = substring(txt, 8)
                LogFunc("11. 작성일자 :"+ tmp)
                tmp, txt = substring(txt, 6)
                LogFunc("12. 매출처수합계 :"+ tmp)
                tmp, txt = substring(txt, 6)
                LogFunc("13. 계산서매수합계 :"+ tmp)
                tmp, txt = substring(txt, 1)
                LogFunc("14. 매출(수입)금액합계음수표시 :"+ tmp)
                tmp, txt = substring(txt, 14)
                LogFunc("15. 매출(수입)금액합계 :"+ tmp)
                tmp, txt = substring(txt, 6)
                LogFunc("16. 사업자등록번호발행분매출처수 :"+ tmp)
                tmp, txt = substring(txt, 6)
                LogFunc("17. 사업자등록번호발행분계산서매수 :"+ tmp)
                tmp, txt = substring(txt, 1)
                LogFunc("18. 사업자등록번호발행분매출(수입)금액음수표시 :"+ tmp)
                tmp, txt = substring(txt, 14)
                LogFunc("19. 사업자등록번호발행분매출(수입)금액 :"+ tmp)
                tmp, txt = substring(txt, 6)
                LogFunc("20. 주민등록번호발행분매출처수 :"+ tmp)
                tmp, txt = substring(txt, 6)
                LogFunc("21. 주민등록번호발행분계산서매수 :"+ tmp)
                tmp, txt = substring(txt, 1)
                LogFunc("22. 주민등록번호발행분매출(수입)금액음수표시 :"+ tmp)
                tmp, txt = substring(txt, 14)
                LogFunc("23. 주민등록번호발행분매출(수입)금액 :"+ tmp)
                tmp, txt = substring(txt, 97)
                LogFunc("24. 공란 :"+ tmp)
            elif tmp == "18":
                tmp, txt = substring(txt, 1)
                LogFunc("3. 기구분 :"+ tmp)
                tmp, txt = substring(txt, 1)
                LogFunc("4. 신고구분 :"+ tmp)
                tmp, txt = substring(txt, 3)
                LogFunc("5. 세무서 :"+ tmp)
                tmp, txt = substring(txt, 6)
                LogFunc("6. 일련번호 :"+ tmp)
                tmp, txt = substring(txt, 10)
                LogFunc("7. 제출의무자(사업자)사업자등록번호 :"+ tmp)
                tmp, txt = substring(txt, 4)
                LogFunc("8. 귀속년도 :"+ tmp)
                tmp, txt = substring(txt, 8)
                LogFunc("9. 거래기간시작년월일 :"+ tmp)
                tmp, txt = substring(txt, 8)
                LogFunc("10. 거래기간종료년월일 :"+ tmp)
                tmp, txt = substring(txt, 8)
                LogFunc("11. 작성일자 :"+ tmp)
                tmp, txt = substring(txt, 6)
                LogFunc("12. 매입처수합계 :"+ tmp)
                tmp, txt = substring(txt, 6)
                LogFunc("13. 계산서매수합계 :"+ tmp)
                tmp, txt = substring(txt, 1)
                LogFunc("14. 매입금액합계음수표시 :"+ tmp)
                tmp, txt = substring(txt, 14)
                LogFunc("15. 매입금액합계 :"+ tmp)
                tmp, txt = substring(txt, 151)
                LogFunc("16. 공란 :"+ tmp)
        else:
            LogFunc("Error : 타입 추가 필요 ("+f_type+"(","")
            
    def check_creditcard(self,f_type,txt):
        LogFunc("======================")
        if f_type == "HL":
            tmp, txt = substring(txt, 2)
            LogFunc("1. 레코드구분 :"+ tmp)
            tmp, txt = substring(txt, 4)
            LogFunc("2. 귀속년도 :"+ tmp)
            tmp, txt = substring(txt, 1)
            LogFunc("3. 반기구분 :"+ tmp)
            tmp, txt = substring(txt, 1)
            LogFunc("4. 반기내월순번 :"+ tmp)
            tmp, txt = substring(txt, 10)
            LogFunc("5. 수취자(제출자)사업자등록번호 :"+ tmp)
            tmp, txt = substring(txt, 60)
            LogFunc("6. 상호(법인명) :"+ tmp)
            tmp, txt = substring(txt, 30)
            LogFunc("7. 성명(대표자) :"+ tmp)
            tmp, txt = substring(txt, 13)
            LogFunc("8. 주민(법인)등록번호 :"+ tmp)
            tmp, txt = substring(txt, 8)
            LogFunc("9. 제출일자 :"+ tmp)
            tmp, txt = substring(txt, 11)
            LogFunc("10. 공란 :"+ tmp)
        elif f_type == "DL":
            tmp, txt = substring(txt, 2)
            LogFunc("1. 레코드구분 :"+ tmp)
            tmp, txt = substring(txt, 4)
            LogFunc("2. 귀속년도 :"+ tmp)
            tmp, txt = substring(txt, 1)
            LogFunc("3. 반기구분 :"+ tmp)
            tmp, txt = substring(txt, 1)
            LogFunc("4. 반기내월 순번 :"+ tmp)
            tmp, txt = substring(txt, 10)
            LogFunc("5. 수취자(제출자)사업자등록번호 :"+ tmp)
            tmp, txt = substring(txt, 1)
            LogFunc("6. 카드구분 :"+ tmp)
            tmp, txt = substring(txt, 20)
            LogFunc("7. 카드회원번호 :"+ tmp)
            tmp, txt = substring(txt, 10)
            LogFunc("8. 공급자(가맹점)사업자등록번호 :"+ tmp)
            tmp, txt = substring(txt, 9)
            LogFunc("9. 거래건수 :"+ tmp)
            tmp, txt = substring(txt, 1)
            LogFunc("10. 음수표시 :"+ tmp)
            tmp, txt = substring(txt, 13)
            LogFunc("11. 공급가액 :"+ tmp)
            tmp, txt = substring(txt, 1)
            LogFunc("12. 음수표시 :"+ tmp)
            tmp, txt = substring(txt, 13)
            LogFunc("13. 세액 :"+ tmp)
            tmp, txt = substring(txt, 54)
            LogFunc("14. 공란 :"+ tmp)
        elif f_type == "TL":
            tmp, txt = substring(txt, 2)
            LogFunc("1. 레코드구분 :"+ tmp)
            tmp, txt = substring(txt, 4)
            LogFunc("2. 귀속년도 :"+ tmp)
            tmp, txt = substring(txt, 1)
            LogFunc("3. 반기구분 :"+ tmp)
            tmp, txt = substring(txt, 1)
            LogFunc("4. 반기내월 순번 :"+ tmp)
            tmp, txt = substring(txt, 10)
            LogFunc("5. 수취자(제출자)사업자등록번호 :"+ tmp)
            tmp, txt = substring(txt, 7)
            LogFunc("6. DATA 건수 :"+ tmp)
            tmp, txt = substring(txt, 9)
            LogFunc("7. 총거래건수 :"+ tmp)
            tmp, txt = substring(txt, 1)
            LogFunc("8. 음수표시 :"+ tmp)
            tmp, txt = substring(txt, 15)
            LogFunc("9. 총공급가액 :"+ tmp)
            tmp, txt = substring(txt, 1)
            LogFunc("10. 음수표시 :"+ tmp)
            tmp, txt = substring(txt, 15)
            LogFunc("11. 총세액 :"+ tmp)
            tmp, txt = substring(txt, 74)
            LogFunc("12. 공란 :"+ tmp)

    