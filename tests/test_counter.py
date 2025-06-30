from nicegui.testing import User
from nicegui import ui


async def test_counter_initial_state(user: User) -> None:
    """Test that counter starts at 0"""
    await user.open('/')
    await user.should_see('0')


async def test_counter_increment(user: User) -> None:
    """Test increment functionality"""
    await user.open('/')
    
    # Click increment button
    user.find('Increment').click()
    await user.should_see('1')
    
    # Click increment again
    user.find('Increment').click()
    await user.should_see('2')


async def test_counter_decrement(user: User) -> None:
    """Test decrement functionality"""
    await user.open('/')
    
    # First increment to have something to decrement
    user.find('Increment').click()
    user.find('Increment').click()
    await user.should_see('2')
    
    # Now decrement
    user.find('Decrement').click()
    await user.should_see('1')
    
    # Decrement again
    user.find('Decrement').click()
    await user.should_see('0')
    
    # Decrement below zero
    user.find('Decrement').click()
    await user.should_see('-1')


async def test_counter_reset(user: User) -> None:
    """Test reset functionality"""
    await user.open('/')
    
    # Increment counter
    user.find('Increment').click()
    user.find('Increment').click()
    user.find('Increment').click()
    await user.should_see('3')
    
    # Reset counter
    user.find('Reset').click()
    await user.should_see('0')


async def test_counter_mixed_operations(user: User) -> None:
    """Test mixed operations"""
    await user.open('/')
    
    # Complex sequence of operations
    user.find('Increment').click()  # 1
    user.find('Increment').click()  # 2  
    user.find('Decrement').click()  # 1
    user.find('Increment').click()  # 2
    user.find('Increment').click()  # 3
    await user.should_see('3')
    
    user.find('Reset').click()      # 0
    await user.should_see('0')
    
    user.find('Decrement').click()  # -1
    user.find('Decrement').click()  # -2
    await user.should_see('-2')


async def test_counter_buttons_exist(user: User) -> None:
    """Test that all required buttons are present"""
    await user.open('/')
    
    # Check all buttons exist
    await user.should_see('Increment')
    await user.should_see('Decrement') 
    await user.should_see('Reset')