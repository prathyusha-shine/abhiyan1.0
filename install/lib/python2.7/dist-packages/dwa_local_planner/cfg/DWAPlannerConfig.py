## *********************************************************
## 
## File autogenerated for the dwa_local_planner package 
## by the dynamic_reconfigure package.
## Please do not edit.
## 
## ********************************************************/

##**********************************************************
## Software License Agreement (BSD License)
##
##  Copyright (c) 2008, Willow Garage, Inc.
##  All rights reserved.
##
##  Redistribution and use in source and binary forms, with or without
##  modification, are permitted provided that the following conditions
##  are met:
##
##   * Redistributions of source code must retain the above copyright
##     notice, this list of conditions and the following disclaimer.
##   * Redistributions in binary form must reproduce the above
##     copyright notice, this list of conditions and the following
##     disclaimer in the documentation and/or other materials provided
##     with the distribution.
##   * Neither the name of the Willow Garage nor the names of its
##     contributors may be used to endorse or promote products derived
##     from this software without specific prior written permission.
##
##  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
##  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
##  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
##  FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
##  COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
##  INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
##  BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
##  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
##  CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
##  LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
##  ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
##  POSSIBILITY OF SUCH DAMAGE.
##**********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'upper': 'DEFAULT', 'lower': 'groups', 'srcline': 231, 'name': 'Default', 'parent': 0, 'srcfile': '/opt/ros/hydro/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT', 'field': 'default', 'state': True, 'parentclass': '', 'groups': [], 'parameters': [{'srcline': 260, 'description': 'The absolute value of the maximum translational velocity for the robot in m/s', 'max': 'std::numeric_limits<double>::infinity()', 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/hydro/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'max_trans_vel', 'edit_method': '', 'default': 0.55, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 260, 'description': 'The absolute value of the minimum translational velocity for the robot in m/s', 'max': 'std::numeric_limits<double>::infinity()', 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/hydro/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'min_trans_vel', 'edit_method': '', 'default': 0.1, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 260, 'description': 'The maximum x velocity for the robot in m/s', 'max': 'std::numeric_limits<double>::infinity()', 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/hydro/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'max_vel_x', 'edit_method': '', 'default': 0.55, 'level': 0, 'min': '-std::numeric_limits<double>::infinity()', 'type': 'double'}, {'srcline': 260, 'description': 'The minimum x velocity for the robot in m/s', 'max': 'std::numeric_limits<double>::infinity()', 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/hydro/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'min_vel_x', 'edit_method': '', 'default': 0.0, 'level': 0, 'min': '-std::numeric_limits<double>::infinity()', 'type': 'double'}, {'srcline': 260, 'description': 'The maximum y velocity for the robot in m/s', 'max': 'std::numeric_limits<double>::infinity()', 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/hydro/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'max_vel_y', 'edit_method': '', 'default': 0.1, 'level': 0, 'min': '-std::numeric_limits<double>::infinity()', 'type': 'double'}, {'srcline': 260, 'description': 'The minimum y velocity for the robot in m/s', 'max': 'std::numeric_limits<double>::infinity()', 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/hydro/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'min_vel_y', 'edit_method': '', 'default': -0.1, 'level': 0, 'min': '-std::numeric_limits<double>::infinity()', 'type': 'double'}, {'srcline': 260, 'description': 'The absolute value of the maximum rotational velocity for the robot in rad/s', 'max': 'std::numeric_limits<double>::infinity()', 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/hydro/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'max_rot_vel', 'edit_method': '', 'default': 1.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 260, 'description': 'The absolute value of the minimum rotational velocity for the robot in rad/s', 'max': 'std::numeric_limits<double>::infinity()', 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/hydro/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'min_rot_vel', 'edit_method': '', 'default': 0.4, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 260, 'description': 'The acceleration limit of the robot in the x direction', 'max': 20.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/hydro/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'acc_lim_x', 'edit_method': '', 'default': 2.5, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 260, 'description': 'The acceleration limit of the robot in the y direction', 'max': 20.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/hydro/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'acc_lim_y', 'edit_method': '', 'default': 2.5, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 260, 'description': 'The acceleration limit of the robot in the theta direction', 'max': 20.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/hydro/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'acc_lim_theta', 'edit_method': '', 'default': 3.2, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 260, 'description': 'The absolute value of the maximum translational acceleration for the robot in m/s^2', 'max': 'std::numeric_limits<double>::infinity()', 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/hydro/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'acc_limit_trans', 'edit_method': '', 'default': 0.1, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 260, 'description': 'Start following closest point of global plan, not first point (if different).', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/opt/ros/hydro/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'prune_plan', 'edit_method': '', 'default': False, 'level': 0, 'min': False, 'type': 'bool'}, {'srcline': 260, 'description': 'Within what maximum distance we consider the robot to be in goal', 'max': 'std::numeric_limits<double>::infinity()', 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/hydro/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'xy_goal_tolerance', 'edit_method': '', 'default': 0.1, 'level': 0, 'min': '-std::numeric_limits<double>::infinity()', 'type': 'double'}, {'srcline': 260, 'description': 'Within what maximum angle difference we consider the robot to face goal direction', 'max': 'std::numeric_limits<double>::infinity()', 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/hydro/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'yaw_goal_tolerance', 'edit_method': '', 'default': 0.1, 'level': 0, 'min': '-std::numeric_limits<double>::infinity()', 'type': 'double'}, {'srcline': 260, 'description': 'Below what maximum velocity we consider the robot to be stopped in translation', 'max': 'std::numeric_limits<double>::infinity()', 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/hydro/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'trans_stopped_vel', 'edit_method': '', 'default': 0.1, 'level': 0, 'min': '-std::numeric_limits<double>::infinity()', 'type': 'double'}, {'srcline': 260, 'description': 'Below what maximum rotation velocity we consider the robot to be stopped in rotation', 'max': 'std::numeric_limits<double>::infinity()', 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/hydro/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'rot_stopped_vel', 'edit_method': '', 'default': 0.1, 'level': 0, 'min': '-std::numeric_limits<double>::infinity()', 'type': 'double'}, {'srcline': 260, 'description': 'The amount of time to roll trajectories out for in seconds', 'max': 'std::numeric_limits<double>::infinity()', 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/hydro/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'sim_time', 'edit_method': '', 'default': 1.7, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 260, 'description': 'The granularity with which to check for collisions along each trajectory in meters', 'max': 'std::numeric_limits<double>::infinity()', 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/hydro/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'sim_granularity', 'edit_method': '', 'default': 0.025, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 260, 'description': 'The granularity with which to check for collisions for rotations in radians', 'max': 'std::numeric_limits<double>::infinity()', 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/hydro/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'angular_sim_granularity', 'edit_method': '', 'default': 0.1, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 260, 'description': 'The weight for the path distance part of the cost function', 'max': 'std::numeric_limits<double>::infinity()', 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/hydro/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'path_distance_bias', 'edit_method': '', 'default': 32.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 260, 'description': 'The weight for the goal distance part of the cost function', 'max': 'std::numeric_limits<double>::infinity()', 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/hydro/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'goal_distance_bias', 'edit_method': '', 'default': 24.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 260, 'description': 'The weight for the obstacle distance part of the cost function', 'max': 'std::numeric_limits<double>::infinity()', 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/hydro/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'occdist_scale', 'edit_method': '', 'default': 0.01, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 260, 'description': 'The amount of time that the robot must stop before a collision in order for a trajectory to be considered valid in seconds', 'max': 'std::numeric_limits<double>::infinity()', 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/hydro/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'stop_time_buffer', 'edit_method': '', 'default': 0.2, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 260, 'description': 'The distance the robot must travel before oscillation flags are reset, in meters', 'max': 'std::numeric_limits<double>::infinity()', 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/hydro/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'oscillation_reset_dist', 'edit_method': '', 'default': 0.05, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 260, 'description': 'The angle the robot must turn before oscillation flags are reset, in radians', 'max': 'std::numeric_limits<double>::infinity()', 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/hydro/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'oscillation_reset_angle', 'edit_method': '', 'default': 0.2, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 260, 'description': 'The distance from the center point of the robot to place an additional scoring point, in meters', 'max': 'std::numeric_limits<double>::infinity()', 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/hydro/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'forward_point_distance', 'edit_method': '', 'default': 0.325, 'level': 0, 'min': '-std::numeric_limits<double>::infinity()', 'type': 'double'}, {'srcline': 260, 'description': "The absolute value of the velocity at which to start scaling the robot's footprint, in m/s", 'max': 'std::numeric_limits<double>::infinity()', 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/hydro/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'scaling_speed', 'edit_method': '', 'default': 0.25, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 260, 'description': "The maximum factor to scale the robot's footprint by", 'max': 'std::numeric_limits<double>::infinity()', 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/hydro/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'max_scaling_factor', 'edit_method': '', 'default': 0.2, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 260, 'description': 'The number of samples to use when exploring the x velocity space', 'max': 2147483647, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/hydro/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'vx_samples', 'edit_method': '', 'default': 3, 'level': 0, 'min': 1, 'type': 'int'}, {'srcline': 260, 'description': 'The number of samples to use when exploring the y velocity space', 'max': 2147483647, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/hydro/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'vy_samples', 'edit_method': '', 'default': 10, 'level': 0, 'min': 1, 'type': 'int'}, {'srcline': 260, 'description': 'The number of samples to use when exploring the theta velocity space', 'max': 2147483647, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/hydro/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'vth_samples', 'edit_method': '', 'default': 20, 'level': 0, 'min': 1, 'type': 'int'}, {'srcline': 260, 'description': 'Use dynamic window approach to constrain sampling velocities to small window.', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/opt/ros/hydro/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'use_dwa', 'edit_method': '', 'default': True, 'level': 0, 'min': False, 'type': 'bool'}, {'srcline': 260, 'description': 'Restore to the original configuration.', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/opt/ros/hydro/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'restore_defaults', 'edit_method': '', 'default': False, 'level': 0, 'min': False, 'type': 'bool'}], 'type': '', 'id': 0}

min = {}
max = {}
defaults = {}
level = {}
type = {}
all_level = 0

#def extract_params(config):
#    params = []
#    params.extend(config['parameters'])    
#    for group in config['groups']:
#        params.extend(extract_params(group))
#    return params

for param in extract_params(config_description):
    min[param['name']] = param['min']
    max[param['name']] = param['max']
    defaults[param['name']] = param['default']
    level[param['name']] = param['level']
    type[param['name']] = param['type']
    all_level = all_level | param['level']
