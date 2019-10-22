# This code is from Julia Cartwright julia@kernel.org

set terminal png medium size 800,600
set output "busy.png"
set datafile commentschars "#"

set logscale y

# trim some of the distortion from the bottom of the plot
set yrang [0.85:*]

plot "loadnort.hist" using 1:2 with histeps title "NON-RT",    \
     "loadrt.hist" using 1:2 with histeps title "PREEMPT_RT"
