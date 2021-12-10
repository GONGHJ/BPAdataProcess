'''
huangjie.gong@uky.edu
Plot the boxplots for daily electricity usage by kWh
Grouped by water heater types
'''
# load processed data
import pyarrow.feather as feather
import numpy as np
Summary  = feather.read_feather(r'Summary_dailykWh.feather',use_threads=True, memory_map=True) # the processed daily kWh
# ================= plot daily electricy usage boxplot by season results =====================
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.patches as mpatches
# from mpl_toolkits.axes_grid1 import make_axes_locatable
mpl.style.use('classic')
# define plots settings
FigureWidth=3.3 #inches; this is used to control the figure width
Proportion=0.69
AxisLineWidth=1.3
LableFontsize= 8
Linewidth = 2
mpl.rcParams['xtick.major.size'] = Linewidth
mpl.rcParams['ytick.major.size'] = Linewidth
mpl.rcParams['axes.labelsize'] = LableFontsize
mpl.rcParams['xtick.labelsize'] = LableFontsize
mpl.rcParams['ytick.labelsize'] = LableFontsize
plt.rcParams["figure.figsize"] = (FigureWidth,FigureWidth*Proportion)
# box format control
boxprops_settings=dict(linestyle='-', linewidth=0.5)
whiskerprops_settings=dict(color='black',linestyle='dotted', linewidth = 0.3)
capprops_settings=dict(color='black',linewidth=0.3)
flierprops_settings=dict(color='red', markeredgecolor='red', markerfacecolor='red', marker = 'o', markersize= 0.5)
medianprops_settings=dict(color='green', linewidth= 1.5)
# Hex code for each continents color
groups_colors=["darkgoldenrod","orchid","darkblue"]
group_hatchs=['\\\\\\','|||','++++']
#%% plot the daily electricity in kWh for all water heaters. Categorized by seasons, grouped by water heater types.
# figure data
Dataforplot_control = Summary[['Season','Type','Daily kWh']]
mapSeasons = {1: 'Spring', 2: 'Summer', 3: 'Winter'}
Dataforplot_control['Season'] = Dataforplot_control['Season'].map(mapSeasons)
Typemap = {1: 'AOS_HPWH', 2: 'AOS_RWH', 3: 'GE_HPWH'}
Dataforplot_control['Type'] = Dataforplot_control['Type'].map(Typemap)
# ================ figure 1: all y axis ranges==============================
fig, ax1 = plt.subplots(1,1, sharex=True, sharey = True, figsize=(FigureWidth,FigureWidth*Proportion), constrained_layout=False)
ax1.set(ylim=(0, 70))
ax1.set_yticks(np.array(range(0,71,10)))
h1 = sns.boxplot(x='Season',y='Daily kWh',data=Dataforplot_control, hue='Type', order = ["Spring","Summer","Winter"], hue_order = ['AOS_RWH', 'AOS_HPWH', 'GE_HPWH'],
                 notch=True, boxprops=boxprops_settings,whiskerprops=whiskerprops_settings, capprops=capprops_settings, flierprops=flierprops_settings,medianprops=medianprops_settings)
# format the patterns
groups = Dataforplot_control.Type.unique().tolist()
groups_dict = dict(zip(groups, groups_colors))
Num_groups = len(groups)
Num_category = len(Dataforplot_control.Season.unique().tolist())
for i in range(0,len(groups)*Num_category):
    mybox = h1.artists[i]
    mybox.set_facecolor('white')
# edge color    
for i in range(0,len(groups)*Num_category):
    mybox = h1.artists[i]
    mybox.set_edgecolor(groups_dict[groups[i%Num_groups]])
# add hatches
for i in range(0,len(groups)*Num_category):
    mybox = h1.artists[i]
    mybox.set_hatch(group_hatchs[i%Num_groups])
# make the legend
legend1 = mpatches.Patch(facecolor='white',edgecolor=groups_colors[0],hatch=group_hatchs[0], label='AOS Resistive')
legend2 = mpatches.Patch(facecolor='white',edgecolor=groups_colors[1],hatch=group_hatchs[1], label='AOS HPWH')
legend3 = mpatches.Patch(facecolor='white',edgecolor=groups_colors[2],hatch=group_hatchs[2], label='GE HPWH')
plt.legend(handles=[legend1, legend2, legend3],bbox_to_anchor=(0.7, 1), ncol=1, labelspacing=0.2, frameon=False , fontsize=LableFontsize, handlelength=4)
plt.ylabel('Daily electricity [kWh]')
plt.savefig('Plots/Boxplot_byseason_type_alldays.png', dpi=600, bbox_inches='tight')
plt.show()
# ==================figure 2: all y axis range in [0, 20]===============
fig, ax1 = plt.subplots(1,1, sharex=True, sharey = True, figsize=(FigureWidth,FigureWidth*Proportion), constrained_layout=False)
ax1.set(ylim=(0, 20))
ax1.set_yticks(np.array(range(0,21,10)))
h1 = sns.boxplot(x='Season',y='Daily kWh',data=Dataforplot_control, hue='Type', order = ["Spring","Summer","Winter"], hue_order = ['AOS_RWH', 'AOS_HPWH', 'GE_HPWH'],
                 notch=True, boxprops=boxprops_settings,whiskerprops=whiskerprops_settings, capprops=capprops_settings,
                 flierprops=dict(color='red', markeredgecolor='red', markerfacecolor='red', marker = 'o', markersize= 0),medianprops=medianprops_settings)
# format the patterns
groups = Dataforplot_control.Type.unique().tolist()
groups_dict = dict(zip(groups, groups_colors))
Num_groups = len(groups)
Num_category = len(Dataforplot_control.Season.unique().tolist())

# facecolor    
for i in range(0,len(groups)*Num_category):
    mybox = h1.artists[i]
    mybox.set_facecolor('white')
# edge color    
for i in range(0,len(groups)*Num_category):
    mybox = h1.artists[i]
    mybox.set_edgecolor(groups_dict[groups[i%Num_groups]])
# add hatches
for i in range(0,len(groups)*Num_category):
    mybox = h1.artists[i]
    mybox.set_hatch(group_hatchs[i%Num_groups])
# make the legend
legend1 = mpatches.Patch(facecolor='white',edgecolor=groups_colors[0],hatch=group_hatchs[0], label='AOS Resistive')
legend2 = mpatches.Patch(facecolor='white',edgecolor=groups_colors[1],hatch=group_hatchs[1], label='AOS HPWH')
legend3 = mpatches.Patch(facecolor='white',edgecolor=groups_colors[2],hatch=group_hatchs[2], label='GE HPWH')
plt.legend(handles=[legend1, legend2, legend3],bbox_to_anchor=(0.7, 1), ncol=1, labelspacing=0.2, frameon=False , fontsize=LableFontsize, handlelength=4)
plt.ylabel('Daily electricity [kWh]')
plt.savefig('Plots/Boxplot_byseason_type_alldays_zoomin.png', dpi=600, bbox_inches='tight')
plt.show()