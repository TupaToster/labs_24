rmdir temp_pics
mkdir temp_pics
for file in "$1"/*.csv do
gnuplot -c plot_smol.gp $file temp_pics/$(file:.csv=.png)
done