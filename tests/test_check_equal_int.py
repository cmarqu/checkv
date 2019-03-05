#!/usr/bin/env python3

"""Tests for ``check_equal()`` for other values."""

# Copyright checkv contributors
# Licensed under the Revised BSD License, see LICENSE for details.
# SPDX-License-Identifier: BSD-3-Clause

import checkv


def test_check_equal_int_0_0_pass(caplog):
    checkv.check_equal(0, 0)
    
    for record in caplog.records:
        assert record.levelname == 'INFO'
    assert "Equality check passed - Got abs (0 - 0) <= 0." in caplog.text


def test_check_equal_int_0_1_pass(caplog):
    checkv.check_equal(0, 10, max_diff=10)
    
    for record in caplog.records:
        assert record.levelname == 'INFO'
    assert "Equality check passed - Got abs (0 - 10) <= 10." in caplog.text


def test_check_equal_int_0_2_pass_not_visible(caplog):
    checkv.pass_visible = False
    checkv.check_equal(0, 10, max_diff=10)
    checkv.pass_visible = True

    # check that no output happened
    assert len(caplog.records) == 0
    assert "" == caplog.text


def test_check_equal_int_0_1_fail(caplog):
    checkv.check_equal(0, 10)
    
    for record in caplog.records:
        assert record.levelname == 'ERROR'
    assert "Equality check failed - Got abs (0 - 10) > 0." in caplog.text

    
def test_check_equal_int_0_1_fail2(caplog):
    checkv.check_equal(0, 10, max_diff=9)
    
    for record in caplog.records:
        assert record.levelname == 'ERROR'
    assert "Equality check failed - Got abs (0 - 10) > 9."  in caplog.text


my_checker = "FIXME"

def test_check_equal_int_my_checker__0_0_pass(caplog):
    checkv.check_equal(0, 0, checker=my_checker)
    
    for record in caplog.records:
        assert record.levelname == 'INFO'
    assert "Equality check passed - Got abs (0 - 0) <= 0." in caplog.text


def test_check_equal_int_my_checker__0_1_pass(caplog):
    checkv.check_equal(0, 10, max_diff=10, checker=my_checker)
    
    for record in caplog.records:
        assert record.levelname == 'INFO'
    assert "Equality check passed - Got abs (0 - 10) <= 10." in caplog.text

    
def test_check_equal_int_my_checker__0_1_fail(caplog):
    checkv.check_equal(0, 10, checker=my_checker)
    
    for record in caplog.records:
        assert record.levelname == 'ERROR'
    assert "Equality check failed - Got abs (0 - 10) > 0." in caplog.text

    
def test_check_equal_int_my_checker__0_1_fail2(caplog):
    checkv.check_equal(0, 10, max_diff=9, checker=my_checker)
    
    for record in caplog.records:
        assert record.levelname == 'ERROR'
    assert "Equality check failed - Got abs (0 - 10) > 9."  in caplog.text
