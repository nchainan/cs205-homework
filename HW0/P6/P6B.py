import multiprocessing as mp
import time
import matplotlib.pyplot as plt

# Sleep for t seconds
def burnTime(t):
    time.sleep(t)
    return t

# Main
if __name__ == '__main__':
    N = 16  # The number of jobs
    P = 4   # The number of processes

    # A thread pool of P processes
    pool = mp.Pool(P)

    # Use a variety of wait times
    ratio = []
    wait_time = [1e-6,1e-5,1e-4,1e-3,1e-2,1e-1,1]

    for t in wait_time:
        # Compute jobs serially and in parallel
        # Use time.time() to compute the elapsed time for each
        a=time.time()
        for x in xrange(0,N):
            burnTime(t)
        b=time.time()
        serialTime = b-a

        time_vec = [t for x in xrange(0,N)]
        print time_vec

        c = time.time()
        pool.map(burnTime, time_vec)
        d = time.time()
        parallelTime = d-c
        # Compute the ratio of these times
        ratio.append(serialTime/parallelTime)

    # Plot the results
    plt.plot(wait_time, ratio, '-ob')
    plt.xscale('log')
    plt.xlabel('Wait Time (sec)')
    plt.ylabel('Serial Time (sec) / Parallel Time (sec)')
    plt.title('Speedup versus function time')
    plt.show()
