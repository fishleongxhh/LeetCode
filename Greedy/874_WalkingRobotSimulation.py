# -*-coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode874: Walking Robot Simulation问题

turn_direction = {
    'N':{-2:'W',-1:'E'},
    'W':{-2:'S',-1:'N'},
    'S':{-2:'E',-1:'W'},
    'E':{-2:'N',-1:'S'}}

def check_obstacle(robot, step, obstacles):
    

def robotSim(commands, obstacles):
    obstacles = set(obstacles)
    robot = {'loc':[0,0], 'direction':'N'}

