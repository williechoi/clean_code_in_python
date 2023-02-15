import logging, threading
import time

from queue import Queue

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(message)s")

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)

fibo_dict = {}
shared_queue = Queue()
input_list = [3, 10, 5, 7]
queue_condition = threading.Condition()


def fibonacci_task(condition):
    with condition:
        while shared_queue.empty():
            logger.info("[%s] - 작업을 기다리고 있습니다" % threading.current_thread().name)
            condition.wait()
        else:
            value = shared_queue.get()
            a, b = 0, 1
            for item in range(value):
                a, b = b, a + b
                fibo_dict[value] = a
            shared_queue.task_done()
            logger.debug("[%s] - 작업 처리 결과는 다음과 같습니다. %s" % (threading.current_thread().name, fibo_dict))


def queue_task(condition):
    logging.debug('작업을 생성하여 큐에 집어넣습니다.')
    with condition:
        for item in input_list:
            shared_queue.put(item)
            time.sleep(1.4)
        logging.debug("봇들에게 작업이 모두 준비되었음을 알립니다.")
        condition.notify_all()


if __name__ == "__main__":
    threads = [threading.Thread(name=f'bot #{i}', daemon=True, target=fibonacci_task, args=(queue_condition,)) for i in
               range(4)]
    for t in threads:
        time.sleep(1.5)
        t.start()

    time.sleep(2.5)
    prod = threading.Thread(name='queue_task_thread', daemon=True, target=queue_task, args=(queue_condition, ))
    prod.start()

    for t in threads:
        t.join()
