#!/bin/dash

lines=wget -qO - https://legacy.handbook.unsw.edu.au/assets/json/search/2005data.json

sed -n "/code/p" < lines
