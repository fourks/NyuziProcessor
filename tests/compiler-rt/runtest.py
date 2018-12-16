#!/usr/bin/env python3
#
# Copyright 2011-2015 Jeff Bush
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

'''
Tests for the compiler-rt (compiler runtime) library, which is built as part of the
LLVM toolchain and contains compiler specific built-in functions.
'''

import sys

sys.path.insert(0, '..')
import test_harness

test_harness.register_generic_test(
    test_harness.find_files(('.c')), ['emulator'])
test_harness.execute_tests()
