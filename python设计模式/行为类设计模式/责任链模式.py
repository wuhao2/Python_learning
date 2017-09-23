# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/31 10:34'

'''请假系统'''


class manager():
    successor = None
    name = ''

    def __init__(self, name):
        self.name = name

    def setSuccessor(self, successor):
        self.successor = successor

    def handleRequest(self, request):
        pass


class lineManager(manager):
    def handleRequest(self, request):
        if request.requestType == 'DaysOff' and request.number <= 3:
            print '%s:%s Num:%d Accepted OVER' % (self.name, request.requestContent, request.number)
        else:
            print '%s:%s Num:%d Accepted CONTINUE' % (self.name, request.requestContent, request.number)
            if self.successor != None:
                self.successor.handleRequest(request)


class departmentManager(manager):
    def handleRequest(self, request):
        if request.requestType == 'DaysOff' and request.number <= 7:
            print '%s:%s Num:%d Accepted OVER' % (self.name, request.requestContent, request.number)
        else:
            print '%s:%s Num:%d Accepted CONTINUE' % (self.name, request.requestContent, request.number)
            if self.successor != None:
                self.successor.handleRequest(request)


class generalManager(manager):
    def handleRequest(self, request):
        if request.requestType == 'DaysOff':
            print '%s:%s Num:%d Accepted OVER' % (self.name, request.requestContent, request.number)


class request():
    requestType = ''
    requestContent = ''
    number = 0


if __name__ == "__main__":
    line_manager = lineManager('LINE MANAGER')
    department_manager = departmentManager('DEPARTMENT MANAGER')
    general_manager = generalManager('GENERAL MANAGER')

    line_manager.setSuccessor(department_manager)
    department_manager.setSuccessor(general_manager)

    req = request()
    req.requestType = 'DaysOff'
    req.requestContent = 'Ask 1 day off'
    req.number = 1
    line_manager.handleRequest(req)

    req.requestType = 'DaysOff'
    req.requestContent = 'Ask 5 days off'
    req.number = 5
    line_manager.handleRequest(req)

    req.requestType = 'DaysOff'
    req.requestContent = 'Ask 10 days off'
    req.number = 10
    line_manager.handleRequest(req)
