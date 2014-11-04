#! /bin/sh

if [ $# -ne 2 ];
then
	echo "useage: $0 export_html_file sharelinks_file"
	exit 1
fi

HTML_FILE=$1
LINKS_FILE=$2
HEADER=header.txt
RESFILE=evernote.txt

function convert()
{
	grep "h1" $HTML_FILE | sed -e 's/<h1>\(.*\)<\/h1>/\1/' > $HEADER 
	paste -d "|" $LINKS_FILE $HEADER > $RESFILE

	#sed -i -e 's/^/* [[/' $RESFILE
	#sed -i -e 's/$/]]/' $RESFILE
	sed -i "s/.*/* [[&]]/" $RESFILE
	vim -c ":%s///g" -c wq $RESFILE
}

function clean()
{
	rm -f $HEADER
}

convert
clean

