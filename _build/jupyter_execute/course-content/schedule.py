#!/usr/bin/env python
# coding: utf-8

# # Schedule
# 
# This is the schedule for the semester.  This page will be frequently updated based on how we progress. Homeworks and links to the lecture will be provided here for easy reference to the calendar.  The assignments refer to the homework **following** a class meeting.  So if on a particular date it says watch a video, that is for next time!

# In[1]:


from IPython.core.display import HTML, Markdown
import itertools
import re

from datetime import datetime, date, timedelta

format = '%A, %B %d, %Y'
short_format = '%a %b %d'
# 1. set the first day of classes
first_day = 'Thursday, September 02, 2021'

# 2. set the last day of class_variables
last_day = 'Tuesday, December 14, 2021'

# 3. set the recurring days of the weeks
days_of_week = ['Monday','Wednesday']

# 4. add in the date of the final exam
final_exam_day = None

# 4. list any exceptions for like holidays and the like
holidays = {'Monday, September 06, 2021': 'Labor Day', 'Monday, October 11, 2021': 'Fall break'}

# 5. add in any additional dates (most commonly legislative day where off cycle class meeting might happen)
extra_days = {'Tuesday, October 12, 2021': 'Legislative Day (classes meet on Monday schedule)'}


# this part runs the script and prints to the terminal the dates
first_day_f=datetime.strptime(first_day, format)
last_day_f=datetime.strptime(last_day, format)

# generator for all the days between two dates
def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days+1)):
        yield start_date + timedelta(n)

holidays_f = [datetime.strptime(x, format) for x in holidays.keys()]
extra_days_f = [datetime.strptime(x, format) for x in extra_days.keys()]

classes_list = []
class_num = 0
for single_date in daterange(first_day_f, last_day_f):
    # limit to either the correct day of week
    # or any additional days
    # (single_date in extra_days_f): #
    date_record = {}
    if (single_date.strftime('%A') in days_of_week) or (single_date in extra_days_f):
        date_string = single_date.strftime(short_format)
        reason = ''
        if single_date in holidays_f:
            reason = 'No class, ' + holidays[single_date.strftime(format)]
            #print(date_string + f' {reason}')
        elif single_date in extra_days_f:
            reason = 'Special date, ' + extra_days[single_date.strftime(format)]
            #print(date_string + f', class {class_num}', f' {reason}')
            class_num += 1
        else:
            #print(date_string + f', class {class_num}')
            class_num += 1
        date_record['date'] = date_string
        date_record['class_num'] = class_num
        date_record['reason'] = reason
        classes_list.append(date_record)

def add_html_row(index, date, reason, agenda, assignment):
    if assignment==None:
        assignment = ''
    if agenda == None:
        agenda = ''
    if reason != '':
        html_str = f'''<tr class="align-top">
                  <th scope="row" class="text-left align-top">{date}<br><span class="badge rounded-pill bg-warning text-dark">Warning</span></th>
                  <td class="text-left align-top"><b>{reason}</b> - {agenda}</td>
                  <td class="text-left align-top">{assignment}</td>
                </tr>'''
    else:
        html_str = f'''<tr class="align-top">
                  <th scope="row" class="text-left align-top">{date}</th>
                  <td class="text-left align-top">{agenda}</td>
                  <td class="text-left align-top">{assignment}</td>
                </tr>'''
    return html_str

def clear_a_tags(raw_html):
    cleanr = re.compile('<a href=.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    cleantext = cleantext.replace('</a>','')
    return cleantext

agendas = []
assignments = []

## Placeholder code for skipped clsas
# agendas.append('<span class="badge rounded-pill bg-danger text-dark">No class</span>')
# assignments.append(None)

# skip class
agendas.append('<span class="badge rounded-pill bg-danger text-dark">No class</span>')
assignments.append(None)

# Class 1
# 1) Brenden lecture: Class logistics (go over syllaubs)
# 2) Student introductions
agendas.append("Organizational meeting, meet and greet fellow classmates<br>")
assignments.append("Read <a href='../chapters/00/00-cogsci.html'>Chapter 1: What is Cognitive Science and how do we study it?</a> before next class.")

# Class 2
# 1) Brenden lecture: What is cognitive science? (lecture1.html)
##   Replacement for Todd's video, see slides
# 2) In class activity ("are they meat?"")
agendas.append("Lecture on 'What is cognitive science?'<br>                 In class activity: <a href='../chapters/00/cogsci-ica.html'>here</a>.<br>")
assignments.append("Read <a href='../chapters/01/00-whystats.html'>Chapter 2: Why do we have to learn statistics?</a> before next class.")

# Class 3
# 1) Brenden lecture: basic research design (part 1) (lecture2.html)
## Examples of good/bad experiments, correlation is not causation, etc.
##  Replacement for Todd's video, see slides
# 2) In class activity (TODO: Not sure what to do for this one?)
agendas.append("Lecture on basic research design (part 1)<br>                 In class activity: <a href='../chapters/01/stats-ica.html'>here</a>.<br>")
assignments.append("Read <a href='../chapters/02/00-jupyter.html'>Chapter 3: Introduction to Jupyter</a> before next class,                    and <i>watch accompanying video.</i>")
agendas[-1] = clear_a_tags(agendas[-1])

# Class 4
# Brenden flipped class: Discussion of jupyter, and walking through...
agendas.append("Review/discussion of JupyterHub.  Walk through of interface.  Begin working on <a href='../homeworks/Homework1.html'>homework 1</a>.")
assignments.append("Read <a href='../chapters/03/00-python.html'>Chapter 4: Introduction to Python for Psychology Undergraduates</a> before next class,                and <i>watch accompanying video.</i><br>                <b><a href='../homeworks/Homework1.html'>Homework 1</a>, due Mon Sep 27.</b>")

# Class 5
# Brenden flipped class: Discussion of Python programming
agendas.append("Review/discussion of basic Python programming. <br>                 In class activity: <a href='../chapters/03/python-ica.html'>here</a>.")
assignments.append("Read <a href='../chapters/04/00-researchdesign.html'>Chapter 5: A brief introduction to research design</a> before next class.<br>                   <b><a href='../homeworks/Homework1.html'>Homework 1</a>, due Mon Sep 27.</b>")

# Class 6
# Brenden Lecture: basic research design (part 2) (lecture3.html)
# Discussion of DV/IV variables, main effet, interaction effect
## Replacement for Todd's video, see slides
agendas.append("Lecture on basic research design (part 2) <br>                 In class activity: <a href='../chapters/04/design-ica.html'>here</a>.")
assignments.append("")
agendas[-1] = clear_a_tags(agendas[-1])

agendas.append("Python practice, begin <a href='../homeworks/hw2/Homework2.html'>Homework 2</a> in class.")
assignments.append("<b>Homework 2, due Tue Oct 12.</b> If you need additional FOR-LOOP help please read through <a href='../tips/fortyforloops.html'>this notebook</a>.")
agendas[-1] = clear_a_tags(agendas[-1])

agendas.append("Continue <a href='../homeworks/hw2/Homework2.html'>Homework 2</a> in class.")
assignments.append("<b>Homework 2, due Tue Oct 12.</b><br>                    Begin reading <a href='../chapters/05/00-data.html'>Chapter 6: Format and structure of digital data</a> up to section 6.10 before next class.")
agendas[-1] = clear_a_tags(agendas[-1])

agendas.append("Review/discussion of data organization and pandas")
assignments.append("<b>Homework 2 due Tue Oct 12.</b><br>                    Read rest of <a href='../chapters/05/00-data.html'>Chapter 6: Format and structure of digital data</a> before next class,                     and <i>watch the video lecture.</i>")

# skip class
agendas.append('<span class="badge rounded-pill bg-danger text-dark">No class</span>')
assignments.append(None)

agendas.append("Work on <a href='../homeworks/hw3.html'>Exploring Data (HW3) notebook</a>.")
assignments.append("Read <a href='../chapters/06/00-plots.html'>Chapter 7: Visualizing data</a> before next class.")
agendas[-1] = clear_a_tags(agendas[-1])

agendas.append("Lecture covering data visualization, matplotlib, and seaborn.")
assignments.append("<b><a href='../homeworks/hw3.html'>Exploring Data (HW3) notebook</a> due Wed Oct 20.</b><br>                    If you didn't read chapter 7, please do.")
assignments[-1] = clear_a_tags(assignments[-1])

agendas.append("Lecture covering descriptive statistics and how to compute with pandas.  Work on <a href='../homeworks/hw3.html'>Exploring Data (HW3) notebook</a> in class in groups.")
assignments.append("<b>Homework 3, due Wed Oct 20.</b><br>                    Read <a href='../chapters/07/00-describingdata.html'>Chapter 8: Describing data</a> before next class.")
agendas[-1] = clear_a_tags(agendas[-1])

agendas.append("Finish <a href='../homeworks/hw3.html'>Exploring Data (HW3) notebook</a> in class and discussion of what people explored.")
assignments.append("Turn in Exploring Data (HW3) notebook tonight (Wed Oct 20).<br>                    Read <a href='../chapters/08/01-sampling.html'>Chapter 9: Samples, populations, and sampling</a> before next class.")
agendas[-1] = clear_a_tags(agendas[-1])

agendas.append("Work on <a href='../chapters/08/sampling-ica.html'>Sampling In-class Activity (Ch8) notebook</a>.")
assignments.append("Complete in class activity if your group was unable to finish.<br>                    Read <a href='../chapters/09/00-hypothesistesting.html'>Chapter 10: Hypothesis testing</a> before next class.")
agendas[-1] = clear_a_tags(agendas[-1])

agendas.append("Work on <a href='../chapters/09/hypothesistesting-ica.html'>Hypothesis testing In-class Activity (Ch10) notebook</a>.")
assignments.append("Complete in class activity if your group was unable to finish.<br>                    Read <a href='../chapters/10/00-ttest.html'>Chapter 11: Comparing one or two means</a> before next class.")
agendas[-1] = clear_a_tags(agendas[-1])

agendas.append("Lecture on <a href='../lectures/lecture11.html'>t-test</a>, Work on <a href='../chapters/10/ttest-ica'>t-test In-class Activity (Ch12) notebook</a>.")
assignments.append("Read <a href='../chapters/11/00-inferences-from-behavior.html'>Chapter 12: Measuring behavior</a> before next class.")
agendas[-1] = clear_a_tags(agendas[-1])

agendas.append("<span class=\"badge rounded-pill bg-info text-dark\">Lab 1</span>Work on <a href='../labs/LabSDT-Pt1.html'>Signal Detection Theory lab</a> ")
assignments.append("Read <a href='../chapters/21/00-ethics-irb.html'>Chapter 13: Research Ethics</a> before next class.")
agendas[-1] = clear_a_tags(agendas[-1])

agendas.append("<span class=\"badge rounded-pill bg-info text-dark\">Lab 1</span>Work on <a href='../labs/LabSDT-Pt2.html'>Signal Detection Theory lab</a>")
assignments.append("Read <a href='../chapters/13/00-linearregression.html'>Chapter 14: Linear Regression</a> before next class.")
agendas[-1] = clear_a_tags(agendas[-1])               
    
agendas.append("<span class=\"badge rounded-pill bg-info text-dark\">Lab 1</span>Work on <a href='../labs/LabSDT-Pt2.html'>Signal Detection Theory lab</a>")
assignments.append("Read <a href='../chapters/14/00-logisticregression.html'>Chapter 15: Logistic Regression</a> before next class.")
agendas[-1] = clear_a_tags(agendas[-1])

agendas.append("<span class=\"badge rounded-pill bg-success\">Lab 2</span>Work on Linear Regression lab")
assignments.append("Read <a href='../chapters/15/00-mixed-effect.html'>Chapter 16: Linear Mixed Effect Models</a>  before next class.")

agendas.append("<span class=\"badge rounded-pill bg-success\">Lab 2</span>Work on Linear Regression lab")
assignments.append("Read <a href='../chapters/17/00-mri.html'>Chapter 18: Functional Magnetic Resonance Imaging</a> before next class.")

# agendas.append('<span class="badge rounded-pill bg-danger text-dark">Class Canceled</span>')
# assignments.append(None)

agendas.append("<span class=\"badge rounded-pill bg-success\">Lab 2</span>Work on Linear Regression lab")
assignments.append("TBD")

agendas.append("<span class=\"badge rounded-pill bg-secondary\">Lab 3</span>Work on Reinforcement Learning lab")
assignments.append("TBD")

agendas.append("<span class=\"badge rounded-pill bg-secondary\">Lab 3</span>Work on Reinforcement Learning lab")
assignments.append("TBD")

agendas.append("<span class=\"badge rounded-pill bg-secondary\">Lab 3</span>Work on Reinforcement Learning lab")
assignments.append("TBD")

agendas.append("Work on final projects")
assignments.append(None)

agendas.append("Work on final projects")
assignments.append(None)

agendas.append("TBD")
assignments.append(None)

rows = ''
for item,agen,assign in itertools.zip_longest(classes_list,agendas,assignments):
    rows+=add_html_row(item['class_num'], item['date'], item['reason'], agenda=agen, assignment=assign)
    
table_html=f'''
    <table class="table table-striped text-left">
  <thead class="thead-dark">
    <tr>
      <th scope="col" class="text-left">Date</th>
      <th scope="col" class="text-left" width="50%">Agenda</th>
      <th scope="col" class="text-left" width="35%">Assignments</th>
    </tr>
  </thead>
  <tbody>
  {rows}
  </tbody>
</table>
'''


# In[2]:


HTML(table_html)


# In[ ]:




