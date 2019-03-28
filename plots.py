import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator
import datetime
from matplotlib.dates import DateFormatter
import pandas as pd

def PltTime(time, data, legend, xlabel, ylabel, ylim1=1, ylim2=1, yticks=0):
    fig = plt.figure(figsize=(12,9))
    ax = fig.gca()
    # ax.minorticks_on()
    # ax.xaxis.set_major_locator(matplotlib.dates.HourLocator(interval=2))
    # ax.xaxis.set_minor_locator(matplotlib.dates.MinuteLocator(interval=60))
    # ax.yaxis.set_major_locator(MultipleLocator(yticks))
    # ax.yaxis.set_minor_locator(MultipleLocator(yticks/2))
    ax.grid(b=True, which='major', color='k', linestyle='-')
    ax.grid(b=True, which='minor', color='k', linestyle=':')
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    plt.gcf().autofmt_xdate()
    formatter = DateFormatter('%H:%M:%S')
    plt.gcf().axes[0].xaxis.set_major_formatter(formatter)
    data = [x for _,x in sorted(zip(time,data))]
    time = sorted(time)
    timet = [datetime.datetime.strptime(x, '%H%M%S') for x in time]
    plt.xlim(timet[0], timet[-1])
    for yy in data:
        plt.scatter(timet, yy, label='')
    plt.legend(legend, loc='upper left')

def PltScatter(xvalue, yvalue, legend, xlabel, ylabel, scale=1.2, xlim=1, xlim2=1, ylim=1, ylim2=1, save=False):
    fig = plt.figure(figsize=(12,7))
    ax = fig.gca()
    ax.grid()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    color = ['red', 'blue']
    for signal in yvalue:
        plt.scatter(xvalue, signal)
    plt.legend(legend)

def PltWfm(time, data, legend, scale=1.5, xlim=1, xlim2=1, ylim=1, ylim2=1, save=False):
    if(xlim==1 and xlim2==1):
        xlim = time[0]
        xlim2 = time[-1]
    fig = plt.figure(figsize=(12,7))
    ax = fig.gca()
    ax.grid(b=True, which='major', color='k', linestyle='-')
    ax.grid(b=True, which='minor', color='grey', linestyle=':')
    ax.xaxis.set_minor_locator(MultipleLocator(100))
    ax.xaxis.set_major_locator(MultipleLocator(500))
    ax.yaxis.set_major_locator(MultipleLocator(10))
    ax.yaxis.set_minor_locator(MultipleLocator(10))
    plt.xlabel('Time [$\mu$s]')
    plt.ylabel('Amplitude [mV]')
    plt.xlim(xlim,xlim2)
    for signal in data:
        plt.plot(time, signal)
    plt.legend(legend)

def plot_single_fft(time, data, data2, label, label2, xlabel, ylabel, xlim, xlim2, ylim, ylim2):
    fig = plt.figure(figsize=(12,7))
    ax = fig.gca()
    ax.grid()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xlim(xlim,xlim2)
    plt.ylim(ylim,ylim2)
    plt.loglog(time, data)
    plt.loglog(time, data2)
    plt.legend(['Cathode', 'Anode','Sum'])

def plot_double_fft(time, freq, data, data2, fft, fft2, label, label2, xlabel, ylabel, xlim, ylim):
    fig = plt.figure(figsize=(12,7))
    ax = fig.gca()
    ax.grid()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xlim(-xlim,xlim)
    plt.ylim(-ylim,ylim)
    plt.plot(time, data)
    plt.plot(time, data2)
    plt.legend(['Cathode', 'Anode','Sum'])

    plt.subplot(421)
    plt.ylabel("Amplitude [mV]")
    plt.plot(t*1E3, ch1, '-b')

    plt.subplot(423)
    plt.ylabel("Amplitude [mV]")
    plt.plot(t*1E3, ch2, '-r')

    plt.subplot(422)
    plt.title("Frequency band pass filter between 0 and 100 kHz")
    plt.ylabel("Amplitude")
    plt.semilogy(xf[1:N//2]/1E3, 2.0/N * np.abs(yf[1:N//2]), '-b')

    plt.subplot(424)
    plt.ylabel("Amplitude")
    plt.semilogy(xf[1:N//2]/1E3, 2.0/N * np.abs(yf2[1:N//2]), '-r')

    plt.subplot(425)
    plt.ylabel("Amplitude [mV]")
    plt.plot(t*1E3, y, '-b')

    plt.subplot(427)
    plt.xlabel("Time [ms]")
    plt.ylabel("Amplitude [mV]")
    plt.plot(t*1E3,y2, '-r')

    plt.subplot(426)
    plt.ylabel("Amplitude")
    plt.semilogy(xf[1:N//2]/1E3, 2.0/N * np.abs(yf3[1:N//2]), '-b')

    plt.subplot(428)
    plt.grid(True)
    plt.xlabel("Frequency [kHz]")
    plt.ylabel("Amplitude")
    plt.semilogy(xf[1:N//2]/1E3, 2.0/N * np.abs(yf4[1:N//2]), '-r')
