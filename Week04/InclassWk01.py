"""Inclass Ex"""
# uncomment function call to use that function

### question1 ###
def question1(text) :
    """question1"""
    ans = (text + "_")*len(text)
    print(ans[:-1])
# question1(input())

### question2 ###
def question2(text) :
    """question1"""
    ntext = text[::3]
    ntext = ntext[::-1]
    print(ntext)
# question2(input())


