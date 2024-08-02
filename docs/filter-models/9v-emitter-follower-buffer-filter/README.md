# 9V Emitter Follower Buffer

This circuit provides stability and noise immunity for the VCO supply.

Here you can see the benefit of the circuit vs. a direct supply connection from the 9V LDO to the VCO VCC pin.

![image](9v-emitter-follower-buffer-filter-en.png)

Without a buffer filter, the following step response would be expected.

![image](regulator-to-vco-no-buffer-filter-en.png)

The impact of various buffer filter capacitor values are modeled here.

![image](9v-emitter-follower-buffer-filter-sizes-en.png)
