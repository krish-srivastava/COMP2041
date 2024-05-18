#!/bin/dash

TEMP_DIR=$(mktemp -d)
cp pigs-* "$TEMP_DIR"
cd "$TEMP_DIR" || exit
trap 'rm -rf "$TEMP_DIR"' EXIT

touch a

expected_output=$(exec 2041 pigs-add a) >/dev/null
current_output=$(./pigs-add a) >/dev/null

if [ "$expected_output"="$current_output" ]; then
    echo "Test passed"
else 
    echo "Test failed"
    exit
fi