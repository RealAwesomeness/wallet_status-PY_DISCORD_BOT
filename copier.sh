#!/bin/bash
count=0
countdos=0
options=[]
file="config.txt"

for line in $(<"config.txt")
do
	options[$count]=$line
	count=$count+1
done

while [ $countdos != $count ]
do
	option="${options[$countdos]}"
	option=${option//$'\n'/}
	originaloption=".$option"
	option="$option.log"
	originaldirectory=$(pwd)
	filedirectory=$originaldirectory"/"$option
	cd ~
	cd $originaloption
	cp "debug.log" $filedirectory
	cd ~
	cd $originaldirectory
	countdos=$countdos+1
done
	
