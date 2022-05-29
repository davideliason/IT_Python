#!/bin/bash

echo The name of the bash script: $0
echo
echo First Arg: $1
echo
echo 2nd Arg: $2
echo
echo The number of passed arguments: $#
echo
echo PID of current: $$
echo
mv $1 new_command_line_arg.txt
echo Finished
