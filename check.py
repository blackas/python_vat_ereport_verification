import os
import sys
import copy
import check_function as check_function
encode_mode = 'euc-kr'

if len(sys.argv) != 2:
    print("error : 확인할 파일 또는 폴더 경로를 입력해주세요")
    sys.exit()

file_path = sys.argv[1]

file_list = os.listdir(file_path)
os.chdir(file_path)

str_business_no = ""

#서식별 구분 코드 
dic_identification_code = {
"I103200":"일반과세자 부가가치세 신고서",
"I106000":"간이과세자 부가가치세 신고서",
"I104400":"사업장현황명세서",
"I103400":"신용카드매출전표등 발행금액등집계표",
"I105800":"영세율첨부서류제출명세서",
"I102300":"의제매입세액공제신고서",
"I103600":"부동산임대공급가액명세서",
"I102800":"대손세액공제(변제)신고서",
"I104500":"사업장별 부가가치세 과세표준 및 납부세액(환급세액)신고명세서",
"I105000":"매출처별 세금계산서 합계표(갑,을)",
"I105200":"매입처별 세금계산서 합계표(갑,을)",
"C107200":"매입처별계산서합계표",
"C107100":"매출처별계산서합계표",
"I105400":"수출실적명세서",
"I103500":"전자화폐결제명세서",
"J400100":"면세유류공급명세서",
"M116300":"재활용폐자원및중고자동차매입세액공제신고서(갑,을)",
"M200100":"월별판매액합계표(농•축산•임•어업용기자재)",
"I103800":"건물 등 감가상각자산 취득명세서",
"I103300":"공제받지못할매입세액명세서",
"M118000":"매입자발행세금계산서합계표(갑)",
"I102600":"과세사업전환 감가상각자산신고서",
"I102400":"신용카드매출전표등 수령명세서(갑,을)",
"I104300":"건물관리명세서",
"I103900":"사업자단위과세의 사업장별 부가가치세 과세표준 및 납부세액(환급세액)신고명세서",
"I103700":"현금매출명세서",
"M120900":"고금의제매입세액공제신고서",
"A102700":"과세표준및세액의결정(경정)청구서",
"A102600":"과세표준수정신고서및추가자진납부계산서",
"I103100":"전자세금계산서발급세액공제신고서",
"I102700":"일반(간이)과세전환 시 재고품등신고서",
"M100100":"세액공제신청서",
"I105600":"내국신용장 • 구매확인서 전자발급명세서",
"M115900":"원산지확인서발급세액공제신고서",
"I104100":"동물진료용역매출명세서",
"I104000":"영세율매출명세서",
"M202300":"외국인관광객면세물품판매 및 환급실적명세서",
"M125200":"구리스크랩등매입세액공제신고서(갑,을)<신규서식추가>",
"I401500":"관세환급금등 명세서",
"I402000":"외국인물품(외교관면세)판매 기록표",
"I401700":"공급가액확정명세서",
"I401600":"선박에 의한 운송용역 공급가액일람표",
"I401800":"외항.선박등에 제공한 재화용역일람표",
"I402100":"외화획득명세서",
"I401900":"재화.용역공급기록표",
"I104200":"사업양도신고서",
"I106900":"외국인관광객 즉시환급 물품 판매 실적명세서",
"M127200":"평창동계올림픽 관련 사업자에 대한 의제매입세액공제 신고서",
"M127300":"2019 광주 세계수영선수권대회 관련 사업자에 대한 의제매입세액공제 신고서",
"M128600":"입국경로에 설치된 보세판매장 공급실적명세서",
"M129200":"소규모 개인사업자 부가가치세 감면 신청서",
"M129400":"외국인관광객 숙박용역 환급실적명세서",
"M129300":"외국인관광객 미용성형 의료용역 환급실적명세서"}

#서식별 코드 매핑 함수
dic_function = {
"I103200":"function_I103200",
"I106000":"function_I106000",
"I104400":"function_I104400",
"I103400":"function_I103400",
"I105800":"function_I105800",
"I102300":"function_I102300",
"I103600":"function_I103600",
"I102800":"function_I102800",
"I104500":"function_I104500",
"I105000":"function_I105000",
"I105200":"function_I105200",
"C107200":"function_C107200",
"C107100":"function_C107100",
"I105400":"function_I105400",
"I103500":"function_I103500",
"J400100":"function_J400100",
"M116300":"function_M116300",
"M200100":"function_M200100",
"I103800":"function_I103800",
"I103300":"function_I103300",
"M118000":"function_M118000",
"I102600":"function_I102600",
"I102400":"function_I102400",
"I104300":"function_I104300",
"I103900":"function_I103900",
"I103700":"function_I103700",
"M120900":"function_M120900",
"A102700":"function_A102700",
"A102600":"function_A102600",
"I103100":"function_I103100",
"I102700":"function_I102700",
"M100100":"function_M100100",
"I105600":"function_I105600",
"M115900":"function_M115900",
"I104100":"function_I104100",
"I104000":"function_I104000",
"M202300":"function_M202300",
"M125200":"function_M125200",
"I401500":"function_I401500",
"I402000":"function_I402000",
"I401700":"function_I401700",
"I401600":"function_I401600",
"I401800":"function_I401800",
"I402100":"function_I402100",
"I401900":"function_I401900",
"I104200":"function_I104200",
"I106900":"function_I106900",
"M127200":"function_M127200",
"M127300":"function_M127300",
"M128600":"function_M128600",
"M129200":"function_M129200",
"M129400":"function_M129400",
"M129300":"function_M129300"}

def check_line(file, line_num, txt):
    global str_business_no
    
    if line_num == 1:
        vat_func.check_head(line_num, txt)
        str_business_no = vat_func.getBusinessNo()
        return
    
    check = check_function.getstring(txt,11) #전자세금계산서 레코드 여부 확인 값
    if check[0] in ["1","2","3","4","5","6"] and check[1:] == str_business_no:
        vat_func.check_taxbill(check[0], txt)
        return
        
    check = check_function.getstring(txt,2)
    if check.isdigit() and check in ["18","17","16","15","14","13"]:

        check_function.LogFunc("================================")
        check_function.LogFunc("레코드 길이 :" + check_function.getlength(txt))
        
        check, txt = check_function.substring(txt, 2)
        check_function.LogFunc("1. 자료구분 :" + check)
        
        tmp, txt = check_function.substring(txt, 7)
        if tmp not in dic_identification_code.keys():
            check_function.LogFunc("error : 잘못된 서식 코드입니다. (" + tmp + ")")
            return

        check_function.LogFunc("2. 서식코드 :" + tmp + " (" + dic_identification_code[tmp] + ")" )

        function_nm = getattr(vat_func, dic_function[tmp])
        function_nm(check, txt)
        return
        
    elif check.isalpha():
        vat_func.check_creditcard(check,txt)
        return

    check = check_function.getstring(txt,1) #전자세금계산서 레코드 여부 확인 값    
    if check.isalpha():                     # in ["C17","D17","E17","C18","D18","E18"]:
        vat_func.check_sumReport(check, txt)
        return


if __name__ == "__main__":
    line_num = 1
    
    for file in file_list:
        f = open(file,'r')
        vat_func = check_function.Vat_Function(file)
        line_num = 1
        lines = f.readlines()
        for line in lines:
            check_line(file, line_num, line)
            line_num += 1
        f.close()
        del(vat_func)