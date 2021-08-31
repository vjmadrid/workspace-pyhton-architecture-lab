

def wait_for(condition, timeout=5):
    """
    wait_for creates a conditional wait so that elements can be safely accessed.
        def my_test(self):
            # code that may run before condition is met
            wait_for(condition)
            # code that will run after condition is met
    Args:
        condition (Condition): a Condition object to evaluate
        timeout (int): seconds to wait before raising a selenium TimeoutException
    Raises:
        TimeoutException: If the condition is not met in time
    """
    condition.wait_for(timeout=timeout)
