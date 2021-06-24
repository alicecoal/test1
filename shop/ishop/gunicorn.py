from multiprocessing import cpu_count

bind = '127.0.0.1:8866'
daemon = True
workers = cpu_count()
