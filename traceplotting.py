#!/usr/bin/env python2

import os
import matplotlib.pyplot as plt
from matplotlib import cm
import pandas as pd
import seaborn as sns
import numpy as np
import scipy
from scipy import stats

# Set seaborn to override matplotlib for plot output
sns.set()
sns.set_style("white", {'font.family': ['sans-serif']})
# The four preset contexts, in order of relative size, are paper, notebook, talk, and poster.
# The notebook style is the default
# sns.set_context("notebook", font_scale=1.5)
sns.set_context("poster", font_scale=1.2)
sns.set_palette(sns.color_palette('cubehelix'))
# plt.style.use("dark_background")


def plotHistogramOfTwoDataSets(data_frame_path, dataset_1_name, dataset_2_name):
    pass


def plotAllContourLengthHistograms(json_path):

    contour_lengths_df = pd.read_json(json_path)
    sns.set()

    nbins = np.linspace(-10,10,30)

    project_names = set(contour_lengths_df['Experiment Directory'].array)
    #print(project_names)

    for name in project_names:


        temp_df = contour_lengths_df.loc[contour_lengths_df['Experiment Directory'] == name ]

        plt.hist(temp_df['Contour Lengths'], 20, histtype= 'bar', label = name)

        try:
            hist_data.append(temp_df['Contour Lengths'])
        except NameError:
            hist_data = [temp_df['Contour Lengths']]

        #plt.hist(hist_data, 50, histtype= 'bar', label = project_names)
            #sns.distplot(temp_df['Contour Lengths'])
    plt.legend(loc='upper right')
    plt.xlabel('Contour Length (nm)')
    plt.ylabel('Occurence')

    save_file_name = json_path.split('/')

    plt.savefig('%s.png' % json_path[:-4])
    plt.savefig('%s.svg' % json_path[:-4])
    plt.close()

def plotLinearVsCircular(json_path):
    sns.set(style = 'whitegrid')
    pal = sns.color_palette()

    contour_lengths_df = pd.read_json(json_path)

    linear_contour_lengths = contour_lengths_df.loc[contour_lengths_df['Circular'] == False]
    circular_contour_lengths = contour_lengths_df.loc[contour_lengths_df['Circular'] == True]

    plt.hist([circular_contour_lengths['Contour Lengths'].array, linear_contour_lengths['Contour Lengths'].array], 25, histtype = 'bar', label = ['Linear Molecules', 'Circular Molecules'])
    plt.xlabel('Contour Length (nm)')
    plt.ylabel('Occurence')
    plt.legend(loc='upper right')
    plt.title('%s Linear vs Circular' % json_path[:-4])
    plt.savefig('%s_linearVcircularHist.png' % json_path[:-4])
    plt.savefig('%s_linearVcircularHist.svg' % json_path[:-4])
    plt.close()

    num_lin_circ_df = pd.DataFrame(data = {'Linear' : [len(circular_contour_lengths)], 'Circular' : [len(linear_contour_lengths)]})

    sns.barplot(data = num_lin_circ_df, order = ['Linear', 'Circular'])
    plt.xlabel('Linear or Circular')
    plt.ylabel('Occurence')
    plt.title('%s Linear vs Circular' % json_path[:-4])
    plt.savefig('%s_barplot.png' % json_path[:-4])
    plt.savefig('%s_barplot.svg' % json_path[:-4])
    plt.close()


def plotkde(df, directory, name, plotextension, grouparg, plotarg):

    sns.set_palette(sns.color_palette('cubehelix'))

    print 'Plotting kde of %s' % plotarg

    # Create a saving name format/directory
    savedir = os.path.join(directory, 'Plots')
    if not os.path.exists(savedir):
        os.makedirs(savedir)
    savename = os.path.join(savedir, name + plotarg + plotextension)

    # Plot and save figures
    fig, ax = plt.subplots(figsize=(10, 7))
    df.groupby(grouparg)[plotarg].plot.kde(ax=ax, legend=True, alpha=1, linewidth=3.0)
    plt.xlim(-20, 200)
    # plt.xlabel(' ')
    # plt.ylabel(' ')
    plt.savefig(savename)

def plothist(df, directory, name, plotextension, grouparg, plotarg):
    sns.set_palette(sns.color_palette('cubehelix'))

    print 'Plotting histogram of %s' % plotarg

    # Create a saving name format/directory
    savedir = os.path.join(directory, 'Plots')
    if not os.path.exists(savedir):
        os.makedirs(savedir)

    # Plot and save figures
    savename = os.path.join(savedir, name + plotarg + '_histogram1' + plotextension)
    fig, ax = plt.subplots(figsize=(10, 7))
    # Pivot dataframe to get required variables in correct format for plotting
    df1 = df.pivot(columns=grouparg, values=plotarg)
    # Plot histogram
    df1.plot.hist(ax=ax, legend=True, bins=bins, alpha=.7, stacked=False)
    plt.xlim(0, 200)
    # plt.xlabel(' ')
    # plt.ylabel(' ')
    plt.savefig(savename)


def plothist2(df, directory, name, plotextension, grouparg, plotarg):
    print 'Plotting histogram of %s' % plotarg

    # Create a saving name format/directory
    savedir = os.path.join(directory, 'Plots')
    if not os.path.exists(savedir):
        os.makedirs(savedir)

    # Plot and save figures
    savename = os.path.join(savedir, name + plotarg + '_histogram' + plotextension)

    fig, ax = plt.subplots(figsize=(10, 7))
    df.groupby(grouparg)[plotarg].plot.hist(ax=ax, legend=True, bins=10, alpha=0.7, stacked=True)
    handles, labels = ax.get_legend_handles_labels()
    plt.xlim(0, 200)
    # plt.xlabel(' ')
    # plt.ylabel(' ')
    plt.savefig(savename)

def plothiststacked2(df, directory, name, plotextension, grouparg, plotarg):
    print 'Plotting histogram of %s' % plotarg

    # Create a saving name format/directory
    savedir = os.path.join(directory, 'Plots')
    if not os.path.exists(savedir):
        os.makedirs(savedir)

    # Plot and save figures
    savename = os.path.join(savedir, name + plotarg + '_histogram_stacked' + plotextension)
    fig, ax = plt.subplots(figsize=(10, 7))
    # Pivot dataframe to get required variables in correct format for plotting
    df1 = df.pivot(columns=grouparg, values=plotarg)
    # Plot histogram
    df1.plot.hist(ax=ax, legend=True, bins=bins, alpha=.7, stacked=True)
    handles, labels = ax.get_legend_handles_labels()
    plt.xlim(0, 200)
    # plt.xlabel(' ')
    # plt.ylabel(' ')
    plt.savefig(savename)


def plotkdemax(df, directory, name, plotextension, plotarg, topos):
    print 'Plotting kde and maxima for %s' % plotarg
    sns.set_palette(sns.color_palette('cubehelix'))

    # sns.set_context("notebook")

    # Create a saving name format/directory
    savedir = os.path.join(directory, 'Plots')
    if not os.path.exists(savedir):
        os.makedirs(savedir)

    # Plot and save figures
    savename = os.path.join(savedir, name + plotarg + '_KDE_new' + plotextension)

    df = df.rename(columns={"Experiment Directory": "expmt"})

    # Determine KDE for each topoisomer
    # Determine max of each KDE and plot
    xs = np.linspace(0, 400, 100)
    kdemax = dict()
    dfstd = dict()
    dfvar = dict()
    dfste = dict()
    # plt.figure()
    for i in topos:
        kdemax[i] = i
        dfstd[i] = i
        dfvar[i] = i
        dfste[i] = i
        x = df.query('expmt == @i')[plotarg]
        a = scipy.stats.gaussian_kde(x)
        b = a.pdf(xs)
        dfstd[i] = np.std(x)
        dfstd[i] = x.std()
        dfvar[i] = np.var(x)
        dfste[i] = stats.sem
        # plt.plot(xs, b)
        kdemax[i] = xs[np.argmax(b)]
    plt.savefig(savename)

    print kdemax

    savename2 = os.path.join(savedir, name + plotarg + '_KDE_max' + plotextension)
    fig = plt.figure(figsize=(10, 7))
    # plt.xlabel('Topoisomer')
    plt.ylabel(' ')
    # Set an arbitrary value to plot to in x, increasing by one each loop iteration
    order = 0
    # Set a value for the placement of the bars, by creating an array of the length of topos
    bars = np.linspace(0, len(topos), len(topos), endpoint=False, dtype=int)
    for i in sorted(topos, reverse=False):
        plt.bar(order, kdemax[i], alpha=1)
        # plt.bar(order, kdemax[i], yerr=dfstd[i], alpha=0.7)
        # plt.bar(order, kdemax[i], yerr=dfvar[i], alpha=0.7)
        order = order + 1
        # Set the bar names to be the topoisomer names
        plt.xticks(bars, sorted(topos, reverse=False))
        plt.savefig(savename2)

if __name__ == '__main__':
    # Set the file path, i.e. the directory where the files are here'
    path = '/Volumes/GoogleDrive/My Drive/AFM research group /Methods paper/Data/Circular'
    name = 'tracestats.json'
    file_name = os.path.join(path, name)

    # file_name = 'new_data/tracestats.json'

    plotAllContourLengthHistograms(file_name)
    plotLinearVsCircular(file_name)

    plotextension = '.pdf'
    bins = 30

    # import data form the json file specified as a dataframe
    df = pd.read_json(file_name)

    # Sort dataframe
    df = df.sort_values(["Experiment Directory", "Image Name", "Molecule number"], ascending=(True, True, True))

    # Obtain list of unique experiments
    expmts = df['Experiment Directory'].unique()
    expmts = sorted(expmts, reverse=False)

    # Add column to calculate length
    df['Calculated Length'] = df['Experiment Directory'].str.extract('(\d+)').astype(int)
    df['Length'] = df['Calculated Length'] * 0.34

    # Plot data as KDE
    plotkde(df, path, name, plotextension, 'Experiment Directory', 'Contour Lengths')
    plotkdemax(df, path, name, plotextension, 'Contour Lengths', expmts)

    # Plot data as histograms
    plothist(df, path, name, plotextension, 'Experiment Directory', 'Contour Lengths')
    plothist2(df, path, name, plotextension, 'Experiment Directory', 'Contour Lengths')
    plothiststacked2(df, path, name, plotextension, 'Experiment Directory', 'Contour Lengths')