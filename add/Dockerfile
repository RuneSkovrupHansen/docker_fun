FROM ubuntu
ENV dir="files"

# Add all .txt files
ADD "$dir"/*.txt "$dir"/

# Print the file path and content of every file in $dir, note that $dir/*
# cannot be surrounded with double quotation marks, since it prevents globbing
CMD /bin/bash -c 'for f in $dir/*; do c=$(cat $f); echo "$f: $c"; echo "$f"; done;'

# Output
#files/txt1.txt: txt1 content
#files/txt2.txt: txt2 content
#files/txt3.txt: txt3 content
