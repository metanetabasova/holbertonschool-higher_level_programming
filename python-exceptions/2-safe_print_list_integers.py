#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Siyahıdan x qədər elementə baxır və yalnız tam ədədləri çap edir."""
    printed_integers = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            printed_integers += 1
        except (ValueError, TypeError):
            continue
        except IndexError:
            break
    print("")
    return printed_integers
