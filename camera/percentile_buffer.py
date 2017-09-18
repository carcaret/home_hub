import numpy

from basic_buffer import Buffer

class PBuffer(Buffer):
    
    def percentile(self, percentile):
        return numpy.percentile(self.get(), percentile)

