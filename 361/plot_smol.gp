#set input ARG1
set output ARG2

set datafile separator ','  # Set comma as the separator
set title "1000 hz, 100 microsec"    # Title of the graph
set xlabel "Frequency, kHz"           # Label for the X-axis
set ylabel "Amplitude, V"          # Label for the Y-axis
set yrange [0:5]
set xrange [0:5]
#set title "Amplitude vs frequency"
set nokey

# Optionally set the output format (e.g., PNG)
set terminal png

# Plotting the data from the CSV file
plot ARG1 using 1:2 with lines title 'Value vs Time'
