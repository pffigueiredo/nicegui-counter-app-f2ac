from pydantic import BaseModel


class CounterState(BaseModel):
    """Model representing the state of a counter"""
    value: int = 0
    
    def increment(self) -> 'CounterState':
        """Return a new CounterState with incremented value"""
        return CounterState(value=self.value + 1)
    
    def decrement(self) -> 'CounterState':
        """Return a new CounterState with decremented value"""
        return CounterState(value=self.value - 1)
    
    def reset(self) -> 'CounterState':
        """Return a new CounterState with value reset to 0"""
        return CounterState(value=0)