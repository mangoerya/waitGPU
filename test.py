import waitGPU

waitGPU.wait(available_memory=9000)
waitGPU.wait(utilization=0.5)
waitGPU.wait(memory_ratio=0.5)