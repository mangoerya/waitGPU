import waitGPU

waitGPU.wait(available_memory=9000)
waitGPU.wait(utilization=50)
waitGPU.wait(memory_ratio=0.5)
waitGPU.wait(nproc=0)
waitGPU.wait(gpu_ids=[1,2], utilization=50)
waitGPU.wait(gpu_ids=[1,2], utilization=50, ngpu=2)