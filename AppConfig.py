# This file contains the configuration of the RIP server application.
config = {
  'server': {
    'host': '127.0.0.1',
    'port': 8080,
  },
  # The 'control' section configures the mapping between the RIP protocol
  # and the actual implementation of the functionality.
  # The 'impl' field should contain the name of the module (.py) and the
  # class that implement the control interface
  'control': {
    'impl_module': 'RIPArduino',
    # Also, if the class name is not the same as the module name:
    #'impl_name': 'RIPGeneric',
    'info': {
      'name': 'RIP Generic',
      'description': 'A generic implementation of RIP',
      'authors': 'J. Chacon, A. My-Taj',
      'keywords': 'Raspberry PI, RIP',
     # global configuration of the sampling
      'sampling_methods': {
        'PeriodicSampler': {
          'first_sampling': '5',
          'period': '1',
        },
        'PeriodicSendOnDelta': {
          'first_sampling': '5',
          'period': '1.0',
        }
      },
      # Server readable objects
      'readables': [{
        'name':'time',
        'description':'Server time in seconds',
        'type':'float',
        'min':'0',
        'max':'Inf',
        'precision':'0',
        'sampling': {
          'type': 'PeriodicSoD',
          'params': {
            'delta': '2'
          }
        }
      }, {
        'name':'Y',
        'description':'Output variables',
        'type':'array',
        'min':'0',
        'max':'Inf',
        'precision':'0',
        'sampling': {
          'type': 'PeriodicSoD',
          'params': {
            'delta': '2'
          }
        }          
      }],
      # Server writable objects
      'writables':  [{
        "name": "params",
        "description": "PID params: kp, ki, kd, u_eq",
        "type": "array",
        "min": "0",
        "max": "0",
        "precision": "0"
      }]
    },
  }
}