# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/31 13:06'
# 在门面模式中，我们提到过火警报警器。在当时，我们关注的是通过封装减少代码重复。
# 而今天，我们将从业务流程的实现角度，来再次实现该火警报警器。

class AlarmSensor:
    def run(self):
        print "Alarm Ring..."
class WaterSprinker:
    def run(self):
        print "Spray Water..."
class EmergencyDialer:
    def run(self):
        print "Dial 119..."

class Observer:
    def update(self):
        pass
class AlarmSensor(Observer):
    def update(self,action):
        print "Alarm Got: %s" % action
        self.runAlarm()
    def runAlarm(self):
        print "Alarm Ring..."
class WaterSprinker(Observer):
    def update(self,action):
        print "Sprinker Got: %s" % action
        self.runSprinker()
    def runSprinker(self):
        print "Spray Water..."
class EmergencyDialer(Observer):
    def update(self,action):
        print "Dialer Got: %s"%action
        self.runDialer()
    def runDialer(self):
        print "Dial 119..."

# 观察者中定义了update接口，如果被观察者状态比较多，或者每个具体的观察者方法比较多，
# 可以通过update传参数进行更丰富的控制。
# 下面构造被观察者。

class Observed:
    observers=[]
    action=""
    def addObserver(self,observer):
        self.observers.append(observer)
    def notifyAll(self):
        for obs in self.observers:
            obs.update(self.action)
class smokeSensor(Observed):
    def setAction(self,action):
        self.action=action
    def isFire(self):
        return True
# 被观察者中首先将观察对象加入到观察者数组中，若发生情况，则通过notifyAll通知各观察者。
# 业务代码如下：

if __name__=="__main__":
    alarm=AlarmSensor()
    sprinker=WaterSprinker()
    dialer=EmergencyDialer()

    smoke_sensor=smokeSensor()
    smoke_sensor.addObserver(alarm)
    smoke_sensor.addObserver(sprinker)
    smoke_sensor.addObserver(dialer)


    if smoke_sensor.isFire():
        smoke_sensor.setAction("On Fire!")
        smoke_sensor.notifyAll()