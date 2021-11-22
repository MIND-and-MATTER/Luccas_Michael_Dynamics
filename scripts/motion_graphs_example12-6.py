import numpy as np
import matplotlib.pyplot as plt

# number_of_plots = 1  # s(t)
number_of_plots = 3  # s(t), v(t), a(t)

start_time = 0.
break_time = 10.
end_time = 30.
times = np.linspace(start_time, end_time)
plot_max_time = end_time + 5.
plot_yspace = [100, 10, 1]
whitespace_factor = 0.02

y_labels = [r'$s$ (ft)', r'$v$ (ft/s)', r'$a$ (ft/s$^2$)']
function_labels = [r'$s = t^2$', r'$s = 20t - 100$']

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif"})


def position(time):
    if time < break_time:
        return time**2
    else:
        return 20.*time - 100.


def velocity(time):
    if time < break_time:
        return 2.*time
    else:
        return 20.


def acceleration(time):
    if time < break_time:
        return 2.
    else:
        return 0.


# Calculate s(t), v(t), and a(t) for all times
positions = []
velocities = []
accelerations = []

for time in times:
    positions.append(position(time))
    velocities.append(velocity(time))
    accelerations.append(acceleration(time))

# Set up plot range and break values
plot_ymin = [0., 0., 0.]
plot_ymax = []
break_yvalues = []

end_position = position(end_time)
plot_ymax.append(end_position + 100)
break_yvalues.append(position(break_time))

end_velocity = velocity(end_time)
plot_ymax.append(end_velocity + 10)
break_yvalues.append(velocity(break_time))

start_acceleration = acceleration(0.)
end_acceleration = acceleration(end_time)
plot_ymax.append(start_acceleration + 1)
break_yvalues.append(acceleration(break_time))


figures, axes = plt.subplots(ncols=number_of_plots)

if number_of_plots > 1:
    # Turn off top and right sides of plots and format x-axes of all plots the same
    for plot_index in np.arange(0, number_of_plots):
        right_side = axes[plot_index].spines["right"]
        right_side.set_visible(False)
        top_side = axes[plot_index].spines["top"]
        top_side.set_visible(False)
        axes[plot_index].set_xlabel(r'$t$ (s)', verticalalignment='center', horizontalalignment='left')
        axes[plot_index].xaxis.set_label_coords(1.+whitespace_factor, 0.00)
        axes[plot_index].set_xlim(0, plot_max_time)
        axes[plot_index].set_xticks([break_time, end_time])
        axes[plot_index].set_ylabel(y_labels[plot_index], rotation='horizontal')
        axes[plot_index].yaxis.set_label_coords(0.00, 1.0+whitespace_factor)
        axes[plot_index].set_ylim(plot_ymin[plot_index], plot_ymax[plot_index])

        if plot_index == 0:
            # s(t)
            axes[plot_index].plot(times, positions)
            axes[plot_index].fill_between(times, 0, positions, facecolor='lightblue')
            axes[plot_index].set_yticks([break_yvalues[plot_index], end_position])
            axes[plot_index].axhline(y=break_yvalues[plot_index], xmin=start_time / plot_max_time,
                                     xmax=break_time / plot_max_time,
                                     color='black', linewidth=0.5)
            axes[plot_index].axhline(y=end_position, xmin=start_time / plot_max_time, xmax=end_time / plot_max_time,
                                     color='black', linewidth=0.5)
            axes[plot_index].axvline(x=end_time, ymin=0., ymax=end_position / plot_ymax[plot_index],
                                     color='black', linewidth=0.5)

        elif plot_index == 1:
            # v(t)
            axes[plot_index].plot(times, velocities)
            axes[plot_index].fill_between(times, 0, velocities, facecolor='lightblue')
            axes[plot_index].set_yticks([break_yvalues[1], end_velocity])
            axes[plot_index].axhline(y=break_yvalues[plot_index], xmin=start_time / plot_max_time,
                                     xmax=break_time / plot_max_time,
                                     color='black', linewidth=0.5)
            axes[plot_index].axvline(x=break_time, ymin=0., ymax=break_yvalues[plot_index]/plot_ymax[plot_index],
                                     color='black', linewidth=0.5)
            axes[plot_index].axhline(y=end_velocity, xmin=start_time/plot_max_time, xmax=end_time/plot_max_time,
                                     color='black', linewidth=0.5)
            axes[plot_index].axvline(x=end_time, ymin=0., ymax=end_velocity/plot_ymax[plot_index],
                                     color='black', linewidth=0.5)
        elif plot_index == 2:
            # a(t)
            axes[plot_index].plot(times, accelerations)
            axes[plot_index].fill_between(times, 0, accelerations, facecolor='lightblue')
            axes[plot_index].set_yticks([break_yvalues[plot_index], start_acceleration])

else:
    plot_index = 0
    right_side = axes.spines["right"]
    right_side.set_visible(False)
    top_side = axes.spines["top"]
    top_side.set_visible(False)
    axes.set_xlabel(r'$t$ (s)', verticalalignment='center', horizontalalignment='left')
    axes.xaxis.set_label_coords(1.+whitespace_factor, 0.00)
    axes.set_xlim(0, plot_max_time)
    axes.set_xticks([break_time, end_time])
    axes.set_ylabel(y_labels[plot_index], rotation='horizontal')
    axes.yaxis.set_label_coords(0.00, 1.+whitespace_factor)
    axes.set_ylim(plot_ymin[plot_index], plot_ymax[plot_index])

    axes.plot(times, positions)
    axes.fill_between(times, 0, positions, facecolor='lightblue')
    axes.set_yticks([break_yvalues[plot_index], end_position])
    axes.axhline(y=break_yvalues[plot_index], xmin=start_time / plot_max_time, xmax=break_time / plot_max_time,
                 color='black', linewidth=0.5)
    axes.axvline(x=break_time, ymin=0., ymax=break_yvalues[plot_index] / plot_ymax[plot_index],
                 color='black', linewidth=0.5)
    axes.axhline(y=end_position, xmin=start_time / plot_max_time, xmax=end_time / plot_max_time,
                 color='black', linewidth=0.5)
    axes.axvline(x=end_time, ymin=0., ymax=end_position / plot_ymax[plot_index],
                 color='black', linewidth=0.5)
    axes.text((1.-whitespace_factor) * 0.5 * break_time, position(0.5 * break_time),
              function_labels[0], horizontalalignment='right')
    axes.text((1.-whitespace_factor) * 0.5 * (break_time + end_time), 0.5 * (break_yvalues[plot_index] + end_position),
              function_labels[1], horizontalalignment='right')

figures.tight_layout()
plt.show()
