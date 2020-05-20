import time

def time_this(num_runs):
    def time_decorator(my_f):
        def wrapper (*args, **kwargs):
            total=0
            for i in range(num_runs):
                start=time.time()
                my_f(*args,**kwargs)
                end=time.time()
                total=total+(end-start)
            avg_time=total/num_runs
            print("Среднее время выполнения %.5f секунд!"%avg_time)
            return my_f
        return wrapper
    return time_decorator

class time_Class:
    def __init__(self,my_f):
        self.my_f=my_f
    def __call__(self, *args,**kwargs):
        start=time.time()
        self.my_f(*args,**kwargs)
        end=time.time()
        print("Время выполнения %.5f секунд!"%(end-start))
