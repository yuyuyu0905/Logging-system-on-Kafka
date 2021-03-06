from decorator_tracking import decorator_send

class Data:
    def __init__(self):
        self.abd=[123]
    @classmethod
    @decorator_send
    def open(cls,dataset_name):
        return dataset_name

    @decorator_send
    def add_attachment(self, topic, name, path, *random_args,**random_kargs):
        return topic

    @decorator_send
    def list_topics(self):
        return 'topic'

    @decorator_send
    def create_topic(self,name,source,format='raw',**meta):
        return 'meta'


a=Data()
while True:
    a.open('data')
    a.add_attachment('topic','name','path','random',random_kargs='randomkwargs')
    a.list_topics()
    a.create_topic('1','2','source')

