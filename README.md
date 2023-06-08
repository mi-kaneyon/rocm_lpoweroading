# rocm_lpoweroading
It is simple ROCm+pytorch power loading script.
- If it is 1st time use, Resnet-50 model will download.
## My test environment.
- Ubuntu 22.04 + Pytorch 2.0.1(ROCm) 

## support information 
https://github.com/RadeonOpenCompute/ROCm/issues/1698
This thread may useful for you.

```

export HSA_OVERRIDE_GFX_VERSION=10.3.0

```


## command instruction 

```
 python rocmbench.py --wattage 100 --vram MAX --duration 5

```
- argument is wattage, vram, loading duration 5min-24H
- You can see almost real time power usage(But too high loading information is delay )

```

|███████████████████████████████████████████-------| 86.7% Complete

======================= ROCm System Management Interface =======================
================================= Concise Info =================================
GPU  Temp (DieEdge)  AvgPwr  SCLK    MCLK   Fan  Perf  PwrCap  VRAM%  GPU%  
0    41.0c           7.0W    500Mhz  96Mhz  0%   auto  194.0W   93%   0%    
================================================================================
============================= End of ROCm SMI Log ==============================


|████████████████████████████████████████████████--| 96.9% Complete

======================= ROCm System Management Interface =======================
================================= Concise Info =================================
GPU  Temp (DieEdge)  AvgPwr  SCLK     MCLK     Fan     Perf  PwrCap  VRAM%  GPU%  
0    47.0c           34.0W   2665Mhz  1000Mhz  20.78%  auto  194.0W   93%   79%   
================================================================================
============================= End of ROCm SMI Log ==============================


```
