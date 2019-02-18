#!/bin/bash
IFS=$'\n'
new_dir=$1
if [ -d "$new_dir" ]; 
then
  	i=1
	while [ -d "$new_dir$j" ]
  	do
    		i=$(( $i+1 ))
  	done
	mv $new_dir $new_dir$i > /dev/null
fi
mkdir $new_dir > /dev/null
archive_name=$2
for (( i=3; i<=$#; i++ ))
do
	all_files=$(find -name "*${!i}" 2> /dev/null)
	cnt=1
	# echo ${!i}
	for item in $all_files
	do
		file=${item##*/}
		name0=${item#*/}
		# echo "$name0"
		name1=${name0//".."/"_"}
		# echo "$name1"
		new_name=${name1//"/"/".."}
		cp $item $new_dir > /dev/null
		cd $new_dir > /dev/null
		mv $file $new_name > /dev/null
		# echo "$cnt $new_name"
		cnt=$(( $cnt + 1 ))
		cd > /dev/null
	done
done
tar -cvzf $archive_name.tar $new_dir > /dev/null
echo "done"