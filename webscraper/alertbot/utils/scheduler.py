# import schedule
# import time
# from alertbot.models import Alert
#
# def job():
#     alertList = Alert.objects.all()
#     alerts = []
#     for a in alertList:
#         alerts.append(a.for_scheduling())
#     print(alerts)
#
# schedule.every(1).seconds.do(job)
#
#
# while 1:
#     schedule.run_pending()
#     time.sleep(1)
#
#
# # import multiprocessing
# # import time
# #
# # data = (
# #     ['a', '2'], ['b', '4'], ['c', '6'], ['d', '8'],
# #     ['e', '1'], ['f', '3'], ['g', '5'], ['h', '7']
# # )
# #
# # def mp_worker((inputs, the_time)):
# #     print " Processs %s\tWaiting %s seconds" % (inputs, the_time)
# #     time.sleep(int(the_time))
# #     print " Process %s\tDONE" % inputs
# #
# # def mp_handler():
# #     p = multiprocessing.Pool(2)
# #     p.map(mp_worker, data)
# #
# # if __name__ == '__main__':
# #     mp_handler()
