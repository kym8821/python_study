from code1 import *
from testCase import *

ANSI_COLOR_CODE = {
    "WHITE":37,
    "RED":31,
    "YELLOW":33,
    "GREEN":32,
}

def createErrorLog(prefix, seed, expected, result):
    return "{3} : x={0}이고 기댓값은 {1}이지만, 결과가 {2}이다.\n".format(seed, expected, result, prefix)

def checkCode(code_name, func, file, tc, ans):
    score = 0
    error_log = ""
    try:
        for i in range(len(tc)):
            x = tc[i]
            expected=ans[i]
            result = func(x)
            if expected == result:
                score+=10
            else:
                error_log = error_log + createErrorLog(prefix=code_name, seed=x, expected=expected, result=result)
    except:
        error_log = error_log + "{} 실행 중 에러 발생".format(code_name)
    finally:
        file.write(error_log)
    # 결과 출력
    if 0<=score<50:
        score_color = ANSI_COLOR_CODE["RED"]
    elif 50<=score<75:
        score_color = ANSI_COLOR_CODE["YELLOW"]
    else:
        score_color = ANSI_COLOR_CODE["GREEN"]
    print('\033[37m' + code_name + ' : ' + 
          '\033[' + str(score_color) + 'm' + str(score) + ' / 100' + '\033[0m')
    return score

err = [1,2,3]
def main():
    file = open("error_log", "w", encoding="UTF-8")
    checkCode("code1", func1, file, tc1, ans1)
    file.close()

main()