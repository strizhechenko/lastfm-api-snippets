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
	common_artists $@ | wc -l
}

main() {
	for user in $1 $2; do
		./get_user_artists_list.sh $user
		xml2text $user
	done

	common_artists $@
	common_artists_count $@
}

main $@
