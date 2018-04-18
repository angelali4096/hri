# Assistive Teleoperation User Study

In this work, we explored how people's trust varies when asked to teleoperate a robot that provides different types of assistance. This work is an extension of Herlant et. al's work on [assitive teleoperation](https://www.ri.cmu.edu/pub_files/2016/3/mode_switching.pdf).

## User Study Overview
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

## User Study Simulation Implementation Details
### Time-Optimal Mode-Switching Algorithm Implementation
- `minBinaryHeap.py`: Min-Binary Heap Implementation
- `node.py`: Graph node representation 
- `timeOptPlanner.py`: Implementation of Dijkstra's algorithm; creates a map that determines the shortest distance to the goal from each `(x, y, mode)`

### Study Interface Implementation
- `basicAnimation.py`: 
- `basicAnimationClass.py`:
- `maps.py`: Contains the pratice map, the diagonal map used in the study and the implementation of the assistance types 
- `mazeMap.py`: Contains the maze map and the the implementation of the assistance types 

### Running the User Study
To run the user study execute:
```
> python userStudy.py --userid <user ID> 
```
Replace `<user ID>` with the user's ID