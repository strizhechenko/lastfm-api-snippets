#!/bin/bash

. config

wget -q "$base_url/?method=library.getartists&api_key=$api_key&user=$1&limit=0" -O $1.xml
