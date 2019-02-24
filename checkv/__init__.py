#!/usr/bin/env python3

# Copyright checkv contributors
# Licensed under the Revised BSD License, see LICENSE for details.
# SPDX-License-Identifier: BSD-3-Clause

import logging
import sys

logging.basicConfig(format='%(message)s', stream=sys.stdout, level=logging.INFO)


check_result_tag = " - "
null_log_level = "null_log_level"
checker = None


def is_pass_visible(checker):
    """FIXME"""
    return True


def passing_check(checker, std_msg, line_num, file_name):
    """Janitor work for a passing check."""
   
    # TODO: increment stat_checks_idx
    # TODO: increment stat_passed_idx
    logging.info(std_msg)


def failing_check(checker, std_msg, line_num, file_name):
    """Janitor work for a failing check."""
    
    # TODO: increment stat_checks_idx
    # TODO: increment stat_failed_idx
    logging.error(std_msg)


def check_equal(got, expected,
                msg=check_result_tag, max_diff=0.0,
                level=null_log_level, line_num=0, file_name=""):
    """Equality Check.
    VUnit doc: https://vunit.github.io/check/user_guide.html#equality-check-check-equal
    """
    
    if abs(got - expected) <= max_diff:
        if is_pass_visible(checker):
            passing_check(
                checker,
                std_msg=(
                    "Equality check passed" + msg +
                    "Got abs (" + str(got) + " - " + str(expected) + ") <= " + str(max_diff) + "." ),
                line_num=line_num, file_name=file_name)
        else:
            passing_check(checker)
    else:
        failing_check(
            checker,
            std_msg=(
                "Equality check failed" + msg +
                "Got abs (" + str(got) + " - " + str(expected) + ") > " + str(max_diff) + "."),
                line_num=line_num, file_name=file_name)
