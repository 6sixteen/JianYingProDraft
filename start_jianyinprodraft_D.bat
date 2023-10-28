@echo off
(   echo D:
    echo cd D:\PersonalProjects\JianYingProDraft\
    echo conda activate MoodyBlues
) > temp_commands.bat
cmd /k temp_commands.bat
del temp_commands.bat
