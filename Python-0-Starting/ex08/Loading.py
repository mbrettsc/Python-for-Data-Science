import sys
import time
import os


def ft_tqdm(lst: range) -> None:
    """ Progress bar for an iterable. """
    total_len = len(lst)
    start_time = time.time()
    bar_len = 40

    for i, elem in enumerate(lst):
        elapsed_time = time.time() - start_time
        terminal_width = os.get_terminal_size().columns
        non_bar_length = len(f' [] {i}/{total_len} 100.00% 00.00s')
        bar_len = terminal_width - non_bar_length
        percent = (i + 1) / total_len
        filled_len = int(bar_len * percent)

        bar = '=' * filled_len + '>' + '.' * (bar_len - filled_len)
        sys.stdout.write(f'\r[{bar}] {percent:.2%} {elapsed_time:.2f}s')
        sys.stdout.flush()
        yield elem

    print()
