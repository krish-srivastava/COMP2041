#!/bin/dash
TEMP_DIR=$(mktemp -d)
cp pigs-* "$TEMP_DIR"
cd "$TEMP_DIR" || exit
trap 'rm -rf "$TEMP_DIR"' EXIT

touch b c d
(exec 2041 pigs-init) >/dev/null
(exec 2041 pigs-add b c d) >/dev/null
(exec 2041 pigs-commit -m "First Message") >/dev/null

expected_output=$(exec 2041 pigs-show :a) >/dev/null
current_output=$(./pigs-show :a) >/dev/null

if [ "$expected_output" = "$current_output" ]; then
    echo "Test passed"
else 
    echo "Test failed"
    exit
fi