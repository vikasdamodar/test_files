from email.mime.multipart import MIMEMultipart
import smtplib
from email.mime.text import MIMEText
from jira import JIRA

options = {'server': 'https://tarams.atlassian.net'}
jira = JIRA(options, basic_auth=('athira.komath@tarams.com', 'Athira@123'))

issues_in_proj = jira.search_issues(
    'project=MBIMA and '
    'resolution = Unresolved and '
    '(labels is null and fixVersion is null) and '
    # 'assignee in (vamsy.krishna, srinidhi.chatrapathi) and '
    # 'status not in (Resolved, Closed) and '
    # 'status=backlog and '
    # 'labels is EMPTY and '
    # 'fixVersion is EMPTY and '
    '(status != Closed and status != Done) and '
    # 'createdDate < "2018-12-31" and '
    'description~"gmms.mathrubhumi.basic" and '
    'summary~"Crashlytics" and '
    'summary!~".java"',
    # 'summary~"ActivityThread.java"',
    maxResults=150
)
print(issues_in_proj, "\n", len(issues_in_proj))

message = "<b>Issues</b> : <br><br>"

for i in issues_in_proj:
    # if i.key in ['MBIMA-1068', 'MBIMA-948']:
    #     continue
    issue = jira.issue(i.key)
    message += "&nbsp;&nbsp;&nbsp;&nbsp; {0}  &nbsp;&nbsp;-&nbsp;&nbsp;  " \
               "{1} <br>".format(
        i.key, i.raw['fields']['summary']
    )
    print(i.key, i.raw['fields']['summary'], i.raw['fields']['status']['name'])
    jira.transition_issue(issue, '41')
    # issue.update(assignee={'name': 'girish.yadawad'})
    jira.add_comment(issue,
                     "Library Issue.\nOut of scope as per our initial analysis.\n Non-reproducible")
    jira.transition_issue(issue, '51')
    # issue.update(assignee={'name': 'girish.yadawad'})
    issue.update(fields={"labels": ['Automated']})
    print("done")
    # issue.update(fields={"fixVersions": [{"name": "IMA_Phone_HotFix_3.14"}]})

from_addr = 'mbsupport@tarams.com'
to_addr = ['vikas.periyadath@tarams.com',
           # 'rajasekhar.pattem@tarams.com',
           'girish.yadawad@tarams.com',
           # 'swadesh.dhal@tarams.com'
           ]
msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = ', '.join(to_addr)
msg.attach(MIMEText(message, 'html'))
msg['Subject'] = 'Issues android '

s = smtplib.SMTP_SSL('smtp.googlemail.com', 465)
s.login("mbsupport@tarams.com", "mbsupport@123")
s.sendmail(from_addr, to_addr, msg.as_string())
s.quit()
