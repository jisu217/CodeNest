#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 21:34:35 2024

@author: jisu
"""

# Quiz11_202404002 강지수
# ToDoList
# TaskManager.py

# 학번/이름 출력문
print("*****************")
print("202404002/강지수")
print("*****************")

# Task 모듈 가져오기
import Task

for i in range(3):
    t = input("\n오늘 할 일 입력:")
    Task.addTask(t)  # addTask 호출

Task.showTask()  # showTask 호출
