# The classic type of the singleton pattern
class ClassicSingeloton:
       _instance = None
       
       def __init__(self):
              raise Exception("This class is a singleton! Use get_instance() method.")
       
       @classmethod
       def get_instance(cls):
              if cls._instance is None:
                     cls._instance = cls.__new__(cls)
              return cls._instance

       
s1 = ClassicSingeloton.get_instance()
s2 = ClassicSingeloton.get_instance()

print(s1 is s2)  # True, both variables point to the same instance

############################################
# The simple type of the the singleton pattern
class Singelton:
       _instance = None

       def __new__(cls):
              if not cls._instance:
                     cls._instance = super(Singelton, cls).__new__(cls)
              return cls._instance
              
s1 = Singelton()
s2 = Singelton()
print(s1 is s2)  # True, both variables point to the same instance


#####################################
#

class SingletonMeta(type):
       _instances = {}
       def __call__(cls, *args, **kwargs):
              if cls not in cls._instances:
                     instance = super().__call__(*args, **kwargs)
                     cls._instances[cls] = instance
              return cls._instances[cls]
       
class Singleton(metaclass=SingletonMeta):
       def __init__(self, value):
              self.value = value

