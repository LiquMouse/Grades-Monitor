import grade #获取成绩模块
import time
from plyer import notification

url = '	https://byyt.ustb.edu.cn/cjgl/yjsxxjd/cjcx'
def get_cookies():
    cookies = {"INCO": "237edcf75ab0119b5f69e9bd3693b230",
            "SESSION": ""}
    with open('C:\\Users\\Wuhlulu\\Desktop\\资料\\教务系统 - 副本\\cookies.txt', 'r') as f:
        session = f.read().strip()
        cookies['SESSION'] = session
    return cookies


sleeps = 1800 #间隔时间，单位秒
notification.notify(
    title='开始监控成绩',
    message='每{}秒检查一次成绩更新'.format(sleeps),
    app_name='Grade Monitor'
)
cookies = get_cookies()
try:
    grades_old = grade.get_grades(url, cookies)
except Exception as e:
    notification.notify(
        title='初始化失败',
        message=str(e),
        app_name='Grade Monitor'
    )
    grades_old = {}
while True:
    try:
        cookies = get_cookies()
        grades_new = grade.get_grades(url, cookies)
        if grades_new != grades_old:
            for course, grade_value in grades_new.items():
                if course not in grades_old:
                    if grade_value < 60:
                        notification.notify(
                            title='!!!!!!!!!!!!!',
                            message=f'课程: {course}\n成绩: {grade_value}',
                            app_name='Grade Monitor'
                        )
                    notification.notify(
                        title='成绩更新',
                        message=f'课程: {course}\n成绩: {grade_value}',
                        app_name='Grade Monitor'
                    )
            grades_old = grades_new
        formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(formatted_time,grades_new)
    except Exception as e:
        notification.notify(
            title='监控出错',
            message=str(e),
            app_name='Grade Monitor'
        )
    time.sleep(sleeps)