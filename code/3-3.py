import sys
寻找女朋友=lambda x:print('%d岁，寻找女朋友ing...'%x)
结婚=lambda x:print('%d岁，结婚啦,xswl'%x)
单身=lambda :print('emmm其实单身也挺好...')
等死=lambda:print('等死,人最终还是要死的，也不知我死的时候是一个人还是两个人，都有可能')

def 生活(结婚年龄):
    for 年龄 in range(5):
        print('%d岁，没印象，应该单身吧？'%年龄)
    for 年龄 in range(5,10):
        print('%d岁～%d岁，有印象，单身!'%(年龄,年龄+1))
    for 年龄 in range(10,20,2):
        print('%d岁～%d岁，依然单身'%(年龄,年龄+2))
    while 40>年龄 >=18:
        try:
            寻找女朋友(年龄)
            还没找到女朋友 = 年龄<结婚年龄-3
            if 还没找到女朋友 and 年龄<30:
                continue
            elif not 还没找到女朋友:
                pass
            else:
                raise Exception('唉，注孤生')
        except Exception as e:
            print(e)
        else:
            结婚(年龄+3)
            return
        finally:
            等死()
            年龄+=1
    单身()

if __name__=='__main__':
    assert len(sys.argv)==2,'输入结婚年龄哦'
    结婚年龄=int(sys.argv[1])
    生活(结婚年龄)

