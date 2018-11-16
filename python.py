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

# Pandas apply by row
df.apply(lambda x: foo(x['a'], x['b'], x['c']), axis=1)

# Find all occurrences of a substring
import re
[m.start() for m in re.finditer('test', 'test test test test')]

# Regex replace
re.sub('(\d)\.(\d)', '\\1_\\2', '12. 12.23')  # > '12. 12_23'

# List of files
import glob
print(glob.glob("/path/to/files/*.txt"))

# Jupyter - Progress bar
from tqdm import tqdm
for i in tqdm(range(10000)):
    ...
