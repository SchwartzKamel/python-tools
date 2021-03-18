import re

phoneRegex = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
resume = '''
Ebony Moore
Akron, OH home: 555-555-5555 cell: 123-456-7891 emoore@email.com
SUMMARY
Strategic Senior Enterprise Account Executive with 15+ years of experience attracting and retaining top accounts, driving revenue growth, closing high-value deals, and building powerhouse sales teams.

EDUCATION
CORAL SPRINGS UNIVERSITY
Aug '01
May '03
Master of Science in Business Administration
EXPERIENCE
CLOUD CLEARWATER
Senior Account Executive
Nov '14
Current
Ranked #1 in new client acquisition and revenue attainment within Ohio office
Open new accounts and expand existing book of business with $3M annual sales goal
Played key role in closing first international deals in the UK, Australia, and Canada
Set and track KPIs to improve sales team productivity and increase sales velocity
Built 10-person demand generation team from the ground up, providing ongoing mentorship and training
CRANE & JENKINS
Account Executive
Aug '05
Oct '07
Managed a 200-account territory with special focus on 15 high-value enterprise accounts
Drove net new revenue for cybersecurity software suite, leveraging deep product knowledge to execute effective demos to senior managers and C-level executives
Maintained average quota attainment of over 115% (achieved 138% of quota in first full quarter)
RIVER TECH
Account Executive
Jun '03
Jul '05
Managed a strategic portfolio of national clients, driving $1.5M over two years across 15 states
Completed 5 consecutive quarters as the top account executive (out of 50+ salespeople)
Oversaw sales pipeline using Salesforce, tracking sales opportunities and closing more deals
SKILLS
Pipeline management
Client relationship management
Closing
Salesforce CRM
AWARDS
President’s Club Winner, 2011
'''
mo = phoneRegex.findall(resume)
print(mo)
