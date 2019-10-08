#!/usr/bin/env python3

"""Tests for ``check_passed()``."""

# Copyright checkv contributors
# Licensed under the Revised BSD License, see LICENSE for details.
# SPDX-License-Identifier: BSD-3-Clause

import checkv

# see https://docs.python.org/3/library/logging.html#logrecord-attributes

def test_check_passed1(caplog):
    checkv.check_passed()
    
    for record in caplog.records:
        assert record.levelname == 'INFO'
        assert record.msg == "Unconditional check passed."
    assert caplog.text == "__init__.py                 28 INFO     Unconditional check passed.\n"


def test_check_passed2(caplog):
    checkv.check_passed("")
    
    for record in caplog.records:
        assert record.levelname == 'INFO'
        assert record.msg == ""


def test_check_passed3(caplog):
    checkv.check_passed("Checking my data.")
    
    for record in caplog.records:
        assert record.levelname == 'INFO'
        assert record.msg == "Checking my data."


def test_check_passed3b(caplog):
    """Appends a dot at the end of the message if necessary."""

    checkv.check_passed("Checking my data")
    
    for record in caplog.records:
        assert record.levelname == 'INFO'
        assert record.msg == "Checking my data."


def test_check_passed3c(caplog):
    """Appends a dot at the end of the message if necessary."""

    checkv.check_passed("x")
    
    for record in caplog.records:
        assert record.levelname == 'INFO'
        assert record.msg == "x."


def test_check_passed4(caplog):
    checkv.check_passed(result="for my data.")
    
    for record in caplog.records:
        assert record.levelname == 'INFO'
        assert record.msg == "Unconditional check passed for my data."


my_checker = "FIXME"
    
def test_check_passed5(caplog):
    checkv.check_passed(checker=my_checker)
    
    for record in caplog.records:
        assert record.levelname == 'INFO'
        assert record.msg == "Unconditional check passed."
