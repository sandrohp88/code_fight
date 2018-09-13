class Counter(object):
    '''
    You've launched your brand new web application not long ago, and while in beta it got beta satisfied visitors. Encouraged by such success, you decided to go ahead and push the very first stable version live.
    You know that each beta visitor spent at least k minutes on your app, so now you'd like to keep track of new visitors of your web application that spent at least k minutes on it. Given the amount of time the visitors used your application and the value of k, return the total number of users that used your app for at least k minutes including those from beta.
    Example
    For beta = 22, k = 5, and visitors = [4, 6, 6, 5, 2, 2, 5],
    the output should be
    countVisitors(beta, k, visitors) = 26.
    4 new visitors spent at least 5 minutes on your application, which summed up with 22 satisfied beta users gives 26.
    '''
    value = 0

    def __init__(self, beta):
        self.value = beta

    def inc(self):
        self.value += 1

    def get(self):
        return self.value


def countVisitors(beta, k, visitors):
    counter = Counter(beta)
    for visitor in visitors:
        if visitor >= k:
            counter.inc()
    return counter.get()


class Functions(object):
    '''
    Although Python does provide a bunch of useful built-in functions, some of them are simply missing for no apparent reason. One example of such function is a sign function implemented in many other languages. sign(x) returns 1 if x is positive, -1 if x is negative, and 0 if x is equal to zero.
    You decided to build your own package of useful functions, and would like to start with the sign function. Given the value of x, return the result of applying the sign function to it.
    Example
    For x = -34, the output should be
    sign(x) = -1.
    -34 is a negative number, thus the output should be -1.
    '''
    @staticmethod
    def sign(x): return -1 if x < 0 else 1 if x > 0 else 0


def sign(x):
    return Functions.sign(x)


class Rectangle(object):
    '''
    Tomorrow is Jim's first day as a teacher in a primary school. He's quite nervous about his new job, and in order to relax he decides to write a simple program, because nothing calms as much as coding.
    Since Jim is going to tell the kids about rectangles, he wants to implement a function that will calculate the area of rectangle of the given height and width and show how the result is obtained. Help Jim to gain his confidence and implement the function he needs.
    Example
    For height = 7 and width = 4, the output should be
    primarySchool(height, width) = "7 x 4 = 28".
    The area of the rectangle of size 7 × 4 is calculated as 7 * 4 and is equal to 28.
    '''

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def __str__(self):
        return '{} x {} = {}'.format(self.height, self.width, self.area)

    @property
    def area(self):
        return self.width * self.height


def primarySchool(height, width):
    return str(Rectangle(height, width))


class CodeFighter(object):
    '''
    At CodeSignal information about the users is stored in the database. Anny is working on the class representation of this information, and needs to come up with a class that creates objects with the following attributes: username, _id, xp and name. She has already come up with a test object:
    username: "annymaster"
    _id: "1234567"
    xp: "1500"
    name: "anny"
    The problem is, she doesn't know if this will be enough. It is possible that the server will require information about additional attributes that are not yet present in Anny's representation.
    Given the attribute the server requested, return its value if it is defined, and the <attribute> attribute is not defined string otherwise.
    Example
    For attribute = "_id", the output should be
    userAttribute(attribute) = "1234567";
    For attribute = "age", the output should be
    userAttribute(attribute) = "age attribute is not defined".
    '''

    def __init__(self, username, _id, xp, name):
        self.username = username
        self._id = _id
        self.xp = xp
        self.name = name

    def __getattr__(self, name):
        return "{} attribute is not defined".format(name)


def userAttribute(attribute):
    codefighter = CodeFighter("annymaster", "1234567", "1500", "anny")
    return getattr(codefighter, attribute)


def sortCodesignalUsers(users):
    res = [CodeSignalUser(*user) for user in users]
    res.sort(reverse=True)
    return list(map(str, res))


class CodeSignalUser:
    '''
    At CodeSignal the users can get to the top of the leaderboard by earning XP (experience points) in different modes. The leaderboard is sorted by players XP in descending order, and in case of a tie - by their ids in ascending order.
    Your task is to implement an algorithm that will return the state of the weekly leaderboard given a list of users.
    Example
    For
    users = [["warrior", "1", "1050"],
            ["Ninja!",  "21", "995"],
            ["recruit", "3", "995"]]
    the output should be
    sortCodesignalUsers(users) = ["warrior", "recruit", "Ninja!"].
    '''

    def __init__(self, username, _id, xp):
        self.username = username
        self._id = _id
        self.xp = xp

    def __lt__(self, other):
        if self.xp == other.xp:
            return int(self._id) > int(other._id)
        return int(self.xp) < int(other.xp)

    def __str__(self):
        return self.username


import itertools


class Team(object):
    '''
    You are organizing a team of eSportsmen, and you are determined to make it cool. You are already thinking about winning the world championship: when it happens, the names of your teammates will be chanted one after another by a large audience. You believe that it will sound cool if and only if the first letter of one player's name will be the same as the last letter in the name of the player before them.
    Now you are considering one particular team. Its members are definitely professional gamers, but you're not sure if all together they form a cool team. Implement a function that will check if the team is cool.
    Example
    For team = ["Mark", "Kelly", "Kurt", "Terk"], the output should be
    isCoolTeam(team) = true.
    The following team announcement will sound cool: "Mark", "Kurt", "Terk", "Kelly".
    '''

    def __init__(self, names):
        self.names = names

    def isCool(self):
        first = [name[0].lower() for name in self.names]
        last = [name[-1].lower() for name in self.names]
        for element in first:
            try:
                last.remove(element)
            except:
                pass
        return len(last) < 2

    def __bool__(self):
        return self.isCool()


def isCoolTeam(team):
    return bool(Team(team))


def main():
    team = ["Mark", "Kelly", "Kurt", "Terk"]
    isCoolTeam(team)


if __name__ == '__main__':
    main()
