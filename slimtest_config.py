#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright © 2014 Mozilla Corporation

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

# Tests for areweslimyet.com. Used by run_slimtest.py or slimtest_batchtester_hook.py

AreWeSlimYetTests = {
  ## A very quick test-run, for testing purposes - doesn't give very useful data
  ## "Slimtest-TalosTP5-Quick":
  # {
  #   'type': "EnduranceTest",
  #   'vars':
  #     {
  #       'test': [ 'mozmill_endurance_test' ],
  #       'entities': 5,
  #       'iterations': 1,
  #       'delay': 0,
  #       'perTabPause': 1,
  #       'settleWaitTime': 3
  #     }
  # },
  ## The current test used for areweslimyet.com. Takes about 90 minutes.
  "Slimtest-TalosTP5-Slow":
  {
    'type': "EnduranceTest",
    'vars':
      {
        'test': [ 'mozmill_endurance_test' ],
        'entities': 100,
        'iterations': 5,
        'delay': 0,
        'perTabPause': 10,
        'settleWaitTime': 30
      }
  },
  ## We also ran tests without a delay for a while, but they produce fairly
  ## useless data
  ##
  # "Slimtest-TalosTP5":
  # {
  #   'type': "EnduranceTest",
  #   'vars':
  #     {
  #       'test': [ 'mozmill_endurance_test' ],
  #       'entities': 100,
  #       'iterations': 5,
  #       'delay': 0,
  #       'perTabPause': 0,
  #       'settleWaitTime': 30
  #     }
  # },
};
