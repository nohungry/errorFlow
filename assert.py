def assertTest(x:list):
    assert x[0] == "Kay是最棒的", "List內部文案錯誤，Kay明明是最棒的"
    x.append("Kay is the best")
    return x

if __name__ == "__main__":
    x = [1, 2, 3, 4, 5, 6]
    listData = assertTest(x)
    print(listData)