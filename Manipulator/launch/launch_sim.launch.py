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
    package_name = "arm2"

    # process urdf file
    pkg_path = os.path.join(get_package_share_directory(package_name))
    xacro_file = os.path.join(pkg_path, "description", "assem2.urdf.xacro")
    robot_description = xacro.process_file(xacro_file)
    rviz_config_path = os.path.join(pkg_path, "rviz", "urdf_config.rviz")

    # robot_state_publisher_node
    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[{"robot_description": robot_description.toxml()}],
    )

    # rviz node
    rviz2_node = Node(
        package="rviz2", executable="rviz2", arguments=["-d", rviz_config_path]
    )

    # gazebo_node
    gazebo_node = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [
                os.path.join(
                    get_package_share_directory("gazebo_ros"),
                    "launch",
                    "gazebo.launch.py",
                )
            ]
        )
    )

    # spawn_node
    spawn_node = Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        arguments=["-topic", "robot_description", "-entity", "arm2"],
        output="screen",
    )

    # Launch them all!!
    return LaunchDescription(
        [robot_state_publisher_node, rviz2_node, gazebo_node, spawn_node]
    )
