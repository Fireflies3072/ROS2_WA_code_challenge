# ROS2_WA_code_challenge

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

I'm still doing it. It takes me a long time to setup the ROS2 environment.