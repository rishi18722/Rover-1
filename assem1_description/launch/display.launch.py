import os
from ament_index_python.packages import get_package_share_directory

from launch_ros.actions import Node
from launch import LaunchDescription
from launch_ros.parameter_descriptions import ParameterValue
from launch.substitutions import Command
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

import xacro


def generate_launch_description():
    # Define package name
    package_name = "assem1_description"
    # process urdf file
    pkg_path = os.path.join(get_package_share_directory(package_name))
    xacro_file = os.path.join(pkg_path, "urdf", "assem1.urdf.xacro")
    robot_description = xacro.process_file(xacro_file)
    # robot_state_publisher_node
    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[{"robot_description": robot_description.toxml()}],
    )
    # joint_state_publisher_gui_node
    joint_state_publisher_gui_node = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui",
    )
    # Launch them all!!
    return LaunchDescription(
        [robot_state_publisher_node, joint_state_publisher_gui_node]
    )
