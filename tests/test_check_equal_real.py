#!/usr/bin/env python3

"""Tests for ``check_equal()`` for floating point values."""

# Copyright checkv contributors
# Licensed under the Revised BSD License, see LICENSE for details.
# SPDX-License-Identifier: BSD-3-Clause

import checkv


def test_check_equal_real_0_0_pass(caplog):
    checkv.check_equal(0.0, 0.0)
    
    for record in caplog.records:
        assert record.levelname == 'INFO'
    assert "Equality check passed - Got abs (0.0 - 0.0) <= 0.0." in caplog.text


def test_check_equal_real_0_1_pass(caplog):
    checkv.check_equal(0.0, 1.0, max_diff=1.0)
    
    for record in caplog.records:
        assert record.levelname == 'INFO'
    assert "Equality check passed - Got abs (0.0 - 1.0) <= 1.0." in caplog.text

    
def test_check_equal_real_0_1_fail(caplog):
    checkv.check_equal(0.0, 1.0)
    
    for record in caplog.records:
        assert record.levelname == 'ERROR'
    assert "Equality check failed - Got abs (0.0 - 1.0) > 0.0." in caplog.text

    
def test_check_equal_real_0_1_fail2(caplog):
    checkv.check_equal(0.0, 1.0, max_diff=0.9)
    
    for record in caplog.records:
        assert record.levelname == 'ERROR'
    assert "Equality check failed - Got abs (0.0 - 1.0) > 0.9."  in caplog.text


my_checker = "FIXME"

def test_check_equal_real_my_checker__0_0_pass(caplog):
    checkv.check_equal(0.0, 0.0, checker=my_checker)
    
    for record in caplog.records:
        assert record.levelname == 'INFO'
    assert "Equality check passed - Got abs (0.0 - 0.0) <= 0.0." in caplog.text


def test_check_equal_real_my_checker__0_1_pass(caplog):
    checkv.check_equal(0.0, 1.0, max_diff=1.0, checker=my_checker)
    
    for record in caplog.records:
        assert record.levelname == 'INFO'
    assert "Equality check passed - Got abs (0.0 - 1.0) <= 1.0." in caplog.text

    
def test_check_equal_real_my_checker__0_1_fail(caplog):
    checkv.check_equal(0.0, 1.0, checker=my_checker)
    
    for record in caplog.records:
        assert record.levelname == 'ERROR'
    assert "Equality check failed - Got abs (0.0 - 1.0) > 0.0." in caplog.text

    
def test_check_equal_real_my_checker__0_1_fail2(caplog):
    checkv.check_equal(0.0, 1.0, max_diff=0.9, checker=my_checker)
    
    for record in caplog.records:
        assert record.levelname == 'ERROR'
    assert "Equality check failed - Got abs (0.0 - 1.0) > 0.9."  in caplog.text
