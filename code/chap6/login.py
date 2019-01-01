import time

import requests
import bs4


def login(username, password, remember_me=True, url="http://acm.zjnu.edu.cn/CLanguage/login"):
    # 获取一个session,会自动帮你处理好cookie,类似下面这样
    # cookies = dict(cookies_are='working')
    # requests.get(url, cookies=cookies)
    # 一些难模拟登录的（比如有验证码），可以手动登录，手动获取cookie,设置cookie
    #
    session = requests.session()
    # 以POST方法提交数据登录,以及设置User-Agent，这个网站没有检验，随便写不写
    resp = session.post(url, data={
        'user_id1': username,
        'password1': password,
        'rememberMe': True,
        'url': '/'
    }, headers={"User-Agent": "balabala"})

    # 获取返回的内容
    content = resp.text
    # 如果登录成功，就可以看到自己的用户名
    assert content.find(username) > 0
    print('登录成功')

    # 返回session,毕竟后面还要用到
    return session


def search_questions(session):
    resp = session.get('http://acm.zjnu.edu.cn/CLanguage/problemlist')
    soup = bs4.BeautifulSoup(resp.text, 'lxml')
    id_list = []

    # 有个下划线,返回所有的class="ac"的tr
    for tr in soup.find_all(class_='ac'):
        # 返回Tag不是字符串<class 'bs4.element.Tag'>
        # print(type(tr))

        # 返回的是第2个子结点的文本值
        id = tr.contents[1].text
        id_list.append(id)
    return id_list


def get_code_test(session):
    resp = session.get('http://acm.zjnu.edu.cn/CLanguage/showsource?solution_id=445870')
    soup = bs4.BeautifulSoup(resp.text, 'lxml')
    print(soup.find('code'))
    '''
        <code>#include&lt;stdio.h&gt;
#include&lt;string.h&gt;
using namespace std;
#define max(a,b) a&gt;b?a:b
#define min(a,b) a&lt;b?a:b
int main(){
	int n,a[100],left[100],right[100];
	int cnt[100];
	while(scanf("%d",&amp;n)!=EOF){
		memset(left,0,sizeof(left));
		memset(right,0,sizeof(right));
		for(int i=0;i&lt;n;i++){
			scanf("%d",&amp;a[i]);
		}
		for(int i=0;i&lt;n;i++){ // i left
			int tmp=0;
			for(int j=0;j&lt;i;j++){
				if(a[j]&lt;a[i]){
					tmp=max(tmp,left[j]);
				}
			}
			left[i]=tmp+1;
		}
		for(int i=n-1;i!=-1;i--){
			int tmp=0;
			for(int j=n-1;j&gt;i;j--){
				if(a[j]&lt;a[i]){
					tmp=max(tmp,right[j]);
				}
			}
			right[i]=tmp+1;
		}
		int minn=200;
		for(int i=0;i&lt;n;i++){
			cnt[i]=n-(left[i]+right[i])+1;
			minn=min(minn,cnt[i]);
		}
		printf("%d\n",minn);
	}
	return 0;
}</code>
    '''


def get_JAVAcode_list(session):
    # language=3表示JAVA语言，score=100表示所有回答中100分的题目，即ac的题目
    # 这些可以通过手动操作之后，抓包获得
    url = 'http://acm.zjnu.edu.cn/CLanguage/status?problem_id=&user_id=201539100122&language=3&score=100'
    resp = session.get(url)
    soup = bs4.BeautifulSoup(resp.text, 'lxml')
    questions = []
    problem_set = set()
    for tr in soup.find_all('tr', attrs={"align": "center", "bgcolor": None}):
        # 输出进行测试，如果不加"bgcolor":None,会匹配到另外2个tr
        # print(tr)
        runid = tr.contents[0].text
        # 所谓文本值，就是把标签去掉，因此在只有一个子结点的情况下，不用再获取子结点
        problemid = tr.contents[2].text
        # print(runid, problemid)
        # 去重
        if problemid not in problem_set:
            # 不加列表会把字符串的每个字符当成一个元素
            problem_set = problem_set.union([problemid])
            #print(problem_set)
            questions.append({
                "runid": runid,# 提交的代码
                "problemid": problemid,# 问题
                # 如果想要多语言提交，要把对应的语言种类也爬下来
            })
    return questions


def get_JAVACODE(session, runid):
    resp = session.get('http://acm.zjnu.edu.cn/CLanguage/showsource?solution_id=%s' % runid)
    soup = bs4.BeautifulSoup(resp.text, 'lxml')
    return soup.find('code').text.replace('&amp;', '&') \
        .replace('&lt;', '<') \
        .replace('&gt;', '>')


def submit(session, questionid, code, language=3):
    resp = session.post('http://acm.zjnu.edu.cn/CLanguage/problems/%s/submit' % questionid, data={
        'language': language,  # java
        'submit':'',
        'source':code,# 你的代码
    })
    # 当然可以查看自己是否交对了，这里没有用到新技术，如果感兴趣，可以自己当课后作业做
    return


if __name__ == '__main__':
    # 大号
    session = login('201539100122', '1q2w3e')
    # 小号
    session2 = login('hc2000', '1q2w3e')
    id_list = search_questions(session)
    # print(id_list)
    # get_code_test(session)
    questions = get_JAVAcode_list(session)
    print(questions)
    count=0
    for question in questions:
        count+=1
        runid = question['runid']
        problemid = question['problemid']
        code = get_JAVACODE(session, runid)
        # 小号提交
        submit(session2, problemid, code)
        # 加sleep是因为提交太快它拒绝判断
        time.sleep(10)
        print('submit question',problemid)