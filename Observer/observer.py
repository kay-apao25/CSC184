import time
from abc import ABCMeta, abstractmethod
import datetime

class Subject(object):
    def __init__(self):
        self.observers = []
        self.cur_time = None
    def register_observer(self, observer):
    	if observer in self.observers:
            print observer, 'already in subscribed observers'
        else:
            self.observers.append(observer)

    def unregister_observer(self, observer):
        try:
            self.observers.remove(observer)
        except ValueError:
            print 'No such observer in subject'

    def notify_observers(self):
        self.cur_time = time.time()
        for observer in self.observers:
            observer.notify(self.cur_time)

class Observer(object):
    """Abstract class for observers, provides notify method as 
    interface for subjects."""
    __metaclass__ = ABCMeta

    @abstractmethod
    def notify(self, unix_timestamp):
        pass

#And a couple of concrete observer derived from abstract observer.
#They need to implement notify method. This method will take UNIX
#timestamp converts it to 12H or 24H format and print it to
#standard out.
f = open('myfile', 'w')
class USATimeObserver(Observer):
    n = 0
    def __init__(self, name):
        self.name = name

    def notify(self, unix_timestamp):
        time = datetime.datetime.fromtimestamp(int(unix_timestamp)).strftime('%Y-' \
        '%m-%d %I:%M%p')
        self.__class__.n += 1
        #print 'Observer', self.name, 'says:', time
        if self.__class__.n == 2:
            f.write(str('Observer ' + self.name + ' says: ' + time + '\n'))

class EUTimeObserver(Observer):
    n = 0
    def __init__(self, name):
        self.name = name

    def notify(self, unix_timestamp):
        time = datetime.datetime.fromtimestamp(int(unix_timestamp)).strftime('%Y-' \
        '%m-%d %H:%M')
        self.__class__.n += 1 
        #print 'Observer', self.name, 'says:', time
        if self.__class__.n == 2:
            f.write('Observer ' + self.name + ' says: ' + time + '\n')

if __name__ == '__main__':
    
    subject = Subject()

    #print 'Adding usa_time_observer'
    #f.write('Adding usa_time_observer\n')
    observer1 = USATimeObserver('usa_time_observer')
    subject.register_observer(observer1)
    subject.notify_observers()
    #f.write('After adding USA time observer: %d\n' % len(subject.observers))


    time.sleep(2)
    #print 'Adding eu_time_observer'
    #f.write('Adding eu_time_observer\n')
    observer2 = EUTimeObserver('eu_time_observer')
    subject.register_observer(observer2)
    subject.notify_observers()
    #f.write('After adding EU time observer: %d\n' % len(subject.observers))

    time.sleep(2)
    #print 'Removing usa_time_observer'
    #f.write('Removing usa_time_observer\n')
    subject.unregister_observer(observer1)
    subject.notify_observers()
    #f.write('After deleting USA time observer: %d\n' % len(subject.observers))

    f.close()