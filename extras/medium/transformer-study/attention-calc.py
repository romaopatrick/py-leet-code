import math
from typing import Optional

def softmax():
    pass

class Tensor:
    pass

def attention(q, k, v) -> Optional[Tensor]:
    dk = q.cols
    return softmax((q*k.transpose())/math.sqrt(dk)) * v