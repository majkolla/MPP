import sys 
import sysconfig 
from dataclasses import dataclass 


@dataclass
class FreeThreadingInfo:
    build_supports_free_threading: bool 
    gil_enabled: bool | None
    
    @property
    def is_free_threaded(self) -> bool: 
        """
        True if this build is free threaded and GIL is disabled
        """
        return self.build_supports_free_threading and (not self.gil_enabed)
    
    