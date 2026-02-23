import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    user_home = os.environ['HOME']
    data_path = os.path.join(user_home, 'stonefish_ws/src/stonefish/Tests/Data')

    scenario_name = 'girona500auv_full.scn'
    
    scenario_file = os.path.join(data_path, scenario_name)

    pkg_stonefish_ros2 = FindPackageShare('stonefish_ros2')

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                PathJoinSubstitution([pkg_stonefish_ros2, 'launch', 'stonefish_simulator.launch.py'])
            ]),
            
            launch_arguments={
                'simulation_data': data_path,
                'scenario_desc': scenario_file,
                'simulation_rate': '20.0',
                'window_res_x': '800',
                'window_res_y': '600',
                'rendering_quality': 'high',
            }.items()
        )
    ])
