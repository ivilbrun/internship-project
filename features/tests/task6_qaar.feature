Feature: User log in & User Guide

  Scenario: User can open User guide page
    Given open Reelly Sign In page
    When user logs in
    Then click on User Guide option
    Then verify the right page opens
    Then verify all lesson videos contain titles