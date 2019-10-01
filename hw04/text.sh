# Here's how to use imagemagick to display text
# Make a blank image
SIZE=320x240
TMP_FILE=/tmp/frame.png

# From: http://www.imagemagick.org/Usage/text/
convert -background lightblue -fill red -font Calibri -pointsize 24 \
      -size $SIZE \
      label:'My name is Mark Procter' \
      -draw "text 0,220 'ECE434 Homework 4'" \
      $TMP_FILE

sudo fbi -noverbose -T 1 $TMP_FILE

# convert -list font 
