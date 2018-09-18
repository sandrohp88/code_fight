import xml.etree.ElementTree as etree
import xml.dom.minidom as minidom


def xmlTags(xml):
    """You want to create your local database containing information about the things you find the coolest. You used to store this information in xml documents, so now you need to come up with an algorithm that will convert the existing format into the new one. First you decided to choose a structure for your scheme, and to do it you want to represent xml document as a tree, i.e. gather all the tags and print them out as follows:
    tag1()
    --tag1.1(attribute1, attribute2, ...)
    ----tag1.1.1(attribute1, attribute2, ...)
    ----tag1.1.2(attribute1, attribute2, ...)
    --tag1.2(attribute1, attribute2, ...)
    ----tag1.2.1(attribute1, attribute2, ...)
    ...
    where attributes of each tag are sorted lexicographically.
    You are a careful person, so the structure of the xml is neatly organized is such a way that:
    there is a single tag at the root level;
    each tag has a single parent tag (i.e. if there are several occurrences of tag a, and in one occurrence it's a child of tag b and in the other one it's a child of tag c, then b = c);
    each appearance of the same tag belongs to the same level.
    Given an xml file, return its structure as shown above. The tags of the same level should be sorted in the order they appear in xml, and the attributes should be sorted lexicographically.
    Example
    For
    xml =
    "<data>
        <animal name="cat">
            <genus>Felis</genus>
            <family name="Felidae" subfamily="Felinae"/>
            <similar name="tiger" size="bigger"/>
        </animal>
        <animal name="dog">
            <family name="Canidae" member="canid"/>
            <order>Carnivora</order>
            <similar name="fox" size="similar"/>
        </animal>
    </data>"
    the output should be
    xmlTags(xml) =
    ["data()",
    "--animal(name)",
    "----genus()",
    "----family(member, name, subfamily)",
    "----similar(name, size)",
    "----order()"]


    Arguments:
        xml {string} -- [representing a xml]
    """
    tree = etree.fromstring(xml)
    pretty_string = minidom.parseString(xml).toprettyxml(indent='--')
    pretty_string = pretty_string.split('\n')[1:-1]
    level = dict()

    for p_string in pretty_string:
        p_string = p_string.replace('/', '')
        start = p_string.find('<')
        possible_end = p_string.find(' ')
        end = p_string.find('>')
        if possible_end < end and end != -1 and possible_end != -1:
            end = possible_end
        # if end == -1:
        #   end = p_string.find('>')
        # print(end)
        if start != -1:
            indent = p_string[:start]
        else:
            indent = ''
        # print(indent)
        key_s = p_string[start+1:end]
        level[key_s] = indent

    nodes = dict()
    nodes_list = list()
    for node in tree.iter():
        if not node.tag in nodes_list:
            nodes_list.append(node.tag)
        nodes[node.tag] = sorted(
            list(set(nodes.get(node.tag, []) + node.keys())))
    result = list()

    for key in nodes_list:
        parameter_list = '('
        for i, parameter in enumerate(nodes[key]):
            if i == len(nodes[key]) - 1:
                parameter_list += parameter
            else:
                parameter_list += parameter + ', '
        parameter_list += ')'
        formated_node = '{}{}{}'.format(level[key], key, parameter_list)
        result.append(formated_node)

    return result


# While migrating to a new operation system, you faced an unexpected problem: now you need to create a new build command for your favorite text editor plugin. The build command is stored as a JSON file that you should now update. In order to make the transition simpler, you decided to write a program that will create a template of the build command by replacing everything but dictionaries in given jsonFile with their default values: numbers with 0, strings with "" and lists with [].
# It is guaranteed that there are only aforementioned types in the given JSON file.
# Example
# For
# jsonFile =
# """
# {
#     "version": "0.1.0",
#     "command": "c:python",
#     "args": ["app.py"],
#     "problemMatcher": {
#         "fileLocation": ["relative", "${workspaceRoot}"],
#         "pattern": {
#             "regexp": "^(.*)+s$",
#             "message": 1
#         }
#     }
# }
# """
# the output should be
# buildCommand(jsonFile) =
# """
# {
#     "version": "",
#     "command": "",
#     "args": [],
#     "problemMatcher": {
#         "fileLocation": [],
#         "pattern": {
#             "regexp": "",
#             "message": 0
#         }
#     }
# }
# """
import json
from collections import OrderedDict


def buildCommand(jsonFile):
    data = json.loads(jsonFile, object_pairs_hook=OrderedDict)
    for key, value in data.items():
        data[key] = return_default(value)
    return json.dumps(data)


def return_default(value):
    if type(value) is str:
        return ''
    if type(value) is list:
        return []
    if type(value) is int or type(value) is float:
        return 0
    if type(value) is OrderedDict:
        for k, v in value.items():
            value[k] = return_default(v)
        return value


# You're creating your own website for Harry Potter fans. As you all believe in magic, you're waiting for your personal letter from Hogwarts, that will definitely arrive to you some day with a magnificent owl. To be prepared for this exciting moment you decided to embed a calendar to your website on which you will mark the days when Hogwarts owls can bring letters.
# Given a month and a year, return an HTML table representing the desired calendar. Follow the same format as provided in the example but omit all whitespace characters (i.e. tabs, newlines and whitespaces) where it is possible, because you care about space efficiency.
# Example
# For month = 11 and year = 2016, the output should be
# websiteCalendar(month, year) =
# "<table border="0" cellpadding="0" cellspacing="0" class="month">
#   <tr>
#     <th colspan="7" class="month">November 2016</th>
#   </tr>
#   <tr>
#     <th class="mon">Mon</th>
#     <th class="tue">Tue</th>
#     <th class="wed">Wed</th>
#     <th class="thu">Thu</th>
#     <th class="fri">Fri</th>
#     <th class="sat">Sat</th>
#     <th class="sun">Sun</th>
#   </tr>
#   <tr>
#     <td class="noday">&nbsp;</td>
#     <td class="tue">1</td>
#     <td class="wed">2</td>
#     <td class="thu">3</td>
#     <td class="fri">4</td>
#     <td class="sat">5</td>
#     <td class="sun">6</td>
#   </tr>
#   <tr>
#     <td class="mon">7</td>
#     <td class="tue">8</td>
#     <td class="wed">9</td>
#     <td class="thu">10</td>
#     <td class="fri">11</td>
#     <td class="sat">12</td>
#     <td class="sun">13</td>
#   </tr>
#   <tr>
#     <td class="mon">14</td>
#     <td class="tue">15</td>
#     <td class="wed">16</td>
#     <td class="thu">17</td>
#     <td class="fri">18</td>
#     <td class="sat">19</td>
#     <td class="sun">20</td>
#   </tr>
#   <tr>
#     <td class="mon">21</td>
#     <td class="tue">22</td>
#     <td class="wed">23</td>
#     <td class="thu">24</td>
#     <td class="fri">25</td>
#     <td class="sat">26</td>
#     <td class="sun">27</td>
#   </tr>
#   <tr>
#     <td class="mon">28</td>
#     <td class="tue">29</td>
#     <td class="wed">30</td>
#     <td class="noday">&nbsp;</td>
#     <td class="noday">&nbsp;</td>
#     <td class="noday">&nbsp;</td>
#     <td class="noday">&nbsp;</td>
#   </tr>
# </table>"
# Input/Output
# [execution time limit] 4 seconds (py3)
# [input] integer month
# 1-based number of a month (i.e. 1 stands for January, 2 stands for February, and so on).
# Guaranteed constraints:
# 1 ≤ month ≤ 12.
# [input] integer year
# 4-digit number of a year. Please don't forget that in leap years February has 29 days.
# Guaranteed constraints:
# 1900 ≤ year ≤ 2100.
# [output] string
# An HTML table corresponding to the given month and the given year.
import calendar


def websiteCalendar(month, year):
    return calendar.HTMLCalendar(0).formatmonth(year, month).replace('\n', '')


# You decided to create a malicious program to play a joke on your friend. He's now struggling with a report for his work, and you want to scare him by spoiling some dates in it (of course you will change them back after you have your moment of joy). However, you don't want him to discover the errors until he starts double-checking the report, so all spoiled dates should be valid.
# Now your goal is to write a program that modifies the curDate according to the rules that specify the changes that should be made. However, if the changes result in an incorrect date, the program should leave the date as is.
# Given the changes and the curDate, return the spoiled date or don't change it if the result appears to be invalid.
# Example
# For curDate = "01 Jul 2016 16:53:24" and
# changes = [2, 3, -1, 0, 5, 4], the output should be
# maliciousProgram(curDate, changes) = "03 Oct 2015 16:58:28";
# For curDate = "15 Mar 1998 12:09:59" and
# changes = [-2, 0, 9, 1, 3, 1], the output should be
# maliciousProgram(curDate, changes) = "15 Mar 1998 12:09:59".
# After changing the date will look like "13 Mar 2007 13:12:60", which is incorrect, because the number of seconds cannot be equal to 60.
# Input/Output
# [execution time limit] 4 seconds (py3)
# [input] string curDate
# The current date in the format "DD MMM YYYY HH:MM:SS", where DD stands for day of the month (1-based), MMM stands for the name of month cut to 3 letters (i.e. "Jan" for January, "Feb" for February and so on), YYYY - for the year, HH - for hour (your friend uses 24-hour clock), MM - for minutes and SS - for seconds. It's guaranteed that given date is correct.
# Guaranteed constraints:
# 01 ≤ DD ≤ 31,
# MMM ∈ ["Jan", "Feb", ..., "Dec"],
# 1900 ≤ YYYY ≤ 2100,
# 00 ≤ HH ≤ 23,
# 00 ≤ MM ≤ 59,
# 00 ≤ SS ≤ 59.
# [input] array.integer changes
# An array that describes how each component of curDate should be updated. changes[i] is equal to the value that should be added to the ith component, where i stands for:
# 0: for the day;
# 1: for the month;
# 2: for the year;
# 3: for the hour;
# 4: for the minute;
# 5: for the second.
# Guaranteed constraints:
# -30 ≤ changes[0] ≤ 30,
# -11 ≤ changes[1] ≤ 12,
# -100 ≤ changes[2] ≤ 100,
# -23 ≤ changes[3] ≤ 23,
# -59 ≤ changes[4] ≤ 59,
# -59 ≤ changes[5] ≤ 59.
# [output] string
# The modified date if it's correct and the given date otherwise (the output should follow the same format as the input). The date is considered to be incorrect if at least one of its components is invalid.
from datetime import datetime


def maliciousProgram(curDate, changes):

    # 1- Convert changes month to num representantion from curDate
    # 2- Create varibles for curDate and changes
    # 3- Sum the corresponding variables if possible, if not, return curDate

    curDateToList = curDate.split(' ')
    curDay = int(curDateToList[0])
    curMonth = datetime.strptime(curDateToList[1], '%b').month
    curYear = int(curDateToList[2])
    curHours, curMinutes, curSeconds = [
        int(number) for number in curDateToList[-1].split(':')]

    chanDay, chanMonth, chanYear, chanHours, chanMinutes, chanSeconds = changes

    curYear = sum_year(curYear, chanYear)
    curMonth = sum_months(curMonth, chanMonth)
    curDay = sum_days(curDay, chanDay, curMonth, curYear)
    curHours = sum_hours(curHours, chanHours)
    curMinutes = sum_minutes(curMinutes, chanMinutes)
    curSeconds = sum_seconds(curSeconds, chanSeconds)
    try:
        date = datetime(curYear, curMonth, curDay,
                        curHours, curMinutes, curSeconds)
        return date
    except:
        return curDate

    # print(curHours, curMinutes, curSeconds)
    # if all([curDay, curMonth, curYear, curHours, curMinutes, curSeconds]):
    #     date = datetime(curYear, curMonth, curDay,
    #                     curHours, curMinutes, curSeconds)
    #     return date.strftime('%d %b %Y %H:%M:%S')
    # else:
    #     return curDate


def sum_days(curDay, chanDay, month, year):
    # if month and year:
    #     number_of_days = monthrange(year, month)[1]
    # else:
    #     return False
    day = curDay + chanDay
    return day


def sum_months(curMonth, chanMonth):
    month = curMonth + chanMonth
    return month  # if month in range(1, 13) else False


def sum_year(curYear, chanYear):
    return curYear + chanYear


def sum_hours(curHours, chanHours):
    hour = curHours + chanHours
    # if hour == 24:
    #     hour = '00'
    # if hour > 24:
    #     hour = False
    return hour


def sum_minutes(curMinutes, chanMinute):
    minute = curMinutes + chanMinute
    return minute  # if minute < 60 else False


def sum_seconds(curSeconds, chanSecond):
    second = curSeconds + chanSecond
    return second  # if second < 60 else False

# You've got tired of fixing your relatives' PCs after they visited some phishing website so you decided to implement a special plug-in for their browsers which will check if the page they are trying to visit is similar to the one in the blacklist.
# For that, you've thought of the special algorithm that for two URLs url1 and url2 computes their similarity as following:
# Initially their similarity is 0
# Then, it is increased by the following rules:
# +5, if the same protocol is used in both URLs.
# +10, if url1 and url2 have the same address.
# +k, if the first k components of path (delimited by /) are exactly the same (and in the same order) between the two URLs.
# +1 if for each varNames common between them. Additional +1 if the respective values are equal too.
# URLs are given in the following format: protocol://address[(/path)*][?query] (where query = varName=value(&varName=value)*, parts given in [] are optional, and parts in ()* may be repeated several times). Each of the named elements (i.e. protocol, address, path, varName and value) are guaranteed to contain only alphanumeric characters and periods.
# Given the two URLs url1 and url2, compute their similarity using the algorithm described above.
# Example
# For
# url1 = "https://codesignal.com/home/test?param1=42&param3=testing&login=admin"
# and
# url2 = "https://codesignal.com/home/secret/test?param3=fish&param1=42&password=admin"
# the output should be
# urlSimilarity(url1, url2) = 19.
# Because these URLs have the same protocols, addresses, first path component (home) and two varNames, with one also having the same value in both of them.
# So the resulting similarity is thus 5 + 10 + 1 + 1 + 1 + 1 = 19.


from urllib.parse import urlparse


def urlSimilarity(url1, url2):
    url1 = urlparse(url1)
    url2 = urlparse(url2)
    similarity = 0

    similarity += 5 if url1.scheme == url2.scheme else 0
    similarity += 10 if url1.netloc == url2.netloc else 0

    url1_path = url1.path.split('/')[1:]
    url2_path = url2.path.split('/')[1:]

    k = 0
    if len(url1_path) > len(url2_path):
        for i, item in enumerate(url2_path):
            if item == url1_path[i]:
                k += 1
    else:
        for i, item in enumerate(url1_path):
            if item == url2_path[i]:
                k += 1
    similarity += k
    if url1.query:
        url1_query = [tuple(element.split('='))
                      for element in url1.query.split('&')]
    else:
        url1_query = []
    if url2.query:
        url2_query = [tuple(element.split('='))
                      for element in url2.query.split('&')]
    else:
        url2_query = []
    print(url1.query, url2.query)
    if url1_query and url2_query:
        for var_name, value in url1_query:
            for var_name2, value2 in url2_query:
                if var_name == var_name2:
                    similarity += 1
                    if value == value2:
                        similarity += 1

    return similarity


# You are creating a new website about HTML parsing. You don't want your page to be too simple, so you would like to estimate the complexity of the main page of your site. In order to measure the complexity of the page, you need to find a set of all tags located on the deepest level of a tree correponsing to HTML document. Given a valid HTML document, find all distinct tags located on the deepest level.
# Example
# For
# document = "<!DOCTYPE html><html> <body> <h1>The best heading ever</h1> <p>The worst paragraph ever.</p> </body></html>"
# the output should be
# pageComplexity(document) = ["h1", "p"].


from bs4 import BeautifulSoup


def pageComplexity(document):
    parsed_html = BeautifulSoup(document, 'html.parser')
    head_tag = parsed_html.find().name
    head_tag = parsed_html.find(head_tag)
    if len(list(head_tag.descendants)) == 1:
        return [head_tag.name]
    level = 0
    for child in head_tag.descendants:
        # print(child)
        if child.name != None:
            tmp_level = len(list(child.parents))
            level = tmp_level if tmp_level > level else level
    tag_dict = dict()
    for child in head_tag.descendants:
        if child.name != None:
            tmp_level = len(list(child.parents))
            if tmp_level == level:
                tag_dict[child.name] = '_'

    return list(tag_dict.keys())


# You've been actively exchanging email with one of your colleagues and noticed that you can't open his attachments. Unfortunately, he's just went on a vacation and you need these attached files right now.
# You've spent some time studying his emails and discovered that your colleague used the buggy email client which instead of using proper MIME Base64 encoding for the attachments used other variants differing in characters that represent values 62 and 63.
# Furthermore, different versions of this email client used different variations of the encoding!
# Given the encoding of the email client which was used to send attachment,
# decode it.
# Here is the default Base64 encoding table:
import base64


def weirdEncoding(encoding, message):
    return str(base64.b64decode(message, altchars=encoding))


def main():
    encoding = "-_"
    message = "U29tZSB2ZXJ5IHN0cmFuZ2UgYW5kIGxvbmcgYXR0YWNobWVudD8+Pw=="  # = 'CodeSignal'
    print(weirdEncoding(encoding, message))
    # document = "<!DOCTYPE html><html><body><h1>The best heading ever</h1> <p>The worst paragraph ever.</p></body></html>"
    # document = '<i>tag</i>'
    # document = '''<body><center><i><h3>This text will be a centered, italicized heading (size 3)</h3><h4>This text will be a centered, italicized heading (size 4)</h4><h5>This text will be a centered, italicized heading (size 5)</h5></i><b>  <!--comment with a lot of <<<<<<<< <tag1> <tag2> <tag3> <OopsYouVeGotWA> >>>>>>>> -->  This text will be centered and boldfaced</b></center></body>'''
    # print(pageComplexity(document))  # = ["h1", "p"]

    # url1 = "https://codesignal.com/home/test?param1=42&param3=testing&login=admin"
    # url2 = "https://codesignal.com/home/secret/test?param3=fish&param1=42&password=admin"
    # url1 = "ftp://www"
    # url2 = "http://anotherexample.com/www?ftp=http"
    # print(urlSimilarity(url1, url2))  # = 19
    # curDate = "01 Jul 2016 16:53:24"
    # changes = [2, 3, -1, 0, 5, 4]
    # curDate = "28 Jan 1900 16:09:10"
    # changes = [1, 1, 0, 5, 10, 15]
    # curDate = "07 Mar 1956 15:38:35"
    # changes = [22, -3, 1, -10, -12, -35]
    # curDate = "31 Dec 2100 23:59:59"
    # changes = [-30, -11, -100, -23, -59, -59]
    # print(maliciousProgram(curDate, changes))  # = "03 Oct 2015 16:58:28";
    # month, year = 11, 2016
    # print(websiteCalendar(month, year))
    # json_file = '{\"version\": 1.0,\"command\": \"c:python\",\"args\": [\"app.py\"],\"problemMatcher\": {\"fileLocation\": [\"relative\", \"${workspaceRoot}\"],\"pattern\": {\"regexp\": \"^(.*)+s$\", \"message\": 1}}}'

    # print(buildCommand(json_file))
    # xml = '''<data>
    #             <animal name="cat">
    #                 <genus>Felis</genus>
    #                 <family name="Felidae" subfamily="Felinae"/>
    #                 <similar name="tiger" size="bigger"/>
    #             </animal>
    #             <animal name="dog">
    #                 <family name="Canidae" member="canid"/>
    #                 <order>Carnivora</order>
    #                 <similar name="fox" size="similar"/>
    #             </animal>
    #         </data>'''
    # xml1 = "<products><product><TITLE> product #1 </TITLE><PRICE> 10.00 </PRICE></product><product><TITLE> product #2 </TITLE><PRICE> 20.00 </PRICE></product></products>"
    # print(xmlTags(xml1))


if __name__ == '__main__':
    main()
