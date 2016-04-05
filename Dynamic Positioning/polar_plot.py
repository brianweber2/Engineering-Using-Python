'''
Project Number: 1514
Subject: Dynamic Positioning Capability Plots

Created By: Brian Weber
Date Created: 10/21/2015

Description:
This script reads a file with Hs and Vw results and prints multiple capability plots.
'''

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# Read data from file
# Hs1, Vw1 = Case 3-I (200te bottom tension | no tug)
# Hs2, Vw2 = Case 3-STF (200te bottom tension | no tug)
# Hs3, Vw3 = Case 3- WCSF (200te bottom tension | 200te tug)
# Hs4, Vw4 = Case 4-I (387te bottom tension | 200te tug)
# Hs5, Vw5 = Case 4-STF (387te bottom tension | 200te tug)
data = np.genfromtxt('mrts_dp_analysis.csv', delimiter=',', skip_header=3, names=['heading','Hs1','Vw1','Hs2','Vw2','Hs3','Vw3','Hs4','Vw4','Hs5','Vw5'])

# Create theta data for limiting Hs and Vw
total_angles = len(data['heading'])
increment = 360/total_angles
headings_analyzed = np.radians(np.arange(0, 370, increment))

# Generate data for the limiting Hs and Vw
limiting_Hs = float(raw_input("\nWhat is the limiting significant wave height (Hs) in meters? "))
limiting_Vw = float(raw_input("\nWhat is the limiting wind speed (Vw) in meters/second? "))
plot_Hs = limiting_Hs * np.ones(len(headings_analyzed))
plot_Vw = limiting_Vw * np.ones(len(headings_analyzed))

# Generate data to plot a vessel on polar plot
ship_theta = np.radians(np.array([338,210,180,150,22,338]))
ship_Hs_line = np.array([2,1.5,2,1.5,2,2])
ship_Vw_line = np.array([6.67,5,6.67,5,6.67,6.67])

# Dry Pipeline (200te bottom tension)
# Setup plot for Hs values
fig1 = plt.figure()
ax1 = fig1.add_subplot(111, polar=True)
ax1.plot(np.radians(data['heading']), data['Hs1'], color='g', lw=2, label='Case 3-I (no tug)')
plt.plot(np.radians(data['heading']), data['Hs2'], color='b', lw=2, label='Case 3-STF (no tug)')
plt.plot(np.radians(data['heading']), data['Hs3'], color='y', lw=2, label='Case 3-WCSF (200te tug)')
plt.plot(headings_analyzed, plot_Hs, color='r', lw=2, label='Limiting Hs (2.5 m)')
plt.plot(ship_theta, ship_Hs_line, color='k')
ax1.set_title("Jascon 18 Heading v.s. Significant Wave Height (Dry Pipeline)", fontsize=20, y=1.08)
ax1.set_xlabel('Vessel Heading [deg]', fontsize=15)
ax1.set_ylim(0,6)
ax1.set_theta_zero_location('S')
ax1.set_theta_direction(1)
ax1.set_thetagrids(np.arange(0,360,30), frac=1.1)
plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter('%d m'))
ax1.set_rgrids([0.1,1,2,3,4,5,6], angle=170.)
plt.legend(bbox_to_anchor=(0.8,0.85), bbox_transform=plt.gcf().transFigure)
plt.tight_layout()
plt.show()
# fig1.savefig('Jascon 18 Heading vs Hs (Dry Pipeline)_Upper Bound Environment.png')

# Setup plot for Vw values
fig2 = plt.figure()
ax2 = fig2.add_subplot(111, polar=True)
ax2.plot(np.radians(data['heading']), data['Vw1'], color='g', lw=2, label='Case 3-I (no tug)')
plt.plot(np.radians(data['heading']), data['Vw2'], color='b', lw=2, label='Case 3-STF (no tug)')
plt.plot(np.radians(data['heading']), data['Vw3'], color='y', lw=2, label='Case 3-WCSF (200te tug)')
plt.plot(ship_theta, ship_Vw_line, color='k')
plt.plot(headings_analyzed, plot_Vw, color='r', lw=2, label='Limiting Vw (15.44 m/s)')
ax2.set_title("Jascon 18 Heading v.s. Wind Speed (Dry Pipeline)", fontsize=20, y=1.08)
ax2.set_xlabel('Vessel Heading [deg]', fontsize=15)
ax2.set_ylim(0,20)
ax2.set_theta_zero_location('S')
ax2.set_theta_direction(1)
ax2.set_thetagrids(np.arange(0,360,30), frac=1.1)
plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter('%d m/s'))
ax2.set_rgrids([0.1,5,10,15,20], angle=170.)
plt.legend(bbox_to_anchor=(0.8,0.85), bbox_transform=plt.gcf().transFigure)
plt.tight_layout()
plt.show()


# Flooded Pipeline (387te bottom tension)
# Setup plot for Hs values
fig3 = plt.figure()
ax3 = fig3.add_subplot(111, polar=True)
ax3.plot(np.radians(data['heading']), data['Hs4'], color='g', lw=2, label='Case 4-I (200te tug)')
plt.plot(np.radians(data['heading']), data['Hs5'], color='b', lw=2, label='Case 4-STF (200te tug)')
plt.plot(headings_analyzed, plot_Hs, color='r', lw=2, label='Limiting Hs (2.5 m)')
plt.plot(ship_theta, ship_Hs_line, color='k')
ax3.set_title("Jascon 18 Heading v.s. Significant Wave Height (Flooded Pipeline)", fontsize=20, y=1.08)
ax3.set_xlabel('Vessel Heading [deg]', fontsize=15)
ax3.set_ylim(0,6)
ax3.set_theta_zero_location('S')
ax3.set_theta_direction(1)
ax3.set_thetagrids(np.arange(0,360,30), frac=1.1)
plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter('%d m'))
ax3.set_rgrids([0.1,1,2,3,4,5,6], angle=170.)
plt.legend(bbox_to_anchor=(0.8,0.85), bbox_transform=plt.gcf().transFigure)
plt.tight_layout()
plt.show()

# Setup plot for Vw values
fig4 = plt.figure()
ax4 = fig4.add_subplot(111, polar=True)
ax4.plot(np.radians(data['heading']), data['Vw4'], color='g', lw=2, label='Case 4-I (200te tug)')
plt.plot(np.radians(data['heading']), data['Vw5'], color='b', lw=2, label='Case 4-STF (200te tug)')
plt.plot(headings_analyzed, plot_Vw, color='r', lw=2, label='Limiting Vw (15.44 m/s)')
plt.plot(ship_theta, ship_Vw_line, color='k')
ax4.set_title("Jascon 18 Heading v.s. Wind Speed (Flooded Pipeline)", fontsize=20, y=1.08)
ax4.set_xlabel('Vessel Heading [deg]', fontsize=15)
ax4.set_ylim(0,20)
ax4.set_theta_zero_location('S')
ax4.set_theta_direction(1)
ax4.set_thetagrids(np.arange(0,360,30), frac=1.1)
plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter('%d m/s'))
ax4.set_rgrids([0.1,5,10,15,20], angle=170.)
plt.legend(bbox_to_anchor=(0.8,0.85), bbox_transform=plt.gcf().transFigure)
plt.tight_layout()
plt.show()


