def calculate_net_pay(vsh_values, cutoff=0.5):
    """
    Calculate Net Pay based on Vsh cutoff.
    """
    net_pay = 0

    for vsh in vsh_values:
        if vsh < cutoff:
            net_pay += 1

    return net_pay


if __name__ == "__main__":
    sample_vsh = [0.2, 0.3, 0.6, 0.4, 0.7]
    net = calculate_net_pay(sample_vsh)

    print(f"Net Pay Zones: {net}")