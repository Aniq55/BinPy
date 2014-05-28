
Example for Octal Counter.
--------------------------

.. code:: python

    # imports
    from __future__ import print_function
    from BinPy.tools import Clock
    from BinPy.Sequential.counters import OctalCounter
    from BinPy.Gates import Connector
    from BinPy.tools.oscilloscope import Oscilloscope
.. code:: python

    # Initialize a toggle connectr for inpput in TFlipFlop
    
    toggle = Connector(1)
    
    # Initializing the Clock
    # A clock of 5 hertz frequency
    
    clock = Clock(1, 5)
    clock.start()
    
    # Initialize enable
    
    enable = Connector(1)
    
    # Initializing OctalCounter with 4 bits and clock
    
    b = OctalCounter(clock.A)
.. code:: python

    # Initializing the Oscillioscope
    
    # starting the oscillioscope
    
    # setting the scale
    
    o = Oscilloscope((clock.A, 'CLK'), (b.out[0], 'BIT3'), (b.out[1], 'BIT2'), (
        b.out[2], 'BIT1'), (b.out[3], 'BIT0'), (enable, 'EN1'))
    
    o.start()
    
    o.setWidth(75)
    o.setScale(0.05)  # Set scale by trial and error.
    
    o.unhold()

.. parsed-literal::

    [0m
    [0m


.. code:: python

    # Initial State
    
    print (b.state())

.. parsed-literal::

    [0, 0, 0, 0]


.. code:: python

    # Triggering the counter sequentially 2^4 + 2 times
    
    for i in range(1, 2 ** 4 + 2):
        b.trigger()
        print (b.state())
    
    o.display()

.. parsed-literal::

    [0, 0, 0, 1]
    [0, 0, 1, 0]
    [0, 0, 1, 1]
    [0, 1, 0, 0]
    [0, 1, 0, 1]
    [0, 1, 1, 0]
    [0, 1, 1, 1]
    [0, 0, 0, 0]
    [0, 0, 0, 1]
    [0, 0, 1, 0]
    [0, 0, 1, 1]
    [0, 1, 0, 0]
    [0, 1, 0, 1]
    [0, 1, 1, 0]
    [0, 1, 1, 1]
    [0, 0, 0, 0]
    [0, 0, 0, 1]
    [0m==========================================================================================
    BinPy - Oscilloscope
    ==========================================================================================
                                                          SCALE - X-AXIS : 1 UNIT WIDTH = 0.05
    ==========================================================================================
              │
              │
              │     ┌────┐   ┌───┐   ┌───┐   ┌───┐   ┌───┐  ┌────┐  ┌───┐   ┌───┐   ┌───┐  
         CLK  │     │    │   │   │   │   │   │   │   │   │  │    │  │   │   │   │   │   │  
              ─ ────┘    └───┘   └───┘   └───┘   └───┘   └──┘    └──┘   └───┘   └───┘   └──
              │
              │
              │
              │
              │                                                                 ┌──────────
        BIT3  │                                                                 │          
              ─ ────────────────────────────────────────────────────────────────┘          
              │
              │
              │
              │
              │                                  ┌──────────────────────────────┐          
        BIT2  │                                  │                              │          
              ─ ─────────────────────────────────┘                              └──────────
              │
              │
              │
              │
              │                  ┌───────────────┐               ┌──────────────┐          
        BIT1  │                  │               │               │              │          
              ─ ─────────────────┘               └───────────────┘              └──────────
              │
              │
              │
              │
              │          ┌───────┐       ┌───────┐       ┌───────┐      ┌───────┐          
        BIT0  │          │       │       │       │       │       │      │       │          
              ─ ─────────┘       └───────┘       └───────┘       └──────┘       └──────────
              │
              │
              │
              │
              │ ┌──────────────────────────────────────────────────────────────────────────
         EN1  │ │                                                                          
              ─ ┘                                                                          
              │
              │
    ││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││
    ──────────────────────────────────────────────────────────────────────────────────────────
    [0m


.. code:: python

    # Calling the instance will trigger
    
    b()
    
    print(b.state())

.. parsed-literal::

    [0, 0, 1, 0]


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

    # Kill the oscilloscope and the clock threads after use.
    
    o.kill()
    clock.kill()