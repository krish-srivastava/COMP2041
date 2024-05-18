#!/bin/bash

for arg in "$@"
do
    file=$(realpath "$arg")
    base_name=$(basename "$file")

    head=$(head -n1 "$file")
    exclamation="#!"
    perl="perl"
    python="python"
    shell="shell"
    perl_extension="pl"
    python_extension="py"
    sh_extension="sh"

    if [ -e "$arg" ]
    then
        echo "# $arg already exists"
    elif ( echo "$base_name" | grep -Eq "\.[a-z]+$" )
    then
        echo "$base_name already has an extension"
    elif !( echo "$head" | grep -Eq "^\#\!")
    then
        echo "# $arg does not have a $exclamation line"
    elif !( echo "$head" | grep -Eq "perl|$python|$sh" )
    then
        echo "# $arg has no extension for $exclamation line"
    else
        if echo "$head" | grep -Eq "$python"
        then
            echo "mv $base_name.$python_extension"
        elif echo "$head" | grep -Eq "$perl"
        then
            echo "mv $base_name.$perl_extension"
        else
            echo "mv $base_name.$sh_extension"
        fi
    fi
done