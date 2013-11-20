#!/bin/bash

set -eu

xml2text() {
	python parser.py $1.xml | sort -u > $1.txt
}

common_artists() {
	echo "Общие артисты" >&2
	diff -U -1 $1.txt $2.txt | grep '^ '
}

common_artists_count() {
	echo "Количество общих артистов." >&2
	common_artists $1 $2 | wc -l
}

main() {
	./get_user_artists_list.sh $1
	./get_user_artists_list.sh $2

	xml2text $1
	xml2text $2

	common_artists_count $2
	common_artists $@
}

main $@
