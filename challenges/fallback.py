from datetime import datetime
from datetime import timedelta


def fallback(time):
    time = time.split(':')
    hour, minute, am_pm = time[0], time[1][:2], time[1][2:]
    time = f'2018-11-2 {hour}:{minute} {am_pm}'.format(
        hour=hour, minute=minute, am_pm=am_pm)
    time = datetime.strptime(time, '%Y-%m-%d %I:%M %p') - timedelta(hours=1)
    hour, minute = str(int(time.strftime('%I'))), time.strftime(':%M%p')
    return hour+minute


def main():
    print(fallback('4:57AM'))


if __name__ == '__main__':
    main()
