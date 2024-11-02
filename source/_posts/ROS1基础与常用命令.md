---
title: ROS1基础与常用命令
date: 2024-11-02 19:32:34
description: 接触ROS差不多有一年多了，最近由于科研的需要，又重新捡了起来。个人觉得快速上手ROS的方法是在理解大概原理的前提下，快速把常用的操作过一遍。在使用ROS的时候，有时一些命令常常想不起来，上网查阅又需要花费大量时间，这里一并总结了一下。
tags: 
    - ROS
    - Linux
    - 日常总结
top_img: /img/ROS1基础与常用命令/cover.png
cover: /img/ROS1基础与常用命令/cover.png
---

# 1. 前言

接触ROS差不多有一年多了，最近由于科研的需要，又重新捡了起来。个人觉得快速上手ROS的方法是在理解大概原理的前提下，快速把常用的操作过一遍。在使用ROS的时候，有时一些命令常常想不起来，上网查阅又需要花费大量时间，这里一并总结了一下。

# 2. ROS的安装

一般的使用场景都是在Ubuntu 20.04 上安装Noetic版本，一般在有代理的情况下，按照[官方的教程](https://wiki.ros.org/noetic/Installation/Ubuntu)，可以一次性安装成功，步骤如下：

1.   设置源列表使计算机接受来自packages.ros.org的软件

     ```bash
     sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
     ```

2.   设置Key

     ```bash
     sudo apt install curl # 安装curl，若已安装则跳过
     ```

     ```bash
     curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
     ```

3.    安装

     ```bash
     sudo apt update #更新软件包索引
     sudo apt install ros-noetic-desktop-full #安装完整版
     ```

4.   设置环境变量

     ```bash
     echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
     source ~/.bashrc
     ```

5.   安装常用的构建依赖项

     ```bash
     sudo apt install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential
     ```

6.   安装和初始化rosdep

     ```bash
     sudo apt install python3-rosdep
     sudo rosdep init
     rosdep update
     ```

安装完成后，后续如果要安装其他软件包，可以在[ROS Packages](https://index.ros.org/packages/page/1/time/#noetic)中寻找，或者使用命令：

```bash
apt search ros-noetic
```

若想安装特定的软件包，可以使用命令：

```bash
sudo apt install ros-noetic-PACKAGE
```

# 3. ROS简介

ROS（Robot Operating System）是一个用于机器人开发的开源框架，旨在简化机器人软件的开发。它提供了一系列工具、库和约定，以便于开发者创建复杂的机器人应用。

1.   **节点（Node）**

     节点是ROS系统中的基本计算单元。每个节点都是一个独立的进程，可以执行特定的任务。不同的节点可以用不同的语言编写。

2.   **话题（Topic）**

     话题是ROS中节点之间通信的方式。节点可以发布（publish）和订阅（subscribe）话题。发布者将消息发送到特定的话题，而订阅者接收该话题的消息。这样，节点之间的耦合度降低，增加了系统的灵活性。

3.   **服务（Service）**

     服务是ROS中另一种通信机制，允许节点通过请求-响应模式进行交互。一个节点提供服务，另一个节点调用该服务。

4.   **消息（Message）**

     消息是ROS中传递的数据结构。每种类型的消息都有其特定的格式，定义了节点之间交换的数据。ROS内置了多种基本消息类型，也支持用户自定义消息类型。

5.   **参数服务器（Parameter Server）**

     参数服务器是一个共享的全局数据库，用于存储配置参数。节点可以读取和写入这些参数，以便动态调整系统的行为。

6.   **工作空间（Workspace）**

     工作空间是ROS开发环境的一个目录，包含了ROS包、库和配置文件。我们可以在工作空间中编写、测试和管理机器人应用。

7.   **包（Package）**

     ROS的功能以包的形式组织。每个包可以包含节点、库、配置文件、文档等。包的结构使得代码的复用和共享变得更加方便。

# 4. 构建工作区

我们这里以在`home`目录中创建一个名为`catkin_ws`的工作区为例

```bash
mkdir -p catkin_ws/src
cd catkin_ws
catkin_make
catkin_make install #添加install文件夹
```

>   这里有一个坑：如果之前在Ubuntu中安装了Anaconda或者miniconda，会出现找不到`empy`包的错误。
>
>   解决方案：
>
>   +   设置启动终端时不自动进入base环境，命令：
>
>       ```bash
>       conda config --set auto_activate_base false
>       ```
>
>   +   重新打开终端，重新编译：
>
>       ```bash
>       rm -rf build devel
>       catkin_make
>       ```

在每次运行软件包时，我们通常要先设置环境变量，为了避免频繁操作，可以将其写入`.bashrc`文件中，这样每次启动终端时会自动设置。

使用命令

```bash
echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

检查环境变量：

```bash
echo $ROS_PACKAGE_PATH
```

# 5. 基础操作例程

## 5.1 小海龟

小海龟例程是ROS非常经典的入门学习包，可以让我们快速熟悉ROS命令行工具的使用

1.   启动ROS Master

     ```bash
     roscore
     ```

2.   启动小海龟仿真器节点

     ```bash
     rosrun turtlesim turtlesim_node
     ```

     <img src="/img/ROS1基础与常用命令/image-20241102115548811.png" alt="image-20241102115548811" style="zoom:50%;" />

3.   启动海龟控制节点

     ```bash
     rosrun turtlesim turtle_teleop_key
     ```

4.   启动上述两个节点之后，我们便可以用键盘来控制海龟的移动。

5.   查看系统计算图

     ```bash
     rqt_graph
     ```

     <img src="/img/ROS1基础与常用命令/image-20241102115935703.png" alt="image-20241102115935703" style="zoom:50%;" />

     从图中可知，目前ROS系统中存在两个节点，一个是海龟仿真器节点`turtlesim`，其订阅了话题`/turtle1/cmd_vel`，还有一个节点是`teleop_turtle`，其往`/turtle1/cmd_vel`中发布信息，这样两个节点间便完成了通讯。

6.   节点相关信息的命令为`rosnode`，示例：

     +   查看节点列表

         ```bash
         rosnode list
         ```

         输出：

         ```
         /rosout
         /rqt_gui_py_node_83022
         /teleop_turtle
         /turtlesim
         ```

     +   查看某个节点的信息

         ```bash
         rosnode info /turtlesim
         ```

         输出：

         ```
         Node [/turtlesim]
         Publications: 
          * /rosout [rosgraph_msgs/Log]
          * /turtle1/color_sensor [turtlesim/Color]
          * /turtle1/pose [turtlesim/Pose]
         
         Subscriptions: 
          * /turtle1/cmd_vel [geometry_msgs/Twist]
         
         Services: 
          * /clear
          * /kill
          * /reset
          * /spawn
          * /turtle1/set_pen
          * /turtle1/teleport_absolute
          * /turtle1/teleport_relative
          * /turtlesim/get_loggers
          * /turtlesim/set_logger_level
         
         
         contacting node http://ubuntu:37017/ ...
         Pid: 82069
         Connections:
          * topic: /rosout
             * to: /rosout
             * direction: outbound (52857 - 127.0.0.1:47492) [26]
             * transport: TCPROS
          * topic: /turtle1/cmd_vel
             * to: /teleop_turtle (http://ubuntu:41229/)
             * direction: inbound (45856 - ubuntu:38849) [32]
             * transport: TCPROS
         ```

7.   话题相关命令为`rostopic`，示例：

     +   查看话题列表：

         ```bash
         rostopic list
         ```

         输出：

         ```
         /rosout
         /rosout_agg
         /statistics
         /turtle1/cmd_vel
         /turtle1/color_sensor
         /turtle1/pose
         ```

     +   发布话题:

         ```bash
         rostopic pub /turtle1/cmd_vel geometry_msgs/Twist "linear:
           x: 1.0
           y: 1.0
           z: 0.0
         angular:
           x: 1.0
           y: 0.0
           z: 0.0" 
         ```

8.   消息相关命令为`rosmsg`，示例：

     +   查看消息类型

         ```bash
         rosmsg show geometry_msgs/Twist
         ```

         输出：

         ```
         geometry_msgs/Vector3 linear
           float64 x
           float64 y
           float64 z
         geometry_msgs/Vector3 angular
           float64 x
           float64 y
           float64 z
         ```

9.   服务相关命令为`rosservice`，示例：

     +   查看提供服务的内容

         ```bash
         rosservice list
         ```

         输出：

         ```
         /clear
         /kill
         /reset
         /rosout/get_loggers
         /rosout/set_logger_level
         /rqt_gui_py_node_84673/get_loggers
         /rqt_gui_py_node_84673/set_logger_level
         /spawn
         /teleop_turtle/get_loggers
         /teleop_turtle/set_logger_level
         /turtle1/set_pen
         /turtle1/teleport_absolute
         /turtle1/teleport_relative
         /turtlesim/get_loggers
         /turtlesim/set_logger_level
         ```

     +   请求产生一个海龟的服务

         ```bash
         rosservice call /spawn "x: 0.0
         y: 0.0
         theta: 0.0
         name: 'turtle2'" 
         ```

         执行完后会在`turtlesim`中产生一个海龟

10.   话题记录和复现工具

      +   话题记录

          ```bash
          rosbag record -a -O cmd_record
          ```

      +   话题复现

          ```bash
          rosbag play cmd_record.bag
          ```

## 5.2 发布和订阅

发布和订阅是ROS最基础的通信机制，这里演示如何创建功能包，编写一个信息发布节点 `Publisher`，和一个信息订阅节点 `Pubscriber`。

### 5.2.1 功能包的构建和编译

1.   创建功能包

     ```bash
     catkin_create_pkg <package_name> [depend1] [depend2] [depend3]
     ```

     示例：

     执行命令创建功能包

     ```bash
     cd ~/catkin_ws/src/
     catkin_create_pkg pub_sub_pkg std_msgs rospy roscpp
     ```

2.   编译功能包

     ```bash
     cd ~/catkin_ws/
     catkin_make
     source /devel/setup.bash
     ```

### 5.2.2 Publisher的编写

#### 5.2.2.1 cpp版本的实现

1.   在`pub_sub_pkg/src/`路径下新建文件`random_number_publisher.cpp`，添加如下内容

     ```cpp
     #include <ros/ros.h>
     #include <std_msgs/Int32.h>
     #include <cstdlib>  // for rand()
     #include <ctime>    // for time()
     
     int main(int argc, char** argv) {
         ros::init(argc, argv, "random_number_publisher");
         ros::NodeHandle nh;
     
         // 创建一个发布者，发布到 "random_number" 主题
         ros::Publisher random_pub = nh.advertise<std_msgs::Int32>("random_number", 10);
     
         // 初始化随机数生成器
         std::srand(static_cast<unsigned int>(std::time(0)));
     
         // 设置循环频率
         ros::Rate loop_rate(1);  // 每秒发布一次
     
         while (ros::ok()) {
             // 创建一个消息并设置随机数
             std_msgs::Int32 msg;
             msg.data = std::rand() % 100;  // 生成 0 到 99 的随机数
     
             // 发布消息
             random_pub.publish(msg);
             ROS_INFO("Published random number: %d", msg.data);
     
             // 休眠直到下一个循环
             ros::spinOnce();
             loop_rate.sleep();
         }
     
         return 0;
     }
     ```

2.   修改 `CMakeLists.txt`

     添加如下内容：

     ```cmake
     add_executable(random_number_publisher src/random_number_publisher.cpp)
     target_link_libraries(random_number_publisher ${catkin_LIBRARIES})
     ```

3.   编译包

     回到工作空间，输入`catkin_make`编译包

#### 5.2.2.2 py版本的实现

1.   在 `pub_sub_pkg/src` 目录下创建一个名为 `random_number_publisher.py` 的文件，并添加如下内容

     ```python
     import rospy
     from std_msgs.msg import Int32
     import random
     
     def random_number_publisher():
         # 初始化节点
         rospy.init_node('random_number_publisher', anonymous=True)
         # 创建一个发布者，发布到 "random_number" 主题
         pub = rospy.Publisher('random_number', Int32, queue_size=10)
         # 设置循环频率
         rate = rospy.Rate(1)  # 每秒发布一次
     
         while not rospy.is_shutdown():
             # 生成随机数
             random_number = random.randint(0, 99)  # 生成 0 到 99 的随机数
             rospy.loginfo("Published random number: %d", random_number)
             # 创建消息并发布
             pub.publish(random_number)
             # 休眠直到下一个循环
             rate.sleep()
     
     if __name__ == '__main__':
         try:
             random_number_publisher()
         except rospy.ROSInterruptException:
             pass
     ```

2.   修改 `CMakeLists.txt`

     添加如下内容：

     ```cmake
     catkin_install_python(PROGRAMS
       src/random_number_publisher.py
       DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
     )
     ```

3.   编译包

     回到工作空间，输入`catkin_make`编译包

### 5.2.3 Subscriber的编写

#### 5.2.3.1 cpp版本的实现

1.   在 `pub_sub_pkg/src` 目录下创建一个名为 `random_number_subscriber.cpp` 的文件，并添加如下内容：

     ```cpp
     #include <ros/ros.h>
     #include <std_msgs/Int32.h>
     
     void randomNumberCallback(const std_msgs::Int32::ConstPtr& msg) {
         ROS_INFO("Received random number: %d", msg->data);
     }
     
     int main(int argc, char** argv) {
         ros::init(argc, argv, "random_number_subscriber");
         ros::NodeHandle nh;
     
         // 创建一个订阅者，订阅 "random_number" 主题
         ros::Subscriber sub = nh.subscribe("random_number", 10, randomNumberCallback);
     
         // 循环等待回调
         ros::spin();
     
         return 0;
     }
     ```

2.   修改 `CMakeLists.txt`

     添加如下内容：

     ```cmake
     add_executable(random_number_subscriber src/random_number_subscriber.cpp)
     target_link_libraries(random_number_subscriber ${catkin_LIBRARIES})
     ```

3.   编译包

     回到工作空间，输入`catkin_make`编译包

#### 5.2.3.2 py版本的实现

1.   在 `pub_sub_pkg/src` 目录下创建一个名为 `random_number_subscriber.py` 的文件，并添加如下内容：

     ```python
     import rospy
     from std_msgs.msg import Int32
     
     def random_number_callback(msg):
         rospy.loginfo("Received random number: %d", msg.data)
     
     def random_number_subscriber():
         # 初始化节点
         rospy.init_node('random_number_subscriber', anonymous=True)
         # 创建一个订阅者，订阅 "random_number" 主题
         rospy.Subscriber('random_number', Int32, random_number_callback)
     
         # 循环等待回调
         rospy.spin()
     
     if __name__ == '__main__':
         random_number_subscriber()
     ```

2.   修改 `CMakeLists.txt`

     添加如下内容：

     ```cmake
     catkin_install_python(PROGRAMS
       src/random_number_subscriber.py
       DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
     )
     ```

3.   编译包

     回到工作空间，输入`catkin_make`编译包

### 5.2.4 运行节点

1.   启动 ROS 核心：

     ```bash
     roscore
     ```

2.   启动发布节点：

     +   若运行cpp版本使用命令

         ```bash
         rosrun pub_sub_pkg random_number_publisher
         ```

     +   若运行py版本使用命令

         ```bash
         rosrun pub_sub_pkg random_number_publisher.py
         ```

3.   启动订阅节点：

     +   若运行cpp版本使用命令

         ```bash
         rosrun pub_sub_pkg random_number_subscriber
         ```

     +   若运行py版本使用命令

         ```bash
         rosrun pub_sub_pkg random_number_subscriber.py
         ```

运行效果如图：

<img src="/img/ROS1基础与常用命令/image-20241102132155934.png" alt="image-20241102132155934" style="zoom:50%;" />

<img src="/img/ROS1基础与常用命令/image-20241102132217586.png" alt="image-20241102132217586" style="zoom:50%;" />

## 5.3 自定义消息类型

面向更加复杂的应用，我们需要创建自定义消息类型来满足开发需求。我们创建一个功能包名为`custom_message`，并在该功能包中进行以下操作。

### 5.3.1 创建自定义消息类型

假设我们创建一个包含一个整数和一个字符串的消息类型。

1.   创建消息文件

     在`custom_message`目录下创建`msg`文件夹，并在该文件夹中创建一个`RandomNumber.msg`文件，添加如下内容

     ```
     int32 number
     string message
     ```

2.   修改 `package.xml`

     在 `package.xml` 文件中添加以下内容

     ```xml
     <build_depend>message_generation</build_depend>
     <exec_depend>message_runtime</exec_depend>
     ```

3.   修改 `CMakeLists.txt`

     可对照下面内容进行修改

     ```cmake
     find_package(catkin REQUIRED COMPONENTS
       roscpp
       rospy
       std_msgs
       message_generation
     )
     
     add_message_files(
       FILES
       RandomNumber.msg
     )
     
     generate_messages(
       DEPENDENCIES
       std_msgs
     )
     ```

4.   可以先用`catkin_make`编译一次，方便之后的源文件调用

然后在之前的`Publisher`和`Subscriber`的基础上修改代码

### 5.3.2 修改发布节点

`random_msg_publisher.cpp`的内容如下：

```cpp
#include <ros/ros.h>
#include <custom_message/RandomNumber.h>
#include <cstdlib>  // for rand()
#include <ctime>    // for time()

int main(int argc, char** argv) {
    ros::init(argc, argv, "random_number_publisher");
    ros::NodeHandle nh;

    // 创建一个发布者，发布到 "random_number" 主题
    ros::Publisher random_pub = nh.advertise<custom_message::RandomNumber>("random_number", 10);

    // 初始化随机数生成器
    std::srand(static_cast<unsigned int>(std::time(0)));

    // 设置循环频率
    ros::Rate loop_rate(1);  // 每秒发布一次

    while (ros::ok()) {
        // 创建一个消息并设置随机数
        custom_message::RandomNumber msg;
        msg.number = std::rand() % 100;  // 生成 0 到 99 的随机数
        msg.message = "Random number generated";
        // 发布消息
        random_pub.publish(msg);
        ROS_INFO("Published: number = %d, message = %s", msg.number, msg.message.c_str());

        // 休眠直到下一个循环
        ros::spinOnce();
        loop_rate.sleep();
    }

    return 0;
}
```

`random_msg_publisher.py`的内容如下：

```python
import rospy
from custom_message.msg import RandomNumber
import random

def random_number_publisher():
    # 初始化节点
    rospy.init_node('random_number_publisher', anonymous=True)
    # 创建一个发布者，发布到 "random_number" 主题
    pub = rospy.Publisher('random_number', RandomNumber, queue_size=10)
    # 设置循环频率
    rate = rospy.Rate(1)  # 每秒发布一次

    while not rospy.is_shutdown():
        msg = RandomNumber()
        msg.number = random.randint(0, 99)
        msg.message = "Random number generated"
        
        rospy.loginfo("Published: number = %d, message = %s", msg.number, msg.message)
        pub.publish(msg)

        rate.sleep()

if __name__ == '__main__':
    try:
        random_number_publisher()
    except rospy.ROSInterruptException:
        pass
```

`CMakeLists.txt`添加

```cmake
add_executable(random_msg_publisher src/random_msg_publisher.cpp)
target_link_libraries(random_msg_publisher ${catkin_LIBRARIES})

catkin_install_python(PROGRAMS
  src/random_msg_publisher.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
```

### 5.3.3 修改订阅节点

`random_msg_subscriber.cpp`内容如下：

```cpp
#include <ros/ros.h>
#include <custom_message/RandomNumber.h>

void randomNumberCallback(const custom_message::RandomNumber::ConstPtr& msg) {
    ROS_INFO("Received: number = %d, message = %s", msg->number, msg->message.c_str());
}

int main(int argc, char** argv) {
    ros::init(argc, argv, "random_number_subscriber");
    ros::NodeHandle nh;

    ros::Subscriber sub = nh.subscribe("random_number", 10, randomNumberCallback);
    ros::spin();

    return 0;
}
```

`random_msg_subscriber.py`内容如下：

```python
import rospy
from custom_message.msg import RandomNumber

def random_number_callback(msg):
    rospy.loginfo("Received: number = %d, message = %s", msg.number, msg.message)

def random_number_subscriber():
    rospy.init_node('random_number_subscriber', anonymous=True)
    rospy.Subscriber('random_number', RandomNumber, random_number_callback)
    rospy.spin()

if __name__ == '__main__':
    random_number_subscriber()
```

`CMakeLists.txt`添加：

```cmake
add_executable(random_msg_subscriber src/random_msg_subscriber.cpp)
target_link_libraries(random_msg_subscriber ${catkin_LIBRARIES})

catkin_install_python(PROGRAMS
  src/random_msg_subscriber.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
```

### 5.3.4 运行节点

1.   启动 ROS 核心：

     ```bash
     roscore
     ```

2.   启动发布节点：

     +   若运行cpp版本使用命令

         ```bash
         rosrun custom_message random_msg_publisher
         ```

     +   若运行py版本使用命令

         ```bash
         rosrun custom_message random_msg_publisher.py
         ```

3.   启动订阅节点：

     +   若运行cpp版本使用命令

         ```bash
         rosrun custom_message random_msg_subscriber
         ```

     +   若运行py版本使用命令

         ```bash
         rosrun custom_message random_msg_subscriber.py
         ```

运行效果如图：

<img src="/img/ROS1基础与常用命令/image-20241102141836960.png" alt="image-20241102141836960" style="zoom:50%;" />

<img src="/img/ROS1基础与常用命令/image-20241102141850785.png" alt="image-20241102141850785" style="zoom:50%;" />

## 5.4 服务通信

服务通信模型中涉及到三个角色：

-   ROS master(管理者)
-   Server(服务端)
-   Client(客户端)

ROS Master 负责保管 Server 和 Client 注册的信息，并匹配话题相同的 Server 与 Client ，帮助 Server 与 Client 建立连接，连接建立后，Client 发送请求信息，Server 返回响应信息。理论模型如下图：

<img src="/img/ROS1基础与常用命令/image-20241102142828094.png" alt="image-20241102142828094" style="zoom:50%;" />

这里实现一个简单的服务通信，客户端发出两个数字请求，服务端返回它们的和。

### 5.4.1 创建功能包

我们创建一个名为 `add_service` 的包，在`src`文件夹下执行命令：

```bash
catkin_create_pkg add_service std_msgs rospy roscpp message_generation
```

### 5.4.2 创建自定义服务消息

1.   在功能包中新建`srv`文件夹，在里面添加`AddTwoInts.srv`文件，内容如下：

     ```
     int64 a
     int64 b
     ---
     int64 sum
     ```

     `---`上方的是请求数据类型，下方的是响应数据类型。这里定义了一个请求包含两个整数 `a` 和 `b`，响应包含它们的和 `sum`。

2.   确保`CMakeLists.txt`被修改成如下：

     ```cmake
     find_package(catkin REQUIRED COMPONENTS
       rospy
       std_msgs
       message_generation
     )
     
     add_service_files(
       FILES
       AddTwoInts.srv
     )
     
     generate_messages(
       DEPENDENCIES
       std_msgs
     )
     ```

3.   确保`package.xml`有如下依赖：

     ```xml
     <build_depend>message_generation</build_depend>
     <exec_depend>message_runtime</exec_depend>
     ```

4.   编译包

### 5.4.3 创建服务端

#### 5.4.3.1 cpp版本的实现

1.   在 `add_service/src` 目录下创建一个名为 `add_service_server.cpp` 的文件，并添加以下代码：

     ```cpp
     #include <ros/ros.h>
     #include <add_service/AddTwoInts.h> // 引入自定义服务消息头文件
     
     // 处理加法请求的回调函数
     bool handle_add_two_ints(add_service::AddTwoInts::Request &req,
                               add_service::AddTwoInts::Response &res) {
         // 计算请求的两个整数之和
         res.sum = req.a + req.b;
         ROS_INFO("Request: a=%ld, b=%ld; Sending back response: sum=%ld", req.a, req.b, res.sum);
         return true; // 返回成功
     }
     
     int main(int argc, char **argv) {
         ros::init(argc, argv, "add_service_server"); // 初始化节点
         ros::NodeHandle n; // 创建节点句柄
     
         // 创建服务，注册到名为 "add_two_ints" 的服务上
         ros::ServiceServer service = n.advertiseService("add_two_ints", handle_add_two_ints);
         ROS_INFO("Ready to add two ints."); // 打印日志信息
         ros::spin(); // 进入循环，等待服务请求
     
         return 0; // 返回成功
     }
     ```

2.   修改 `CMakeLists.txt`，添加如下内容：

     ```cmake
     add_executable(add_service_server src/add_service_server.cpp)
     target_link_libraries(add_service_server ${catkin_LIBRARIES})
     ```

3.   编译

#### 5.4.3.2 py 版本的实现

1.   在 `add_service/src` 目录下创建一个名为 `add_service_server.py` 的文件，并添加以下代码：

     ```python
     import rospy
     from add_service.srv import AddTwoInts, AddTwoIntsResponse # 引入自定义服务消息
     
     # 处理加法请求的回调函数
     def handle_add_two_ints(req):
         result = req.a + req.b # 计算请求的两个整数之和
         rospy.loginfo("Request: a={}, b={}; Sending back response: sum={}".format(req.a, req.b, result))
         return AddTwoIntsResponse(result) # 返回结果
     
     # 服务端初始化
     def add_service_server():
         rospy.init_node('add_service_server') # 初始化节点
         s = rospy.Service('add_two_ints', AddTwoInts, handle_add_two_ints) # 注册服务
         rospy.loginfo("Ready to add two ints.") # 打印日志信息
         rospy.spin() # 进入循环，等待服务请求
     
     if __name__ == "__main__":
         add_service_server() # 启动服务端
     ```

2.   修改 `CMakeLists.txt`，添加如下内容：

     ```cmake
     catkin_install_python(PROGRAMS
     src/add_service_server.py
       DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
     )
     ```

3.   编译

### 5.4.4 创建客户端

#### 5.4.4.1 cpp版本的实现

1.   在 `add_service/src` 目录下创建一个名为 `add_service_client.cpp` 的文件，并添加以下代码：

     ```cpp
     #include <ros/ros.h>
     #include <add_service/AddTwoInts.h> // 引入自定义服务消息头文件
     
     int main(int argc, char **argv) {
         // 检查命令行参数数量
         if (argc != 3) {
             ROS_INFO("Usage: add_service_client <num1> <num2>");
             return 1; // 返回错误
         }
     
         ros::init(argc, argv, "add_service_client"); // 初始化节点
         ros::NodeHandle n; // 创建节点句柄
     
         // 创建服务客户端，连接到 "add_two_ints" 服务
         ros::ServiceClient client = n.serviceClient<add_service::AddTwoInts>("add_two_ints");
         add_service::AddTwoInts srv; // 创建服务请求对象
         srv.request.a = atoll(argv[1]); // 将第一个参数转为整数并赋值
         srv.request.b = atoll(argv[2]); // 将第二个参数转为整数并赋值
     
         // 调用服务并检查是否成功
         if (client.call(srv)) {
             ROS_INFO("Sum: %ld", srv.response.sum); // 打印返回的和
         } else {
             ROS_ERROR("Failed to call service add_two_ints"); // 打印错误信息
             return 1; // 返回错误
         }
     
         return 0; // 返回成功
     }
     ```

2.   修改 `CMakeLists.txt`，添加如下内容：

     ```cmake
     add_executable(add_service_client src/add_service_client.cpp)
     target_link_libraries(add_service_client ${catkin_LIBRARIES})
     ```

3.   编译

#### 5.4.4.2 py版本的实现

1.   在 `add_service/src` 目录下创建一个名为 `add_service_client.py` 的文件，并添加以下代码：

     ```python
     import sys
     import rospy
     from add_service.srv import AddTwoInts # 引入自定义服务消息
     
     # 客户端请求加法服务
     def add_two_ints_client(x, y):
         rospy.wait_for_service('add_two_ints') # 等待服务可用
         try:
             add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoInts) # 创建服务代理
             resp = add_two_ints(x, y) # 调用服务
             return resp.sum # 返回结果
         except rospy.ServiceException as e:
             print("Service call failed: {}".format(e)) # 打印错误信息
     
     if __name__ == "__main__":
         # 检查命令行参数数量
         if len(sys.argv) != 3:
             print("Usage: add_service_client.py [num1] [num2]")
             sys.exit(1) # 返回错误
     
         num1 = int(sys.argv[1]) # 将第一个参数转为整数
         num2 = int(sys.argv[2]) # 将第二个参数转为整数
     
         rospy.init_node('add_service_client') # 初始化节点
         print("Requesting {} + {}".format(num1, num2)) # 打印请求信息
         sum = add_two_ints_client(num1, num2) # 请求服务
         print("Sum: {}".format(sum)) # 打印结果
     ```

2.   修改 `CMakeLists.txt`，添加如下内容：

     ```cmake
     catkin_install_python(PROGRAMS
     src/add_service_client.py
       DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
     )
     ```

3.   编译

### 5.4.5 运行节点

1.   启动 ROS 核心：

     ```bash
     roscore
     ```

2.   启动服务端节点：

     +   若运行cpp版本使用命令

         ```bash
         rosrun add_service add_service_server
         ```

     +   若运行py版本使用命令

         ```bash
         rosrun add_service add_service_server.py
         ```

3.   启动客户端节点：

     +   若运行cpp版本使用命令

         ```bash
         rosrun add_service add_service_client num1 num2
         ```

     +   若运行py版本使用命令

         ```bash
         rosrun add_service add_service_client.py num1 num2
         ```

运行效果如图：

![/img/ROS1基础与常用命令/image-20241102151924299](image-20241102151924299.png)

![/img/ROS1基础与常用命令/image-20241102151943338](image-20241102151943338.png)

## 5.5 参数操作

### 5.5.1 创建功能包

在`src`文件夹中执行如下命令：

```bash
catkin_create_pkg param_example std_msgs rospy roscpp
```

### 5.5.2 cpp实现

1.   在 `param_example/src` 目录下创建一个名为 `param_example_node.cpp` 的文件，并添加以下代码：

     ```cpp
     #include <ros/ros.h>
     
     int main(int argc, char **argv) {
         ros::init(argc, argv, "param_example_node"); // 初始化节点
         ros::NodeHandle n; // 创建节点句柄
     
         // 设置参数
         n.setParam("example_param", 10); // 设置名为 "example_param" 的参数
     
         // 获取参数
         int param_value;
         if (n.getParam("example_param", param_value)) { // 获取参数值
             ROS_INFO("Got parameter: example_param=%d", param_value); // 打印参数值
         } else {
             ROS_WARN("Could not get parameter: example_param"); // 打印警告
         }
     
         // 修改参数
         n.setParam("example_param", 20); // 修改参数值
     
         // 重新获取参数
         if (n.getParam("example_param", param_value)) {
             ROS_INFO("Updated parameter: example_param=%d", param_value); // 打印更新后的参数值
         }
     
         ros::spinOnce(); // 处理回调
         return 0; // 返回成功
     }
     ```

2.   在 `CMakeLists.txt` 文件中添加 C++ 可执行文件的配置：

     ```cmake
     add_executable(param_example_node src/param_example_node.cpp)
     target_link_libraries(param_example_node ${catkin_LIBRARIES})
     ```

3.   编译

### 5.5.3 py实现

1.   在 `param_example/src` 目录下创建一个名为 `param_example_node.py` 的文件，并添加以下代码：

     ```python
     import rospy
     
     if __name__ == "__main__":
         rospy.init_node('param_example_node') # 初始化节点
     
         # 设置参数
         rospy.set_param('example_param', 10) # 设置名为 "example_param" 的参数
     
         # 获取参数
         param_value = rospy.get_param('example_param', None) # 获取参数值
         if param_value is not None:
             rospy.loginfo("Got parameter: example_param={}".format(param_value)) # 打印参数值
         else:
             rospy.logwarn("Could not get parameter: example_param") # 打印警告
     
         # 修改参数
         rospy.set_param('example_param', 20) # 修改参数值
     
         # 重新获取参数
         param_value = rospy.get_param('example_param')
         rospy.loginfo("Updated parameter: example_param={}".format(param_value)) # 打印更新后的参数值
     
         rospy.spin() # 进入循环
     ```

2.   在 `CMakeLists.txt` 文件中如下配置：

     ```cmake
     catkin_install_python(PROGRAMS
       src/param_example_node.py
       DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
     )
     ```

3.   编译

### 5.5.4 运行节点

启动 ROS 核心：

```bash
roscore
```

运行节点：

+   cpp版本

    ```bash
    rosrun param_example param_example_node
    ```

+   py版本

    ```bash
    rosrun param_example param_example_node.py
    ```

运行结果：

![/img/ROS1基础与常用命令/image-20241102154254201](image-20241102154254201.png)

# 6. launch文件的使用

`launch` 文件是一种 XML 格式的文件，用于定义和管理节点的启动过程。通过 `launch` 文件，可以一次性启动多个节点，设置参数，定义节点间的连接（如话题、服务等），并配置其他相关选项。这使得管理复杂的机器人系统变得更加简单和高效。

## 6.1 新建launch文件

在功能包下新建 `launch` 目录, 目录下新建 `xxxx.launch` 文件。一个简单示例如下

```xml
<launch>
    <param name="example_param" value="10"/> <!-- 设置全局参数 -->

    <node pkg="param_example" type="param_example_node" name="param_example_node" output="screen">
        <param name="node_param" value="5"/> <!-- 设置节点特定参数 -->
    </node>
</launch>
```

## 6.2 launch文件的标签和属性

在 ROS 的 `launch` 文件中，有多种属性和标签可用于配置节点的启动、参数设置、依赖管理等，常见的属性和标签如下：

1.   `<launch>`

     根元素：每个 `launch` 文件都以 `<launch>` 标签开始，表示该文件的开始。

2.   `<node>`

     +   `pkg`：节点所属的 ROS 包名称。
     +   `type`：节点的可执行文件名。
     +   `name`：节点的名称（可以与可执行文件名相同，但推荐使用不同的名称以便于识别）。
     +   `output`：节点的输出方式，可以是 `screen`（在终端显示）或 `log`（输出到日志文件）。
     +   `args`：传递给节点的命令行参数。
     +   `respawn`：如果节点崩溃是否自动重启，取值为 `true` 或 `false`。
     +   `respawn_delay`：当 `respawn` 为 `true` 时，重启节点的延迟时间（单位为秒）。
     +   `required`：如果节点是必需的，设置为 `true`，否则设置为 `false`。

     示例：

     ```xml
     <node pkg="my_package" type="my_node" name="my_node_name" output="screen" respawn="true" respawn_delay="2"/>
     ```

     子级标签有：

     -   `env` 环境变量设置
     -   `remap` 重映射节点名称
     -   `rosparam` 参数设置
     -   `param` 参数设置

3.   `<param>`

     设置参数，主要属性如下：

     -   `name`：参数名称。
     -   `value`：参数的值，可以是常量、字符串、布尔值等。
     -   `type`：参数类型，支持 `int`, `double`, `string`, `bool` 等。

     示例：

     ```xml
     <param name="param_name" value="param_value"/>
     ```

4.   `<rosparam>`

     用于加载参数文件，支持 YAML 格式。

     -   `file`：指定要加载的 YAML 文件的路径。
     -   `command`：可以是 `load` 或 `dump`，分别用于加载和导出参数。

     示例：

     ```xml
     <rosparam file="$(find my_package)/config/params.yaml" command="load"/>
     ```

5.   `<include>`

     用于从其他 `launch` 文件中引用节点。

     -   `file`：要包含的 `launch` 文件的路径，可以使用 `$(find package_name)` 来引用包内的文件。

     示例：

     ```xml
     <include file="$(find another_package)/launch/another_launch_file.launch"/>
     ```

6.   `<group>`

     将多个节点或参数分组，可以设置特定的属性。

     -   `name`：分组名称，通常用于命名空间。
     -   `ns`：定义命名空间。

     示例：

     ```xml
     <group ns="my_namespace">
         <node pkg="my_package" type="my_node" name="my_node_name"/>
     </group>
     ```

7.   `<test>`

     用于运行测试节点，主要属性如下：

     -   `pkg`：测试节点所属的 ROS 包名称。
     -   `type`：测试节点的可执行文件名。
     -   `name`：测试节点的名称。

     示例：

     ```xml
     <test pkg="my_package" type="test_node" name="test_node_name"/>
     ```

8.   `<arg>`

     定义命令行参数，主要属性如下：

     -   `name`：参数名称。
     -   `default`：默认值。

     示例：

     ```xml
     <arg name="my_arg" default="default_value"/>
     ```

     使用 `$(arg my_arg)` 可以引用该参数。

9.   `<remap>`

     用于重映射话题名称。

     -   `from`：原始话题名称。
     -   `to`：新话题名称。

     ```xml
     <remap from="/old_topic" to="/new_topic"/>
     ```

## 6.3 调用launch文件

使用命令

```bash
roslaunch 包名 xxx.launch
```

`roslaunch` 命令执行launch文件时，首先会判断是否启动了 `roscore`，如果启动了，则不再启动，否则，会自动调用 `roscore`。

# 7. 常用的ROS命令

## 7.1 ROS信息命令

### 7.1.1 rosnode

节点相关命令

```bash
rosnode ping    测试到节点的连接状态
rosnode list    列出活动节点
rosnode info    打印节点信息
rosnode machine    列出指定设备上节点
rosnode kill    杀死某个节点
rosnode cleanup    清除不可连接的节点
```

### 7.1.2 rostopic

话题相关命令

```bash
rostopic bw     显示主题使用的带宽
rostopic delay  显示带有 header 的主题延迟
rostopic echo   打印消息到屏幕
rostopic find   根据类型查找主题
rostopic hz     显示主题的发布频率
rostopic info   显示主题相关信息
rostopic list   显示所有活动状态下的主题
rostopic pub    将数据发布到主题
rostopic type   打印主题类型
```

### 7.1.3 rosmsg

消息相关命令

```bash
rosmsg show    显示消息描述
rosmsg info    显示消息信息
rosmsg list    列出所有消息
rosmsg md5    显示 md5 加密后的消息
rosmsg package    显示某个功能包下的所有消息
rosmsg packages    列出包含消息的功能包
```

### 7.1.4 rosservice

服务相关命令

```bash
rosservice args 打印服务参数
rosservice call    使用提供的参数调用服务
rosservice find    按照服务类型查找服务
rosservice info    打印有关服务的信息
rosservice list    列出所有活动的服务
rosservice type    打印服务类型
rosservice uri    打印服务的 ROSRPC uri
```

### 7.1.5 rossrv

服务信息相关命令

```bash
rossrv show    显示服务消息详情
rossrv info    显示服务消息相关信息
rossrv list    列出所有服务信息
rossrv md5    显示 md5 加密后的服务消息
rossrv package    显示某个包下所有服务消息
rossrv packages    显示包含服务消息的所有包
```

### 7.1.6 rosparam

参数相关命令

```bash
rosparam set    设置参数
rosparam get    获取参数
rosparam load    从外部文件加载参数
rosparam dump    将参数写出到外部文件
rosparam delete    删除参数
rosparam list    列出所有参数
```

### 7.1.7 rosbag

记录和重放相关命令

```bash
check        确定 bag 在当前系统中是否可播放，或者是否可以迁移
compress     压缩一个或多个包文件
decompress   解压缩一个或多个包文件
decrypt      解密一个或多个包文件
encrypt      加密一个或多个 bag 文件
filter       过滤bag的内容
fix          修复 bag 文件中的消息，以便它可以在当前系统中播放。
info         总结一个或多个文件包的内容。
play         以时间同步的方式播放一个或多个包文件的内容。
record       录制包含指定 topic 内容的 bag 文件。
reindex      重新索引一个或多个 bag 文件。
```

### 7.1.8 rosversion

显示ROS功能包的版本信息

```bash
-h, --help          显示此帮助消息并退出
-s, --skip-newline  跳过尾随换行符
-d, --distro        输出 ROS 发行版名称
-a, --all           显示所有 ROS 软件包名称及其版本
```

## 7.2 ROS shell 命令

`ROS shell`命令又被称为`rosbash`。相关命令如下：

| 命令  | 命令释义                  | 详细说明                  | 参考模板                      |
| ----- | ------------------------- | ------------------------- | ----------------------------- |
| roscd | ros+cd(changes directory) | 移动到指定的ROS功能包目录 | roscd [功能包名称]            |
| rosls | ros+ls(lists files)       | 显示ROS功能包的文件和目录 | rosls [功能包名称]            |
| rosed | ros+ed(editor)            | 编辑ROS功能包的文件       | rosed [功能包名称] [文件名称] |
| roscp | ros+cp(copies files)      | 复制ROS功能包的文件       | —                             |
| rospd | ros+pushd                 | 添加目录至ROS目录索引     | —                             |
| rosd  | ros+directory             | 显示ROS目录索引中的目录   | —                             |

## 7.3 ROS 执行命令

ROS 执行命令管理ROS节点的运行。

| 命令      | 命令释义   | 详细说明                                                                  | 参考模板                              |
| --------- | ---------- | ------------------------------------------------------------------------- | ------------------------------------- |
| roscore   | ros+core   | master（ROS名称服务） + rosout（日志记录） + parameter server（参数管理） | roscore [选项]                        |
| rosrun    | ros+run    | 运行单个节点                                                              | rosrun [功能包名称] [节点名称]        |
| roslaunch | ros+launch | 运行多个节点或设置运行选项                                                | roslaunch [功能包名称] [launch文件名] |
| rosclean  | ros+clean  | 检查或删除ROS日志文件                                                     | rosclean [选项]     

## 7.4 ROS catkin命令

ROS catkin命令ROS的catkin命令用于使用catkin 构建系统来构建功能包。

| 命令                      | 详细说明                                                          | 参考模板                                                         |
| ------------------------- | ----------------------------------------------------------------- | ---------------------------------------------------------------- |
| catkin_create_pkg         | 自动生成功能包                                                    | catkin_create_pkg [功能包名称] [依赖性功能包1] [依赖性功能包2] … |
| catkin_make               | 基于catkin 构建系统的构建                                         | catkin_make --[选项]                                             |
| catkin_eclipse            | 把用catkin 构建系统生成的功能包修改，使得可以在Eclipse 环境中使用 | catkin_eclipse                                                   |
| catkin_prepare_release    | 发布时用到的日志整理和版本标记                                    | catkin_prepare_release                                           |
| catkin_generate_changelog | 发布时生成或更新CHANGELOG.rst文件                                 | catkin_generate_changelog                                        |
| catkin_init_workspace     | 初始化catkin 构建系统的工作目录                                   | catkin_init_workspace                                            |
| catkin_find               | 搜索catkin                                                        | catkin_find [功能包名称]                                         |

## 7.5 ROS功能包命令

ROS 功能包命令用于操作ROS功能包，比如显示功能包信息、安装相关功能包等。

| 命令          | 命令释义           | 详细说明                              | 参考模板                      |
| ------------- | ------------------ | ------------------------------------- | ----------------------------- |
| rospack       | ros+pack(age)      | 显示与ROS功能包相关的信息             | rospack [选项] [功能包名称]   |
| rosinstall    | ros+install        | 安装ROS附加功能包                     | ——                            |
| rosdep        | ros+dep(endencies) | 安装该功能包的依赖性文件              | rosdep [选项]                 |
| roslocate     | ros+locate         | 与ROS功能包信息有关的命令             | roslocate [选项] [功能包名称] |
| roscreate-pkg | ros+create-pkg     | 自动生成ROS功能包                     | （用于旧的rosbuild系统）      | —— |
| rosmake       | ros+make           | 构建ROS功能包（用于旧的rosbuild系统） | ——                            |

# 8. 参考资料

+   [ROS/Tutorials - ROS Wiki](https://wiki.ros.org/ROS/Tutorials)
+   [Introduction · Autolabor-ROS机器人入门课程《ROS理论与实践》零基础教程](http://www.autolabor.com.cn/book/ROSTutorials/index.html)
+   [《学习篇》学会这18个常用ROS命令集合就能入门ROS了_ros常用命令-CSDN博客](https://blog.csdn.net/qq_31136513/article/details/106272169)
