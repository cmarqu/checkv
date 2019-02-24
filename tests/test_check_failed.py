#!/usr/bin/env python3

"""Tests for ``check_failed()``."""

# Copyright checkv contributors
# Licensed under the Revised BSD License, see LICENSE for details.
# SPDX-License-Identifier: BSD-3-Clause

import checkv


def test_check_failed1(caplog):
    checkv.check_failed()
    
    for record in caplog.records:
        assert record.levelname == 'ERROR'
    assert "Unconditional check failed." in caplog.text


def test_check_failed2(caplog):
    checkv.check_failed("")
    
    for record in caplog.records:
        assert record.levelname == 'ERROR'
    assert "" in caplog.text  # FIXME


def test_check_failed3(caplog):
    checkv.check_failed("Checking my data.")
    
    for record in caplog.records:
        assert record.levelname == 'ERROR'
    assert "Checking my data." in caplog.text


def test_check_failed4(caplog):
    checkv.check_failed(result="for my data.")
    
    for record in caplog.records:
        assert record.levelname == 'ERROR'
    assert "Unconditional check failed for my data." in caplog.text


my_checker = "FIXME"
    
def test_check_failed5(caplog):
    checkv.check_failed(checker=my_checker)
    
    for record in caplog.records:
        assert record.levelname == 'ERROR'
    assert "Unconditional check failed." in caplog.text
