# -----------------------------------------------------------------------------
#       file:   plot_temps.py
#     author:   dpomondo
#
#      class:   MITx 6.200x edx.org
#               week 1 Lecture 1
#
# -----------------------------------------------------------------------------
import pylab


def open_file():
    fil = open('julyTemps.txt', 'r')
    high = list()
    low = list()
    for line in fil:
        fields = line.split()
        if len(fields) != 3 or not fields[0].isdigit():
            continue
        else:
            high.append(int(fields[1]))
            low.append(int(fields[2]))
    return low, high


def make_plot(low_temps, high_temps):
    diff_temps = []
    length = min(len(low_temps), len(high_temps))
    for t in range(length):
        diff_temps.append(high_temps[t] - low_temps[t])
    pylab.plot(range(1, length + 1), diff_temps)
    pylab.plot(range(1, length + 1), low_temps, 'r')
    pylab.plot(range(1, length + 1), high_temps, 'ro')
    pylab.title('Temperature differences in July in Boston')
    pylab.xlabel('Date')
    pylab.ylabel('Temp Difference')
    pylab.show()

if __name__ == '__main__':
    low, high = open_file()
    make_plot(low, high)
