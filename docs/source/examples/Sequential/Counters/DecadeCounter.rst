
Example for Decade Counter.
---------------------------

.. code:: python

    # imports
    
    from __future__ import print_function
    from BinPy.tools import Clock
    from BinPy.Sequential.counters import DecadeCounter
    from BinPy.Gates import Connector
    from BinPy.tools.oscilloscope import Oscilloscope
.. code:: python

    # Initialize a toggle connectr for inpput in TFlipFlop
    
    toggle = Connector(1)
.. code:: python

    # Initializing the Clock
    # A clock of 5 hertz frequency
    
    clock = Clock(1, 5)
    
    clock.start()
    
    clk_conn = clock.A
.. code:: python

    # Initialize enable
    
    enable = Connector(1)
.. code:: python

    # Initializing the counter
    
    # Initializing DecadeCounter with clock_conn
    
    b = DecadeCounter(clk_conn)
.. code:: python

    # Initiating the oscilloscope
    
    o = Oscilloscope((clk_conn, 'CLK'), (b.out[0], 'BIT3'), (b.out[1], 'BIT2'), (
        b.out[2], 'BIT1'), (b.out[3], 'BIT0'), (enable, 'EN1'))
    
    # starting the oscillioscope thread - This does not initiate the recording.
    
    o.start()
    
    # setting the scale
    
    o.setScale(0.05)  # Set scale by trial and error.
    
    # Set the width of the oscilloscope to fit the ipython notebook.
        
    o.setWidth(100)

.. parsed-literal::

    [0m


.. code:: python

    # unhold the oscilloscope to start the recording.
    
    o.unhold()
    
    # Initial State
    
    print (b.state())
    
    # Triggering the counter sequentially 2^4 times
    
    for i in range(1, 2 ** 4):
        b.trigger()
        print (b.state())
    
    # Display the oscilloscope - Implicitly the o.hold() will be called first to stop the recording.
    
    o.display()

.. parsed-literal::

    [0m
    [0, 0, 0, 0]
    [0, 0, 0, 1]
    [0, 0, 1, 0]
    [0, 0, 1, 1]
    [0, 1, 0, 0]
    [0, 1, 0, 1]
    [0, 1, 1, 0]
    [0, 1, 1, 1]
    [1, 0, 0, 0]
    [1, 0, 0, 1]
    [0, 0, 0, 0]
    [0, 0, 0, 1]
    [0, 0, 1, 0]
    [0, 0, 1, 1]
    [0, 1, 0, 0]
    [0, 1, 0, 1]
    [0m===================================================================================================================
    BinPy - Oscilloscope
    ===================================================================================================================
                                                                                   SCALE - X-AXIS : 1 UNIT WIDTH = 0.05
    ===================================================================================================================
              │
              │
              │   ┌───┐   ┌──┐   ┌───┐   ┌───┐   ┌───┐   ┌───┐   ┌───┐   ┌───┐   ┌───┐   ┌───┐   ┌───┐   ┌───┐   ┌──
         CLK  │   │   │   │  │   │   │   │   │   │   │   │   │   │   │   │   │   │   │   │   │   │   │   │   │   │  
              ─ ──┘   └───┘  └───┘   └───┘   └───┘   └───┘   └───┘   └───┘   └───┘   └───┘   └───┘   └───┘   └───┘  
              │
              │
              │
              │
              │                                                      ┌──────────────────────────────────────────────
        BIT3  │                                                      │                                              
              ─ ─────────────────────────────────────────────────────┘                                              
              │
              │
              │
              │
              │                      ┌───────────────────────────────┐                                              
        BIT2  │                      │                               │                                              
              ─ ─────────────────────┘                               └──────────────────────────────────────────────
              │
              │
              │
              │
              │       ┌──────────────┐               ┌───────────────┐               ┌──────────────────────────────
        BIT1  │       │              │               │               │               │                              
              ─ ──────┘              └───────────────┘               └───────────────┘                              
              │
              │
              │
              │
              │ ┌─────┐      ┌───────┐       ┌───────┐       ┌───────┐       ┌───────┐                              
        BIT0  │ │     │      │       │       │       │       │       │       │       │                              
              ─ ┘     └──────┘       └───────┘       └───────┘       └───────┘       └──────────────────────────────
              │
              │
              │
              │
              │ ┌───────────────────────────────────────────────────────────────────────────────────────────────────
         EN1  │ │                                                                                                   
              ─ ┘                                                                                                   
              │
              │
    │││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││
    ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────
    [0m


.. code:: python

    # Calling the instance will trigger
    
    b()
    
    print(b.state())

.. parsed-literal::

    [0, 1, 1, 0]


.. code:: python

    # Setting the Counter
    
    b.setCounter()
    
    print(b.state())

.. parsed-literal::

    [1, 1, 1, 1]


.. code:: python

    # Resetting the Counter
    
    b.resetCounter()
    
    print(b.state())

.. parsed-literal::

    [0, 0, 0, 0]


.. code:: python

    # Disabling the Counter
    
    b.disable()
    
    b.trigger()
    
    print(b.state())

.. parsed-literal::

    [0, 0, 0, 0]


.. code:: python

    # Enabling the Counter
    
    b.enable()
    
    b.trigger()
    
    print(b.state())

.. parsed-literal::

    [0, 0, 0, 0]


.. code:: python

    # Kill the oscilloscope thread
    
    o.kill()
    
    # Kill the clock thread
    
    clock.kill()