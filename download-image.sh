sed 's/.*src="\([^"]*\).*/\1/' satu.txt > sed-img.txt
while read line; do
	if [[ $line != *http* ]]
		then
		wget download "http://www.itb.ac.id$line"
	else 
		wget download "$line"
	fi;
done < sed-img.txt


