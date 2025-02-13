def func1():
    """
    # Executions Control
    ## Execution Termination
    Sometimes when we run long term executions, such as model training, we need the option to terminate the execution. This is facilitated using terminate at Checkpoint.
    To stop an execution set the code checkpoints to check if this execution received a termination and if it did, raise the Termination Exception.
    This allows you to save some work that was already done before terminating.
    For example:
    """


def func2():
    """
    Each time there is a "kill_event" the service runner checks to see if this execution received a termination request.
    To kill such execution we use
    """


def func3():
    """
    ## Execution Timeout
    You can tell an execution to stop after a given number of seconds with the timeout parameter (the default time is 1 hour).
    In case a service reset, such as in timeout or service update, If there are running executions the service will wait for the execution timeout before resetting.
    The number have to be a natural number (int).
    """


def func4():
    """
    You can decide what to do to executions that have experienced a timeout. There are 2 options of timeout handling:
    1. Mark execution as failed
    2. Retry
    """


def func5():
    """
    ## Monitoring Execution Completion

    With the SDK, you have the ability to monitor the progress of a single execution until it reaches either a `success` or `failed` status.
    Keep in mind that the local instance of dl.Execution does not automatically synchronize with the current status, requiring periodic polling to obtain the updated information.
    You can easily accomplish this by using the following commands:

    """


def func6():
    """
    The process will be suspended (with background polling) until there is a change in the execution status.

    """