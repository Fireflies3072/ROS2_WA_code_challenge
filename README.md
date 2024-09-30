# WA_code_challenge

## merge_arrays

**Build**

Use the following code to build the project.

```cmd
colcon build
```

**Use**

In one terminal, run the following commands.

```cmd
source install/local_setup.sh
ros2 run merge_arrays merge_arrays_node
```

In the second terminal, run the following commands.

```cmd
source install/local_setup.sh
ros2 topic pub /input/array1 std_msgs/Int32MultiArray "{data: [1, 4, 8, 12, 26]}"
```

In the third terminal, run the following commands.

```cmd
source install/local_setup.sh
ros2 topic pub /input/array2 std_msgs/Int32MultiArray "{data: [3, 9, 18, 20, 30]}"
```

## PID

**Discovery**

In the PID file, I set up some parameters to reduce error and make the output converge faster. I find the `Kp` and `Kd` values the higher the better. It is possible that the time interval for simulation is not short enough to show more details. There may be a high overshoot between the sample points.