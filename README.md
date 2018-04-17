# Assistive Teleoperation User Study

In this work, we explored how people's trust varies when asked to teleoperate a robot that provides different types of assistance. This work is an extension of Herlant et. al's work on [assitive teleoperation](https://www.ri.cmu.edu/pub_files/2016/3/mode_switching.pdf).

### Time-Optimal Mode Switching
The domain we are exploring is assistive healthcare robotic arms. These high-dimensional robot arms are often controlled by a low-dimensional joystick input and requires switching modes. Each mode controls different degrees of freedom on the robot.  Herlant et. al identified that mode switching consumes about 17.4% of execution time even for able bodied users. They proposed a time-optimal mode-switching algorithm, that determines the optimal mode switch, using Dijkstra's algorithm, to minimize the time taken to complete a. This time-optimal mode-switching strategy was tested on three levels (assistance types):
- **Manual**: The user has full control over mode switching; the robot provides no assistance
- **Automatic**: The robot automatically switches the mode whenever it enters a new region based determined by an optimality map. This change happens the first time the robot enters the zone. The user can change the mode as they please..
- **Forced**:  The robot automatically switches the mode to the time-optimal mode. However, after every action the user took, the robot would switch back to the time-optimal mode. 

### Study Design/Structure
We extended Herlant et. al's work by examining the user's trust with each assistance type based on the visbility of the environment they were navigating the robot through.

The design/structure of our user study is as follows:
- **Simple Map**: The first map is for a practice so that the user can familiarize themselves with the controls
- **Diagonal Map**: The user has **full visibility** of this map and they must complete it 3 times with each assistance type (given in a random order)
- **Maze Map**: The user has **partial visibility** of this map and they must complete it 3 times with each assistance type (given in a random order)

### Running the User Study
To run the user study execute:
```
> python userStudy.py
```

TODO: update `--args` to include user ID
