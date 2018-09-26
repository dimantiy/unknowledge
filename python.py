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
class Foo(Bar):
  def baz(self, arg):
    return super(Foo, self).baz(arg)  # Python 2
    return super().baz(arg)           # Python 3

# Pandas remove columns
df = df.drop(columns=['B', 'C'])
