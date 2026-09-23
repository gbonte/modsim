import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Constants
BUSY = 1
IDLE = 0

STATE = {}

def initialize():
    global STATE
    STATE.update({
        "next_event_type": None,
        "num_events": 2,
        "num_in_q": 0,
        "num_in_s": 0,
        "server_status": IDLE,
        "sim_time": 0.0,
        "time_arrival": [],
        "time_next_event": np.zeros(2),
        "time_last_event": 0.0,
        "nums_in_q": [],
        "nums_in_s": [],
        "delays": [],
        "queue": [],
        "services": [],
        "arrivals": [],
        "departures": [],
        "inter_events": [],
        "server_s": [],
        "Q_LIMIT": 100,
        "warmup_frac": 0.2,  # default warm-up fraction
    })
    # First arrival scheduled using mean_interarrival set before initialize()
    STATE["time_next_event"][0] = STATE["sim_time"] + np.random.exponential(STATE["mean_interarrival"])
    STATE["time_next_event"][1] = math.inf

def timing():
    t_next = STATE["time_next_event"]
    min_time_next_event = math.inf
    next_event_type = 0
    for i in range(STATE["num_events"]):
        if t_next[i] < min_time_next_event:
            min_time_next_event = t_next[i]
            next_event_type = i + 1  # 1: arrival, 2: departure
    if next_event_type == 0:
        raise RuntimeError(f"Event list empty at time {STATE['sim_time']}")
    STATE["next_event_type"] = next_event_type
    STATE["sim_time"] = min_time_next_event

def update_time_avg_stats():
    time_since_last_event = STATE["sim_time"] - STATE["time_last_event"]
    STATE["time_last_event"] = STATE["sim_time"]

    if STATE["next_event_type"] == 1:
        STATE["arrivals"].append(STATE["sim_time"])
    elif STATE["next_event_type"] == 2:
        STATE["departures"].append(STATE["sim_time"])

    STATE["nums_in_s"].append(STATE["num_in_s"])
    STATE["nums_in_q"].append(STATE["num_in_q"])
    STATE["inter_events"].append(time_since_last_event)
    STATE["server_s"].append(STATE["server_status"])

def arrive():
    # Schedule next arrival
    STATE["time_next_event"][0] = STATE["sim_time"] + np.random.exponential(STATE["mean_interarrival"])

    # Increment number in system
    STATE["num_in_s"] += 1

    if STATE["server_status"] == BUSY:
        # Join queue
        STATE["num_in_q"] += 1
        if STATE["num_in_q"] > STATE["Q_LIMIT"]:
            raise RuntimeError(f"Queue overflow at time {STATE['sim_time']}")
        STATE["time_arrival"].append(STATE["sim_time"])
    else:
        # Immediate service: delay 0
        STATE["delays"].append(0.0)
        STATE["server_status"] = BUSY
        service = np.random.exponential(STATE["mean_service"])
        STATE["time_next_event"][1] = STATE["sim_time"] + service
        STATE["services"].append(service)

def depart():
    # One customer leaves system
    STATE["num_in_s"] -= 1

    if STATE["num_in_q"] == 0:
        # No one waiting; server idle
        STATE["server_status"] = IDLE
        STATE["time_next_event"][1] = math.inf
    else:
        # Start service for head of queue
        STATE["num_in_q"] -= 1
        delay = STATE["sim_time"] - STATE["time_arrival"][0]
        STATE["delays"].append(delay)

        service = np.random.exponential(STATE["mean_service"])
        STATE["time_next_event"][1] = STATE["sim_time"] + service
        STATE["services"].append(service)

        # Shift queue
        STATE["time_arrival"] = STATE["time_arrival"][1:]

def visualize(queue, time_):
    # Console visualization (optional; can be noisy for large runs)
    print(f"Time={time_:.4f}: {queue}")

def mean_ci(data, alpha=0.001):
    """Return mean and (lower, upper) 95% CI (Student t) for a sample array."""
    arr = np.asarray(data, dtype=float)
    n = arr.size
    if n == 0:
        return (float('nan'), (float('nan'), float('nan')))
    mean = float(arr.mean())
    if n == 1:
        return (mean, (mean, mean))
    se = stats.sem(arr)
    h = se * stats.t.ppf(1 - alpha/2, n - 1)
    return mean, (mean - h, mean + h)

def discard_warmup(seq, frac):
    k = int(len(seq) * frac)
    return seq[k:]

def report(n_done, warmup_frac=None):
    if warmup_frac is None:
        warmup_frac = STATE["warmup_frac"]

    nums_in_s = discard_warmup(STATE["nums_in_s"], warmup_frac)
    nums_in_q = discard_warmup(STATE["nums_in_q"], warmup_frac)
    delays = discard_warmup(STATE["delays"], warmup_frac)
    services = discard_warmup(STATE["services"], warmup_frac)
    server_s = discard_warmup(STATE["server_s"], warmup_frac)

    avg_delay, ci_delay = mean_ci(delays)
    avg_service, ci_service = mean_ci(services)
    utilization, ci_util = mean_ci(server_s)
    avg_q, ci_q = mean_ci(nums_in_q)
    avg_system, ci_system = mean_ci(nums_in_s)

    print("\n--- Report (after warm-up discard) ---")
    print(f"Customers processed (approx): {n_done}")
    print(f"Average delay: {avg_delay:.4f}  CI=({ci_delay[0]:.4f}, {ci_delay[1]:.4f})")
    print(f"Average service time: {avg_service:.4f}  CI=({ci_service[0]:.4f}, {ci_service[1]:.4f})")
    print(f"Server utilization: {utilization:.4f}  CI=({ci_util[0]:.4f}, {ci_util[1]:.4f})")
    print(f"Average number in queue: {avg_q:.4f}  CI=({ci_q[0]:.4f}, {ci_q[1]:.4f})")
    print(f"Average number in system: {avg_system:.4f}  CI=({ci_system[0]:.4f}, {ci_system[1]:.4f})")
    print(f"Total arrivals: {len(STATE['arrivals'])}")
    print(f"Total departures: {len(STATE['departures'])}")

def compare_with_mm1(lambda_, mu, warmup_frac=None):
    if warmup_frac is None:
        warmup_frac = STATE["warmup_frac"]

    # Theory
    rho = lambda_ / mu
    L = rho / (1 - rho)
    Lq = rho**2 / (1 - rho)
    W = 1 / (mu - lambda_)
    Wq = rho / (mu - lambda_)
    S = 1 / mu

    # Simulation (discard warm-up)
    nums_in_s = discard_warmup(STATE["nums_in_s"], warmup_frac)
    nums_in_q = discard_warmup(STATE["nums_in_q"], warmup_frac)
    delays = discard_warmup(STATE["delays"], warmup_frac)
    services = discard_warmup(STATE["services"], warmup_frac)
    server_s = discard_warmup(STATE["server_s"], warmup_frac)

    utilization_sim, ci_util = mean_ci(server_s)
    L_sim, ci_L = mean_ci(nums_in_s)
    Lq_sim, ci_Lq = mean_ci(nums_in_q)
    Wq_sim, ci_Wq = mean_ci(delays)
    S_sim, ci_S = mean_ci(services)

    # Approximate W via Little's Law using effective lambda
    W_sim = float('nan')
    ci_W = (float('nan'), float('nan'))
    if len(nums_in_s) > 1 and len(STATE["departures"]) > 1:
        total_time = STATE["sim_time"]
        lambda_eff = len(STATE["departures"]) / total_time if total_time > 0 else float('nan')
        if lambda_eff and not math.isnan(lambda_eff) and lambda_eff > 0:
            W_sim = L_sim / lambda_eff
            # CI via propagation (approximate): CI(L)/lambda_eff
            ci_W = (ci_L[0] / lambda_eff, ci_L[1] / lambda_eff)

    print("\n--- M/M/1 Theoretical vs Simulation (after warm-up) ---")
    print(f"Utilization: theory={rho:.4f}, sim={utilization_sim:.4f}  CI=({ci_util[0]:.4f}, {ci_util[1]:.4f})")
    print(f"L (avg in system): theory={L:.4f}, sim={L_sim:.4f}  CI=({ci_L[0]:.4f}, {ci_L[1]:.4f})")
    print(f"Lq (avg in queue): theory={Lq:.4f}, sim={Lq_sim:.4f}  CI=({ci_Lq[0]:.4f}, {ci_Lq[1]:.4f})")
    print(f"W (avg time in system): theory={W:.4f}, sim~={W_sim:.4f}  CI~=({ci_W[0]:.4f}, {ci_W[1]:.4f})")
    print(f"Wq (avg wait in queue): theory={Wq:.4f}, sim={Wq_sim:.4f}  CI=({ci_Wq[0]:.4f}, {ci_Wq[1]:.4f})")
    print(f"Service time: theory={S:.4f}, sim={S_sim:.4f}  CI=({ci_S[0]:.4f}, {ci_S[1]:.4f})")

def plot_results(warmup_frac=None):
    if warmup_frac is None:
        warmup_frac = STATE["warmup_frac"]

    # Indicate warm-up cut on plots
    cut_idx = int(len(STATE["nums_in_s"]) * warmup_frac)

    plt.figure(figsize=(12, 8))

    plt.subplot(231)
    plt.plot(STATE["nums_in_s"], label="Num in system")
    if cut_idx > 0: plt.axvline(cut_idx, color='gray', linestyle='--', alpha=0.6)
    plt.title("Number in System"); plt.xlabel("Event index"); plt.ylabel("Num in system")

    plt.subplot(232)
    plt.plot(STATE["nums_in_q"], label="Num in queue", color='tab:orange')
    if cut_idx > 0: plt.axvline(cut_idx, color='gray', linestyle='--', alpha=0.6)
    plt.title("Number in Queue"); plt.xlabel("Event index"); plt.ylabel("Num in queue")

    plt.subplot(233)
    plt.plot(STATE["inter_events"], color='tab:green')
    if cut_idx > 0: plt.axvline(cut_idx, color='gray', linestyle='--', alpha=0.6)
    plt.title("Inter-event Times"); plt.xlabel("Event index"); plt.ylabel("Time since last event")

    plt.subplot(234)
    plt.plot(STATE["server_s"], color='tab:red')
    if cut_idx > 0: plt.axvline(cut_idx, color='gray', linestyle='--', alpha=0.6)
    plt.title("Server Busy Indicator"); plt.xlabel("Event index"); plt.ylabel("Busy=1, Idle=0")

    plt.subplot(235)
    plt.hist(STATE["delays"][cut_idx:], bins=20, color='skyblue', edgecolor='black')
    plt.title("Delays Distribution (post warm-up)"); plt.xlabel("Delay"); plt.ylabel("Frequency")

    plt.subplot(236)
    plt.hist(STATE["services"][cut_idx:], bins=20, color='salmon', edgecolor='black')
    plt.title("Service Times Distribution"); plt.xlabel("Service time"); plt.ylabel("Frequency")

    plt.tight_layout()
    plt.show()

def main():
    # Model parameters
    lambda_ = 0.208     # arrival rate
    mu = 0.352          # service rate
    max_num_custs = 20 # number of arriving customers to simulate

    # Warm-up fraction (can be tuned)
    STATE["warmup_frac"] = 0.5

    # Map to exponential scales
    STATE["mean_interarrival"] = 1 / lambda_
    STATE["mean_service"] = 1 / mu

    # Optional reproducibility
    # np.random.seed(42)

    # Initialize and run
    initialize()
    num_custs = 1
    while num_custs < max_num_custs:
        timing()
        update_time_avg_stats()
        if STATE["next_event_type"] == 1:
            arrive()
            STATE["queue"].append(num_custs)
            num_custs += 1
        elif STATE["next_event_type"] == 2:
            depart()
            STATE["queue"] = STATE["queue"][1:] if len(STATE["queue"]) >= 2 else []
        # Comment out to reduce console noise
        # visualize(STATE["queue"], STATE["sim_time"])

    # Reporting and comparison (post warm-up)
    report(n_done=max_num_custs - 10, warmup_frac=STATE["warmup_frac"])
    compare_with_mm1(lambda_=lambda_, mu=mu, warmup_frac=STATE["warmup_frac"])

    # Plots with warm-up vertical line
    plot_results(warmup_frac=STATE["warmup_frac"])

if __name__ == "__main__":
    main()