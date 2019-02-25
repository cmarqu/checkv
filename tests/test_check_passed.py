#!/usr/bin/env python3

"""Tests for ``check_passed()``."""

# Copyright checkv contributors
# Licensed under the Revised BSD License, see LICENSE for details.
# SPDX-License-Identifier: BSD-3-Clause

import checkv


def test_check_passed1(caplog):
    checkv.check_passed()
    
    for record in caplog.records:
        assert record.levelname == 'INFO'
    assert "Unconditional check passed." in caplog.text


def test_check_passed2(caplog):
    checkv.check_passed("")
    
    for record in caplog.records:
        assert record.levelname == 'INFO'
    assert "" in caplog.text  # FIXME


def test_check_passed3(caplog):
    checkv.check_passed("Checking my data.")
    
    for record in caplog.records:
        assert record.levelname == 'INFO'
    assert "Checking my data." in caplog.text


def test_check_passed4(caplog):
    checkv.check_passed(result="for my data.")
    
    for record in caplog.records:
        assert record.levelname == 'INFO'
    assert "Unconditional check passed for my data." in caplog.text


my_checker = "FIXME"
    
def test_check_passed5(caplog):
    checkv.check_passed(checker=my_checker)
    
    for record in caplog.records:
        assert record.levelname == 'INFO'
    assert "Unconditional check passed." in caplog.text
