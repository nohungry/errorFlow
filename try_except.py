import time

# 設計一個list故意讓他可以產生錯誤 (未加try - except)
def tryList(x:list):
    words = "Kay is so wonderful"
    maxNum = len(x)
    x[maxNum] = words
    return x

# 設計一個list超出範圍後，仍然可以繼續進行後續程式
def tryList(x:list):
    try:
        words = "Kay is so wonderful"
        maxNum = len(x)
        x[maxNum] = words
        return x
    # 假如 12 - 16 任一行遇到 indexError，則執行下列的程式碼。
    except IndexError:
        print("except process on")
        time.sleep(10)
        print("research target List maximun length")
        keyWords = "Kay is so clever"
        normanWords = "Norman is so hungry"
        x.append(keyWords)
        x.append(normanWords)
        return x
    # 假如 12 - 16 任一行遇到其他錯誤(撇除indexError) ，則執行下列的程式碼。
    except:
        print("發生撰寫程式者未知的錯誤")


if __name__ == "__main__":
    testList = ["1", "2", "3", 4, 5, 6, 7]
    listData = tryList(testList)
    print(listData)
        