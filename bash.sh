#!/bin/bash

function about_your_PC {
    mypc=`hostname`
    myos=`uname -a`
    echo "Hostname of your computer:"
    echo $mypc
    echo "OS:"
    echo $myos
}

function hashing_data_in_a_file() {
    if [ -f $1 ]
    then
        while IFS= read -r line 
        do  
            echo "$line" | sha256sum  >> hash.txt 
        done < $1 
    else
        echo "----------------------------------------------------------------"
        echo "ERROR: No such file exists."
    fi
}

function copy_group_files_to_a_new_directory() { 
    if [ -f *$1* ]
    then
    mkdir $2 
    echo $(cp *$1* $2)
    else
        echo "----------------------------------------------------------------"
        echo "ERROR: No such file exists."
    fi 
}

echo "Welcome to Multifunctional Assistant for the work of the System Administrator."
func_num=100
while [[ $func_num -gt 0 ]]
do
echo "----------------------------------------------------------------"
echo "Functions: "
echo "1. About your PC"
echo "2. Hashing data in a file"
echo "3. Copying a group of files to a new directory"
echo "0. Exit"
echo -n "Please, choose the number of the special function: "
read func_num

if [[ $func_num == 1 ]]
then
    echo "----------------------------------------------------------------"
    echo "About your PC."
    about_your_PC
elif [[ $func_num == 2 ]]
then 
    echo "----------------------------------------------------------------"
    echo "Hashing data in a file."
    echo "Please, write argument."
    echo -n "The name of the file in which to hash the data: "
    read file_name
    hashing_data_in_a_file $file_name
elif [[ $func_num == 3 ]]
then 
    echo "----------------------------------------------------------------"
    echo "Copying a group of files to a new directory."
    echo "Please, write argument."
    echo -n "The name of the group of files to be copied: "
    read group_name
    echo -n "The name of the directory where the files will be copied to: "
    read directory_name
    copy_group_files_to_a_new_directory $group_name $directory_name
elif [[ $func_num == 0 ]]
then
    echo "----------------------------------------------------------------"
    echo "Exit"
    echo "It was nice to work with you. See you soon."
    exit
fi
done
