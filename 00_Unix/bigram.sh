sed 's/[^a-zA-Z]\+/\n/g' | grep -v '^$' > $$words
tail -n +2 $$words > $$nextwords |
sort | uniq -c

#remove the temporary files

rm $$words $$nextwords
