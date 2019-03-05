#!/usr/bin/env python3

# Copyright checkv contributors
# Licensed under the Revised BSD License, see LICENSE for details.
# SPDX-License-Identifier: BSD-3-Clause

import logging
import sys

logging.basicConfig(format='%(message)s', stream=sys.stdout, level=logging.INFO)


null_log_level = "null_log_level"
pass_visible = True

def is_pass_visible(checker):
    """Return whether a passing test should be printed."""
    # FIXME: make this per checker
    return pass_visible


def passing_check(checker, std_msg=None, line_num=None, file_name=None, level=None):
    """Janitor work for a passing check."""
   
    # TODO: increment stat_checks_idx
    # TODO: increment stat_passed_idx
    if std_msg is not None:
        logging.info(std_msg)


def failing_check(checker, std_msg=None, line_num=None, file_name=None, level=None):
    """Janitor work for a failing check."""
    
    # TODO: increment stat_checks_idx
    # TODO: increment stat_failed_idx
    if std_msg is not None:
        logging.error(std_msg)



#  function std_msg (
#    constant check_result : string;
#    constant msg          : string;
#    constant ctx          : string)
#    return string is
#    constant msg_i : string(1 to msg'length) := msg;
#
#    function replace_result_tag (msg, check_result : string) return string is
#    begin
#      if msg'length < check_result_tag'length then
#        return msg;
#      elsif msg(1 to check_result_tag'length) = check_result_tag then
#        return check_result & msg(check_result_tag'length + 1 to msg'right);
#      else
#        return msg;
#      end if;
#    end function replace_result_tag;
#
#    function append_context (msg, ctx : string) return string is
#    begin
#      if msg = "" then
#        return ctx;
#      elsif ctx = "" then
#        return msg;
#      else
#        return msg & " - " & ctx;
#      end if;
#    end function append_context;
#  begin
#    return append_context(replace_result_tag(msg_i, check_result), ctx);
#  end function std_msg;


# -----------------------------------------------------------------------------
# -- check_(almost)_equal for real
# -----------------------------------------------------------------------------

def check_equal(got, expected,
                checker=None, 
                msg=" - ", max_diff=0.0,
                level=null_log_level, line_num=0, file_name=""):
    """Equality Check.
    VUnit doc: https://vunit.github.io/check/user_guide.html#equality-check-check-equal
    """

    assert got is not None
    assert expected is not None
    
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

# -----------------------------------------------------------------------------
# -- check_failed
# -----------------------------------------------------------------------------
def check_failed(msg=""+".",
                 checker=None,
                 result=None,
                 level=null_log_level,
                 line_num=0, file_name=""):

    if result is not None:
        msg = " " + result
    
    failing_check(checker, std_msg=("Unconditional check failed" + msg + ""),
                  level=level, line_num=line_num, file_name=file_name)


# -----------------------------------------------------------------------------
# -- check_passed
# -----------------------------------------------------------------------------
def check_passed(msg=""+".",
                 checker=None,
                 result=None,
                 level=null_log_level,
                 line_num=0, file_name=""):

    if result is not None:
        msg = " " + result
    
    passing_check(checker, std_msg=("Unconditional check passed" + msg + ""),
                  level=level, line_num=line_num, file_name=file_name)
