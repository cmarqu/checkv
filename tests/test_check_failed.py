#!/usr/bin/env python3

"""Tests for ``check_failed()``."""

# Copyright checkv contributors
# Licensed under the Revised BSD License, see LICENSE for details.
# SPDX-License-Identifier: BSD-3-Clause

import checkv


def test_check_failed1(caplog):
    checkv.check_failed()

    for record in caplog.records:
        assert record.levelname == "ERROR"
        assert record.msg == "Unconditional check failed."
    assert (
        caplog.text.endswith("Unconditional check failed.\n")
    )


def test_check_failed2(caplog):
    checkv.check_failed("")

    for record in caplog.records:
        assert record.levelname == "ERROR"
        assert record.msg == ""


def test_check_failed3(caplog):
    checkv.check_failed("Checking my data.")

    for record in caplog.records:
        assert record.levelname == "ERROR"
        assert record.msg == "Checking my data."


def test_check_failed3b(caplog):
    """Appends a dot at the end of the message if necessary."""

    checkv.check_failed("Checking my data")

    for record in caplog.records:
        assert record.levelname == "ERROR"
        assert record.msg == "Checking my data."


def test_check_failed3c(caplog):
    """Appends a dot at the end of the message if necessary."""

    checkv.check_failed("x")

    for record in caplog.records:
        assert record.levelname == "ERROR"
        assert record.msg == "x."


def test_check_failed4(caplog):
    checkv.check_failed(result="for my data.")

    for record in caplog.records:
        assert record.levelname == "ERROR"
        assert record.msg == "Unconditional check failed for my data."


my_checker = "FIXME"


def test_check_failed5(caplog):
    checkv.check_failed(checker=my_checker)

    for record in caplog.records:
        assert record.levelname == "ERROR"
        assert record.msg == "Unconditional check failed."
