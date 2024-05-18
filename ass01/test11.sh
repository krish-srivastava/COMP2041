#!/bin/dash
TEMP_DIR=$(mktemp -d)
cp pigs-* "$TEMP_DIR"
cd "$TEMP_DIR" || exit
trap 'rm -rf "$TEMP_DIR"' EXIT

touch b c
(exec 2041 pigs-init) >/dev/null
(exec 2041 pigs-add b) >/dev/null
(exec 2041 pigs-commit -m "First Message") >/dev/null
(exec 2041 pigs-add c) >/dev/null
(exec 2041 pigs-commit -m "Second Message") >/dev/null

expected_output=$(exec 2041 pigs-show 2:d) >/dev/null
current_output=$(./pigs-show 2:d) >/dev/null

if [ "$expected_output" = "$current_output" ]; then
    echo "Test passed"
else 
    echo "Test failed"
    exit
fi