#!/bin/dash
TEMP_DIR=$(mktemp -d)
cp pigs-* "$TEMP_DIR"
cd "$TEMP_DIR" || exit
trap 'rm -rf "$TEMP_DIR"' EXIT

mkdir Hello_World
(exec 2041 pigs-init) >/dev/null

expected_output=$(exec 2041 pigs-add Hello_World) >/dev/null
current_output=$(./pigs-add Hello_World) >/dev/null

if [ "$expected_output" = "$current_output" ]; then
    echo "Test passed"
else 
    echo "Test failed"
    exit
fi