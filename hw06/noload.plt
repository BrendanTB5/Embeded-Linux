# This code is from Julia Cartwright julia@kernel.org

set terminal png medium size 800,600
set output "notbusy.png"
set datafile commentschars "#"

set logscale y

# trim some of the distortion from the bottom of the plot
set yrang [0.85:*]

plot "noloadnort.hist" using 1:2 with histeps title "NON-RT",    \
     "noloadrt.hist" using 1:2 with histeps title "PREEMPT_RT"
