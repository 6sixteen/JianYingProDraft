@echo off
(   echo H:
    echo cd H:\PROJECT\JianYingProDraft\test
    echo conda activate Moody_Blues
) > temp_commands.bat
cmd /k temp_commands.bat
del temp_commands.bat
