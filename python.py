# Current date and time
import datetime
datetime.datetime.now().isoformat()

# Max int
import sys
sys.maxint   # Python 2
sys.maxsize  # Python 3

# Generate Exception
raise Exception('Describe exception')
raise SpecificException('Specific exception')

# Call parent class's method
super(Foo, self).foo(1, 2)  # Python 2
super().foo(1, 2)           # Python 3
